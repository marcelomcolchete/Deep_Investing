from django.core.management.base import BaseCommand, CommandError
from contas.models import Stock, HistoricalStock
from contas.mineracao import*


class Command(BaseCommand):

	def handle(self, *args, **options):
		number_of_stocks = Stock.objects.count()
		while Stock.objects.count():
			ids = Stock.objects.values_list('pk', flat=True)[:100]
			Stock.objects.filter(pk__in = ids).delete()

		while HistoricalStock.objects.count():
			ids = HistoricalStock.objects.values_list('pk', flat=True)[:100]
			HistoricalStock.objects.filter(pk__in = ids).delete()
		print('All '+str(number_of_stocks)+' deleteds.')
