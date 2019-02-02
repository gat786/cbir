from PyQt4 import QtGui
import shutil
import os

dirName = "temp"

def getImage(widget):
    filename = QtGui.QFileDialog.getOpenFileName(widget,
        'Select Image',
        'c:\\',
        "Images (*.png *.jpg)"
        )
    print("selected file is "+filename)
    if not os.path.exists(dirName):
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ")
    else:    
        print("Directory " , dirName ,  " already exists")
    shutil.copyfile(filename,dirName+'/editing.jpg')