from PyQt5 import QtWidgets, uic
import sys

class Essay_report(QtWidgets.QMainWindow):
    def __init__(self):
        super(Essay_report, self).__init__()
        self.initUI()

    def initUI(self): 
        uic.loadUi('./UI/Essay_report.ui', self)