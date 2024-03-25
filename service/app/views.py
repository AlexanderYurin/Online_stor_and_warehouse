from collections import defaultdict

from django.db.models import Prefetch
from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect, render
from django.views import View

from app.models import OrderItems, Product, ProductPlacement


# Create your views here.


class get_total_orders(View):
	def get(self, request: HttpRequest) -> HttpResponse:
		orders_ids = map(int, request.GET.keys())

		data = OrderItems.objects.filter(order_id__in=orders_ids).select_related("order").prefetch_related(
			Prefetch("product", queryset=Product.objects.prefetch_related("product_placements"))
		)
		if not data.exists():
			return render(request, "main.html", context={"no_order": "Заказы отсутствуют!"})

		order = defaultdict(list)
		for product in data:
			id_product = product.product.id
			product_title = product.product.title
			quantity = product.quantity
			order_id = product.order.id
			racks = product.product.product_placements.all()
			if racks.exists():
				main_rack = ""
				additional_rack = []
				for i in range(len(racks)):
					if racks[i].main_rack:
						main_rack = racks[i].rack
					additional_rack.append(racks[i].rack)
				order[main_rack].append((id_product, quantity, product_title, order_id, ", ".join(additional_rack)))

		return render(request, "main.html", context={"order": order.items()})
