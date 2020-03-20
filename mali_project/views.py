# -*- coding: utf-8 -*
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
import re, os, qrcode, requests, json, random
from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.utils.html import format_html
from django.urls import reverse
from django.db.models import Count
from django.db.models.functions import Lower
from datetime import datetime
from mali_project.crud_view.crud_view import DomainMixin
from mali_project.forms import ContactForm, LoginForm
from mali.forms import FormML
from rdc.forms import FormRDC
from mali.models import MaliModel
from rdc.models import RDCModel
from mali_project import settings
from django.db.models import Avg, ExpressionWrapper, DecimalField, F  
from django.db.models.functions import ExtractYear, ExtractMonth 
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt



DOMAIN_MAP = {
	'Mali': MaliModel,
	'Congo': RDCModel
}
domain = os.environ.get('DJANGO_DOMAIN')




def home(request):
	print(domain)
	if domain:
		form = FormML(initial={'domain': domain}) if domain == 'Mali' else FormRDC()
		return render(request, 'mali_project/index.html', {'form': form})
	else:
		return render(request, 'mali_project/project_selector.html')

def scanView(request):
	return render(request, 'mali_project/scan.html')

# Requete ajax --> a deplacer dans une nouvelle application django
@csrf_exempt
def addform(request):
	
	if request.method == 'POST':
		form = FormML(request.POST or None) if domain == 'Mali' else FormRDC(
			request.POST or None)

		if form.is_valid():
			form_id= request.POST.get('identifiant')
			response_template = "<img src='static/img/{}.jpeg' />"
			instance = form.save()
			return JsonResponse({'path': format_html(response_template, form_id)}, status=200)
		else:
			# print type(form.errors)
			# errors_string= '\n'.join(['<strong>%s</strong>: %s'.format(k, form.errors) for k in form.errors?as])
			return JsonResponse({'error': form.errors.as_ul()}, status=404)

class RecordFinder(DomainMixin, View):
	def get(self, request, *args, **kwargs):
		result_json= {
  			"results": [],
		}			
		try:
			obj= self.model.objects.get(pk=kwargs['record_id'])
		except Exception as e:
			return JsonResponse({})
		obj_to_json= model_to_dict(obj, fields=['identifiant', 'prenom', 'nom_famille'])
		result_json['results'].append(obj_to_json)
		
		return JsonResponse(result_json)
		
# Requete ajax --> a deplacer dans une nouvelle application django
def approbeForm(request, form_id):

	if request.is_ajax() and request.method == 'POST':
		model = MaliModel if domain == 'Mali' else RDCModel
		obj_to_approbe = get_object_or_404(model, pk = form_id)
		obj_to_approbe.etat= 'Valide'
		obj_to_approbe.save()
		return JsonResponse({'result': True, 'message': 'Formulaire approuvé'})
	else:
		return JsonResponse({'reason':'Non autorisé' }, status=405)


class ContactView(View):
	def get(self, request):
		form = ContactForm()
		return render(request, 'mali_project/contact.html', {'contact_form': form})

	def post(self,  request):
		form = ContactForm(request.POST)
		if form.is_valid():
			recaptcha_response = request.POST.get('g-recaptcha-response')
			data = {
				'secret': settings.CAPTCHA,
				'response': recaptcha_response,
			}
			r = requests.post(
				'https://www.google.com/recaptcha/api/siteverify', data=data)
			result = r.json()

			if result['success']:
				form.save()
				messages.success(request, 'Votre message a été bien envoyé')
			else:
				messages.error(request, 'Votre captcha n\'est pas valide')
			return render(request, 'mali_project/contact.html', {'contact_form': form})


def about(request):
	return render(request, 'mali_project/about.html')


class LoginView(View):
	def get(self, request):
		f = LoginForm()
		return render(request, 'mali_project/login.html', {'form': f})

	def post(self, request):
		f = LoginForm(request.POST or None)
		if f.is_valid:
			username = request.POST.get('identifiant', '')
			password = request.POST.get('password', '')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.success(request, 'Vous êtes à présent identifié')
				return redirect(request.GET.get('next') or 'home')
			else:
				messages.error(
					request, 'Un problème est survenu lors de l\'authentification')
		else:
			messages.error(request, 'Formulaire non rempli correctement')
		return render(request, 'mali_project/login.html', {'form': f})

