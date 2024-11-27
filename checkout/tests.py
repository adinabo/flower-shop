import stripe
from django.test import TestCase, Client
from django.urls import reverse
from products.models import Product
from django.conf import settings
from stripe.error import AuthenticationError, StripeError

from django.contrib.auth.models import User

class CheckoutViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.product = Product.objects.create(
            name="Rose Bouquet",
            price=29.99,
            sku="rose001"
        )
        self.checkout_url = reverse('checkout')

        # Create and log in a user if authentication is required
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')

    def test_checkout_page_loads(self):
        response = self.client.get(self.checkout_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')


class StripeIntegrationTest(TestCase):
    def setUp(self):
        """
        This will run before each test. 
        """
        stripe.api_key = settings.STRIPE_SECRET_KEY  
        self.public_key = settings.STRIPE_PUBLIC_KEY  

    def test_stripe_secret_key_valid(self):
        """
        Test if the secret key is valid by making a simple API call to create a PaymentIntent.
        """
        try:
            # Create a test PaymentIntent with the secret key
            payment_intent = stripe.PaymentIntent.create(
                amount=1000,  # $10.00
                currency="usd",
                payment_method_types=["card"],
            )
            # Check if the PaymentIntent is created successfully
            self.assertEqual(payment_intent['currency'], 'usd')
            self.assertEqual(payment_intent['amount'], 1000)
        except AuthenticationError:
            self.fail("Invalid secret key - Authentication failed.")
        except StripeError as e:
            self.fail(f"Stripe API error occurred: {e}")

    def test_stripe_public_key_valid(self):
        """
        Test if the public key is valid by making a test API call for client-side integration.
        """
        try:
            # For public key, the test will only simulate creating a PaymentIntent on the client side
            # This would generally be tested in frontend JavaScript, but we can simulate the interaction.
            stripe_public_key = self.public_key
            self.assertIsNotNone(stripe_public_key)
            self.assertTrue(stripe_public_key.startswith('pk_test_') or stripe_public_key.startswith('pk_live_'))
        except AuthenticationError:
            self.fail("Invalid public key - Authentication failed.")
        except StripeError as e:
            self.fail(f"Stripe API error occurred: {e}")

    def test_stripe_keys_integrated(self):
        """
        Test both the public and secret keys to ensure they are correctly set up and integrated.
        """
        self.test_stripe_secret_key_valid()
        self.test_stripe_public_key_valid()

    def test_invalid_public_key(self):
        """
        Test if an invalid public key results in an error.
        """
        invalid_public_key = "pk_test_invalidkey123"
        stripe.api_key = invalid_public_key

        # Test if the invalid public key causes an error when creating a PaymentIntent
        with self.assertRaises(StripeError):
            stripe.PaymentIntent.create(
                amount=1000,
                currency="usd",
                payment_method_types=["card"],
            )
            
