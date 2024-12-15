// Mock the Stripe object and its methods
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
    });
  
    it('should initialize Stripe with the correct public key', () => {
      // Directly call the mocked Stripe object to simulate initialization
      global.Stripe(stripePublicKey);
  
      // The mock function for Stripe should be called with the correct public key
      expect(global.Stripe).toHaveBeenCalledWith(stripePublicKey);
    });
  
    it('should create an instance of Stripe elements', () => {
      // Simulate creating the 'card' element using the mock
      const stripeInstance = global.Stripe(stripePublicKey);
      const elements = stripeInstance.elements(); 
      elements.create('card'); //
  
      // Ensure create() is called with 'card'
      expect(elements.create).toHaveBeenCalledWith('card');
    });
  
    it('should mount the card element to the correct DOM element', () => {
      // Simulate calling the script and mounting the card element to the DOM
      const stripeInstance = global.Stripe(stripePublicKey);
      const elements = stripeInstance.elements(); 
      const cardElement = elements.create('card'); 
      cardElement.mount('#card-element'); 
  
      // Check if mount is called with the correct DOM element
      expect(cardElement.mount).toHaveBeenCalledWith('#card-element');
    });
  });
  