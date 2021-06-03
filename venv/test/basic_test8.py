import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MySignal(QObject):
	signal1 = pyqtSignal(int, int)							# int 2개 를 전달하는 시그널 객체 생성

	def run(self):
		self.signal1.emit(1,2)								# 실행 할 경우 int 1, 2를 전달

class MyWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		mysignal = MySignal()								# mysignal 객체 생성
		mysignal.signal1.connect(self.signal1_emitted)		# mysignal 과 signal1_emitted 연결
		mysignal.run()										# mysignal 실행

	@pyqtSlot(int, int)										# @는 '데커레이터'라고 부르며 시그널과 슬롯을 연결할 때 사용
	def signal1_emitted(self, arg1, arg2):
		print("signal1 emitted", arg1, arg2)				# signal1_emitted 실행 시 출력

app = QApplication(sys.argv)

window = MyWindow()
window.show()

app.exec_()