class LogoutView(View):
	template_name = 'mali_project/index.html'

	def get(self, request):
		if request.user.is_active:
			logout(request)
			messages.success(request, 'Vous avez été deconnecté avec succès')
			return redirect(reverse('home'))
		messages.error(request, 'Vous n\'etes pas connecté')
		return render(request, 'mali_project/index.html', {'form': form})

class StatsView(DomainMixin, View):
	
	def get(self, request):
		RDC_STATS_FIELDS=[
			'perte_appetit',
			'fatigue_intense',
			'douleur_musculaire',
			'respiration_difficile',
			'douleur_abdominale',
			'difficulte_avaler','yeux_rouge',
			'saignement_inexplique',
			'deces_inexplique',
		]

		MALI_STATS_FIELDS= [
			'fievre',
			'ecchymose',
			'saignement_nez',
			'contact_ebola',
			'etablissement_ebola',
			'cephale_douleur',
		]
		#get the model for the domain
		chart_scope = MALI_STATS_FIELDS if self.domain == 'Mali' else RDC_STATS_FIELDS
		context = {}
		try:
			model = DOMAIN_MAP[domain]
		except KeyError:
			raise Exception('Unknown subdomain')

		#Stats are always given by gender
		chart_args = {
			'genre': Count('genre'),
		}

		while len(chart_scope) > 0 :
			item = chart_scope.pop() 
			chart_args[item] = Count(item)
			context[item] = model.objects.values('genre', response=Lower(item)).order_by('-genre').annotate(count_response= chart_args[item]).filter(response=u'oui')
			
			del chart_args[item]

		result_avg= model.objects.annotate(age=datetime.now().year- ExtractYear('date_naissance')).aggregate(moyenne=Avg('age'))['moyenne']
		year_avg= float('{0:.2f}'.format(result_avg))

		#Annoter le nombre de voyageur par pays avec annotation
		venant_de_stats = model.objects.values(name=Lower('venant_de')).annotate(count=ExpressionWrapper(Count('venant_de') / model.objects.count()*100, output_field= DecimalField()))
		allant_a_stats = model.objects.values(name=Lower('allant_a')).annotate(count=ExpressionWrapper(Count('venant_de') / model.objects.count()*100, output_field= DecimalField()))

		#GROUP_BY tres important dans le template
		line_year_chart = model.objects.annotate(year=ExtractYear('date_enregistrement')).values('year', 'genre').annotate(Count('genre')).order_by('-year')
		gender_repartition = model.objects.values('genre').annotate(nombre=Count('genre'))

		return render(request, 'stats/stats.html', {
			'bar_chart_data':context, 
			'pie_venant_de': json.dumps(self.create_doughnut_json(venant_de_stats, 'Diagramme de secteur des voyageurs entrants')),
			'pie_allant_a': json.dumps(self.create_doughnut_json(allant_a_stats, 'Diagramme de secteur des voyageurs sortants')),
			'year_avg': year_avg,
			'total_form': model.objects.count(),
			'genre_repartition': gender_repartition,
		})
	
	def create_doughnut_json(self, queryset, title):
		config = {
			'type': 'doughnut',
			'data': {
				'datasets': [{
					'data': [],
					'backgroundColor': [],
					'label': 'Taux de voyageur'
				}],
				'labels': []
			},
			'options': {
				'responsive': True,
				'legend': {
					'position': 'top',
				},
				'title': {
					'display': True,
					'text': title,
				},
				'animation': {
					'animateScale': True,
					'animateRotate': True
				}
			}
		}

		r = lambda: random.randint(0, 255)
		for obj in queryset:
			config['data']['datasets'][0]['data'].append(float('{0:.2f}'.format(obj['count'])))
			config['data']['labels'].append(obj['name'])
			config['data']['datasets'][0]['backgroundColor'].append('#%02X%02X%02X' %( r(), r(), r()))
		return config




	


