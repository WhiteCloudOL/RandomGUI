from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSlot
import random, sys, time
import GUI as u1  # 假设你的 Ui_MainWindow 类在 GUI 模块中
import GUI2 as u2
import GUI3 as u3
import GUI4 as u4


class MyMainWindow(QMainWindow):
    def openrandomint(self):
        win2.show()
        return

    def openrandomintn(self):  # 人数统计列表htz，未写入程序
        win3.show()
        return

    def openrandg(self):    # 组随机，未完成
        win4.show()
        return

    def __init__(self):
        super().__init__()

        # 实例化 Ui_MainWindow 类
        self.ui = u1.Ui_Mainwindow()

        # 调用 setupUi 方法并传递当前的 QMainWindow 对象
        self.ui.setupUi(self)


class Form2Window(QMainWindow): # 随机摇号/随机数窗口
    @pyqtSlot()
    def reset(self):
        try:
            f2, t2 = int(self.ui.lineEdit_2.text()), int(self.ui.lineEdit_3.text())
        except:
            f2, t2 = 0, 100
        if f2 <= t2:
            global ht2, count, htz
            ht2 = [i for i in range(f2, t2 + 1)]
            htz = [0] * len(ht2)
            count = 0
        self.ui.textEdit.setText("")
        self.ui.lineEdit.setText("")

    @pyqtSlot()
    def run(self):
        global ht2, count, htz
        count += 1
        ygs = len(ht2)
        gs = int(self.ui.lineEdit_4.text())
        if ht2:
            if ygs >= gs:
                rs = [i for i in random.sample(ht2, gs)]
            else:
                rs = [i for i in random.sample(ht2, ygs)]
            if not self.ui.checkBox.isChecked():
                for i in rs:
                    ht2.remove(i)
                    htz[i] += 1
            else:
                for i in rs:
                    htz[i] += 1
            self.ui.lineEdit.setText(str(rs))
            self.ui.lineEdit_5.setText(str(count))
            self.ui.lineEdit_6.setText(str(len(ht2)))
            self.ui.textEdit.insertPlainText("第" + str(count) + "次：" + str(rs) + "\n")
        else:
            self.ui.lineEdit.setText("已抽尽")

    @pyqtSlot()
    def rable(self):
        global re2
        if self.ui.checkBox.isChecked():
            re2 = 1
        else:
            re2 = 0

    def __init__(self, parent=None):
        super(Form2Window, self).__init__(parent)
        self.ui = u2.Ui_UI_Form2()
        self.ui.setupUi(self)


class Form3Window(QMainWindow):
    def __init__(self, parent=None):
        super(Form3Window, self).__init__(parent)
        self.ui = u3.Ui_UI_Form3()
        self.ui.setupUi(self)


class Form4Window(QMainWindow):
    def __init__(self, parent=None):
        super(Form4Window, self).__init__(parent)
        self.ui = u4.Ui_UI_Form4()
        self.ui.setupUi(self)


if __name__ == '__main__':
    ht2 = [i for i in range(0, 101)]
    re2 = 0
    count = 0
    htz = [0] * len(ht2)  # 各个随机数次数统计，未写入
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    win2 = Form2Window()
    win3 = Form3Window()
    win4 = Form4Window()
    sys.exit(app.exec_())
