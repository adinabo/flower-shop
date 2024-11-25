document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.add-to-cart-form').forEach(form => {
        form.addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent default form submission

            const productId = form.querySelector('.add-to-cart-button')?.getAttribute('data-product-id');
            if (!productId) {
                console.error('Product ID is missing.');
                return;
            }

            const csrfToken = form.querySelector('[name=csrfmiddlewaretoken]')?.value;
            if (!csrfToken) {
                console.error('CSRF Token is missing.');
                return;
            }

            const redirectInput = form.querySelector('[name=redirect_url]');
            if (!redirectInput) {
                console.error('Redirect URL input is missing.');
                return;
            }
            const redirectUrl = redirectInput.value;

            console.log('Sending fetch request with JSON body...');
            console.log('Product ID:', productId);
            console.log('Redirect URL:', redirectUrl);
            console.log('CSRF Token:', csrfToken);

            fetch(`/products/bag/add/${productId}/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ redirect_url: redirectUrl })
            })
                .then(response => {
                    console.log('Response status:', response.status);
                    if (!response.ok) {
                        throw new Error(`Failed to add to cart: ${response.status} ${response.statusText}`);
                    }
                    return response.json();
                })
                .then(data => {
                    console.log('Success response:', data);

                    // Display success toast
                    const toastContainer = form.parentElement.querySelector('.toast-container');
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
                    console.error('Error:', error);

                    // Display error toast
                    const toastContainer = form.parentElement.querySelector('.toast-container');
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
