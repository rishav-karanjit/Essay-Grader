from PyQt5 import QtWidgets, uic
import sys

class DetailsUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(DetailsUI, self).__init__()
        self.initUI()

    def initUI(self): 
        uic.loadUi('Word_Details.ui', self) 