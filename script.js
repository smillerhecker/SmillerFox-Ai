document.getElementById("send-btn").addEventListener("click", function() {
    let userInput = document.getElementById("user-input").value;
    if (userInput.trim() !== "") {
        appendMessage(userInput, 'user');
        document.getElementById("user-input").value = "";
        
        // Simulate chatbot response after a delay
        setTimeout(() => {
            let botResponse = generateBotResponse(userInput);
            appendMessage(botResponse, 'bot');
        }, 1000);
    }
});

function appendMessage(message, sender) {
    const messageContainer = document.createElement("div");
    messageContainer.classList.add(sender + "-message");
    messageContainer.textContent = message;
    
    document.getElementById("chat-messages").appendChild(messageContainer);
    document.getElementById("chat-messages").scrollTop = document.getElementById("chat-messages").scrollHeight; // Scroll to the bottom
}

function generateBotResponse(input) {
    // Simple rule-based response for the chatbot
    if (input.toLowerCase().includes("hello")) {
        return "Hi! How can I help you today?";
    } else if (input.toLowerCase().includes("how are you")) {
        return "I'm doing great, thanks for asking!";
    } else {
        return "I'm not sure how to respond to that. Could you rephrase?";
    }
}
