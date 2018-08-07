# blue printing
# flask blue print
# http://flask.pocoo.org/docs/1.0/blueprints/

from flask import Blueprint, render_template, request

cn = Blueprint('cn', __name__, template_folder='templates')

@cn.route('/createnote', methods=['POST', 'GET'])
def show():
    if request.method == 'POST':
    # check the request method
        if request.form.get('createnote_btn'):
        # check if the submit button clicked
            text =  request.form.get('notetext')
            # get the note text
            return text
            # return the note text

    return render_template("createnote.html")