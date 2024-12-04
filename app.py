from flask import Flask, request, jsonify
from model import get_bot_response  # Import the function to get responses from the model

app = Flask(__name__)

# Route for serving the chatbot's responses
@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({'error': 'No input provided'}), 400
    
    # Get the AI response from the model
    response = get_bot_response(user_input)
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True)
