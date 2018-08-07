# blue printing
# flask blue print
# http://flask.pocoo.org/docs/1.0/blueprints/

from flask import Blueprint, render_template

cn = Blueprint('cn', __name__, template_folder='templates')

@cn.route('/createnote')
def show():
    return render_template("createnote.html")