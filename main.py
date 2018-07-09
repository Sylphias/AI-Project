import sys
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import os
from VQA import Ui_Dialog as Dialog
from PIL import Image
import numpy as np
import cv2


class VQAApp(QtWidgets.QMainWindow, Dialog):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)
		self.submitBut.clicked.connect(self.processQuestion)
		self.uploadBut.clicked.connect(self.uploadFile)

	def test(self):
		self.ansLabel.show()
		self.loaderLabel.hide()
		self.ansLabel.setText = "Answer: "
	@QtCore.pyqtSlot()
	def processQuestion(self):
		img = cv2.imread(self.file_path)
		img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		img_pil = Image.fromarray(img)
		print(img_pil)
		question = self.questionInp.toPlainText()
		if(len(question) == 0 or question == ""):
			self.ansLabel.setText = "Error: Please enter a question"
			return
		#start loader while it processes
		self.loaderLabel.show()
		self.ansLabel.hide()
		#call function to process image and question in model

		# self.ansLabel.setText = "Answer: "



	@QtCore.pyqtSlot()
	def uploadFile(self):
		fileName = self.openFileNameDialog()
		self.fileInp.setText(fileName)
		## Gets absolute path of image uploaded
		self.file_path = os.path.abspath(fileName)
		pixmap = QtGui.QPixmap(self.file_path)
		self.imgView.setPixmap(pixmap)
		self.imgView.setAlignment(QtCore.Qt.AlignCenter)
		self.show()


	def openFileNameDialog(self):
		options = QtWidgets.QFileDialog.Options()
		options |= QtWidgets.QFileDialog.DontUseNativeDialog
		fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","PNG files (*.png)", options=options)
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
