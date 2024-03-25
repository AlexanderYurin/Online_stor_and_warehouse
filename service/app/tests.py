from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class YourTestCase(TestCase):
	fixtures = ["data.json"]

	def test_get_total_no_orders(self):
		response = self.client.get(reverse("main"))

	def test_get_total_orders(self):
		response = self.client.get(reverse("main"), data={1: "1"})
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "заказ №1")
