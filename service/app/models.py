from django.db import models


class Product(models.Model):
	title = models.CharField(max_length=50)
	price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)

	def __str__(self):
		return self.title


class Rack(models.Model):
	title = models.CharField(max_length=50)
	product = models.ForeignKey(to=Product, on_delete=models.CASCADE, related_name="racks")
	main = models.BooleanField(default=False)
	quantity = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.title


class Order(models.Model):
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.pk}"


class OrderItems(models.Model):
	order = models.ForeignKey(to=Order, on_delete=models.CASCADE, related_name="order")
	product = models.ForeignKey(to=Product, on_delete=models.SET_NULL, null=True)
	quantity = models.PositiveIntegerField(default=0)

	def __str__(self):
		return f"{self.pk}"
