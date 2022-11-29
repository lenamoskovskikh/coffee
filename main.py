

a = None
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets

class Widget(QMainWindow):
    def __init__(self):
        global a
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect('coffee.db')
        self.cur = self.con.cursor()
        self.new()
        a = self


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






if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec_())