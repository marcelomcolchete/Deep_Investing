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
    path('stock/', views.listagem_stocks, name='url_stocks'),
# -- Stocks -- #
    path('stock/<str:stock_name>', views.stock_resumo),
    path('stock/<str:stock_name>/dados_historicos', views.stock_dados_historicos),
    path('stock/<str:stock_name>/resumo', views.stock_resumo)
]