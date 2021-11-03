from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm
from .decorators import allowed_users
# Create your views here.

def home(request):
	context = {}
	return render(request, 'publications/home.html', context)

@login_required(login_url='login')
def Publications(request):
	return render(request, 'publications/publications.html')

def registerPage(request):
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, user + ', sua conta foi criada com sucesso!')

			return redirect('login')

	context = {'form': form}
	return render(request, 'publications/register.html', context)

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

def logoutUser(request):
	logout(request)
	return redirect('login')