# blue printing
# flask blue print
# http://flask.pocoo.org/docs/1.0/blueprints/

from flask import Blueprint, render_template
import glob  
# it's a package for
# listing files inside of directories

def fetch_notes():
    final_notes = []
    notes = glob.glob('noteapp/notes/*.note')
    
    for note in notes:
        with open(note) as _file:
        # open each note file
            final_notes.append(_file.read())
            # read the note file
            # and append it to the final_notes list
        _file.close()
        # must close each file
        
    return final_notes
    
    
bp = Blueprint('bp', __name__, template_folder='templates')

@bp.route('/')
def show():
    return render_template("index.html", notes = fetch_notes())
    # that means that notes variable will
    # be accessible from the index.html file