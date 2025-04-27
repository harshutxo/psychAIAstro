from flask import Flask, request, jsonify, render_template
from chatbot_responses import get_response_from_huggingface

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.form['message']
        response = get_response_from_huggingface(user_input)
        return jsonify({'response': response})
    except Exception as e:
        print(f"Error in chat endpoint: {e}")
        return jsonify({'response': "I apologize, but something went wrong."})

if __name__ == '__main__':
    app.run(debug=True)