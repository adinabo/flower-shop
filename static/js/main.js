document.getElementById('newsletter-form').addEventListener('submit', function(e) {
        e.preventDefault();
        document.getElementById('success-message').style.display = 'block';
    });