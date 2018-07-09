import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from VQA import Ui_Dialog as Dialog


class VQAApp(QtWidgets.QMainWindow, Dialog):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

def main():
    app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
    form = VQAApp()                 # We set the form to be our ExampleApp (design)
    form.show()                         # Show the form
    app.exec_()                         # and execute the app


if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                              # run the main function
