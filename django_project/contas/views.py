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
			return redirect('url_register')
		except User.DoesNotExist:
			username_user = None
		try:
			email_user = User.objects.get(email=email)
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
		user = authenticate(username=username_login,password=password_login)
		if user is not None:
			login(request,user)
			#render(request,'contas/index.html',data)
			return redirect('url_home')
		else:
			messages.error(request, 'Usuário e senha inválidos. Favor tentar novamente.')
	return redirect('url_login')

def pagina_logout(request):
	data={}
	logout(request)
	render(request,'contas/login.html',data)
	return redirect('url_login')

def listagem_stocks(request):
	data={}
	return render(request,'contas/listagem_stocks.html',data)

# -- Stocks -- #

def stock_dados_historicos(request,stock_name):
	data={}
	stock_selecionado = Stock.objects.get(nome=stock_name)
	ultimo_stock = stock_selecionado.dados_historicos.all().last()
	ultimo_stock_dia_anterior1 = stock_selecionado.dados_historicos.all().reverse()[1:2][0].fechamento_ajustado
	stock_dados_historicos = stock_selecionado.dados_historicos.all().reverse()
	ultimo_fechamento_ajustado = ultimo_stock.fechamento_ajustado
	diferenca_abertura_fechamento = round(ultimo_fechamento_ajustado - ultimo_stock_dia_anterior1,2)
	diferenca_porcentagem = round((diferenca_abertura_fechamento*100)/ultimo_stock_dia_anterior1,2)

	# Passagem de data pro navegador

	data['stock_name'] = stock_selecionado.nome
	data['historical_stock'] = stock_dados_historicos

	data['stock_last_price'] = round(ultimo_fechamento_ajustado,2)
	data['stock_last_open'] = round(ultimo_stock.abertura,2)
	data['stock_last_max'] = round(ultimo_stock.maximo,2)
	data['stock_last_min'] = round(ultimo_stock.minimo,2)
	data['stock_last_volume'] = round(ultimo_stock.volume,2)

	data['stock_diference'] = diferenca_abertura_fechamento
	data['stock_diferecen_percent'] = diferenca_porcentagem

	return render(request,'contas/stocks/dados_historicos.html',data)

def stock_resumo(request,stock_name):
	data={}
	stock_selecionado = Stock.objects.get(nome=stock_name)
	ultimo_stock = stock_selecionado.dados_historicos.all().last()
	ultimo_stock_dia_anterior1 = stock_selecionado.dados_historicos.all().reverse()[1:2][0].fechamento_ajustado
	stock_dados_historicos = stock_selecionado.dados_historicos.all().reverse()[0:60]
	ultimo_fechamento_ajustado = ultimo_stock.fechamento_ajustado
	diferenca_abertura_fechamento = round(ultimo_fechamento_ajustado - ultimo_stock_dia_anterior1,2)
	diferenca_porcentagem = round((diferenca_abertura_fechamento*100)/ultimo_stock_dia_anterior1,2)

	# Passagem de data pro navegador

	data['stock_name'] = stock_selecionado.nome
	data['historical_stock'] = stock_dados_historicos

	data['stock_last_price'] = round(ultimo_fechamento_ajustado,2)
	data['stock_last_open'] = round(ultimo_stock.abertura,2)
	data['stock_last_max'] = round(ultimo_stock.maximo,2)
	data['stock_last_min'] = round(ultimo_stock.minimo,2)
	data['stock_last_volume'] = round(ultimo_stock.volume,2)

	data['stock_diference'] = diferenca_abertura_fechamento
	data['stock_diferecen_percent'] = diferenca_porcentagem

	return render(request,'contas/stocks/resumo.html',data)