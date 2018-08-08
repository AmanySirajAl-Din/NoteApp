# blue printing
# flask blue print
# http://flask.pocoo.org/docs/1.0/blueprints/

from flask import Blueprint, render_template
import glob  
# it's a package for
# listing files inside of directories

def fetch_notes():
    notes = glob.glob('noteapp/notes/*.note')
    return notes
    
    
bp = Blueprint('bp', __name__, template_folder='templates')

@bp.route('/')
def show():
    return render_template("index.html", notes = fetch_notes())
    # that means that notes variable will
    # be accessible from the index.html file