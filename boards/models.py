from django.db import models
from django.contrib.auth.models import User
# Cada clase será transformada en tablas de base de datos y serán traducidos en columnas. 

# Create your models here.

class Board(models.Model):
	name = models.CharField(max_length=30, unique=True) # unique=TRUE: obliga a que el campo sea único a nivel de base de datos.
	description = models.CharField(max_length=100) # max_length: que tan grande debe ser la columna. Validar lo que ingrese el usuario
	def __str__(self):
		return self.name

class Topic(models.Model):
	subject = models.CharField(max_length=255)
	last_updated = models.DateTimeField(auto_now_add=True)# auto_now_add=True: debe colocar la fecha y hora actual cuando una entrada es creada
	board = models.ForeignKey(Board, related_name='topics', on_delete=models.CASCADE)
	"""
	ForeignKey: este creará un enlace entre los modelos y una relación apropiada a nivel de base de datos. Por ejemplo, en el modelo Topic, el campo board es una llave foránea al modelo Board. Esto de le dice a Django que una instancia de Topic se relaciona solo con una instancia de Board.
	related_name: será usado para crear una relación inversa donde las instancias de Board tendrán acceso a una lista de instancias de Topic que le pertenecerán
	""" 
	starter = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)

class Post(models.Model):
	message = models.TextField(max_length=4000)
	topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(null=True)
	created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
	updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE) # updated_by field establece related_name=’+’. Esto le indica a Django que no necesitamos esta relación inversa para que la ignore. 	

