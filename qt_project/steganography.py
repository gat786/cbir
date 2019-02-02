# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\projects\AllProjectsEver\projects\scripts\random\cbir\designs\steganography.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from qt_project import file
import os
from qt_project import logic

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Steganography(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(624, 261)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 261))
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(44, 62, 80);\n"
""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.choose_image = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choose_image.sizePolicy().hasHeightForWidth())
        self.choose_image.setSizePolicy(sizePolicy)
        self.choose_image.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.choose_image.setObjectName(_fromUtf8("choose_image"))
        self.choose_image.clicked.connect(lambda: loadImageInLabel(widget=self.choose_image,label=self.image_view))

        self.horizontalLayout_3.addWidget(self.choose_image)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.image_view = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_view.sizePolicy().hasHeightForWidth())
        self.image_view.setSizePolicy(sizePolicy)
        self.image_view.setText(_fromUtf8(""))
        self.image_view.setObjectName(_fromUtf8("image_view"))
        self.horizontalLayout_2.addWidget(self.image_view)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.hidden_text = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hidden_text.sizePolicy().hasHeightForWidth())
        self.hidden_text.setSizePolicy(sizePolicy)
        self.hidden_text.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.hidden_text.setAlignment(QtCore.Qt.AlignCenter)
        self.hidden_text.setObjectName(_fromUtf8("hidden_text"))
        self.verticalLayout.addWidget(self.hidden_text)

        self.check_hidden = QtGui.QPushButton(self.centralwidget)
        self.check_hidden.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.check_hidden.setObjectName(_fromUtf8("check_hidden"))
        self.check_hidden.clicked.connect(lambda : checkHiddenMessage(hidden_text_label = self.hidden_text))

        self.verticalLayout.addWidget(self.check_hidden)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.secret_entry = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.secret_entry.sizePolicy().hasHeightForWidth())

        self.secret_entry.setSizePolicy(sizePolicy)
        self.secret_entry.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.secret_entry.setObjectName(_fromUtf8("secret_entry"))
        self.verticalLayout.addWidget(self.secret_entry)

        self.add_hidden = QtGui.QPushButton(self.centralwidget)
        self.add_hidden.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.add_hidden.setObjectName(_fromUtf8("add_hidden"))
        self.add_hidden.clicked.connect(lambda : addHiddenData(self.secret_entry))

        self.verticalLayout.addWidget(self.add_hidden)
        self.save_image = QtGui.QPushButton(self.centralwidget)
        self.save_image.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.save_image.setObjectName(_fromUtf8("save_image"))
        self.save_image.clicked.connect(lambda : save_image_to_disk(self.save_image))
        self.verticalLayout.addWidget(self.save_image)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_3, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Steganography", None))
        self.label.setText(_translate("MainWindow", "Select Image to be edited", None))
        self.choose_image.setText(_translate("MainWindow", "Select", None))
        self.label_3.setText(_translate("MainWindow", "Hidden Message Detetected ", None))
        self.hidden_text.setText(_translate("MainWindow", "Not Detected Yet", None))
        self.check_hidden.setText(_translate("MainWindow", "Get Hidden Text", None))
        self.label_4.setText(_translate("MainWindow", "Enter Message to be hidden", None))
        self.add_hidden.setText(_translate("MainWindow", "Add Hidden Text", None))
        self.save_image.setText(_translate("MainWindow", "Save Image", None))

imagePath = "/temp/editing.png"

def loadImageInLabel(widget,label):
    try:
        file.getImage(widget=widget)
        label.setPixmap(QtGui.QPixmap(os.getcwd() + imagePath))
    except FileNotFoundError:
        print("Please select a valid file")

def checkHiddenMessage(hidden_text_label):
    cursorLoading()
    try:
        data = logic.checkIfDataIsHidden(os.getcwd() + imagePath)
        hidden_text_label.setText(str(data))
        hidden_text_label.setStyleSheet("color:#FFFFFF")
    except FileNotFoundError:
        hidden_text_label.setText("Please Select a Image First")
        hidden_text_label.setStyleSheet("color:#FF0000")
    normalCursor()

def addHiddenData(edit_widget):
    cursorLoading()
    data = edit_widget.text()
    print("added data is "+data)
    logic.addSecret(os.getcwd() + imagePath,data)
    normalCursor()

def save_image_to_disk(widget):
    file.saveImage(widget)

def cursorLoading():
    QtGui.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)

def normalCursor():
    QtGui.QApplication.restoreOverrideCursor()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Steganography()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

def createWindow():
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Steganography()
    ui.setupUi(MainWindow)
    MainWindow.show()


