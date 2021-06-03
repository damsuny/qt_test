import sys
from PyQt5.QtWidgets import *       # PyQt5.QtWidgets 는 GUI 프로그래밍을 위한 여러 클래스가 정의 되어 있습니다.

app = QApplication(sys.argv)        # app 객체를 생성합니다. 뒤에 이벤트 루프를 위해 만들어 줍니다.

label = QLabel("Hello")             # label 이라는 객체를 생성합니다. QLabel에 "Hello" 텍스트를 넘겨줍니다.
label.show()                        # 객체를 보여주기 위한 show() 를 사용합니다.

app.exec_()                         # 이벤트 루프를 위해 작성합니다. 위젯을 X버튼 누르기 전까지 반복하는 이벤트 루프입니다.