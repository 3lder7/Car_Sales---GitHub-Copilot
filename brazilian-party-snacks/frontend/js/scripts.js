document.addEventListener('DOMContentLoaded', () => {
    const snackList = document.getElementById('snack-list');
    const addSnackButton = document.getElementById('add-snack-button');
    const snackInput = document.getElementById('snack-input');

    addSnackButton.addEventListener('click', () => {
        const snackName = snackInput.value.trim();
        if (snackName) {
            const listItem = document.createElement('li');
            listItem.textContent = snackName;
            snackList.appendChild(listItem);
            snackInput.value = '';
        } else {
            alert('Please enter a snack name.');
        }
    });
});