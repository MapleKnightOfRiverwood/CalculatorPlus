from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QPushButton
from PyQt5.QtCore import Qt, QUrl
import sys, os
import shutil  # For copy function
from fileDropboxWidget import DropBoxWidget


class Ui_fileEncryption(object):
    def __init__(self):
        self.theDropBox = None
        self.model = None

    def setupUi(self, fileEncryption):
        fileEncryption.setObjectName("fileEncryption")
        fileEncryption.resize(951, 631)
        fileEncryption.setMinimumSize(QtCore.QSize(951, 631))
        fileEncryption.setMaximumSize(QtCore.QSize(951, 631))


        self.theDropBox = DropBoxWidget(fileEncryption)
        self.theDropBox.move(630, 10)
        self.theDropBox.show()


        self.instructionText = QtWidgets.QLabel(fileEncryption)
        self.instructionText.setGeometry(QtCore.QRect(640, 350, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.instructionText.setFont(font)
        self.instructionText.setObjectName("instructionText")
        self.instructionText1 = QtWidgets.QLabel(fileEncryption)
        self.instructionText1.setGeometry(QtCore.QRect(640, 410, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.instructionText1.setFont(font)
        self.instructionText1.setScaledContents(False)
        self.instructionText1.setWordWrap(True)
        self.instructionText1.setObjectName("instructionText1")
        self.instructionText2 = QtWidgets.QLabel(fileEncryption)
        self.instructionText2.setGeometry(QtCore.QRect(640, 470, 291, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.instructionText2.setFont(font)
        self.instructionText2.setWordWrap(True)
        self.instructionText2.setObjectName("instructionText2")
        self.instructionText3 = QtWidgets.QLabel(fileEncryption)
        self.instructionText3.setGeometry(QtCore.QRect(640, 520, 311, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.instructionText3.setFont(font)
        self.instructionText3.setWordWrap(True)
        self.instructionText3.setObjectName("instructionText3")

        self.treeView = QtWidgets.QTreeView(fileEncryption)
        self.treeView.setGeometry(QtCore.QRect(10, 10, 611, 611))
        self.treeView.setObjectName("treeView")

        self.retranslateUi(fileEncryption)
        QtCore.QMetaObject.connectSlotsByName(fileEncryption)

    def retranslateUi(self, fileEncryption):
        _translate = QtCore.QCoreApplication.translate
        fileEncryption.setWindowTitle(_translate("fileEncryption", "File Encryption"))
        self.instructionText.setText(_translate("fileEncryption", "Instructions:"))
        self.instructionText1.setText(_translate("fileEncryption", "Drop your file into the box above to encrypt"))
        self.instructionText2.setText(_translate("fileEncryption", "View your encrypted file on the left"))
        self.instructionText3.setText(_translate("fileEncryption", "Right click on your file and select \"Export\" to export it to desktop"))

        self.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)  # Enable custom menu
        self.treeView.customContextMenuRequested.connect(self.exportMenu)  # Add our custom menu to the tree view

        self.populateWindow()

    def populateWindow(self):
        userHome = os.path.expanduser("~")
        appdataFilesPath = userHome + "\AppData\Local\CaldulatorPlus\TheFiles"
        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath(QtCore.QDir.rootPath())
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.model.index(appdataFilesPath))
        self.treeView.setColumnWidth(0, 250)
        self.treeView.setAlternatingRowColors(True)
        self.treeView.setSortingEnabled(True)

    def exportMenu(self):
        menu = QtWidgets.QMenu()
        exportButton = menu.addAction("Export to desktop")
        exportButton.triggered.connect(self.exportFile)
        deleteButton = menu.addAction("Delete")
        deleteButton.triggered.connect(self.deleteFile)
        cursor = QtGui.QCursor()
        menu.exec_(cursor.pos())

    def exportFile(self):
        userHome = os.path.expanduser("~")
        desktopPath = userHome + "\Desktop"
        appdataPath = "D:\Python Projects\DesignerProject\Appdata"

        index = self.treeView.currentIndex()
        filePath = self.model.filePath(index)
        filePathFixed = filePath.replace('/', '\\')

        fileName = os.path.basename(filePath)
        desktopPathWithName = desktopPath + "\\" + fileName


        shutil.copyfile(filePath, desktopPathWithName)  # Copy the file to desktop

        print("Copied file is: " + filePathFixed)
        print("Created file is: " + desktopPathWithName)

    def deleteFile(self):
        index = self.treeView.currentIndex()
        filePath = self.model.filePath(index)
        filePathFixed = filePath.replace('/', '\\')

        os.remove(filePathFixed)

        print("Deleted file is: " + filePath)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fileEncryption = QtWidgets.QWidget()
    ui = Ui_fileEncryption()
    ui.setupUi(fileEncryption)
    fileEncryption.show()
    sys.exit(app.exec_())