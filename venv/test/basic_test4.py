import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *                   # 아이콘 변경 기능이 있는 setWindowIcon()을 위한 import

class Mywindow(QMainWindow):                # 클래스 생성합니다.
    def __init__(self):                     # 초기속성을 위한 메서드를 생성합니다.
	    super().__init__()                  # super를 이용하여 초기 값을 부모 클래스에 있는 값을 사용합니다. self.__init__()은 자식 클래스 값을 사용합니다.
	    self.setGeometry(100,200,300,400)   # 숫자는 window 좌상측 기준으로 x축 좌표, y축 좌표, window 너비, window 높이
	    self.setWindowTitle("PyQt5")        # window의 타이틀 변경
	    self.setWindowIcon(QIcon("icon.png"))   # window의 아이콘 변경(타이틀 옆에 있는 작은 아이콘 16x16 size)

app = QApplication(sys.argv)

window = Mywindow()
window.show()

app.exec_()