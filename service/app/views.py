from collections import defaultdict

from django.db.models import Prefetch
from django.shortcuts import redirect, render
from django.views import View

from app.models import OrderItems, Product, ProductPlacement


# Create your views here.


class get_total_orders(View):
	def get(self, request):
		orders_ids = map(int, request.GET.keys())

		data = OrderItems.objects.filter(order_id__in=orders_ids).select_related("order").prefetch_related(
			Prefetch("product", queryset=Product.objects.prefetch_related("product_placements"))
		)
		order = defaultdict(list)
		for product in data:
			id_product = product.product.id
			product_title = product.product.title
			quantity = product.quantity
			order_id = product.order.id
			racks = product.product.racks.all()
			if racks.exists():
				subracks = " ".join(filter(lambda x: not x.main, racks))
				order[next(filter(lambda x: x.main, racks))].append((id_product, quantity, product_title, order_id, subracks))

		return render(request, "main.html", context={"order": order.items()})
