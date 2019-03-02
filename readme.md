Steps to run this project successfully

1. Firstly create a virtual environment with python 3.6 version and activate that virtual environment 

For creating virtual environment first install python version 3.6 in your system add python to your path adding to path is similar to that of java

after adding python to path download this file: - 

https://bootstrap.pypa.io/get-pip.py

open the folder where you have downloaded this file with terminal

run this command
> python get-pip.py

pip will be installed after this

to install virtual env run this command
>pip install virtualenv

after installing virtualenv go to the directory where you normally create your projects and create a virtual environment
>virtualenv cbir

to activate environment
>cd cbir
>source bin/activate

2. copy the files in this git repo to the virtual environment directory you have just created.

3. Install all the libraries listed in requirements.txt in the base folder
>pip install -r requirements.txt

4. install Qt by downloading the software from Qt official website

https://download.qt.io/archive/qt/4.8/

5. install pyqt in your virtual environment by downloading the appropriate file from this link

https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyqt4

now you are ready to run this project. You can start this project by running the __init__.py file in the base directory as
>python __init__.py