from django.http import HttpResponse
from django.shortcuts import redirect, render

def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('home')
		else:
			return view_func(request, *args, **kwargs)
	return wrapper_func

def allowed_user(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):

			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name
			if group in allowed_roles:
				return view_func(request, *args, **kwargs)
			else:
				return render(request, 'publications/no_permission.html')
		return wrapper_func
	return decorator

def registre_dec(view_func):
	def wrapper_func(request, *args, **kwargs):
		group = None
		if request.user.groups.exists:
			group = request.user.groups.all()[0].name
			context = {'group': group}

		if group == 'Registrado':
			return view_func(request, *args, **kwargs)
		else:
			return render(request, 'publications/already.html', context)
	return wrapper_func