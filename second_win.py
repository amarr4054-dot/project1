# write a code for the second screen of appfrom PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from instr import *
from final_win import *
class TestWin(Widget):
    def __Init__(self):
        super()._Init__()
        self.initUI()
        self.connects() #tambahkan
        self.set_appear()
        self.show()
    def next_click(self): #tambahkan
        self.tw = TestWin()
        self.hide()
    def connects(self): #tambahkan
        self.btn_next.clicked.connect(self.next_click)
    def set_appear(self): #tambahkan
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self): #tambahkan
        self.btn_next = QPushButton(txt_sendresult, self)
        self.btn_test1 = QPushButton(txt_starttest1, self)
        self.btn_test2 = QPushButton(txt_starttest2, self)
        self.btn_test3 = QPushButton(txt_starttest3, self)
        self.text_name = QLabel(txt_name)
        self.text_age = QLabel(txt_age)
        self.text_test = QLabel(txt_test1)
        self.text_test = QLabel(txt_test2)
        self.text_test = QLabel(txt_test2)
        self.text_timer = QLabel(txt_timer)
        self.line_name = QLineEdit(txt_hintname)
        self.line_age = QLineEdit(txt_hintage)
        self.line_test1 = QLineEdit(txt_hinttest1)
        self.line_test2 = QLineEdit(txt_hinttest2)
        self.line_test3 = QLineEdit(txt_hinttest3)
