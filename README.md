# Note web app created with Python

## Creating a web-application (Youtube tutorial)

### Youtube Links:
[Creating a web-application in Python [PART 1]](https://www.youtube.com/watch?v=Dqd8ZHWErpE)

[Creating a web-application in Python [PART 2]](https://www.youtube.com/watch?v=2Nuhh_C4FbM&t=6s)

[Creating a web-application in Python [PART 3]](https://www.youtube.com/watch?v=TwpUpVpknCE)

[Creating a web-application in Python [PART 4]](https://www.youtube.com/watch?v=2SPjxL-66AM)

===================================================================

### Programming Steps:

#### 1- Create __main__.py 
    (Linx command: touch __main__.py)
    (Win command: echo.> __main__.py)
Run this file by python IDLE to run the app 

#### 2- Create app.py 
    (Linx command: touch app.py)
    (Win command: echo.> app.py)

#### 3- Add the main code
to run the app

#### 4- Config python packages
by adding __init__.py to the files' folders
    (Linx command: touch __init__.py)
* noteapp folder >> package
* views folder >> package
    
#### 5- install flask package
* Install it on current machine
    
        (command: pip install flask)
        (command: python -m pip install --upgrade pip)
    
* Can also be installed on a virtual machine
[Python Virtual Environments](https://realpython.com/python-virtual-environments-a-primer/)

#### 6- Add a template with style
    
#### 7- Create new template using Blueprint package
index.html
index.py

#### 8- Create new view (createnote) and add the links
createnote.html
createnote.py

#### 9- Add create note form

#### 10- Allow the post method
Allow the post method for the submit button of the form in views folder createnote.py file
    
    @cn.route('/createnote', methods=['POST', 'GET'])
    
#### 11- Handle the POST method

#### 12- Return the note text
    text =  request.form.get('notetext')
    return text
    
#### 13- Create note files
    with open('noteapp/notes/{}.note'.format(random_string()), 'w+') as _file:
    # {} will be replaced with the random_string()
        _file.write(text)

        _file.close()
        
#### 14- Fetch the notes files
Fetch the notes files to the index.py file
    
#### 15- Use the fetched notes files in index page

#### 16- Use the text of the fetched notes files in index page

#### 17- Redirect to the index page after creating a new note

