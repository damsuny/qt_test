import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import pykorbit

form_class = uic.loadUiType("window.ui")[0]

class MyWindow(QMainWindow, form_class):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

		self.timer = QTimer(self)						# 화면 객체 생성
		self.timer.start(1000)							# 타임인터벌 1초마다 실행
		self.timer.timeout.connect(self.inquiry)		# inquiry 를 연결

	def inquiry(self):
		cur_time = QTime.currentTime()					# 현재 시간 객체 생성
		str_time = cur_time.toString("hh:mm:ss")		# 시간을 문자형(str)으로 변경
		self.statusBar().showMessage(str_time)			# 시간 보여줌
		price = pykorbit.get_current_price("BTC")		# 가격 불러옴
		self.lineEdit.setText(str(price))				# 가격을 lineedit에 표시

app = QApplication(sys.argv)

window = MyWindow()
window.show()

app.exec_()