import assistant
from flask import Flask, request

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

if app.debug:
    import env


@app.route("/ask", methods=["POST"])
def ask():
    body = request.get_json()
    prompt = body["prompt"]
    response = assistant.ask_assistant(prompt)
    return {"ask": response}
