# Note web app created with Python

## Creating a web-application (Youtube tutorial)

### Youtube Links:
[Creating a web-application in Python [PART 1]](https://www.youtube.com/watch?v=Dqd8ZHWErpE)

[Creating a web-application in Python [PART 2]](https://www.youtube.com/watch?v=2Nuhh_C4FbM&t=6s)

[Creating a web-application in Python [PART 3]](https://www.youtube.com/watch?v=TwpUpVpknCE)

[Creating a web-application in Python [PART 4]](https://www.youtube.com/watch?v=2SPjxL-66AM)

- - -
## Part1,2,3: Create Note web app (Using Notes Files)
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

    [Source: Python Virtual Environments](https://realpython.com/python-virtual-environments-a-primer/)

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

        
- - -

## Part4: Create Note web app (Using DataBase and VM)
### Programming Steps:

#### 1- Setup a virtual environment
#### Using VirtualBox and Vagrant you can follow the steps in this [link](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0)

#### OR Using VirtualBox and Debian:
You can follow thesteps in this [link](https://www.youtube.com/watch?v=sc-kHLUn_9E)
* **VirtualBox:**
    * Search for VirtualBox
    * open the link [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
    * **Download** the version for your OS
    * **Install** it
    * **Open** it

* **Debian:**
    It is the operating system the Linux distribution that will be used in this part
    * Search for debian netinstall
    * open the link [Debian](https://www.debian.org/CD/netinst/)     
    * Download netinst CD image that compatable with your machine
        
        (For me it's amd64 because I have 64-bit)
        
* **VirtualBox Program Window:**
    * Click on **'New'** top button
    
        (or click on 'Machine' dropdown menu then click 'New')
    * Click on **'Expert Mode'** button
    * Choose **'Type'**: Linux
    * Choose **'Version'**: Debian (64-bit)
    * Increase the **'Memory Size'** to be more than 2600 MB
    * Name your virtual machine
    * Click on **'Create'** button
    * Click on **'Create'** button on the another pop-up
        
        (Before clicking it .. you can make the 'File Size' 8.00GB as the tutorial)        
    * Click on **'Start'** top button to Boot up your newely created VM
        
        (or click on 'Machine' dropdown menu then click 'Start')
        
* **VM Window:**
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
        * Choose Software to install:>>only select
            * SSH server
            * Standard system utilities
            
        and deselect all other choices
        * Install Grub boot loader>>Yes
        * Device for boot loader>>/dev/sda
        * Finish the installation
    * On the newely created **VM DOS**:
        * VMname login: **root**
        * Press Enter
        * Password: ****
        * Press Enter
     
* **VM DOS:**
    * VMname login: **root**
    * Press Enter
    * Password: ****
    * Press Enter
    * Test the VM connection by typing the following terminal command:
    
            ping 8.8.8.8
        If there is a **Reply** then it works
    * Now we will install the MongoDB
    
            apt update
            apt-get update
            apt-get install mongodb
            Do you want to continue? [Y/n] _
            Do you want to continue? [Y/n] Y
            
    * Click **'Machine'** dropdown menu then choose 'Settings'
    * On the 'Settings' window choose **'Network'** tab
    * Then for **'Attached to:'** choose **'Bridged Adapter'**
    * Then click **'OK'** button
    * Click **'File'** dropdown menu then choose 'Close'
    * On the 'Close' window choose **'Power off'** then click **'OK'** button
    
* **VirtualBox Program Window:**
    * Click on **'Start'** top button to Boot up your newely created VM
    
        (or click on 'Machine' dropdown menu then click 'Start')
        
* **VM DOS:**
    * VMname login: **root**
    * Press Enter
    * Password: ****
    * Press Enter  
    * Get the IP address of the VM type this command:
                
            ifconfig 
    If "ifconfig" command wasn't found then type:
            
            ip address
        OR
            ip a

[Source: How to install missing ifconfig command](https://linuxconfig.org/how-to-install-missing-ifconfig-command-on-debian-linux)
        
* Open & Edit the hosts file:    
    * Follow the following link's steps for your OS:

    [How to Edit Your Hosts File on Windows, Mac, or Linux](https://www.howtogeek.com/howto/27350/beginner-geek-how-to-edit-your-hosts-file/)
    
    windows path c:\windows\system32\drivers\etc\hosts

    * Then add the IP address of the VM
    
    10.10.2.151 &nbsp;&nbsp;&nbsp;&nbsp;   %VMHostname%
    
    For me it was:

    10.10.2.151 &nbsp;&nbsp;&nbsp;&nbsp;   amany.dev
    
    For the tutorial it was:
    
    192.168.1.86 &nbsp;&nbsp;&nbsp;&nbsp;   youtube.dev
    
* On Test your VM host by typing the following terminal command:

        ping %VMHostname%
    If there is a **Reply** then it works
            
* **VM DOS:**
    * Type this command:
    
            nano /etc/ssh/sshd_config
    * Press Enter
    * Navigate with the up & down Keys to go to:
        
            #PermitRootLogin without-password
    * To Enable root login over SSH replace 'without-password' to:
            
            PermitRootLogin yes
[Enable SSH root login](https://linuxconfig.org/enable-ssh-root-login-on-ubuntu-16-04-xenial-xerus-linux-server-desktop)
    * Save with 'ctrl+O' or '^O' 
    * Save with 'ctrl+X' or '^X' 
    * Type these commands:
            
            systemctl restart ssh
            systemctl restart sshd
        
* On **Terminal**:
    
            ssh root@%VMHostname%
            root@%VMHostname%'s password: ****
    * Now you have accessed the VM
        
            root@VMname:~#_
    * For Debian 9 follow the steps in the this [link](https://www.globo.tech/learning-center/install-mongodb-debian-9/)
    
    * The yotube tutorial steps:
        * Now start the mongodb server:
        
                root@VMname:~# mongo
        * To exit the serve click ctrl+C (^C)
        * To check if the mongodb.service is running type this command:
                
                systemctl status mongodb.service
                
        * To exit the serve click ctrl+C (^C)
        * To check if the mongodb.service is running type this command:
                
                systemctl status mongodb.service
                
        * If "mongo" didn't work:
        
                root@VMname:~# mongod
        * If "mongod" has an error 'dbpath (/data/db/) does not exist'

        OR 'Data directory /data/db not found' 

        Type this :

                    mkdir -p /data/db/
                    
        * If mongodb server can't start:
        
                    chmod -R 777 /data/db/
        * Now start the mongodb server:
        
                root@VMname:~# mongo
        