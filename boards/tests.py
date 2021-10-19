from django.test import TestCase
from django.urls import reverse
from django.urls import resolve
from .views import home, board_topics, new_topic
from .models import Board 

# Create your tests here.

class HomeTests(TestCase):
	def setUp(self):
		self.board = Board.objects.create(name='Django', description='Django board.')
		url = reverse('home')
		self.response = self.client.get(url)

	# Este es un caso de prueba muy simple pero extremadamente útil. 
	# Estamos probando el código de estado de la respuesta. El código de estado 200 significa éxito.	
	def test_home_view_status_code(self):
		self.assertEquals(self.response.status_code, 200)	
		
	# En la segunda prueba, estamos haciendo uso de la función de resolución. 
	# Django la utiliza para hacer coincidir una URL solicitada con una lista de URLs listadas en el módulo urls.py. 
	# Esta prueba se asegurará de que la URL /, que es la URL raíz, devuelva la vista de inicio.
	def test_home_url_resolves_home_view(self):
		view = resolve('/')
		self.assertEquals(view.func, home)
		
	def test_home_view_contains_link_to_topics_page(self):
		board_topics_url = reverse('board_topics', kwargs={'pk':self.board.pk})
		self.assertContains(self.response, 'href="{0}"'.format(board_topics_url)) # Si la respuesta del body contiene el texto proporcionado.

class BoardTopicsTests(TestCase):
	def setUp(self):
		Board.objects.create(name='Django', description='Django board.') # Crea una instancia de Board para usar en el test. Django no corre test sobre la base de datos en uso. Crea una nueva base de datos al vuelo, aplica las migraciones de los modelos, corre el test y destruye la base de datos.

	# Testea si devuelve un estado 200 para un tablero existente.
	def test_board_topics_view_success_status_code(self):
		url = reverse('board_topics', kwargs={'pk': 1})
		response = self.client.get(url)
		self.assertEquals(response.status_code, 200)

	# Testea si devuelve un estado 404 para un tablero que no existe.
	def test_board_topics_view_not_found_status_code(self):
		url = reverse('board_topics', kwargs={'pk': 99})
		response = self.client.get(url)
		self.assertEquals(response.status_code, 404)

	# Testea si Django una la funcion correcta de vista para renderisar los topics.
	def test_board_topics_url_resolves_board_topics_view(self):
		view = resolve('/boards/1/')
		self.assertEquals(view.func, board_topics)

	def test_board_topics_view_contains_link_back_to_homepage(self):
		board_topics_url = reverse('board_topics', kwargs={'pk': 1})
		response = self.client.get(board_topics_url)
		homepage_url = reverse('home')
		self.assertContains(response, 'href="{0}"'.format(homepage_url))

class NewTopicTests(TestCase):
    def setUp(self):
        Board.objects.create(name='Django', description='Django board.')

    # Revisa si la petición a la vista (view) es exitosa
    def test_new_topic_view_success_status_code(self):
        url = reverse('new_topic', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    # Revisa si la vista levanta un error 404 si el tablero no existe    
    def test_new_topic_view_not_found_status_code(self):
        url = reverse('new_topic', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    # Revisa si la vista correcta esta en uso
    def test_new_topic_url_resolves_new_topic_view(self):
        view = resolve('/boards/1/new/')
        self.assertEquals(view.func, new_topic)

    # Se asegura que puedas regresar a la lista de tops
    def test_new_topic_view_contains_link_back_to_board_topics_view(self):
        new_topic_url = reverse('new_topic', kwargs={'pk': 1})
        board_topics_url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(new_topic_url)
        self.assertContains(response, 'href="{0}"'.format(board_topics_url))
