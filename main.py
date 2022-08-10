import sys
from PySide6 import QtWidgets
from interface import Interface

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    interface_game = Interface()
    interface_game.show()
    sys.exit(app.exec())