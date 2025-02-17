// Function to display messages for 3 seconds
function displayMessages() {
    const messageContainer = document.getElementById('messageContainer');
    if (messageContainer) {
        messageContainer.style.display = 'block';
        setTimeout(function() {
            messageContainer.style.display = 'none';
        }, 3000); // 3000 milliseconds = 3 seconds
    }
}

// Call the function when the page loads
window.onload = function() {
    displayMessages();
};