# blue printing
# flask blue print
# http://flask.pocoo.org/docs/1.0/blueprints/

from flask import Blueprint, render_template, request, redirect

import random


cn = Blueprint('cn', __name__, template_folder='templates')

def random_string(length=10):
    final_string = ''
    chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
    
    for i in range(0, length):
        final_string += chars[random.randint(0, len(chars)-1)]
        # append random char 
    
    return final_string

@cn.route('/createnote', methods=['POST', 'GET'])
def show():
    if request.method == 'POST':
    # check the request method
        if request.form.get('createnote_btn'):
        # check if the submit button clicked
            text =  request.form.get('notetext')
            # get the note text
            #return text
            # return the note text
            
            with open('noteapp/notes/{}.note'.format(random_string()), 'w+') as _file:
            # {} will be replaced with the random_string()
                _file.write(text)
            
                _file.close()
    return render_template("createnote.html")