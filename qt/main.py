# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\projects\AllProjectsEver\projects\scripts\random\cbir\designs\main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(693, 444)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(44, 62, 80);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(20, 100, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.stegano_button = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stegano_button.sizePolicy().hasHeightForWidth())
        self.stegano_button.setSizePolicy(sizePolicy)
        self.stegano_button.setMinimumSize(QtCore.QSize(0, 40))
        self.stegano_button.setStyleSheet(_fromUtf8("QWidget#stegano_button{\n"
"    color: #95a5a6\n"
"}\n"
"\n"
"QWidget#stegano_button:hover{\n"
"        color: #ffffff\n"
"}"))
        self.stegano_button.setAlignment(QtCore.Qt.AlignCenter)
        self.stegano_button.setObjectName(_fromUtf8("stegano_button"))
        self.verticalLayout_2.addWidget(self.stegano_button)
        self.facial_recog_button = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.facial_recog_button.sizePolicy().hasHeightForWidth())
        self.facial_recog_button.setSizePolicy(sizePolicy)
        self.facial_recog_button.setMinimumSize(QtCore.QSize(0, 40))
        self.facial_recog_button.setStyleSheet(_fromUtf8("QWidget#facial_recog_button{\n"
"    color: #95a5a6\n"
"}\n"
"\n"
"QWidget#facial_recog_button:hover{\n"
"        color: #ffffff\n"
"}"))
        self.facial_recog_button.setAlignment(QtCore.Qt.AlignCenter)
        self.facial_recog_button.setObjectName(_fromUtf8("facial_recog_button"))
        self.verticalLayout_2.addWidget(self.facial_recog_button)
        self.image_editing_button = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_editing_button.sizePolicy().hasHeightForWidth())
        self.image_editing_button.setSizePolicy(sizePolicy)
        self.image_editing_button.setMinimumSize(QtCore.QSize(0, 40))
        self.image_editing_button.setStyleSheet(_fromUtf8("QWidget#image_editing_button{\n"
"    color: #95a5a6\n"
"}\n"
"\n"
"QWidget#image_editing_button:hover{\n"
"        color: #ffffff\n"
"}"))
        self.image_editing_button.setAlignment(QtCore.Qt.AlignCenter)
        self.image_editing_button.setObjectName(_fromUtf8("image_editing_button"))
        self.verticalLayout_2.addWidget(self.image_editing_button)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "CBIR", None))
        self.label.setText(_translate("MainWindow", "Choose any one option", None))
        self.stegano_button.setText(_translate("MainWindow", "Steganography", None))
        self.facial_recog_button.setText(_translate("MainWindow", "Facial Recognition", None))
        self.image_editing_button.setText(_translate("MainWindow", "Editing", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

