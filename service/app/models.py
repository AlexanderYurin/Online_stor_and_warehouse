from django.core.exceptions import ValidationError
from django.db import models


class Product(models.Model):
	title = models.CharField(max_length=50)

	def __str__(self):
		return self.title


class ProductPlacement(models.Model):
	rack = models.CharField(max_length=50)
	product = models.ForeignKey(to=Product, on_delete=models.CASCADE, related_name="product_placements")
	main_rack = models.BooleanField(default=True)
	quantity = models.PositiveIntegerField(default=0)

	def __str__(self):
		answer = "Главный"
		if not self.main_rack:
			answer = "Дополнительный"
		return f"{self.product.title} на Стеллаже {self.rack} {answer}"

	def clean(self):
		if self.main_rack and ProductPlacement.objects.filter(product=self.product, main_rack=True).exists():
			raise ValidationError(
				"Только один стеллаж может быть главным для каждого продукта."
			)

	class Meta:
		unique_together = (("rack", "product", "main_rack"),)


class Order(models.Model):
	def __str__(self):
		return f"{self.pk}"


class OrderItems(models.Model):
	order = models.ForeignKey(to=Order, on_delete=models.CASCADE, related_name="order")
	product = models.ForeignKey(to=Product, on_delete=models.SET_NULL, null=True)
	quantity = models.PositiveIntegerField(default=0)

	def __str__(self):
		return f"{self.pk}"
