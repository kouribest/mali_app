from django.test import TestCase
from random import choice, randint
from mali.models import MaliModel as mali
from mali.forms import FormML
from mali_project.models import Domain as dm, randomStringDigits
from datetime import datetime, timedelta, tzinfo
from django_countries import countries
from django.utils import timezone
from django.forms.models import model_to_dict
from django.test import Client
import requests, json


class TestViews(TestCase):

	def setUp(self):
		self.client = Client()	
		login = os.environ.get('DJANGO_ADMIN_USERNAME')
		password = os.environ.get('DJANGO_ADMIN_PASSWORD')

	def test_home_view(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)