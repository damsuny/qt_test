import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("mywindow.ui")[0]					# designer 를 사용하여 만든 mywindow.ui 를 불러 옴

class MyWindow(QMainWindow, form_class):
	def __init__(self):
		super().__init__()
		self.setupUi(self)										# ui 를 셋업함
		self.pushButton.clicked.connect(self.btn_clicked)

	def btn_clicked(self):
		print("버튼 클릭")

app = QApplication(sys.argv)

window = MyWindow()
window.show()

app.exec_()