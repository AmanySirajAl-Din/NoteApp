from flask import Flask
from noteapp.views.index import bp as index_bp

app = Flask(__name__)

# creatin a route to go to

#@app.route('/')
#def home():
    #return "Hello World"

app.register_blueprint(index_bp)