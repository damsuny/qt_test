import sys
from PyQt5.QtWidgets import *

class Mywindow(QMainWindow):            # 클래스 생성합니다.
    def __init__(self):                 # 초기속성을 위한 메서드를 생성합니다.
        super().__init__()              # super를 이용하여 초기 값을 부모 클래스에 있는 값을 사용합니다. self.__init__()은 자식 클래스 값을 사용합니다.

app = QApplication(sys.argv)

window = Mywindow()
window.show()

app.exec_()