from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data['prompt']
    task = data['task']
    ai_prompt = f"Given the text:\n{prompt}\nGenerate {task}:"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": ai_prompt}]
    )
    result = response['choices'][0]['message']['content']
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
