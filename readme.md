




## Automatic Tests

This project includes automated tests to ensure the functionality of the **checkout page** and **Stripe integration**. The tests validate both frontend and backend components, including Stripe payment processing.

The test suite uses Django's built-in testing framework (`django.test`) and covers the following:

- **Checkout Page**: Verifies that the checkout page loads correctly.
- **Stripe Integration**: Ensures the correct Stripe keys are used, and that API calls to Stripe are functional.

### Checkout Page Tests

The `CheckoutViewsTestCase` class tests the **checkout page** rendering.

#### Test: `test_checkout_page_loads`
Verifies that the checkout page:
- Returns a status code of `200` (OK).
- Uses the correct template (`checkout/checkout.html`).

### Stripe Integration Tests

The `StripeIntegrationTest` class ensures that Stripe integration is working as expected, including verifying the **public** and **secret keys**.

#### Test: `test_stripe_secret_key_valid`
Verifies the **secret key** by making a simple `PaymentIntent` API call to Stripe. It checks:
- The request successfully creates a `PaymentIntent` with the correct amount and currency.
- If authentication fails, the test will raise an `AuthenticationError`.

#### Test: `test_stripe_public_key_valid`
Checks if the **public key** is valid by simulating a `PaymentIntent` creation on the frontend. It verifies that the public key starts with `pk_test_` or `pk_live_` as expected for Stripe keys.

#### Test: `test_stripe_keys_integrated`
Combines `test_stripe_secret_key_valid` and `test_stripe_public_key_valid` to ensure both keys are properly integrated.

#### Test: `test_invalid_public_key`
Checks if an invalid **public key** results in a `StripeError` when attempting to create a `PaymentIntent`.

