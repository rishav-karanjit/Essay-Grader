from PyQt5 import QtWidgets, uic
import sys
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog

class Essay_report(QtWidgets.QMainWindow):
    def __init__(self):
        super(Essay_report, self).__init__()
        self.initUI()
        

    def initUI(self): 
        uic.loadUi('./UI/Essay_report.ui', self)
        self.show()
        self.tab = self.findChild(QtWidgets.QTabWidget, 'tabWidget')

        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer,self)

        if dialog.exec_() == QPrintDialog.Accepted:
        	self.print_(printer)