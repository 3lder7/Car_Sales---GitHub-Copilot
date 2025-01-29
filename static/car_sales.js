document.addEventListener('DOMContentLoaded', function() {
    // Select all buttons on the page
    const buttons = document.querySelectorAll('button');

    // Add click event listener to each button
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            // Get the car name and brand from data attributes
            const carName = button.getAttribute('car');
            // Show alert with car name and brand
            alert(`O carro ${carName} foi vendido!`);
        });
    });
});