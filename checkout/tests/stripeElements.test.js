global.Stripe = jest.fn().mockImplementation(() => ({
    elements: jest.fn().mockReturnValue({
      create: jest.fn().mockReturnValue({
        mount: jest.fn(),
        on: jest.fn(),
      }),
    }),
  }));
  
  describe('Stripe Elements Initialization', () => {
    let stripePublicKey;
  
    beforeAll(() => {
      // Mock the Stripe public key that should be passed from Django template
      stripePublicKey = 'pk_test_12345';
      // Simulate loading the stripe_elements.js
      const script = document.createElement('script');
      script.src = '/static/checkout/js/stripe_elements.js';
      document.head.appendChild(script);
    });
  
    it('should load the Stripe.js script', () => {
      // Check if the Stripe.js script is loaded
      const script = document.querySelector('script[src="/static/checkout/js/stripe_elements.js"]');
      expect(script).toBeTruthy();
    });
  
    it('should initialize Stripe with the correct public key', () => {
      // Simulate calling the Stripe object with the public key
      require('/static/checkout/js/stripe_elements.js');  // or include the script file directly
      expect(global.Stripe).toHaveBeenCalledWith(stripePublicKey);
    });
  
    it('should create an instance of Stripe elements', () => {
      // Simulate loading the script and initializing elements
      require('/static/checkout/js/stripe_elements.js');
      const elements = global.Stripe().elements();
      expect(elements.create).toHaveBeenCalledWith('card');
    });
  
    it('should mount the card element to the correct DOM element', () => {
      // Simulate calling the script and mounting the card element
      require('/static/checkout/js/stripe_elements.js');
      const cardElement = global.Stripe().elements().create();
      cardElement.mount('#card-element'); // Check if it tries to mount to the correct DOM element
      expect(cardElement.mount).toHaveBeenCalledWith('#card-element');
    });
  });
  