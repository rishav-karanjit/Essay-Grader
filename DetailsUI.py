from PyQt5 import QtWidgets, uic
import sys

from Backend.word_details import WordDetails
class DetailsUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(DetailsUI, self).__init__()
        self.initUI()

    def initUI(self): 
        uic.loadUi('./UI/Word_Details.ui', self) 
        
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