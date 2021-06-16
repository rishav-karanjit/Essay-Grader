from PyQt5 import QtWidgets, uic
import sys
from Model.Loadmodel import Load_model
from PyQt5 import QtWidgets, uic, QtCore

class ScoreUI(QtWidgets.QMainWindow):
	def __init__(self,main):
		self.main = main
		super(ScoreUI, self).__init__()
		self.load_model = Load_model()
		self.initUI()
		self.show()
		self.main.close()

	def initUI(self):
		uic.loadUi('./UI/Score_2.ui', self)

		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

		score = self.load_model.Load_StackModel()
		self.findChild(QtWidgets.QLabel, 'Score').setText(str(score[0]))
		self.Close = self.findChild(QtWidgets.QPushButton, 'Close')
		self.minimize = self.findChild(QtWidgets.QPushButton, 'minimize')
		self.Close.clicked.connect(self.Close_and_Open)
		self.minimize.clicked.connect(self.showMinimized)

	def Close_and_Open(self):
		self.main.show()
		self.close()
