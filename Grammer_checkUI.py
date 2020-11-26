from PyQt5 import QtWidgets, uic
import sys

class Mistakes(QtWidgets.QMainWindow):
    def __init__(self):
        super(Mistakes, self).__init__()
        self.initUI()

    def initUI(self): 
        uic.loadUi('./UI/Mistakes.ui', self)