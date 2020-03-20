# -*- coding: utf-8 -*
from __future__ import unicode_literals
from django.views.generic import UpdateView, DeleteView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import get_object_or_404
from mali_project.filter import (MaliFilter, RdcFilter)
from mali.models import MaliModel
from mali.forms import FormML
from rdc.models import RDCModel
from rdc.forms import FormRDC, FormAdminCongo
from mali_project.forms import FilterForm
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.urls import reverse
import os


class CustomPermissionMixin(PermissionRequiredMixin):
    """docstring for CustomPermissionMixin"""
    raise_exception = True
    PERMISSION_LIST = {
        'Mali': ('mali.change_malimodel',),
        'Congo': ('rdc.change_rdcmodel',)
    }

    def get_permission_required(self):
        return self._set_domain_permission()

    def _set_domain_permission(self):
        try:
            return self.PERMISSION_LIST[self.domain]
        except Exception as e:
            raise e


class DomainMixin(object):
    """As everything depend on the subdomain, this will set attribute domain"""

    def dispatch(self, *args, **kwargs):
        self.domain = os.environ.get('DJANGO_DOMAIN')
        self.model = MaliModel if self.domain == 'Mali' else RDCModel
        return super(DomainMixin, self).dispatch(*args, **kwargs)


class UpdateForm(DomainMixin, SuccessMessageMixin, UpdateView):
    model = None
    domain = None
    login_url = '/admin'
    template_name = 'mali_project/crud/update.html'
    success_message = 'Enregistrement mise à jour avec succès'

    def dispatch(self, *args, **kwargs):
        self.authorized = True if self.request.user.groups.all().count() else False
        print(self.authorized)
        return super(UpdateForm, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        """Put pk in the context in order to display corresponding QRCode on the front"""
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['can_approbe'] = self.authorized
        return context

    def get_form_class(self):
        if self.domain == 'Congo':
            if self.request.user.groups.all().count() > 0:  # bug fix to check user's permissions
                return FormAdminCongo
            else:
                return FormRDC
        return FormML

    def get_object(self):
        """Function use kwargs to access url args like pk"""

        obj = get_object_or_404(self.model, pk=self.kwargs['pk'])

        # check if user want update an approuved record
        if obj.etat == 'Valide' and not self.authorized:
            raise PermissionDenied(
                'Vous ne pouvez pas modifier un formulaire déja approuvé')
        return obj

    def get_success_url(self):
        return (
            reverse('record_list') if self.authorized else reverse('home')
        )


class ListRecord(DomainMixin, CustomPermissionMixin, SuccessMessageMixin, ListView):
    model = None
    template_name = 'mali_project/crud/list.html'
    paginate_by = 35
    success_message = 'Enregistrement modifié avec success'

    def get_queryset(self):
        self.model = MaliModel if self.domain == 'Mali' else RDCModel
        initial_qs = super(ListRecord, self).get_queryset()
        custom_filter_class = MaliFilter(self.request.GET, queryset=initial_qs) if self.domain == 'Mali' else RdcFilter(
            self.request.GET, queryset=initial_qs)
        self.filter_form = custom_filter_class.form
        return custom_filter_class.qs

    def get_context_data(self, **kwargs):
        context = super(ListRecord, self).get_context_data(**kwargs)
        context['filter_form'] = self.filter_form if hasattr(
            self, 'filter_form') else FilterForm()
        page_object = context['page_obj']
        page_step = range(page_object.number - 3, page_object.number + 4)
        context['page_step'] = page_step
        return context


class DeleteRecord(DomainMixin, CustomPermissionMixin, DeleteView):
    """docstring for ClassName"""
    model = None
    template_name = 'mali_project/crud/delete.html'
    success_message = 'Suppression correctement effectuée'
    success_url = 'list_registration'

    def delete(self, request, *args, **kwargs):
        messages.success(request, self.success_message)
        return super(DeleteRecord, self).delete(request, *args, **kwargs)
