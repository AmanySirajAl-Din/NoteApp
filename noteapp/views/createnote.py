# blue printing
# flask blue print
# http://flask.pocoo.org/docs/1.0/blueprints/

from flask import Blueprint, render_template, request
import sys

cn = Blueprint('cn', __name__, template_folder='templates')

@cn.route('/createnote', methods=['POST', 'GET'])
def show():
    if request.method == 'POST':
        if request.form.get('createnote_btn'):
            return "Clicked!"

    return render_template("createnote.html")