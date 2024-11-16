from django.test import TestCase, Client
from django.urls import reverse
from products.models import Product

class CheckoutViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.product = Product.objects.create(
            name="Rose Bouquet",
            price=29.99,
            sku="rose001"
        )
        self.checkout_url = reverse('checkout')

    def test_checkout_page_loads(self):
        response = self.client.get(self.checkout_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')

