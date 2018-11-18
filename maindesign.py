# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 14:18:42 2018

@author: aayush
"""

import sys
import os 
        


from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog,QMainWindow,QFileDialog,QLabel,QProgressBar 
from PyQt5.QtGui import QIcon, QPixmap


from PyQt5.uic import loadUi
import image_emotion_gender_demo




class LoginPage(QMainWindow):
    def __init__(self):
        super(LoginPage, self).__init__()
        loadUi('E:/secondpage.ui', self)
        self.show()
        self.test()
        
    def test(self):
        self.pushButton.clicked.connect(self.testnew)
    def testnew(self):    
        filename =QFileDialog.getOpenFileName(self,'Test Dialog', os.getcwd(), 'All Files(*.*)')
        b = f'"{filename[0]}"'
        
        print(b)
       # label=QLabel(self)
        #label.setPixmap(QPixmap(b))
        
        
        #self.label_2.setText(b)
        #self.setWindowIcon(QIcon())
        #label.show()
        
        
     # print(filename)  
class HomePage(QMainWindow):
    def __init__(self):
        super(HomePage, self).__init__()
        loadUi('E:/thirdpage.ui', self)
        self.pushButton.clicked.connect(self.executeLoginPage)
        self.pushButton_4.clicked.connect(self.executevideo)
        self.pushButton_2.clicked.connect(self.executeimage)
        self.pushButton_3.clicked.connect(self.executelivevideo)
#        self.progress=QProgressBar(self)
 #       self.progress.setGeometry(30,180,841,23)
        #self.pushButton_2.clicked.connect(self.executeVideo)
        #self.btnRegisterPage.clicked.connect(self.executeRegisterPage)

    def executelivevideo(self):
        import video_emotion_gender_demo
        video_emotion_gender_demo.runscript()
        
    def executeLoginPage(self):
        
        self.completed= 20
        self.progressBar.setValue(self.completed)
        
        filename =QFileDialog.getOpenFileName(self,'Test Dialog', os.getcwd(), 'All Files(*.*)')
        b = f'"{filename[0]}"'
        self.label_4.setText(filename[0])
        self.completed= 40
        self.progressBar.setValue(self.completed)
        
        print(b)
    
    def executeimage(self) :
       
        path=self.label_4.text()  
        print("hi2")
                    
        self.completed= 55
        self.progressBar.setValue(self.completed)
        ret=image_emotion_gender_demo.main(path)
        self.completed= 80
        self.progressBar.setValue(self.completed)
        print("abcdefg"+ret[0])
        self.completed=100
        self.progressBar.setValue(self.completed)
        if ret[0] == "angry" :
            self.label_8.setText(ret[0] + "=> Not good for health ")
        if ret[0] == "sad" :
            self.label_8.setText(ret[0] + "=> Hmm.. not doing well ?")
        if ret[0] == "happy" :
            self.label_8.setText(ret[0] + "=> Seems you are happy enough")
        if ret[0] == "disgust" :
            self.label_8.setText(ret[0] + "=> Noo. Not at all .")
        if ret[0] == "neutral" :
            self.label_8.setText(ret[0] + "=> Have a good day")
        if ret[0] == "fear" :
            self.label_8.setText(ret[0]+"=> Don't signup for it !")
        if ret[0] == "surprise" :
            self.label_8.setText(ret[0]+ "=> The best things happen unexpectedly .")
            
        self.label_10.setText(str(ret[1]))
        QMainWindow.hide()
        
    def executevideo(self) :
        #os.system("E:/seleniumdemo/seleniumdemo/dmo.py")
        import demo
        demo.main("E:/face_classification-master/trained_models/detection_models/haarcascade_frontalface_default.xml")
        
app = QApplication(sys.argv)
widget = HomePage()
widget.show()
sys.exit(app.exec_())        