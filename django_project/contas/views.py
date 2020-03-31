# Funções e classes do Django

from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import AnonymousUser
from .models import Stock, HistoricalStock

# Funções e classes do Deep Investing

from .bolsa import*
from .mineracao import*
from .leitura import*
from .tratamento import* 

# Funções e classes do python

import datetime
import os
import pandas as pd # Biblioteca de ciência de dados https://pandas.pydata.org/pandas-docs/stable/

# Definições

User = get_user_model()
@csrf_protect

# Funções de redirecionamento do site

def home(request):
	data = {}
	return render(request, 'contas/index.html', data)

def user_home(request):
	data = {}
	return render(request,'contas/home.html', data)

def about(request):
	data = {}
	return render(request, 'contas/about.html', data)

def contact(request):
	data = {}
	data['stocks'] = list()
	for stock in Stock.objects.all():
		data['stocks'].append(stock.nome)
	return render(request, 'contas/contact.html', data)

def news(request):
	data = {}
	return render(request, 'contas/news.html', data)

def user_perfil(request):
	# Precisa editar ainda
	data = {}
	return render(request, 'contas/user.html', data)

def pagina_register(request):
	data = {}
	return render(request, 'contas/register.html', data)

def submit_register(request):
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		email = request.POST.get('email')
		try:
			username_user = User.objects.get(username=username)
			print('Username já cadastrado')
			return redirect('url_register')
		except User.DoesNotExist:
			username_user = None
		try:
			email_user = User.objects.get(email=email)
			print('Email já cadastrado')
			return redirect('url_register')
		except Exception as e:
			email_user = None

		new_user = User.objects.create_user(username, email, password)
		new_user.save()
		return redirect('url_login')

def pagina_login(request):
	data = {}
	return render(request, 'contas/login.html', data)

def submit_login(request):
	data = {}

	if request.POST:
		username_login = request.POST.get('username')
		password_login = request.POST.get('password')
		print(username_login)
		print(password_login)
		user = authenticate(username=username_login,password=password_login)
		print(user)
		if user is not None:
			print('Logou')
			login(request,user)
			render(request,'contas/index.html',data)
			return redirect('url_index')
		else:
			messages.error(request, 'Usuário e senha inválidos. Favor tentar novamente.')
			print('Nao logou')
	return redirect('url_login')

def pagina_logout(request):
	data={}
	logout(request)
	render(request,'contas/login.html',data)
	return redirect('url_login')

# -- Stocks --

def listagem_stocks(request):
	data={}
	return render(request,'contas/listagem_stocks.html',data)

def BIDI4(request):
	data={}
	stock_selecionado = Stock.objects.get(nome='BIDI4.SA')
	data['stock_name'] = "BIDI4.SA"
	data['historical_stock'] = stock_selecionado.dados_historicos.all()
	return render(request,'contas/BIDI4.SA.html',data)

def VALE3(request):
	data={}
	stock_selecionado = Stock.objects.get(nome='VALE3.SA')
	data['stock_name'] = "VALE3.SA"
	data['historical_stock'] = stock_selecionado.dados_historicos.all()
	return render(request,'contas/VALE3.SA.html',data)