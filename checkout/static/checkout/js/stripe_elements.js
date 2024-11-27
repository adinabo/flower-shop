/* Core logic/payment flow for this comes from here:
   https://stripe.com/docs/payments/accept-a-payment
*/

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);

// Ensure the Stripe.js library is loaded
function loadStripeElements() {
    console.log("loadStripeElements function is being called."); // confirm if the function is triggered

    if (window.Stripe) {
        console.log("Stripe.js has loaded successfully.");

        var stripePublicKey = document.getElementById('id_stripe_public_key').textContent.slice(1, -1);
        var stripe = Stripe(stripePublicKey);  // Initialize Stripe
        var elements = stripe.elements();  // Initialize Stripe Elements

        if (elements) {
            console.log("Stripe Elements initialized.");
        }

        var style = {
            base: {
                color: '#000',
                fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
                fontSmoothing: 'antialiased',
                fontSize: '16px',
                '::placeholder': {
                    color: '#aab7c4'
                }
            },
            invalid: {
                color: '#dc3545',
                iconColor: '#dc3545'
            }
        };

        var card = elements.create('card', { style: style });
        card.mount('#card-element');  // Mount the card element to the div with id 'card-element'
        console.log("Card element created and mounted.");
    } else {
        console.error("Stripe.js has not loaded correctly.");
    }
}

// Load Stripe Elements only after the page is fully loaded
document.addEventListener('DOMContentLoaded', loadStripeElements);

console.log("stripe_elements.js loaded successfully.");

