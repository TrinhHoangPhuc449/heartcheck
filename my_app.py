from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)

from instr import*
from second_win import*
class MainWin(QWidget):
    def __init__(self):
        '''the window which the greeting is located in'''
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()

    def initUI(self):
        '''Creates graphic elements'''
        self.btn_next = QPushButton(txt_next,self)
        self.hello_text = QLabel(txt_hello)
        self.layout_line.addwidget(self.btn_next,alignment - Qt.AlignCenter)
        self.setLayout(self.layout_line)
    def next_click(self):
        self.tw = testWin()
        self.hide()
    

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    def set_appeat(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)

