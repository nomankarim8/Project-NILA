import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
from apikey import get_api_key

app = Flask(__name__)
CORS(app)

API_KEY = get_api_key()
client = OpenAI(api_key=API_KEY) if API_KEY else None


def get_nila_reply(question):
    if not API_KEY:
        raise RuntimeError("OpenAI API key is not set.")

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are NILA, a friendly AI assistant."},
            {"role": "user", "content": question},
        ],
        max_tokens=200,
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()

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
