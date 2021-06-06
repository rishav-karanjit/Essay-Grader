from PyQt5.QtCore import QObject, QThread, pyqtSignal, QPoint
from PyQt5 import QtWidgets, uic
import sys
from Backend.grammarcheck import gcheck
from loading import Loading
class Mistakes(QtWidgets.QMainWindow):
    def __init__(self,main):
    	self.main = main
    	super(Mistakes, self).__init__()
    	self.initUI()
        #self.show()

    def initUI(self): 
        uic.loadUi('./UI/Mistakes.ui', self)
        self.StartGrammerCheck()

        self.Close = self.findChild(QtWidgets.QPushButton, 'Close')
        self.minimize = self.findChild(QtWidgets.QPushButton, 'minimize')

        self.Close.clicked.connect(self.Close_and_Open)
        self.minimize.clicked.connect(self.showMinimized)

        f = open("backend/grammer_mistake.txt", "r")
        self.gmistake_textedit = self.findChild(QtWidgets.QPlainTextEdit, 'gmistake')
        self.gmistake_textedit.setReadOnly(True)
        self.gmistake_textedit.insertPlainText(f.read())

        f = open("backend/essay.txt", "r")
        self.essay_textedit = self.findChild(QtWidgets.QPlainTextEdit, 'essay')
        self.essay_textedit.setReadOnly(True)
        self.essay_textedit.insertPlainText(f.read())

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

    def StartGrammerCheck(self):
        # Step 2: Create a QThread object
        self.thread = QThread()
        # Step 3: Create a worker object
        self.worker = Worker()
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        # Step 6: Start the thread
        self.window2=Loading()
        self.window2.show()
        self.main.close()
        self.thread.start()
        
        # # Final resets
        self.thread.finished.connect(
            lambda: self.show()         
        )
        self.thread.finished.connect(
            lambda: self.window2.close()
        )

    def Close_and_Open(self):
        self.main.show()
        self.close()
        
class Worker(QObject):
    finished = pyqtSignal()

    def run(self):
        grammer = gcheck()
        grammer.Check_Grammer()
        self.finished.emit()   