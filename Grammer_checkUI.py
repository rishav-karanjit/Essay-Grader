from PyQt5 import QtWidgets, uic
import sys
from Backend.grammarcheck import gcheck
class Mistakes(QtWidgets.QMainWindow):
    def __init__(self):
        super(Mistakes, self).__init__()
        self.initUI()

    def initUI(self): 
        uic.loadUi('./UI/Mistakes.ui', self)
        grammer = gcheck()
        grammer.Check_Grammer()

        f = open("backend/grammer_mistake.txt", "r")
        self.gmistake_textedit = self.findChild(QtWidgets.QPlainTextEdit, 'gmistake')
        self.gmistake_textedit.insertPlainText(f.read())

        f = open("backend/essay.txt", "r")
        self.essay_textedit = self.findChild(QtWidgets.QPlainTextEdit, 'essay')
        self.essay_textedit.insertPlainText(f.read())
        