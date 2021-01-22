import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from schenky import Ui_Schenky

app = QtWidgets.QApplication(sys.argv)
Schenky = QtWidgets.QMainWindow()
ui = Ui_Schenky()
ui.setupUi(Schenky)
Schenky.show()
sys.exit(app.exec_())
