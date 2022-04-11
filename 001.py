import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QToolTip
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import QCoreApplication
import random

class 대표선출프로그램(QWidget):
    def __init__(self):
        super().__init__()
        self.UI초기화()
        
    
    def UI초기화(self):
        self.이미지()
        self.버튼()
        self.툴팁()
        self.대리인번호()
        
        self.setWindowTitle('대표를 선출하라!')
        self.setWindowIcon(QIcon('img/weniv-licat.png'))
        self.setGeometry(500, 500, 400, 400)  # (x, y, width, height)
        self.show()
    
    def 이미지(self):
        self.대표이미지 = QLabel(self)
        self.대표이미지.setPixmap(QPixmap('img/weniv-licat.png').scaled(35, 44))
        self.대표이미지.move()
    
    def 버튼(self):
        pass
    
    def 툴팁(self):
        pass
    
    def 대리인번호(self):
        pass
    
프로그램무한반복 = QApplication(sys.argv)  # 계속해서 evnent를 감시
실행인스턴스 = 대표선출프로그램()
프로그램무한반복.exec_()  # 이 코드가 없으면 프로그램을 한 번 실행하게 됨. 실제로 무한반복 하도록 하는 코드
