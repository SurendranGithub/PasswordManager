from PyQt5 import QtCore, QtGui, QtWidgets
import random
import sqlite3
import time
from de_en_code import encode
from deencrypt import decode1, encode1

class Ui_Dialog(object):
    def password_generate(self):
        upper = "ABCDEGHIJKLMNOPQRSTUVWXYZ"
        lower = "abcdefghijklmnopqrstuvwxyz"
        number = "0123456789"
        symbols = "/*-+&%#@!?><$"
        total = upper + lower + number + number + symbols
        password = ""
        for i in range(self.spinBox.value()):
            temp = random.choice(total)
            password += temp
        self.passwrd = password
        self.passwordasof.setText(self.passwrd)
    def check(self):
        if self.addname.text() == "":
            self.label_6.setText("Please enter a domain name")
            return
        else:
            a = encode1(self.addname.text())
        if self.passwordasof.text() == "":
            self.label_6.setText("Please generate a password")
            return
        else:
            b = encode1(self.passwordasof.text())
        if self.usernameasof.text() == "":
            domainuser = encode1("-----")
        else:
            domainuser = encode1(self.usernameasof.text())
        if self.webappadd.text() == "":
            webappaddress = encode1("-----")
        else:
            webappaddress = encode1(self.webappadd.text())
        conc = sqlite3.connect("new.db")
        curs = conc.cursor()
        f = open("dummy.txt", "r")
        self.user = encode(decode1(f.readline()))
        f.close()
        time_now = time.strftime("%B %d %Y %H:%M:%S", time.localtime())
        self.cmd = "insert into " + self.user + " values (\"" + a + "\" , \"" + webappaddress + "\", \"" + domainuser + "\", \"" + b + "\", \"" + time_now + "\");"
        curs.execute(self.cmd)
        conc.commit()
        conc.close()
        from passwordelite import Ui_MainWindow
        self.win = QtWidgets.QMainWindow()
        self.ui2 = Ui_MainWindow()
        self.ui2.setupUi(self.win)
        self.ui2.loaddata(self.user)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(387, 305)
        Dialog.setMinimumSize(QtCore.QSize(387, 305))
        Dialog.setMaximumSize(QtCore.QSize(387, 305))
        Dialog.setStyleSheet("background-color : lightgrey")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Imagine_ChildWorks.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 118, 121, 16))
        self.label.setObjectName("label")
        self.addname = QtWidgets.QLineEdit(Dialog)
        self.addname.setGeometry(QtCore.QRect(140, 18, 221, 22))
        self.addname.setStyleSheet("QLineEdit{\n"
"    background-color : #ededed;\n"
"    border-radius : 10px;\n"
"    border : 1px solid black;\n"
"}\n"
"QLineEdit:focus{\n"
"    border : 1px solid orangered;\n"
"    background-color : white;\n"
"}")
        self.passwrd = ""
        self.addname.setObjectName("addname")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(67, 203, 70, 20))
        self.label_2.setObjectName("label_2")
        self.usernameasof = QtWidgets.QLineEdit(Dialog)
        self.usernameasof.setGeometry(QtCore.QRect(140, 68, 221, 22))
        self.usernameasof.setStyleSheet("QLineEdit{\n"
"    background-color : #ededed;\n"
"    border-radius : 10px;\n"
"    border : 1px solid black;\n"
"}\n"
"QLineEdit:focus{\n"
"    border : 1px solid orangered;\n"
"    background-color : white;\n"
"}")
        self.usernameasof.setObjectName("usernameasof")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(80, 21, 51, 16))
        self.label_3.setObjectName("label_3")
        self.webappadd = QtWidgets.QLineEdit(Dialog)
        self.webappadd.setGeometry(QtCore.QRect(140, 118, 221, 22))
        self.webappadd.setStyleSheet("QLineEdit{\n"
"    background-color : #ededed;\n"
"    border-radius : 10px;\n"
"    border : 1px solid black;\n"
"}\n"
"QLineEdit:focus{\n"
"    border : 1px solid orangered;\n"
"    background-color : white;\n"
"}")
        self.webappadd.setObjectName("webappadd")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(60, 68, 71, 16))
        self.label_4.setObjectName("label_4")
        self.passwordasof = QtWidgets.QLineEdit(Dialog)
        self.passwordasof.setGeometry(QtCore.QRect(140, 204, 221, 22))
        self.passwordasof.setStyleSheet("QLineEdit{\n"
"    background-color : #ededed;\n"
"    border-radius : 10px;\n"
"    border : 1px solid black;\n"
"}\n"
"QLineEdit:focus{\n"
"    border : 1px solid orangered;\n"
"    background-color : white;\n"
"}")
        self.passwordasof.setObjectName("passwordasof")
        self.OK = QtWidgets.QPushButton(Dialog, clicked = lambda : self.check())
        self.OK.setGeometry(QtCore.QRect(207, 260, 93, 28))
        self.OK.setStyleSheet("QPushButton{\n"
"    background-color : white; \n"
"    color : blue;\n"
"    border-radius : 10px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color : skyblue;\n"
"    color : white;\n"
"    border : 1px solid black;\n"
"    font-weight : bold;\n"
"    font-size : 15px;\n"
"}")
        self.OK.setObjectName("OK")
        self.OK.clicked.connect(Dialog.close)
        self.Cancel = QtWidgets.QPushButton(Dialog)
        self.Cancel.setGeometry(QtCore.QRect(107, 260, 93, 28))
        self.Cancel.setStyleSheet("QPushButton{\n"
"    background-color : white; \n"
"    color : blue;\n"
"    border-radius : 10px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color : skyblue;\n"
"    color : white;\n"
"    border : 1px solid black;\n"
"    font-weight : bold;\n"
"    font-size : 15px;\n"
"}")
        self.Cancel.setObjectName("Cancel")
        self.changebtn = QtWidgets.QPushButton(Dialog, clicked = lambda : self.password_generate())
        self.changebtn.setGeometry(QtCore.QRect(210, 162, 171, 28))
        self.changebtn.setStyleSheet("QPushButton{\n"
"    background-color : white; \n"
"    color : blue;\n"
"    border-radius : 10px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color : skyblue;\n"
"    color : white;\n"
"    border : 1px solid black;\n"
"    font-weight : bold;\n"
"    font-size : 13px;\n"
"}")
        self.changebtn.setObjectName("changebtn")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(4, 168, 151, 16))
        self.label_5.setObjectName("label_5")
        self.spinBox = QtWidgets.QSpinBox(Dialog)



        self.spinBox.setGeometry(QtCore.QRect(160, 166, 42, 22))
        self.spinBox.setStyleSheet("background-color : #ededed;")
        self.spinBox.setObjectName("spinBox")
        

        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(100, 230, 211, 20))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "New entry"))
        self.label.setText(_translate("Dialog", "Web/App address : "))
        self.label_2.setText(_translate("Dialog", "Password :"))
        self.label_3.setText(_translate("Dialog", "Name* : "))
        self.label_4.setText(_translate("Dialog", "User name :"))
        self.OK.setText(_translate("Dialog", "OK"))
        self.Cancel.setText(_translate("Dialog", "Cancel"))
        self.Cancel.clicked.connect(Dialog.close)
        self.changebtn.setText(_translate("Dialog", "Generate new password"))
        self.label_5.setText(_translate("Dialog", "Lenght of the password :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
