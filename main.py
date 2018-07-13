import sys
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import os
from gui.VQA import Ui_Dialog as Dialog
from PIL import Image
import numpy as np
import cv2
import threading
from pytorch_vqa import sample

class VQAApp(QtWidgets.QMainWindow, Dialog):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.threshold = 0.01
		self.setupUi(self)
		regex = QtCore.QRegExp("^(?!\s*$).+")
		input_validator = QtGui.QRegExpValidator(regex, self.questionInp)
		self.questionInp.setValidator(input_validator)
		self.ansLabel.hide()
		## Initializing the sampler
		self.sampler = sample.Sample('pytorch_vqa/model.pth')
		# self.connect(self.questionInp, SIGNAL("returnPressed()"), self.submitBut)
		self.submitBut.clicked.connect(self.processQuestion)
		self.questionInp.returnPressed.connect(self.processQuestion)
		self.uploadBut.clicked.connect(self.uploadFile)

	@QtCore.pyqtSlot()
	def processQuestion(self):
		if not self.questionInp.hasAcceptableInput():
			self.questionInp.setStyleSheet("border: 1px solid red;")
			return
		if self.fileInp.text() == "":
			self.fileInp.setStyleSheet("border: 1px solid red;")
			return
		self.questionInp.setStyleSheet("border: 1px solid green;")
		self.fileInp.setStyleSheet("border: 1px solid green;")
		# Start loading GIF while processing question
		self.loaderLabel.show()
		self.questionInp.setDisabled(True)
		# Disable submit button while processing question
		self.submitBut.setDisabled(True)
		# Updates GUI events on main thread
		# Converting image to PIL format
		img = cv2.imread(self.file_path)
		img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		self.img_pil = Image.fromarray(img)
		self.question = self.questionInp.text()
		# Error checking
		# if(len(self.question) == 0 or self.question == ""):
		# 	self.ansLabel.setText("Error: Please enter a question.")
		# 	return
		QtWidgets.QApplication.processEvents()
		# Thread to modify elements on GUI
		t = threading.Thread(target=self.saveThread)
		t.start()

	def receiveOutput(self, image, question):
		result = self.sampler.sample(image, question)
		string_result = ""
		for i in range(len(result)):
			conf = result[i][1]
			if conf > self.threshold:
				string_result += "{}: {:.2f}\n".format(result[i][0], conf)
		string_result = string_result[:-2]
		return string_result

	def saveThread(self):
		self.ansLabel.hide()
		self.result = self.receiveOutput(self.img_pil, self.question)
		self.ansLabel.setText(self.result)
		self.questionInp.setDisabled(False)
		self.submitBut.setDisabled(False)
		self.loaderLabel.hide()
		self.ansLabel.show()

	@QtCore.pyqtSlot()
	def uploadFile(self):
		fileName = self.openFileNameDialog()
		if fileName == "":
			return
		self.fileInp.setText(fileName)
		## Gets absolute path of image uploaded
		self.file_path = os.path.abspath(fileName)
		pixmap = QtGui.QPixmap(self.file_path)
		self.imgView.setPixmap(pixmap.scaled(427, 240, QtCore.Qt.KeepAspectRatio))
		self.imgView.setAlignment(QtCore.Qt.AlignCenter)
		self.show()


	def openFileNameDialog(self):
		options = QtWidgets.QFileDialog.Options()
		options |= QtWidgets.QFileDialog.DontUseNativeDialog
		fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","JPG files (*.jpg)", options=options)
		if fileName:
			return fileName
		return ""

def main():
	app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
	form = VQAApp()                 # We set the form to be our ExampleApp (design)
	form.show()                         # Show the form
	app.exec_()                         # and execute the app


if __name__ == '__main__':              # if we're running file directly and not importing it
	main()                              # run the main function
