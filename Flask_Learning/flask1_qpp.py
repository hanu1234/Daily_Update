from flask import Flask

app = Flask(__name__)


@app.route('/') # root which is home page of our application
def home():
    return "Hello world"


app.run(port=5000)
