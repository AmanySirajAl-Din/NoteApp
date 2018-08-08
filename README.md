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
    (Linux command: touch __main__.py)
    (Win command: echo.> __main__.py)
    Run this file by python IDLE to run the app 

#### 2- Create app.py 
    (Linux command: touch app.py)
    (Win command: echo.> app.py)

#### 3- Add the main code
    to run the app

#### 4- Config python packages
    by adding __init__.py to the files' folders
    (Linux command: touch __init__.py)
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
    for the submit button of the form
    in views folder createnote.py file
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

        
=================================================

## Part4: Using DataBase
### Programming Steps:

#### 1- Setup a virtual environment
* **Debian:**
    **Debian** is the operating system the Linux distribution that will be used in this part
    * Search for debian
    * open the link [Debian](https://www.debian.org/CD/netinst/)     
    * Download netinst CD image that compatable with your machine
        ( for me it's amd64 because I have 64-bit)
* **VirtualBox:**
    * **Download** the version for your OS
    * **Install** it
    * **Open** it
    * Click on **'New'** top button 
        (or click on 'Machine' dropdown menu then click 'New')
    * Click on **'Expert Mode'** button
    * Choose **'Type'**: Linux
    * Choose **'Version'**: Linux 
    * Increase the **'Memory Size'** to be more than 2600 MB
    * Name your virtual machine
    * Click on **'Create'** button
    * Click on **'Create'** button on the another pop-up
        (Before clicking it .. you can make the 'File Size' 8.00GB as the tutorial)
    * Click on **'Start'** top button to Boot up your newely created VM
        (or click on 'Machine' dropdown menu then click 'Start')
    * On the new Pop-up choose where the **'Debian ISO file'**
    * Click on the **'Start'** button
    * Choose **'install'** on thr VM window and follow the steps
        * language settings
        * Hostname
        * Root password
        * Guided partitioning>> 'Guided-use entire disk'
        * partitioning scheme>> 'All files in one partition'
        * Finish
        * Write the changes to disk?>>Yes
        
    
    
        