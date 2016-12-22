import django_tables2 as tables
from .models import Drink

class DrinkTable(tables.Table):
    class Meta:
        model= Drink
        attrs = {'class': 'paleblue'}
