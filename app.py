from flask import Flask, request, jsonify
from qrng import *

app = Flask(__name__)

@app.route("/home")
def get_user():
    return str(get_random())


if __name__ == "__main__":
    app.run(debug=True)