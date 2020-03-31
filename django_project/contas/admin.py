from django.contrib import admin
from .models import Stock, HistoricalStock

admin.site.register(HistoricalStock)
admin.site.register(Stock)

# Register your models here.
