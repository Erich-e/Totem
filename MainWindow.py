import sys
from PyQt4 import QtGui


class mainWindow(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.init_ui()

	def init_ui(self):

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	window = mainWindow()
	window.show()
	app.exec_()
	sys.exit()