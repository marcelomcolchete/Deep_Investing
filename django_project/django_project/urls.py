"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import contas.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.user_home, name='url_home'),
    path('index', views.home, name='url_index'),
    path('contact', views.contact),
    path('news', views.news),
    path('about', views.about),
    path('register/', views.pagina_register, name='url_register'),
    path('register/submit', views.submit_register),
    path('login/', views.pagina_login, name='url_login'),
    path('login/submit', views.submit_login),
    path('logout',views.pagina_logout),
    path('user', views.user_perfil, name='url_perfil'),
    # -- Stocks -- #
    path('stock/', views.listagem_stocks, name='url_stocks'),
    path('stock/BIDI4.SA', views.BIDI4_resumo),
    path('stock/BIDI4.SA/dados_historicos', views.BIDI4_dados_historicos),
    path('stock/BIDI4.SA/resumo', views.BIDI4_resumo)
]
