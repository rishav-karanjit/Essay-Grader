from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5 import QtWidgets, uic
import sys

class Loadinga(QtWidgets.QMainWindow):
    def __init__(self):
        super(Loading, self).__init__()
        self.initUI()
        self.show()

    def initUI(self): 
        uic.loadUi('./UI/Loading.ui', self)

    def finnished(self):
    	self.close