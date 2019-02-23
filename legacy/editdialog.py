'''
Popup to edit tasks
'''

import datetime
from PyQt4 import QtGui, QtCore

class EditDialog(QtGui.QDialog):
	def __init__(self, parent=None, params={}, task_controller=None):
		QtGui.QWidget.__init__(self, parent)
		self.params = params
		self.task_controller = task_controller
		self.setModal(True)
		self.init_ui()

	def init_ui(self):
		self.layout = QtGui.QGridLayout()
		self.layout.addWidget(QtGui.QLabel("Task: "), 0, 0)
		self.title_edit = QtGui.QLineEdit(self.params.get('old_title'))
		self.layout.addWidget(self.title_edit, 0, 1)

		self.layout.addWidget(QtGui.QLabel("Description: "), 1, 0)
		self.desc_edit = QtGui.QTextEdit(self.params.get('old_desc'))
		self.layout.addWidget(self.desc_edit, 1, 1)

		self.layout.addWidget(QtGui.QLabel("Due Date: "), 2, 0)
		self.date_edit = QtGui.QCalendarWidget()
		self.date_edit.setSelectedDate(self.params.get("old_dd"))
		self.layout.addWidget(self.date_edit, 2, 1)

		self.submit_layout = QtGui.QHBoxLayout()
		self.submit_button = QtGui.QPushButton("Submit")
		self.submit_layout.addWidget(self.submit_button)
		self.submit_layout.addStretch(1)
		self.layout.addLayout(self.submit_layout, 3, 1)

		self.setLayout(self.layout)

		self.submit_button.clicked.connect(self.submit_edit)

	def submit_edit(self):
		title = str(self.title_edit.text())
		if title:
			desc = str(self.desc_edit.toPlainText())
			qt_date = self.date_edit.selectedDate()
			due_date = datetime.datetime.strptime(str(qt_date.toString(QtCore.Qt.ISODate)), "%Y-%m-%d").date()
			self.task_controller.edit_task(new_title=title, new_desc=desc, new_dd=due_date, **self.params)
		self.close()
