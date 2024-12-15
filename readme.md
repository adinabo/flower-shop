
## Petalia


The Petalia Flower Shop app was created to provide a seamless, user-friendly platform for customers to explore and purchase floral arrangements online. With the increasing trend of e-commerce and the growing demand for personalized shopping experiences, the app aims to make flower shopping convenient, accessible, and enjoyable for all users.

Key motivations for developing Petalia Flower Shop include:

Accessibility: Traditional flower shops often have limited operating hours and inventory visibility. This app allows users to shop for flowers anytime and view available arrangements in real time.

Convenience: Busy lifestyles can make it difficult for customers to visit physical stores. The app offers a streamlined browsing and purchasing process, ensuring users can select and order flowers in just a few clicks.

Customization: Flowers are often purchased for special occasions or as gifts, requiring unique arrangements. Petalia includes features that allow users to personalize their orders, enhancing the customer experience.

Aesthetic Appeal: As a flower shop, showcasing the beauty of the products is crucial. The app was designed with a clean and visually appealing interface to highlight the vibrancy and elegance of the floral arrangements.

Scalability: Petalia serves as a scalable solution for small and medium-sized florists looking to expand their reach online without requiring a significant investment in standalone e-commerce infrastructure.

Sustainability and Growth: By digitizing the flower shopping process, Petalia not only simplifies operations but also provides valuable insights into customer preferences, enabling businesses to adapt and grow.


## Customer User Stories

1. As a customer,I want to browse the available flower arrangements, so that I can select a bouquet that suits my needs.

2. As a customer,I want to search for flowers by category, color, or occasion, sSo that I can quickly find the most suitable options.

3. As a customer, I want to see detailed information about each flower arrangement (e.g., size, type, and price), so that I can make an informed purchase.

4. As a customer, I want to customize my bouquet with specific flowers or a personal message, so that I can make the gift more meaningful.

5. As a customer, I want to add items to my shopping cart and review my selections, so that I can easily manage my order before checkout.

6. As a customer, I want to securely enter my payment and delivery details,
So that I can complete my purchase without any concerns.

7. As a customer, I want to track my order history, so that I know which orders I've places.

8. As a visitor, I want to explore the website without creating an account, so that I can decide if I want to make a purchase.

9. As a user, I want to create an account and log in securely, so that I can save my personal details and order history.

10. As a usr, I want the app to be mobile-friendly and responsive, so that I can easily shop on my phone or tablet.

11. I want the website to load quickly and run smoothly, so that I have a pleasant browsing experience.

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

## Manual Tests
1. 
2. 
3. 
4. Placing an order
One issue encountered when placing an order was that it didn't return checkout_success everytime an order was placed. When opening with Dev Tools, it did work on mobile but not on desktop. Also, the grand total was not being returned on the checkout success page. 



All images have been taken from: Usplash
Favicon was taken from: https://icons8.com/icons/set/
