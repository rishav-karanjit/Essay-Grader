from PyQt5 import QtWidgets, uic
import sys
from Model.Loadmodel import Load_model
class ScoreUI(QtWidgets.QMainWindow):
    def __init__(self,main):
        super(ScoreUI, self).__init__()
        self.load_model = Load_model()
        self.initUI()
        self.show()

    def initUI(self): 
        uic.loadUi('./UI/Score.ui', self)
        score = self.load_model.Load_StackModel()
        self.findChild(QtWidgets.QLabel, 'Score').setText(str(score[0]))
