# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VQA.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(534, 640)
        self.submitBut = QtWidgets.QPushButton(Dialog)
        self.submitBut.setGeometry(QtCore.QRect(150, 520, 231, 25))
        self.submitBut.setObjectName("submitBut")
        self.imgView = QtWidgets.QGraphicsView(Dialog)
        self.imgView.setGeometry(QtCore.QRect(50, 120, 427, 240))
        self.imgView.setObjectName("imgView")
        self.fileInp = QtWidgets.QLineEdit(Dialog)
        self.fileInp.setGeometry(QtCore.QRect(50, 80, 331, 25))
        self.fileInp.setObjectName("fileInp")
        self.uploadBut = QtWidgets.QPushButton(Dialog)
        self.uploadBut.setGeometry(QtCore.QRect(390, 80, 89, 25))
        self.uploadBut.setObjectName("uploadBut")
        self.questionInp = QtWidgets.QTextEdit(Dialog)
        self.questionInp.setGeometry(QtCore.QRect(50, 410, 431, 51))
        self.questionInp.setObjectName("questionInp")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 50, 181, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 380, 181, 17))
        self.label_2.setObjectName("label_2")
        self.ansLabel = QtWidgets.QLabel(Dialog)
        self.ansLabel.setGeometry(QtCore.QRect(230, 480, 67, 17))
        self.ansLabel.setObjectName("ansLabel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "VQA AI Project"))
        self.submitBut.setText(_translate("Dialog", "Submit"))
        self.uploadBut.setText(_translate("Dialog", "Select Image"))
        self.label.setText(_translate("Dialog", "1) Upload Image"))
        self.label_2.setText(_translate("Dialog", "2) Enter Question"))
        self.ansLabel.setText(_translate("Dialog", "Answer: "))

