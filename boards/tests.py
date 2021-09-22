from django.test import TestCase
from django.urls import reverse
from django.urls import resolve
from .views import home

# Create your tests here.

class HomeTests(TestCase):
	def test_home_view_status_code(self):
		url = reverse('home')
		response = self.client.get(url)
		self.assertEquals(response.status_code, 200)
	"""
	Este es un caso de prueba muy simple pero extremadamente útil. Estamos probando el código de estado de la respuesta. El código de estado 200 significa éxito.
	"""		
	def test_home_url_resolves_home_view(self):
		view = resolve('/')
		self.assertEquals(view.func, home)
	"""
	En la segunda prueba, estamos haciendo uso de la función de resolución. Django la utiliza para hacer coincidir una URL solicitada con una lista de URLs listadas en el módulo urls.py. Esta prueba se asegurará de que la URL /, que es la URL raíz, devuelva la vista de inicio.
	"""		