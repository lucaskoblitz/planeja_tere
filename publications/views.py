from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic.edit import CreateView

from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group

from .models import Publication
from .forms import CreateUserForm, CreateWaitingPost
from .decorators import unauthenticated_user, allowed_user, registre_dec
# Create your views here.

def is_registrado(user):
	return user.groups.filter(name='Registrado')

def home(request):
	context = {}
	return render(request, 'publications/home.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['Diretoria', 'Coordenação'])
def Publications(request):
	return render(request, 'publications/publications.html')

@unauthenticated_user
def registerPage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='Registrado')
			user.groups.add(group)

			messages.success(request, username + ', sua conta foi criada com sucesso!')

			return redirect('login')

	context = {'form': form}
	return render(request, 'publications/register.html', context)

@unauthenticated_user
def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Usuário ou senha incorretos')
	context = {}
	return render(request, 'publications/login.html', context)

@login_required(login_url='login')
@registre_dec
def sejaAssociado(request):
	group = request.user.groups.all()[0].name
	context = {'group': group}
	return render(request, 'publications/beassociated.html', context)


class solicitar_pub(CreateView):
	form_class = CreateWaitingPost
	model = Publication
	template_name = 'publications/solicitar_pub.html'

def logoutUser(request):
	logout(request)
	return redirect('login')
