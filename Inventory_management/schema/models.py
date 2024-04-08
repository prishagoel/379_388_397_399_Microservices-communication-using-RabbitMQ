from django.db import models

class Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)

dummy_items = [
    {'item': 'laptop', 'quantity': 10},
    {'item': 'printer', 'quantity': 5},
    {'item': 'keyboard', 'quantity': 8},
    {'item': 'monitors', 'quantity': 20},
    {'item': 'tablet', 'quantity': 15},
]

for order_data in dummy_items:
    Inventory.objects.create(**order_data)

class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

dummy_items = [
    {'item': 'laptop', 'quantity': 2},
    {'item': 'printer', 'quantity': 3},
    {'item': 'keyboard', 'quantity': 1},
    {'item': 'monitors', 'quantity': 5},
    {'item': 'tablet', 'quantity': 6},
]

for order_data in dummy_items:
    Orders.objects.create(**order_data)
