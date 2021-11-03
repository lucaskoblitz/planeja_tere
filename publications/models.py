from django.db import models

# Create your models here.

class Publication(models.Model):
	title = models.CharField(max_length=25)
	post = models.TextField(max_length=400)

