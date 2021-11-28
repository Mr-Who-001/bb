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
        self.pushButton.clicked.connect(self.f)

    def f(self):
        self.w2 = Example()
        self.w2.show()
        self.hide()


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.pushButton.clicked.connect(self.g)

    def g(self):
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        result = cur.execute('SELECT * FROM coffe WHERE названиесорта = ?', (self.lineEdit_6.text(),)).fetchall()
        try:
            if result == []:
                cur.execute("INSERT INTO coffe VALUES(null, ?, ?, ?, ?, ?, ?);", (self.lineEdit_6.text(),
                                                                                  self.lineEdit_3.text(),
                                                                                  self.lineEdit_2.text(),
                                                                                  self.lineEdit_4.text(),
                                                                                  self.lineEdit_5.text(),
                                                                                  self.lineEdit_7.text(),))
                con.commit()
            else:
                cur.execute('''DELETE FROM coffe WHERE названиесорта = ?''', (self.lineEdit_6.text(),))
                con.commit()
                cur.execute("INSERT INTO coffe VALUES(null, ?, ?, ?, ?, ?, ?);", (self.lineEdit_6.text(),
                                                                                  self.lineEdit_3.text(),
                                                                                  self.lineEdit_2.text(),
                                                                                  self.lineEdit_4.text(),
                                                                                  self.lineEdit_5.text(),
                                                                                  self.lineEdit_7.text(),))
                con.commit()
        except BaseException:
            print(0)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())