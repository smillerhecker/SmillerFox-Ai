document.getElementById("send-btn").addEventListener("click", function() {
    let userInput = document.getElementById("user-input").value;
    if (userInput.trim() !== "") {
        appendMessage(userInput, 'user');
        document.getElementById("user-input").value = "";

        // Make a POST request to the Flask backend
        fetch('/get_response', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: userInput })
        })
        .then(response => response.json())
        .then(data => {
            if (data.response) {
                appendMessage(data.response, 'bot');
            }
        })
        .catch(error => {
            console.error("Error:", error);
            appendMessage("Sorry, there was an error with the chatbot.", 'bot');
        });
    }
});

function appendMessage(message, sender) {
    const messageContainer = document.createElement("div");
    messageContainer.classList.add(sender + "-message");
    messageContainer.textContent = message;
    
    document.getElementById("chat-messages").appendChild(messageContainer);
    document.getElementById("chat-messages").scrollTop = document.getElementById("chat-messages").scrollHeight; // Scroll to the bottom
}
