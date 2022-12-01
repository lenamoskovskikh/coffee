

a = None
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(396, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 50, 55, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 40, 201, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 390, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 55, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 80, 201, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 55, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 130, 201, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 180, 55, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(100, 180, 201, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 240, 55, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 280, 55, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 330, 55, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(100, 230, 201, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(100, 270, 201, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(100, 320, 201, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 390, 121, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(0, 460, 371, 31))
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 396, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "id"))
        self.pushButton.setText(_translate("MainWindow", "редактировать"))
        self.label_2.setText(_translate("MainWindow", "sort"))
        self.label_3.setText(_translate("MainWindow", "roast"))
        self.label_4.setText(_translate("MainWindow", "type"))
        self.label_5.setText(_translate("MainWindow", "taste"))
        self.label_6.setText(_translate("MainWindow", "price"))
        self.label_7.setText(_translate("MainWindow", "amount"))
        self.pushButton_2.setText(_translate("MainWindow", "добавить"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(931, 734)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 911, 591))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 630, 181, 51))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 931, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "изменить"))


class Widget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        global a
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect('coffee.db')
        self.cur = self.con.cursor()
        self.pushButton.clicked.connect(self.run)
        self.new()
        a = self

    def run(self):
        self.secwindow = SecondWindow()
        self.secwindow.show()


    def new(self):
        result = self.cur.execute(f"""SELECT * FROM type""").fetchall()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(['id', 'sort', 'roast', 'type', 'taste', 'price', 'amount'])
        #объем в граммах
        #цена в рублях

        for value, item in enumerate(result):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for el, row in enumerate(item):
                self.tableWidget.setItem(value, el, QTableWidgetItem(str(row)))


class SecondWindow(QMainWindow, Ui_MainWindow2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect('coffee.db')
        self.cur = self.con.cursor()
        self.label_8.setText('для добавления все, кроме id') #для изменения нужно ввести id уже существующей записи, а далее новую информацию
        self.pushButton.clicked.connect(self.delete)
        self.pushButton_2.clicked.connect(self.add)

    def delete(self):
        self.label_8.setText('')
        id = self.lineEdit.text()
        sort = self.lineEdit_2.text()
        roast = self.lineEdit_3.text()
        type = self.lineEdit_4.text()
        taste = self.lineEdit_5.text()
        price = self.lineEdit_6.text()
        amount = self.lineEdit_7.text()
        try:
            self.cur.execute(
                f"""UPDATE type SET sort = '{sort}' WHERE id = {int(id)}""")
            self.cur.execute(
                f"""UPDATE type SET roast = '{roast}' WHERE id = {int(id)}""")
            self.cur.execute(
                f"""UPDATE type SET type = '{type}' WHERE id = {int(id)}""")
            self.cur.execute(
                f"""UPDATE type SET taste = '{taste}' WHERE id = {int(id)}""")
            self.cur.execute(
                f"""UPDATE type SET price = '{int(price)}' WHERE id = {int(id)}""")
            self.cur.execute(
                f"""UPDATE type SET price = '{int(amount)}' WHERE id = {int(id)}""")
        except Exception:
            self.label_8.setText('Неверно заполнена форма')
            return
        self.con.commit()
        self.con.close()
        Widget.new(a)
        self.close()

    def add(self):
        self.label_8.setText('')
        id = self.lineEdit.text()
        sort = self.lineEdit_2.text()
        roast = self.lineEdit_3.text()
        type = self.lineEdit_4.text()
        taste = self.lineEdit_5.text()
        price = self.lineEdit_6.text()
        amount = self.lineEdit_7.text()
        try:
            self.cur.execute(f"""
                                INSERT INTO type(sort, roast, type, taste, price, amount) VALUES('{sort}', '{roast}', '{type}', '{taste}', '{int(price)}', '{int(amount)}')""")
        except Exception:
            self.label_8.setText('Неверно заполнена форма')
            return
        self.con.commit()
        self.con.close()
        Widget.new(a)
        self.close()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec_())