from JarvisUi import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer, QTime, QDate
from PyQt5.uic import loadUiType
import main
import os
import webbrowser as web
import sys

class MainThread(QThread):
    
    def __init__(self):
        super(MainThread,self).__init__()
        
    def run(self):
        main.TaskExe()
        
startExe = MainThread()        
        
class Gui_Start(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)
        
        self.gui.Start.clicked.connect(self.startTask)
        self.gui.Stop.clicked.connect(self.close)
        self.gui.Chrome.clicked.connect(self.chrome_app)
        self.gui.WhatsApp.clicked.connect(self.whatsapp_app)
        self.gui.YouTube.clicked.connect(self.youtube_app)
        
    def chrome_app(self):
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        
    def youtube_app(self):
        web.open("https://www.youtube.com/")
        
    def whatsapp_app(self):
        web.open("https://web.whatsapp.com/")
        
    def startTask(self):
        
        self.gui.label1 = QtGui.QMovie("B.G-20210629T070120Z-001//B.G//Iron_Template_1.gif")
        self.gui.Gif_1.setMovie(self.gui.label1)
        self.gui.label1.start()
        
        self.gui.label2 = QtGui.QMovie("JARVIS GUI//Gif_6.gif")
        self.gui.Gif_2.setMovie(self.gui.label2)
        self.gui.label2.start()
        
        self.gui.label3 = QtGui.QMovie("JARVIS GUI//Gif 3.gif")
        self.gui.Gif_3.setMovie(self.gui.label3)
        self.gui.label3.start()
        
        self.gui.label4 = QtGui.QMovie("ExtraGui-20210629T070440Z-001//ExtraGui//Earth.gif")
        self.gui.Gif_4.setMovie(self.gui.label4)
        self.gui.label4.start()
        
        timer = QTimer(self)
        timer.timeout.connect(self.showTimeLive)
        timer.start(999)
        startExe.start()
        
    def showTimeLive(self):
        show_time = QTime.currentTime()
        time = show_time.toString()
        show_date = QDate.currentDate()
        date = show_date.toString()
        label_time = "Time: " + time
        label_date = "Date: " + date
        
        self.gui.Text_Time.setText(label_time)
        self.gui.Text_Date.setText(label_date)
        
GuiApp = QApplication(sys.argv)
jarvis_gui = Gui_Start()
jarvis_gui.show()
exit(GuiApp.exec_())