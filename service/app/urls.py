from django.urls import path

from app.views import get_total_orders

urlpatterns = [
    path("", get_total_orders.as_view(), name="main"),
]