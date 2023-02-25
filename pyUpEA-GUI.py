from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
import sys
import os
from MainWindow import Ui_MainWindow
sys.path.append(os.path.relpath("./pyUpEA"))
import pyUpEA as pue


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.ui.label.setText("AAA")
    window.show()

    sys.exit(app.exec())
