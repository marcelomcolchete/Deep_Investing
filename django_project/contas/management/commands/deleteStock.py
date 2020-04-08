from django.core.management.base import BaseCommand, CommandError
from contas.models import Stock, HistoricalStock
from contas.mineracao import*


class Command(BaseCommand):

	def add_arguments(self, parser):
		parser.add_argument('stock_name', type=str)

	def handle(self, *args, **options):
		stock_name = options['stock_name']
		stock_selecionado = Stock.objects.get(nome=stock_name)
		dados_historicos = stock_selecionado.dados_historicos.all()
		for dado in dados_historicos:
			dado.delete()
		stock_selecionado.delete()
		print('Stock '+str(stock_name)+' deleted.')

