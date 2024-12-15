
## Challenges encountered
Once challenging mileston in my project was setting up the AWS bucket for statics. The issue here was mainly with the products as it took me a while to notice that when uploading a product using admin, it was changing the actual name of the file, making it different than what I had in the bucket. So with every product uploaded, I would have one name in admin, then one name in my bucket, both different than what I've uploaded. I have't found the cause, but I've manually changed that to make sure my product image is displaying correctly.


## Automated Tests

This project includes automated tests to ensure the correct functionality of the **checkout page** and **Stripe integration**. The tests cover both frontend and backend components, including the Stripe payment processing logic.

The test suite uses Django's built-in testing framework (`django.test`) and covers the following areas:

- **Checkout Page**: Verifies that the checkout page renders correctly.
- **Stripe Integration**: Ensures the correct Stripe keys are being used, and that API calls to Stripe are functional.

### Checkout Page Tests

The `CheckoutViewsTestCase` class tests the **checkout page** rendering.

#### Test: `test_checkout_page_loads`
Verifies that the checkout page:
- Returns a status code of `200` (OK).
- Uses the correct template (`checkout/checkout.html`).

### Stripe Integration Tests

The `StripeIntegrationTest` class ensures that the integration with Stripe works as expected, including validating the **public** and **secret keys**.

#### Test: `test_stripe_secret_key_valid`
Validates the **secret key** by making a `PaymentIntent` API call to Stripe. It checks:
- The request successfully creates a `PaymentIntent` with the correct amount and currency.
- If authentication fails, the test raises an `AuthenticationError`.

#### Test: `test_stripe_public_key_valid`
Checks if the **public key** is valid by simulating the creation of a `PaymentIntent` on the frontend. It verifies that the public key starts with `pk_test_` or `pk_live_` as expected for Stripe keys.

#### Test: `test_stripe_keys_integrated`
Combines `test_stripe_secret_key_valid` and `test_stripe_public_key_valid` to ensure both keys are properly integrated.

#### Test: `test_invalid_public_key`
Verifies that an invalid **public key** results in a `StripeError` when attempting to create a `PaymentIntent`.

### Stripe Elements Tests

The Stripe Elements tests ensure the correct behavior of the **Stripe Elements** integration:

- **Stripe Initialization**: Ensures that the Stripe object is correctly initialized with the public key from the backend (Django).
- **Element Creation**: Validates that the `card` element is created using the mocked `elements.create` method.
- **Element Mounting**: Confirms that the `mount` function is called with the correct DOM element (`#card-element`), simulating the mounting of the payment form.

### Mocking Stripe API

Since Jest runs in a Node.js environment and cannot interact with the actual Stripe API or load static files like `stripe_elements.js`, the **Stripe API** is **mocked** using Jest's mock functions. This allows us to simulate Stripe Elements' behavior and test the integration logic without making real API calls or loading external resources.

The tests can be run using the following command:

```bash
npx jest


All images have been taken from: 
Favicon was taken from: https://icons8.com/icons/set/
