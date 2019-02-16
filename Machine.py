"""
Winning Combinations:
    3x seven = 500
    3x any = 100
    2x any = 10
"""

import random
import time

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(793, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 791, 311))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.reel_one_lbl = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.reel_one_lbl.setObjectName("reel_one_lbl")
        self.horizontalLayout.addWidget(self.reel_one_lbl)
        self.reel_two_lbl = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.reel_two_lbl.setObjectName("reel_two_lbl")
        self.horizontalLayout.addWidget(self.reel_two_lbl)
        self.reel_three_lbl = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.reel_three_lbl.setObjectName("reel_three_lbl")
        self.horizontalLayout.addWidget(self.reel_three_lbl)
        self.balanceLbl = QtWidgets.QLabel(self.centralwidget)
        self.balanceLbl.setGeometry(QtCore.QRect(330, 430, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setItalic(False)
        font.setUnderline(True)
        self.balanceLbl.setFont(font)
        self.balanceLbl.setTextFormat(QtCore.Qt.AutoText)
        self.balanceLbl.setScaledContents(False)
        self.balanceLbl.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.balanceLbl.setObjectName("balanceLbl")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(260, 480, 281, 61))
        self.lcdNumber.setSmallDecimalPoint(True)
        self.lcdNumber.setDigitCount(8)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber.setProperty("value", 0)
        # self.lcdNumber.setProperty("intValue", 421)
        self.lcdNumber.setObjectName("lcdNumber")
        self.spinButton = QtWidgets.QPushButton(self.centralwidget)
        self.spinButton.setGeometry(QtCore.QRect(290, 330, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.spinButton.setFont(font)
        self.spinButton.setObjectName("spinButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 793, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.spinButton.clicked.connect(self.spinPressed)
        self.money_balance = float(0)


    def spinPressed(self, MainWindow):
        
        fruit = ["apple.png", "banana.png", "pear.png", "bell.png", "cherry.png", "7.png"]
        new_reels = []
        
        for i in range(3):
            random_fruit = random.randint(0, len(fruit)-1)
            
            new_reels.append(fruit[random_fruit])
        
        self.updateReels(new_reels)
        self.checkWinning(new_reels)
        self.updateBalance()
    

    def updateReels(self, reels):        
        one_width = self.reel_one_lbl.width()
        one_height = self.reel_one_lbl.height()
        pixmap_one = QtGui.QPixmap(reels[0])

        two_width = self.reel_two_lbl.width()
        two_height = self.reel_two_lbl.height()
        pixmap_two = QtGui.QPixmap(reels[1])

        three_width = self.reel_three_lbl.width()
        three_height = self.reel_three_lbl.height()
        pixmap_three = QtGui.QPixmap(reels[2])
        

        self.reel_one_lbl.setPixmap(pixmap_one.scaled(one_width, one_height, QtCore.Qt.KeepAspectRatio))
        self.reel_two_lbl.setPixmap(pixmap_two.scaled(two_width, two_height, QtCore.Qt.KeepAspectRatio))
        self.reel_three_lbl.setPixmap(pixmap_three.scaled(three_width, three_height, QtCore.Qt.KeepAspectRatio))
        

    def checkWinning(self, reels):
        self.money_balance -= 5
        
        if reels[0] == "7.png" and reels[0] == reels[1] and reels[0] == reels[2]:
            self.money_balance += 500 # 777!
            
        elif reels[0] == reels[1] and reels[0] == reels[2]:
            self.money_balance += 100 # ALL THREE

        elif reels[0] == reels[1] or reels[1] == reels[2]:
            self.money_balance += 10 # 2 the same.
        else:
            pass
        

    def updateBalance(self):
        self.lcdNumber.setProperty("value", self.money_balance)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fruit Machine - by Reece"))
        self.reel_one_lbl.setText(_translate("MainWindow", ""))
        self.reel_two_lbl.setText(_translate("MainWindow", ""))
        self.reel_three_lbl.setText(_translate("MainWindow", ""))
        self.balanceLbl.setText(_translate("MainWindow", "Balance"))
        self.spinButton.setText(_translate("MainWindow", "Spin!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

