'''
UI component for task managment
'''

import sys
from PyQt4 import QtGui, QtCore
from taskframe import TaskFrame
from projectframe import ProjectFrame

class MainWindow(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.init_apps()
		self.init_ui()

	def init_apps(self):
		self.task_frame = TaskFrame()
		self.project_frame = ProjectFrame()

	def init_ui(self):
		self.resize(1000, 500)
		with open("./QTDark.stylesheet") as f:
			self.setStyleSheet(f.read())
		self.layout = QtGui.QVBoxLayout()

		self.main_frame = QtGui.QTabWidget()
		self.main_frame.addTab(self.task_frame, "Tasks")
		self.main_frame.addTab(self.project_frame, "Projects")
		self.layout.addWidget(self.main_frame)

		cwidget = QtGui.QWidget()
		cwidget.setLayout(self.layout)
		self.setCentralWidget(cwidget)

	def clean_up(self):
		self.task_frame.save_tasks()


if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	window = MainWindow()
	window.show()
	app.lastWindowClosed.connect(window.clean_up)
	app.exec_()
	sys.exit()