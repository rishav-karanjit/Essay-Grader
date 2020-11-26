from PyQt5 import QtWidgets, uic
import sys

class Score(QtWidgets.QMainWindow):
    def __init__(self):
        super(Score, self).__init__()
        self.initUI()

    def initUI(self): 
        uic.loadUi('./UI/Score.ui', self)