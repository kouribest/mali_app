from mali_project.models import Domain


class CurrentDomainMiddleware(object):
	def process_request(self, request):
		"""Tldextract module return the hostaddress as list of named tuple.
		   The hostaddress is searched trougth the database
		"""
		try:
				request.subdomain= Domain.objects.get_current(request)
		except:
				request.subdomain= ''
		return None