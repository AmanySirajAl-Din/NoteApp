from flask import Flask
from flask import render_template


app = Flask(__name__)

# creatin a route to go to

@app.route('/')
def home():
    return render_template("layout.html")
