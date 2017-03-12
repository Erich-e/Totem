'''
Storage for a project
'''

from PyQt4 import QtGui

class ProjectFrame(QtGui.QWidget):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.init_ui()

	def init_ui(self):
		self.layout = QtGui.QHBoxLayout()
		self.selection_layout = QtGui.QVBoxLayout()
		self.info_layout = QtGui.QVBoxLayout()

		self.selection_scroll = QtGui.QScrollArea()
		self.selection_layout.addWidget(self.selection_scroll)

		self.info_scroll = QtGui.QScrollArea()
		self.info_layout.addWidget(self.info_scroll)

		self.new_task_layout = QtGui.QGridLayout()
		self.new_task_layout.addWidget(QtGui.QLabel("TODO:"), 0, 0)
		self.title_edit = QtGui.QLineEdit()
		self.new_task_layout.addWidget(self.title_edit, 0, 1)

		self.task_submit_row = QtGui.QHBoxLayout()
		self.task_submit_button = QtGui.QPushButton("Add Task")
		self.task_submit_row.addWidget(self.task_submit_button)
		self.task_submit_row.addStretch(1)
		self.new_task_layout.addLayout(self.task_submit_row, 1, 1)

		self.info_layout.addLayout(self.new_task_layout)

		self.layout.addLayout(self.selection_layout)
		self.layout.addLayout(self.info_layout)
		self.setLayout(self.layout)	