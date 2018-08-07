from flask import Flask
from noteapp.views.index import bp
from noteapp.views.createnote import cn

app = Flask(__name__)

# creatin a route to go to

#@app.route('/')
#def home():
    #return "Hello World"

app.register_blueprint(bp)
app.register_blueprint(cn)