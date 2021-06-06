from PyQt5 import QtWidgets, uic
import sys
from PyQt5 import QtCore
import time

class Loading(QtWidgets.QDialog):
    def __init__(self):
        super(Loading, self).__init__()
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        uic.loadUi('./UI/Loading.ui', self)
        self.initUI()

    def initUI(self): 
        self.progressBar = self.findChild(QtWidgets.QProgressBar, 'progressBar')
        self.thread={}
        self.start_worker()
    
    def start_worker(self):
        self.thread[1] = ThreadClass(parent=None)
        self.thread[1].start()
        self.thread[1].any_signal.connect(self.my_function)

    def my_function(self,counter):
        cnt=counter
        self.progressBar.setValue(cnt) 

class ThreadClass(QtCore.QThread):
    
    any_signal = QtCore.pyqtSignal(int)
    def __init__(self, parent=None):
        super(ThreadClass, self).__init__(parent)
        self.is_running = True
    def run(self):
        #print('Starting thread...')
        cnt=0
        while (True):
            cnt+=1
            if cnt==99: cnt=0
            time.sleep(0.01)
            self.any_signal.emit(cnt) 
    def stop(self):
        self.is_running = False
        #print('Stopping thread...')
        self.terminate()

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     mw = Loading()
    
#     app.exec_()