# export FLASK_APP=ziyinw3_flask
# flask run

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"