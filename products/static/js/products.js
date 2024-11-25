document.addEventListener('DOMContentLoaded', () => {
    console.log('DOM fully loaded and parsed');

    // Attach event listeners to all "Add to Cart" forms
    document.querySelectorAll('.add-to-cart-form').forEach(form => {
        console.log('Attaching event listener to form:', form);

        form.addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent default form submission
            console.log('Form submission prevented');

            // Extract data
            const formData = new FormData(form);
            const productId = form.querySelector('.add-to-cart-button').getAttribute('data-product-id');
            const csrfToken = form.querySelector('[name=csrfmiddlewaretoken]').value;
            const redirectUrl = formData.get('redirect_url');
            const toastContainer = form.parentElement.querySelector('.toast-container');

            // Log extracted data
            console.log('Product ID:', productId);
            console.log('CSRF Token:', csrfToken);
            console.log('Redirect URL:', redirectUrl);

            // Send AJAX request
            fetch(`/bag/add/${productId}/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ redirect_url: redirectUrl })
            })
                .then(response => {
                    console.log('Fetch response received, status:', response.status);
                    if (!response.ok) {
                        console.error('Response not OK, throwing error');
                        throw new Error('Failed to add to cart.');
                    }
                    return response.json();
                })
                .then(data => {
                    console.log('Response data:', data);

                    // Display success toast
                    const toast = document.createElement('div');
                    toast.className = 'toast bg-success text-white p-2 rounded shadow-sm';
                    toast.innerHTML = `
                        <div>${data.message}</div>
                    `;
                    toastContainer.appendChild(toast);

                    // Auto-remove toast after 3 seconds
                    setTimeout(() => {
                        toast.remove();
                    }, 3000);
                })
                .catch(error => {
                    console.error('Error occurred during fetch:', error);

                    // Display error toast
                    const toast = document.createElement('div');
                    toast.className = 'toast bg-danger text-white p-2 rounded shadow-sm';
                    toast.innerHTML = `
                        <div>Failed to add item to cart.</div>
                    `;
                    toastContainer.appendChild(toast);

                    setTimeout(() => {
                        toast.remove();
                    }, 3000);
                });
        });
    });
});
