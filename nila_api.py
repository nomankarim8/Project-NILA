from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
from apikey import api_data

# Initialize Flask
app = Flask(__name__)
CORS(app)

# OpenAI API Key
openai.api_key = api_data

# AI Response Function
def get_nila_reply(question):
    prompt = f"User: {question}\nNILA:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200,
        stop=["User:"]
    )
    return response.choices[0].text.strip()

# API Route
@app.route('/nila', methods=['POST'])
def nila_api():
    data = request.get_json()
    question = data.get("question", "")
    
    if not question:
        return jsonify({"error": "No question provided"}), 400

    try:
        reply = get_nila_reply(question)
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run server
if __name__ == '__main__':
    app.run(debug=True, port=5000)
