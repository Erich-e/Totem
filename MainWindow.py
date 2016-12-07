'''
UI component for task managment
'''
import sys
from PyQt4 import QtGui
from tasks import task_list


class mainWindow(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.tasks = task_list()
		self.init_ui()

	def init_ui(self):
		self.resize(1000, 500)
		with open("./QTDark.stylesheet") as f:
			self.setStyleSheet(f.read())
		self.layout = QtGui.QHBoxLayout()
		self.task_display = QtGui.QAbstractScrollArea()
		self.menu_display = QtGui.QVBoxLayout()

		self.task_layout = QtGui.QGridLayout()
		self.task_layout.addWidget(QtGui.QLabel("Task: "), 0, 0)
		self.title_edit = QtGui.QLineEdit()
		self.task_layout.addWidget(self.title_edit, 0, 1)

		self.task_layout.addWidget(QtGui.QLabel("Description: "), 1, 0)
		self.desc_edit = QtGui.QTextEdit()
		self.task_layout.addWidget(self.desc_edit, 1, 1)

		self.task_layout.addWidget(QtGui.QLabel("Due Date: "), 2, 0)
		self.date_edit = QtGui.QCalendarWidget()
		self.task_layout.addWidget(self.date_edit, 2, 1)

		self.submit_button_layout = QtGui.QHBoxLayout()
		self.task_button = QtGui.QPushButton("New Task")
		self.submit_button_layout.addWidget(self.task_button)
		self.submit_button_layout.addStretch(1)
		self.task_layout.addLayout(self.submit_button_layout, 3, 1)

		self.menu_display.addLayout(self.task_layout)
		self.menu_display.addStretch(1)

		self.layout.addWidget(self.task_display)
		self.layout.addLayout(self.menu_display)

		cwidget = QtGui.QWidget()
		cwidget.setLayout(self.layout)
		self.setCentralWidget(cwidget)

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	window = mainWindow()
	window.show()
	app.exec_()
	sys.exit()