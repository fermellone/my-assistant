import assistant
from flask import Flask, request
from flask_cors import CORS
import os
import platform

app = Flask(__name__)
CORS(app)

if app.debug:
    import env


@app.route("/ask", methods=["POST"])
def ask():
    body = request.get_json()
    prompt = body["prompt"]
    response = assistant.ask_assistant(prompt)
    return {"response": response}


def create_app():
    print("app running")
    return app


if __name__ == "__main__":
    # if platform is macos the port should be 8081 else 5000
    print('platform: ' + platform.platform())
    app.run(port=8081 if platform.platform().startswith('macOS') else 5000)
