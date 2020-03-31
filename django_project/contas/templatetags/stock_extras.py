from django import template
from contas.models import Stock

register = template.Library()

@register.filter
def stock_list(value):
	stocks = list()
	for stock in Stock.objects.all():
		stocks.append(stock.nome)
	return stocks