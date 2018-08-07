# blue printing
# flask blue print
# http://flask.pocoo.org/docs/1.0/blueprints/

from flask import Blueprint, render_template

bp = Blueprint('bp', __name__, template_folder='templates')

@bp.route('/')
def show():
    return render_template("index.html")