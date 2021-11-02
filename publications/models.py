from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
	DIRETORIA = 'DI'
	COORDENADOR = 'CO'
	ASSOCIADO = 'AS'
	REGISTRADO = 'RE'

	USER_TYPE_CHOICE = [
		(DIRETORIA, 'Diretoria'),
		(COORDENADOR, 'Coordenador'),
		(ASSOCIADO, 'Associado'),
		(REGISTRADO, 'Registrado')
	]
	user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICE, default=REGISTRADO)
