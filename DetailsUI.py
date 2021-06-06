from PyQt5 import QtWidgets, uic, QtCore
import sys
from PyQt5.QtCore import QPoint

from Backend.word_details import WordDetails

class DetailsUI(QtWidgets.QMainWindow):
    def __init__(self,main):
        self.main = main
        super(DetailsUI, self).__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.initUI()
        self.show()
        self.main.close()

    def initUI(self): 
        uic.loadUi('./UI/Word_Details.ui', self) 
        
        self.Close = self.findChild(QtWidgets.QPushButton, 'Close')
        self.minimize = self.findChild(QtWidgets.QPushButton, 'minimize')

        self.Close.clicked.connect(self.Close_and_Open)
        self.minimize.clicked.connect(self.showMinimized)
        
        f = open("backend/essay.txt", "r")
        self.essay_textedit = self.findChild(QtWidgets.QPlainTextEdit, 'essay')
        self.essay_textedit.setReadOnly(True)
        self.essay_textedit.insertPlainText(f.read())

        self.WordDetails = WordDetails()

        self.No_of_chars = self.findChild(QtWidgets.QLabel,'No_of_chars')
        self.No_of_chars.setText(WordDetails.Get_No_of_char(self))

        self.No_of_words = self.findChild(QtWidgets.QLabel,'No_of_words')
        self.No_of_words.setText(WordDetails.Get_No_of_words(self))

        self.No_of_paragraph = self.findChild(QtWidgets.QLabel,'No_of_paragraph')
        self.No_of_paragraph.setText(WordDetails.Get_No_of_para(self))

        self.No_of_unique = self.findChild(QtWidgets.QLabel,'No_of_unique')
        self.No_of_unique.setText(WordDetails.Get_No_of_unique_words(self))

        self.No_of_common = self.findChild(QtWidgets.QLabel,'No_of_common')
        self.No_of_common.setText(WordDetails.GetMostCommonWords(self))
        
        Word = WordDetails()
        noun_count, adj_count, verb_count, adv_count = Word.Part_of_speech()
        
        self.No_of_noun = self.findChild(QtWidgets.QLabel,'No_of_noun')
        self.No_of_noun.setText(str(noun_count))

        self.No_of_adj = self.findChild(QtWidgets.QLabel,'No_of_adj')
        self.No_of_adj.setText(str(adj_count))

        self.No_of_verb = self.findChild(QtWidgets.QLabel,'No_of_verb')
        self.No_of_verb.setText(str(verb_count))

        self.No_of_adverb = self.findChild(QtWidgets.QLabel,'No_of_adverb')
        self.No_of_adverb.setText(str(adv_count))

        self.start = QPoint(0, 0)
        self.pressing = False

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end-self.start
            self.setGeometry(self.mapToGlobal(self.movement).x(),
                                self.mapToGlobal(self.movement).y(),
                                self.width(),
                                self.height())
            self.start = self.end

    def Close_and_Open(self):
        self.main.show()
        self.close()