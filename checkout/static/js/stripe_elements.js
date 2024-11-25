/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

var stripePublicKey = JSON.parse(document.getElementById('id_stripe_public_key').textContent);
var clientSecret = JSON.parse(document.getElementById('id_client_secret').textContent);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
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
var card = elements.create('card', {style: style});
card.mount('#card-element');

// Real-time error handling
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Handling the form submission
var form = document.getElementById('payment-form');
form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true });
    $('#submit-button').attr('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);

    // Create payment method
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card
        }
    }).then(function(result) {
        if (result.error) {
            // Show error message
            var errorDiv = document.getElementById('card-errors');
            errorDiv.textContent = result.error.message;
            $('#loading-overlay').fadeToggle(100);
            $('#payment-form').fadeToggle(100);
        } else {
            // Redirect to confirmation page if payment is successful
            window.location.href = "/checkout/complete/";
        }
    });
});
