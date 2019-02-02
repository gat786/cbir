from PyQt4 import QtGui
import shutil
import os

dirName = "temp"

def getImage(widget):
    filename = QtGui.QFileDialog.getOpenFileName(widget,
        'Select Image',
        'c:\\',
        "Images (*.png)"
        )
    print("selected file is "+filename)
    if not os.path.exists(dirName):
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ")
    else:    
        print("Directory " , dirName ,  " already exists")
    shutil.copyfile(filename,dirName+'/editing.png')

def saveImage(widget):
    filename = QtGui.QFileDialog.getSaveFileName(widget)
    print("selected file name is "+filename)
    shutil.copyfile(dirName+'/editing.png',filename+".png")