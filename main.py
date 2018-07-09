import sys
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from VQA import Ui_Dialog as Dialog


class VQAApp(QtWidgets.QMainWindow, Dialog):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.submitBut.clicked.connect(self.processQuestion)
        self.uploadBut.clicked.connect(self.test)
    def test(self):
        self.ansLabel.show()
        self.loaderLabel.hide()
        self.ansLabel.setText = "Answer: "

    def processQuestion(self):
        question = self.questionInp.toPlainText()
        if(len(question) == 0 or question == ""):
            self.ansLabel.setText = "Error: Please enter a question"
            return
        #start loader while it processes
        self.loaderLabel.show()
        self.ansLabel.hide()
        #call function to process image and question in model

        # self.ansLabel.setText = "Answer: "



def main():
    app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
    form = VQAApp()                 # We set the form to be our ExampleApp (design)
    form.show()                         # Show the form
    app.exec_()                         # and execute the app


if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                              # run the main function
