import random  # For demonstration purposes, using random responses

# Example AI model function (replace with your actual model logic)
def get_bot_response(user_input):
    if 'hello' in user_input.lower():
        return "Hi! How can I assist you today?"
    elif 'how are you' in user_input.lower():
        return "I'm doing great, thanks for asking!"
    else:
        return random.choice([
            "Sorry, I didn't understand that.",
            "Can you rephrase your question?",
            "I'm still learning, but I can help with some things!"
        ])
