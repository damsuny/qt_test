import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)            # app 객체를 생성합니다.

btn = QPushButton("Hello")              # btn 객체를 생성합니다. Hello 버튼을 생성합니다.
btn.show()                              # btn을 보여줍니다.

app.exec_()                             # 이벤트 루프입니다.