from PyQt5 import QtWidgets, uic
import sys

class Plagarism_c(QtWidgets.QMainWindow):
    def __init__(self):
        super(Plagarism_c, self).__init__()
        self.initUI()

    def initUI(self): 
        uic.loadUi('./UI/PLAGARISM_CHECK.ui', self)