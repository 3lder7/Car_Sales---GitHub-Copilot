// This file contains unit tests for the JavaScript code in scripts.js, ensuring that the interactive features work as intended.

describe('Snack Interaction Tests', () => {
    it('should display snack details when a snack is clicked', () => {
        // Setup: Create a mock snack element
        const snackElement = document.createElement('div');
        snackElement.classList.add('snack');
        snackElement.dataset.name = 'Coxinha';
        document.body.appendChild(snackElement);

        // Simulate click event
        snackElement.click();

        // Assertion: Check if the snack details are displayed
        const details = document.querySelector('.snack-details');
        expect(details.textContent).toContain('Coxinha');
    });

    it('should add snack to cart when "Add to Cart" button is clicked', () => {
        // Setup: Create a mock snack and button
        const snackElement = document.createElement('div');
        snackElement.classList.add('snack');
        snackElement.dataset.name = 'Pão de Queijo';
        document.body.appendChild(snackElement);

        const button = document.createElement('button');
        button.classList.add('add-to-cart');
        button.textContent = 'Add to Cart';
        document.body.appendChild(button);

        // Simulate button click
        button.click();

        // Assertion: Check if the cart has the snack
        const cart = document.querySelector('.cart');
        expect(cart.textContent).toContain('Pão de Queijo');
    });
});