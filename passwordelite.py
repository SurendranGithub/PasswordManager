from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from de_en_code import decode, encode
from deencrypt import decode1, encode1

class Ui_MainWindow(object):
    def searchcontent(self, letters, username):
        if len(letters) > 0:
            conc = sqlite3.connect("new.db")
            curs = conc.cursor()
            self.cmd = "select count(Time) from " + str(username) + " where addressname like \'" + encode1(str(letters)) + "%\';"
            curs.execute(self.cmd)
            self.count = curs.fetchone()
            self.count = self.count[0]
            self.cmd = "select * from " + str(username) + " where addressname like '" + encode1(str(letters)) + "%';"
            self.tableWidget.setRowCount(self.count)
            tablerow = 0
            for rows in curs.execute(self.cmd):
                self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(decode1(rows[0])))
                self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(decode1(rows[1])))
                self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(decode1(rows[2])))
                self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(decode1(rows[3])))
                self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(rows[4]))
                tablerow += 1  
            conc.commit()
            conc.close()
    def loaddata(self, username):
        self.namehere.setText(decode(username))
        conc = sqlite3.connect("new.db")
        curs = conc.cursor()
        self.cmd = "select count(Time) from " + str(username) + ";"
        curs.execute(self.cmd)
        self.count = curs.fetchone()
        self.count = self.count[0]
        self.cmd = "select * from " + username + ";"
        self.tableWidget.setRowCount(self.count)
        tablerow = 0
        for rows in curs.execute(self.cmd):
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(decode1(rows[0])))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(decode1(rows[1])))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(decode1(rows[2])))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(decode1(rows[3])))
            self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(rows[4]))
            tablerow += 1  
        conc.commit()
        conc.close()      
    def logout(self):
        from login import Ui_LoginPage
        self.logwin = QtWidgets.QMainWindow()
        self.ui = Ui_LoginPage()
        self.ui.setupUi(self.logwin)
        self.logwin.show()
    def add(self):
        from newpass import Ui_Dialog
        self.addnew = QtWidgets.QDialog()
        self.ui2 = Ui_Dialog()
        self.ui2.setupUi(self.addnew)
        self.addnew.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setSizeIncrement(QtCore.QSize(0, 0))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Imagine_ChildWorks.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: lightgrey;")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 230, 740, 261))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setStyleSheet("background-color: white;")
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setAutoScrollMargin(10)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(147)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.LOGO = QtWidgets.QLabel(self.centralwidget)
        self.LOGO.setGeometry(QtCore.QRect(-10, 20, 821, 71))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.LOGO.setFont(font)
        self.LOGO.setStyleSheet("background-color : skyblue; border : 2px solid black;")
        self.LOGO.setAlignment(QtCore.Qt.AlignCenter)
        self.LOGO.setObjectName("LOGO")
        self.appname = QtWidgets.QLabel(self.centralwidget)
        self.appname.setGeometry(QtCore.QRect(180, 100, 451, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.appname.setFont(font)
        self.appname.setAlignment(QtCore.Qt.AlignCenter)
        self.appname.setObjectName("appname")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 140, 81, 16))
        self.label.setObjectName("label")


        self.namehere = QtWidgets.QLabel(self.centralwidget)
        self.namehere.setGeometry(QtCore.QRect(120, 140, 381, 16))
        self.namehere.setObjectName("namehere")
        f = open("dummy.txt", "r")
        self.user = encode(decode1(f.readline()))
        f.close()
        self.loaddata(self.user)
        

        self.searchbar = QtWidgets.QLineEdit(self.centralwidget)
        self.searchbar.setGeometry(QtCore.QRect(30, 190, 481, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.searchbar.setFont(font)
        self.searchbar.setStyleSheet("background-color : white;")
        self.searchbar.setText("")
        self.searchbar.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.searchbar.setObjectName("searchbar")
        self.logoutbtn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.logout())
        self.logoutbtn.setGeometry(QtCore.QRect(700, 130, 61, 31))
        self.logoutbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logoutbtn.setStyleSheet("QPushButton\n"
"{\n"
"    background-color : lightblue;\n"
"    border-radius : 15px;\n"
"    border : 2px solid black;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color : skyblue;\n"
"}")
        self.logoutbtn.setObjectName("logoutbtn")
        self.logoutbtn.clicked.connect(MainWindow.close)
        self.addnewbtn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.add())
        self.addnewbtn.setGeometry(QtCore.QRect(330, 510, 141, 41))
        self.addnewbtn.setStyleSheet("QPushButton{\n"
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
        self.addnewbtn.setObjectName("addnewbtn")
        self.loaddata(self.user)
        self.srchbtn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.searchcontent(self.searchbar.text(), self.user))
        self.srchbtn.setGeometry(QtCore.QRect(520, 190, 121, 31))
        self.srchbtn.setStyleSheet("QPushButton{\n"
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
        self.srchbtn.setObjectName("srchbtn")
        self.srchresetbtn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.loaddata(self.user))
        self.srchresetbtn.setGeometry(QtCore.QRect(650, 190, 121, 31))
        self.srchresetbtn.setStyleSheet("QPushButton{\n"
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
        self.srchresetbtn.setObjectName("srchresetbtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Imagine ChildWorks - Password Elite"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Web/App address"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Username"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Password"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "TOC"))
        self.LOGO.setText(_translate("MainWindow", "Imagine ChildWorks"))
        self.appname.setText(_translate("MainWindow", "Password Elite"))
        self.label.setText(_translate("MainWindow", "User name  :"))
        self.searchbar.setPlaceholderText(_translate("MainWindow", " Search domain name"))
        self.logoutbtn.setText(_translate("MainWindow", "Logout"))
        self.addnewbtn.setText(_translate("MainWindow", "Add new"))
        self.srchbtn.setText(_translate("MainWindow", "Search"))
        self.srchresetbtn.setText(_translate("MainWindow", "Refresh"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
