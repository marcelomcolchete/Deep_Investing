from django.db import models
import datetime

class HistoricalStockManager(models.Manager):
	def create_historical(self,data,maximo,minimo,abertura,fechamento,volume,fechamento_ajustado,mes,ano):
		historical_stock = self.create(data=data,maximo=maximo,minimo=minimo,abertura=abertura,fechamento=fechamento,volume=volume,fechamento_ajustado=fechamento_ajustado,mes=mes,ano=ano)
		return historical_stock

class HistoricalStock(models.Model):
	data = models.DateField()
	maximo = models.FloatField()
	minimo = models.FloatField()
	abertura = models.FloatField()
	fechamento = models.FloatField()
	volume = models.IntegerField()
	fechamento_ajustado = models.FloatField()
	mes = models.IntegerField()
	ano = models.IntegerField()

	objects = HistoricalStockManager()

	def __str__(self): 
		return str(self.data)+" | "+str(self.abertura)

	class Meta:
		ordering = ['data']

class StockManager(models.Manager):
	def create_stock(self,nome,dataFrame):
		new_stock = self.create(nome=nome)
		dados_historicos = list()
		for i in range(0,len(dataFrame)):
			data_dataFrame = datetime.datetime.strptime(dataFrame[i][0], "%Y-%m-%d").date()
			new_historical = HistoricalStock.objects.create_historical(data=data_dataFrame,maximo=dataFrame[i][1],minimo=dataFrame[i][2],abertura=dataFrame[i][3],fechamento=dataFrame[i][4],volume=dataFrame[i][5],fechamento_ajustado=dataFrame[i][6],mes=dataFrame[i][11],ano=dataFrame[i][12])
			new_historical.save()
			new_stock.dados_historicos.add(new_historical)
		return new_stock

class Stock(models.Model):
	nome = models.CharField(max_length=10)
	dados_historicos = models.ManyToManyField(HistoricalStock)
	objects = StockManager()

	def __str__(self): 
		return self.nome