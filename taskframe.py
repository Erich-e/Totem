'''
Task managing main portion
'''

import datetime
from PyQt4 import QtCore
from PyQt4 import QtGui
from tasks import TaskList, t_read, t_write
from taskcontroller import TaskController

class TaskFrame(QtGui.QWidget):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.load_tasks()
		self.taskController = TaskController(self.tasks)
		self.init_ui()

	def init_ui(self):
		self.layout = QtGui.QHBoxLayout()
		self.task_display = None
		self.menu_display = QtGui.QVBoxLayout()

		self.display_tasks()

		self.menu_layout = QtGui.QGridLayout()
		self.menu_layout.addWidget(QtGui.QLabel("Task: "), 0, 0)
		self.title_edit = QtGui.QLineEdit()
		self.menu_layout.addWidget(self.title_edit, 0, 1)

		self.menu_layout.addWidget(QtGui.QLabel("Description: "), 1, 0)
		self.desc_edit = QtGui.QTextEdit()
		self.menu_layout.addWidget(self.desc_edit, 1, 1)

		self.menu_layout.addWidget(QtGui.QLabel("Due Date: "), 2, 0)
		self.date_edit = QtGui.QCalendarWidget()
		self.menu_layout.addWidget(self.date_edit, 2, 1)

		self.submit_button_layout = QtGui.QHBoxLayout()
		self.submit_button = QtGui.QPushButton("New Task")
		self.submit_button_layout.addWidget(self.submit_button)
		self.submit_button_layout.addStretch(1)
		self.undo_button = QtGui.QPushButton("Undo")
		self.submit_button_layout.addWidget(self.undo_button)
		self.menu_layout.addLayout(self.submit_button_layout, 3, 1)
		self.submit_button.clicked.connect(self.insert_task)

		self.menu_display.addLayout(self.menu_layout)
		self.menu_display.addStretch(1)

		self.layout.addLayout(self.menu_display)
		self.setLayout(self.layout)

	def display_tasks(self):

		def gen_rm_cmd(task):
			return lambda: self.remove_task(task)

		if self.tasks.size != 0:
			display_layout = QtGui.QVBoxLayout()
			for task in self.tasks:
				next_block = QtGui.QGroupBox()
				block_layout = QtGui.QVBoxLayout()

				title_row = QtGui.QHBoxLayout()
				title_row.addWidget(QtGui.QLabel(task.title))
				title_row.addStretch(1)
				remove_btn = QtGui.QPushButton('X')	
				title_row.addWidget(remove_btn)
				block_layout.addLayout(title_row)

				desc_row = QtGui.QHBoxLayout()
				desc_row.addWidget(QtGui.QLabel(task.description))
				desc_row.addStretch(1)
				desc_row.addWidget(QtGui.QLabel(task.date_str()))
				block_layout.addLayout(desc_row)

				next_block.setLayout(block_layout)
				display_layout.addWidget(next_block)

				remove_btn.clicked.connect(gen_rm_cmd(task))

			display_layout.addStretch(1)
			inner_wrapper = QtGui.QWidget()
			inner_wrapper.setLayout(display_layout)
		else:
			inner_wrapper = QtGui.QWidget()

		if self.task_display:
			self.layout.removeWidget(self.task_display)
			self.task_display.deleteLater()
		self.task_display = QtGui.QScrollArea()
		inner_wrapper.setMaximumWidth(self.task_display.width())
		self.task_display.setWidget(inner_wrapper)
		self.task_display.setWidgetResizable(True)
		self.layout.insertWidget(0, self.task_display)


	def load_tasks(self):
		try:
			self.tasks = t_read("save.json")
		except:
			self.tasks = TaskList()
			err = QtGui.QErrorMessage()	
			err.showMessage("Corrupted save file")
			err.exec_()

	def save_tasks(self):
		t_write("save.json", self.tasks)

	def insert_task(self):
		title = str(self.title_edit.text())
		if title:
			desc = str(self.desc_edit.toPlainText())
			qt_date = self.date_edit.selectedDate()
			due_date = datetime.datetime.strptime(str(qt_date.toString(QtCore.Qt.ISODate)), "%Y-%m-%d").date()
			self.taskController.insert_task(title=title, description=desc, due_date=due_date)
			self.display_tasks()
			self.title_edit.clear()
			self.desc_edit.clear()

	def remove_task(self, task=None, title="", description="", due_date=None):
		if(task):
			self.taskController.remove_task(task=task)
		else:
			self.taskController.remove_task(title=title, description=description, due_date=due_date)
		self.display_tasks()
