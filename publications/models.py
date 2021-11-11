from django.db import models
# Create your models here.

class Publication(models.Model):
	title = models.CharField(max_length=25)
	post = models.TextField(max_length=400)
	author = models.CharField(max_length=35, default='Anonimus')

	def get_absolute_url(self):
		return '/post_com_sucesso/'

	def __str__(self):
		return self.title