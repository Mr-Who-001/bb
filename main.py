import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
import sqlite3


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        result = cur.execute('SELECT * FROM coffe').fetchall()
        self.tw.setRowCount(len(result))
        for i in range(len(result)):
            self.tw.setItem(i, 0, QTableWidgetItem(str(result[i][0])))
            self.tw.setItem(i, 1, QTableWidgetItem(str(result[i][1])))
            self.tw.setItem(i, 2, QTableWidgetItem(str(result[i][2])))
            self.tw.setItem(i, 3, QTableWidgetItem(str(result[i][3])))
            self.tw.setItem(i, 4, QTableWidgetItem(str(result[i][4])))
            self.tw.setItem(i, 5, QTableWidgetItem(str(result[i][5])))
            self.tw.setItem(i, 6, QTableWidgetItem(str(result[i][6])))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())