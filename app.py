from flask import Flask, jsonify, request
import os

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Terve from Dockerized Python app!",
        "hint": "Try /greet?name=YourName or /square?number=4"
    })


@app.route("/greet")
def greet():
    name = request.args.get("name", "friend")
    return jsonify({"greeting": f"Terve, {name}!"})


@app.route("/square")
def square():
    try:
        number = int(request.args.get("number", "0"))
    except ValueError:
        return jsonify({"error": "Please provide a valid integer in 'number'"}), 400

    return jsonify({
        "number": number,
        "square": number * number
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7000))
    app.run(host="0.0.0.0", port=port)
