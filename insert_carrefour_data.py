import json
from tables.models import Table, TableBrand

def insert_data():
    with open('carrefour.json', 'r') as f:
        data = json.load(f)
        carrefour = TableBrand.objects.filter(name='Carrefour').first()
        table_objects = [Table(brand=carrefour, **t) for t in data]
        Table.objects.bulk_create(table_objects)

