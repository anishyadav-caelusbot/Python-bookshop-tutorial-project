# Create your models here.
from django.db import models
class customers(models.Model):
	customerid=models.CharField(max_length=200)
	name=models.CharField(max_length=200)
	address=models.TextField()
	city=models.TextField()
	state=models.TextField()
	zipcode=models.IntegerField()
	country=models.TextField()


class orders(models.Model):
	orderid=models.IntegerField()
	customerid=models.TextField()
	amount=models.IntegerField()
	date=models.TextField()
	order_status=models.TextField()
	ship_name=models.TextField()
	ship_address=models.IntegerField()
	ship_city=models.TextField()
	ship_state=models.TextField()
	ship_zip=models.IntegerField()
	ship_country=models.TextField()

class books(models.Model):
	isbn=models.TextField()
	author=models.TextField()
	title=models.TextField()
	catid=models.TextField()
	price=models.TextField()
	description=models.TextField()

class categories(models.Model):
	catid=models.TextField()
	catname=models.TextField()

class order_items(models.Model):
	orderid=models.TextField()
	isbn=models.TextField()
	item_price=models.TextField()
	quantity=models.TextField()
	primary_key=models.TextField()



