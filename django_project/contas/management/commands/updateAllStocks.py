from django.core.management.base import BaseCommand, CommandError
from contas.models import Stock, HistoricalStock
from contas.mineracao import*
import datetime


class Command(BaseCommand):

	def handle(self, *args, **options):
		number_of_stocks = Stock.objects.all()
		for stock in number_of_stocks:
			stock_name = stock.nome
			stock_selecionado = Stock.objects.get(nome=stock_name)
			ultima_data = str(stock_selecionado.dados_historicos.last().data)
			data_atual = str(datetime.date.today())

			if (data_atual != ultima_data):
				dataFrame = downloadAcao(stock_name,ultima_data).values
				for i in range(0,len(dataFrame)):
					data_dataFrame = datetime.datetime.strptime(dataFrame[i][0], "%Y-%m-%d").date()
					new_historical = HistoricalStock.objects.create_historical(data=data_dataFrame,maximo=dataFrame[i][1],minimo=dataFrame[i][2],abertura=dataFrame[i][3],fechamento=dataFrame[i][4],volume=dataFrame[i][5],fechamento_ajustado=dataFrame[i][6],mes=dataFrame[i][11],ano=dataFrame[i][12])
					new_historical.save()
					stock_selecionado.dados_historicos.add(new_historical)
					stock_selecionado.save()
					print('HistoricalStock '+str(data_dataFrame)+' add successfully.')
			else:
				print('Stock '+str(Stock.objects.get(nome=stock_name).pk)+' already been updated.')

