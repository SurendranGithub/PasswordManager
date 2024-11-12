from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import time
from de_en_code import decode, encode
from deencrypt import decode1, encode1

class Ui_SignupPage(object):

    def openloginpage(self):
        from login import Ui_LoginPage
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_LoginPage()
        self.ui.setupUi(self.window)
        self.window.show()

    def signedup(self, SPage):
        if self.username.text().isalnum():
               self.signupinfo.setText("")
               self.subuser = encode(self.username.text())
               if (4 > len(self.subuser)) or (len(self.subuser) > 20):
                       self.signupinfo.setText("User name must have 4-20 characters")
                       return
               users = sqlite3.connect("new.db")
               cusers = users.cursor()
               self.temp = 0
               self.userlist = []
               self.cmd = "select name from users;"
               cusers.execute(self.cmd)
               self.usertup = cusers.fetchall()
               self.cmd = "select count(name) from users;"
               cusers.execute(self.cmd)
               self.usercount = cusers.fetchone()
               self.usercount = self.usercount[0]
               for i in range(self.usercount):
                   self.userlist.append(self.usertup[i][0])
               for i in range(self.usercount):
                   if str(self.userlist[i]).lower() == self.subuser.lower():
                       self.temp = 1
               if self.temp == 1:
                       self.signupinfo.setText("User name already exists.")
               else :
                       if (4 > len(self.password.text())) or (len(self.password.text()) > 20):
                               self.signupinfo.setText("Password must have 4-20 characters")
                               return
                       self.signupinfo.setText("")
                       self.siguser = encode(self.username.text())
                       self.sigpass = encode(self.password.text())
                       self.sigconpass = encode(self.confirmpassword.text())
                       if self.sigpass != self.sigconpass:
                           self.signupinfo.setText("Password and Conformation password are not same.")
                           self.password.setText("")
                           self.confirmpassword.setText("")
                       else:
                           time_now = time.strftime("%B %d %Y %H:%M:%S", time.localtime())
                           self.cmd = "insert into users values (\"" + encode1(decode(self.siguser)) + "\", \"" + encode1(decode(self.sigpass)) + "\");"
                           cusers.execute(self.cmd)
                           self.cmd = "create table \"" + self.siguser + "\" (\"addressname\" TEXT, \"domain\" TEXT, \"username\" TEXT, \"password\" TEXT, \"Time\" TEXT);"
                           cusers.execute(self.cmd)
                           f = open("users.txt", "a")
                           txt = self.siguser + " => " + time_now + "\n"
                           f.write(txt)
                           f.close()
                           f = open("dummy.txt", "w")
                           f.write(encode1(decode(self.subuser)))
                           f.close()
                           users.commit()
                           SPage.close()
                           from passwordelite import Ui_MainWindow
                           self.window2 = QtWidgets.QMainWindow()
                           self.ui2 = Ui_MainWindow()
                           self.ui2.setupUi(self.window2)
                           self.ui2.namehere.setText(decode(self.siguser))
                           self.ui2.user.join(decode(self.siguser))
                           self.window2.show()
               users.commit()
               users.close()
        else:
                self.signupinfo.setText("Username must be alphabet or numberics")

    def setupUi(self, SignupPage):
        SignupPage.setObjectName("SignupPage")
        SignupPage.resize(450, 560)
        SignupPage.setMinimumSize(QtCore.QSize(450, 560))
        SignupPage.setMaximumSize(QtCore.QSize(450, 560))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Imagine_ChildWorks.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SignupPage.setWindowIcon(icon)
        SignupPage.setStyleSheet("background-color: lightgrey;")
        self.centralwidget = QtWidgets.QWidget(SignupPage)
        self.centralwidget.setObjectName("centralwidget")
        self.appname = QtWidgets.QLabel(self.centralwidget)
        self.appname.setGeometry(QtCore.QRect(0, 120, 451, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.appname.setFont(font)
        self.appname.setAlignment(QtCore.Qt.AlignCenter)
        self.appname.setObjectName("appname")
        self.LOGO = QtWidgets.QLabel(self.centralwidget)
        self.LOGO.setGeometry(QtCore.QRect(-50, 20, 561, 71))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.LOGO.setFont(font)
        self.LOGO.setStyleSheet("background-color : skyblue; border : 2px solid black;")
        self.LOGO.setAlignment(QtCore.Qt.AlignCenter)
        self.LOGO.setObjectName("LOGO")
        self.signupinfo = QtWidgets.QLabel(self.centralwidget)
        self.signupinfo.setGeometry(QtCore.QRect(10, 440, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.signupinfo.setFont(font)
        self.signupinfo.setStyleSheet("background-color : transparent; color : red;")
        self.signupinfo.setText("")
        self.signupinfo.setAlignment(QtCore.Qt.AlignCenter)
        self.signupinfo.setObjectName("signupinfo")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 170, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(110, 190, 241, 41))
        self.username.setStyleSheet("QLineEdit{\n"
"    background-color : #ededed;\n"
"    border-radius : 10px;\n"
"    border : 1px solid black;\n"
"}\n"
"QLineEdit:focus{\n"
"    border : 1px solid orangered;\n"
"    background-color : white;\n"
"}")
        self.username.setObjectName("username")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 240, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setStyleSheet("QLabel::after{content : '*'; color : red;}")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(110, 260, 241, 41))
        self.password.setStyleSheet("QLineEdit{\n"
"    background-color : #ededed;\n"
"    border-radius : 10px;\n"
"    border : 1px solid black;\n"
"}\n"
"QLineEdit:focus{\n"
"    border : 1px solid orangered;\n"
"    background-color : white;\n"
"}")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.confirmpassword = QtWidgets.QLineEdit(self.centralwidget)
        self.confirmpassword.setGeometry(QtCore.QRect(110, 330, 241, 41))
        self.confirmpassword.setStyleSheet("QLineEdit{\n"
"    background-color : #ededed;\n"
"    border-radius : 10px;\n"
"    border : 1px solid black;\n"
"}\n"
"QLineEdit:focus{\n"
"    border : 1px solid orangered;\n"
"    background-color : white;\n"
"}")
        self.confirmpassword.setText("")
        self.confirmpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpassword.setObjectName("confirmpassword")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 310, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setGeometry(QtCore.QRect(110, 390, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.reset.setFont(font)
        self.reset.setStyleSheet("QPushButton{\n"
"    background-color : lightblue; \n"
"    border-radius : 20px; \n"
"    border : 2px solid black;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color : skyblue;\n"
"};")
        self.reset.setObjectName("reset")
        self.signupbtn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.signedup(SignupPage))
        self.signupbtn.setGeometry(QtCore.QRect(240, 390, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.signupbtn.setFont(font)
        self.signupbtn.setStyleSheet("QPushButton{\n"
"    background-color : lightblue; \n"
"    border-radius : 20px; \n"
"    border : 2px solid black;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color : skyblue;\n"
"};")
        self.signupbtn.setObjectName("signupbtn")
        self.loginbtn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.openloginpage())
        self.loginbtn.clicked.connect(SignupPage.close)
        self.loginbtn.setGeometry(QtCore.QRect(260, 488, 111, 20))
        self.loginbtn.setStyleSheet("QPushButton{\n"
"    background-color : lightblue; \n"
"    border-radius : 10px; \n"
"    border : 2px solid black;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color : skyblue;\n"
"};")
        self.loginbtn.setObjectName("loginbtn")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 490, 161, 20))
        self.label_4.setStyleSheet("background-color : transparent;")
        self.label_4.setObjectName("label_4")
        SignupPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SignupPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 26))
        self.menubar.setObjectName("menubar")
        SignupPage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SignupPage)
        self.statusbar.setObjectName("statusbar")
        SignupPage.setStatusBar(self.statusbar)

        self.retranslateUi(SignupPage)
        self.reset.clicked.connect(self.username.clear) # type: ignore
        self.reset.clicked.connect(self.signupinfo.clear) # type: ignore
        self.reset.clicked.connect(self.password.clear) # type: ignore
        self.reset.clicked.connect(self.confirmpassword.clear) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(SignupPage)

    def retranslateUi(self, SignupPage):
        _translate = QtCore.QCoreApplication.translate
        SignupPage.setWindowTitle(_translate("SignupPage", "Password Elite - Sign up"))
        self.appname.setText(_translate("SignupPage", "Password Elite"))
        self.LOGO.setText(_translate("SignupPage", "Imagine ChildWorks"))
        self.label.setText(_translate("SignupPage", "User name : "))
        self.label_2.setText(_translate("SignupPage", "Password :"))
        self.label_3.setText(_translate("SignupPage", "Confirm Password :"))
        self.reset.setText(_translate("SignupPage", "Reset"))
        self.signupbtn.setText(_translate("SignupPage", "Sign up"))
        self.loginbtn.setText(_translate("SignupPage", "Login"))
        self.label_4.setText(_translate("SignupPage", "Already have an account  :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SignupPage = QtWidgets.QMainWindow()
    ui = Ui_SignupPage()
    ui.setupUi(SignupPage)
    SignupPage.show()
    sys.exit(app.exec_())
