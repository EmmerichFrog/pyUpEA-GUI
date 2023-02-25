from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
import sys
from MainWindow import Ui_MainWindow

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
