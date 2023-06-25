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
    return {"response": response}


def create_app():
    print("app running")
    return app


# if __name__ == "__main__":
#     from waitress import serve


#     serve(app, host="0.0.0.0", port=8080)

if __name__ == "__main__":
    app.run(port=5000)
