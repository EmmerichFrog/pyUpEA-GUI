from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile, QRunnable, Slot, QThreadPool
import sys
import os
import time
from MainWindow import Ui_MainWindow
sys.path.append(os.path.relpath("./pyUpEA"))
import pyUpEA as pue


apiUrl = "https://api.github.com/repos/pineappleEA/pineapple-src/releases/latest"

try:
    path = sys.argv[1]
except:
    path = os.getcwd()        
if path == "":
    path = os.getcwd()
print(path)

try:
    returned = pue.queryGithubLatestRelease(apiUrl)
except:
    label = "Can't connect"
    #time.sleep(3)
    sys.exit(0)

latestVersion = returned[0]
downloadUrl = returned[1]
check = pue.currentVersionCheck(latestVersion, path)

class downloadWorker(QRunnable):

    @Slot()  # QtCore.Slot
    def run(self):
        global path
        global downloadUrl
        global latestVersion
        global label1
        window.ui.OK.setDisabled(True)
        if check[0] == 0 or check[0] == 1:
            label1 = "Downloading..."
            window.ui.label.setText("Downloading...")
            window.ui.progressBar.setVisible(True)
            #time.sleep(1)
            pue.getGithubLatestRelease(downloadUrl, path, latestVersion)
            label1 = "Done."
            window.ui.label.setText(label1)
            time.sleep(1)
            os._exit(0)
        else:
            time.sleep(1)   
            os._exit(0)

class progressWorker(QRunnable):

    @Slot()  # QtCore.Slot
    def run(self):
        window.ui.progressBar.setMaximum(0)
        window.ui.progressBar.setMinimum(0)
        window.ui.progressBar.setValue(0)

class MainWindow(QMainWindow):


    def __init__(self):
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.OK.clicked.connect(self.okPressedThread)
        self.ui.Cancel.clicked.connect(self.cancelPressedThread)

    def okPressedThread(self):
        
        downloadWorker1 = downloadWorker()
        progressWorker1 = progressWorker()
        self.threadpool.start(downloadWorker1)
        self.threadpool.start(progressWorker1)

    def cancelPressedThread(self):
        sys.exit(0)


if __name__ == "__main__":


    app = QApplication([])

    window = MainWindow()
    
    window.ui.progressBar.setVisible(False)
    window.show()
    #window.ui.label.setText("Checking...")
    
    if check[0] == 0:
        label1 = "No version found. Download: " + latestVersion + "?"
    elif check[0] == 1:
        label1 = "Latest version:\t" + latestVersion + "\nCurrent version:\tEA-" + check[1] + "\nUpdate?"
    else:
        label1 = "Up to date"


    window.setWindowTitle("pyUpEA")
    window.ui.label.setText(label1)

    app.exec()


