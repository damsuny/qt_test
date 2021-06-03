import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setGeometry(100,200,300,200)
		self.setWindowTitle("PyQt5")
		self.setWindowIcon(QIcon("icon.png"))

		btn = QPushButton("버튼", self)			# 버튼 생성
		btn.move(10,10)							# 버튼 위치
		btn.clicked.connect(self.btn_clicked)	# 버튼 클릭 이벤트 연결

	def btn_clicked(self):
		print("버튼 클릭")						# 버튼 클릭 이벤트

app = QApplication(sys.argv)

window = MyWindow()
window.show()

app.exec_()