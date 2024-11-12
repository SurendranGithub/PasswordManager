from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from de_en_code import decode, encode
from deencrypt import decode1, encode1

class Ui_LoginPage(object):
    def opensignuppage(self):
        from signup import Ui_SignupPage
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SignupPage()
        self.ui.setupUi(self.window)
        self.window.show()        

    def submitted(self, Lpage):
        if self.username.text().isalnum():
            if len(self.username.text()) > 3 and len(self.username.text()) < 20:
                users = sqlite3.connect("new.db")
                cusers = users.cursor()
                self.temp = 0
                self.subuser = encode1(self.username.text())
                self.subpass = encode1(self.password.text())
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
                    if self.userlist[i] == self.subuser:
                        self.temp = 1
                if self.temp == 1:
                    self.usererr.setText("")
                    self.passerr.setText("")
                    self.cmd = "select * from users where name = \"" + self.subuser + "\";"
                    cusers.execute(self.cmd)
                    self.orpass = cusers.fetchall()
                    if self.subpass != str(self.orpass[0][1]):
                        self.passerr.setText("Invalid password")
                    else:
                        f = open("dummy.txt", "w")
                        f.write(self.subuser)
                        f.close()
                        from passwordelite import Ui_MainWindow
                        self.window2 = QtWidgets.QMainWindow()
                        self.ui2 = Ui_MainWindow()
                        self.ui2.setupUi(self.window2)
                        self.ui2.namehere.setText(decode1(self.subuser))
                        self.window2.show()
                        Lpage.close()
                else:
                    self.usererr.setText("User doesn't found.")
                users.commit()
                users.close()
            else:
                self.usererr.setText("User does not found")
        else:
                self.signupinfo.setText("Username must be alphabet or numberics")


    def setupUi(self, LoginPage):
        LoginPage.setObjectName("LoginPage")
        LoginPage.setEnabled(True)
        LoginPage.resize(450, 560)
        LoginPage.setMinimumSize(QtCore.QSize(450, 560))
        LoginPage.setMaximumSize(QtCore.QSize(450, 560))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        LoginPage.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Imagine_ChildWorks.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LoginPage.setWindowIcon(icon)
        LoginPage.setStyleSheet("background-color: lightgrey;")
        LoginPage.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(LoginPage)
        self.centralwidget.setObjectName("centralwidget")
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
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(110, 200, 241, 41))
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 180, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(110, 290, 241, 41))
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
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 270, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.submit = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.submitted(LoginPage))
        self.submit.setGeometry(QtCore.QRect(240, 370, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.submit.setFont(font)
        self.submit.setStyleSheet("QPushButton{\n"
"    background-color : lightblue; \n"
"    border-radius : 20px; \n"
"    border : 2px solid black;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color : skyblue;\n"
"};")
        self.submit.setObjectName("submit")
        # self.submit.clicked.connect(LoginPage.close)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 490, 121, 16))
        self.label_3.setStyleSheet("background-color : transparent;")
        self.label_3.setObjectName("label_3")
        self.newuser = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.opensignuppage())
        self.newuser.clicked.connect(LoginPage.close)
        self.newuser.setGeometry(QtCore.QRect(240, 488, 111, 20))
        self.newuser.setStyleSheet("QPushButton{\n"
"    background-color : lightblue; \n"
"    border-radius : 10px; \n"
"    border : 2px solid black;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color : skyblue;\n"
"};")
        self.newuser.setObjectName("newuser")
        self.appname = QtWidgets.QLabel(self.centralwidget)
        self.appname.setGeometry(QtCore.QRect(0, 120, 451, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.appname.setFont(font)
        self.appname.setAlignment(QtCore.Qt.AlignCenter)
        self.appname.setObjectName("appname")
        self.usererr = QtWidgets.QLabel(self.centralwidget)
        self.usererr.setGeometry(QtCore.QRect(110, 240, 241, 20))
        self.usererr.setStyleSheet("background-color : transparent; color : red;")
        self.usererr.setText("")
        self.usererr.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.usererr.setObjectName("usererr")
        self.clearbtn = QtWidgets.QPushButton(self.centralwidget)
        self.clearbtn.setGeometry(QtCore.QRect(110, 370, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.clearbtn.setFont(font)
        self.clearbtn.setStyleSheet("QPushButton{\n"
"    background-color : lightblue; \n"
"    border-radius : 20px; \n"
"    border : 2px solid black;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color : skyblue;\n"
"};")
        self.clearbtn.setObjectName("clearbtn")
        self.passerr = QtWidgets.QLabel(self.centralwidget)
        self.passerr.setGeometry(QtCore.QRect(110, 330, 241, 20))
        self.passerr.setStyleSheet("background-color : transparent; color : red;")
        self.passerr.setText("")
        self.passerr.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.passerr.setObjectName("passerr")
        LoginPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 26))
        self.menubar.setObjectName("menubar")
        LoginPage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginPage)
        self.statusbar.setObjectName("statusbar")
        LoginPage.setStatusBar(self.statusbar)

        self.retranslateUi(LoginPage)
        self.clearbtn.clicked.connect(self.username.clear) # type: ignore
        self.clearbtn.clicked.connect(self.password.clear) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(LoginPage)
        LoginPage.setTabOrder(self.username, self.password)
        LoginPage.setTabOrder(self.password, self.submit)
        LoginPage.setTabOrder(self.submit, self.newuser)
        LoginPage.setTabOrder(self.newuser, self.clearbtn)

    def retranslateUi(self, LoginPage):
        _translate = QtCore.QCoreApplication.translate
        LoginPage.setWindowTitle(_translate("LoginPage", "Password Elite - Login"))
        self.LOGO.setText(_translate("LoginPage", "Imagine ChildWorks"))
        self.label.setText(_translate("LoginPage", "User name : "))
        self.label_2.setText(_translate("LoginPage", "Password :"))
        self.submit.setText(_translate("LoginPage", "Submit"))
        self.label_3.setText(_translate("LoginPage", "Create a new user  :"))
        self.newuser.setText(_translate("LoginPage", "New user"))
        self.appname.setText(_translate("LoginPage", "Password Elite"))
        self.clearbtn.setText(_translate("LoginPage", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginPage = QtWidgets.QMainWindow()
    ui = Ui_LoginPage()
    ui.setupUi(LoginPage)
    LoginPage.show()
    sys.exit(app.exec_())
