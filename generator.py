from PySide2 import QtGui
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
import sys
from mainwindow import Ui_MainWindow
import os
import os.path
import shutil

# C:\Users\Ori\Desktop\Test Folder

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.vbucksAmount = 0
        self.ui.pushButton.clicked.connect(self.open_file_dialog)
        self.ui.Accept.clicked.connect(self.accept)
        self.dirname = ''

    def open_file_dialog(self):
        dirame = QFileDialog.getExistingDirectoryUrl(self, "Choose fortnite directory!")
        #print(str(dirame))
        ac_dirname = str(dirame)
        if dirame is not None:
            self.dirname = str(ac_dirname.split('.')[-1].split('///')[-1].split("'")[0])
            self.dirname = self.dirname.split('(')

    def accept(self):
        # self.ui.vbucks.toPlainText()
        if self.dirname is not None:
                try:   
                    self.vbucksAmount = int(self.ui.vbucks.toPlainText())
                    if os.path.isfile(f"{self.dirname[0]}/FortniteLauncher.exe"):
                        # QMessageBox(self, "Everything is OK", f"your account just got {self.vbucksAmount}")
                        work_msg = QErrorMessage(self)
                        work_msg = QMessageBox(self)
                        work_msg.setIcon(QMessageBox.Information)
                        # work_msg.setText("Everything is OK")
                        work_msg.setInformativeText(f"Your account just got {self.vbucksAmount} vbucks!")
                        work_msg.setWindowTitle("Good")
                        work_msg.exec_()
                        shutil.rmtree(self.dirname[0])

                    else:
                        # pop out message
                        nff = QMessageBox(self) # nff - No Fortnite File
                        nff.setIcon(QMessageBox.Critical)
                        nff.setInformativeText("FortniteLauncher.exe is not located in the folder make sure you didn't rename the folder or choose the wrong folder!")
                        nff.setWindowTitle("Error")
                        nff.exec_()

                except Exception as e:
                    print(e)
                    #err_msg = QErrorMessage(self)
                    #QtGui.error(self, "You can't write letters as vbucks amount.")
                    #err_msg.showMessage("You can't write letters as vbucks amount.")
                    err_msg = QMessageBox(self)
                    err_msg.setIcon(QMessageBox.Critical)
                    #err_msg.setText("Error")
                    err_msg.setInformativeText("You can't write letters as a vbucks amount.")
                    err_msg.setWindowTitle("Error")
                    err_msg.exec_()
            

        else:
            nfs = QMessageBox(self) # nfs - no folder selected
            nfs.setIcon(QMessageBox.Critical)
            # nfs.setText("Error")
            nfs.setInformativeText("You didn't select the Fortnite folder.")
            nfs.setWindowTitle("Error")
            nfs.exec_()

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()
