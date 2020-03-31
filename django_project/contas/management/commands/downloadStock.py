from django.core.management.base import BaseCommand, CommandError
from contas.models import Stock, HistoricalStock
from contas.mineracao import*

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('stock_name', type=str)

    def handle(self, *args, **options):
        stock_name = options['stock_name']
        dataFrame = downloadAcao(stock_name,0).values
        new_stock = Stock.objects.create_stock(nome=stock_name,dataFrame=dataFrame)
        new_stock.save()
        print('Stock '+str(Stock.objects.get(nome=stock_name).pk)+' created.')
