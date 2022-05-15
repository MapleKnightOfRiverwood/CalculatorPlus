import os

from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia, QtTest
import pyperclip  # For copy function
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from photoWidget import PhotoWidgetUI
from developerInfoWidget import DevInfoUI
from decimalFrame import DecimalFrameUI
from fileEncryptionWidget import Ui_fileEncryption


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.equalPressed = False
        self.decimalPlace = 6

        # Use QMediaPlayer to play sound
        self.url = QtCore.QUrl.fromLocalFile("D:\Python Projects\DesignerProject\sound.mp3")
        self.content = QtMultimedia.QMediaContent(self.url)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(self.content)

        # Declare the photoWidget here as it is not part of the main widget
        self.thePhotoWidget = QtWidgets.QWidget()
        self.photoWidgetUI = PhotoWidgetUI()
        self.photoWidgetUI.setupUi(self.thePhotoWidget, app)

        # Declare the fileEncryptionWidget here as it is not part of the main widget
        self.theFileEncryptionWidget = QtWidgets.QMainWindow()
        self.fileEncryptionUI = Ui_fileEncryption()
        self.fileEncryptionUI.setupUi(self.theFileEncryptionWidget)

        # Icon file
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap("D:\Python Projects\DesignerProject\iconC.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)

        self.settingPasscode = False
        self.firstPasscode = None
        self.secondPasscode = None
        self.isFirstPasscode = True
        self.thePasscode = None


    def setupUi(self):
        self.setObjectName("MainFrame")
        self.resize(581, 701)
        self.setMinimumSize(QtCore.QSize(581, 701))
        self.setMaximumSize(QtCore.QSize(581, 701))

        self.setWindowIcon(self.icon)

        self.MainWidget = QtWidgets.QWidget(self)
        self.MainWidget.setObjectName("MainWidget")

        self.label = QtWidgets.QLabel(self.MainWidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 541, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignCenter)

        self.pushButton = QtWidgets.QPushButton(self.MainWidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 220, 131, 101))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.MainWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 220, 131, 101))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.MainWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 220, 131, 101))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.MainWidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 330, 131, 101))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.MainWidget)
        self.pushButton_5.setGeometry(QtCore.QRect(150, 330, 131, 101))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.MainWidget)
        self.pushButton_6.setGeometry(QtCore.QRect(290, 330, 131, 101))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.MainWidget)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 440, 131, 101))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.MainWidget)
        self.pushButton_8.setGeometry(QtCore.QRect(150, 440, 131, 101))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.MainWidget)
        self.pushButton_9.setGeometry(QtCore.QRect(290, 440, 131, 101))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.MainWidget)
        self.pushButton_10.setGeometry(QtCore.QRect(440, 110, 131, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.MainWidget)
        self.pushButton_11.setGeometry(QtCore.QRect(440, 200, 131, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.MainWidget)
        self.pushButton_12.setGeometry(QtCore.QRect(440, 290, 131, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.MainWidget)
        self.pushButton_13.setGeometry(QtCore.QRect(440, 380, 131, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.MainWidget)
        self.pushButton_14.setGeometry(QtCore.QRect(440, 470, 131, 181))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.MainWidget)
        self.pushButton_15.setGeometry(QtCore.QRect(10, 550, 271, 101))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.MainWidget)
        self.pushButton_16.setGeometry(QtCore.QRect(290, 550, 131, 101))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_18 = QtWidgets.QPushButton(self.MainWidget)
        self.pushButton_18.setGeometry(QtCore.QRect(10, 110, 131, 101))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.MainWidget)
        self.pushButton_19.setGeometry(QtCore.QRect(150, 110, 131, 101))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.MainWidget)
        self.pushButton_20.setGeometry(QtCore.QRect(290, 110, 131, 101))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setObjectName("pushButton_20")

        self.setCentralWidget(self.MainWidget)

        # Menu bar & Status bar on the main window
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 581, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")

        self.actionCopy_Result = QtWidgets.QAction(self)
        self.actionCopy_Result.setObjectName("actionCopy_Result")
        self.actionSetDecimalPlace = QtWidgets.QAction(self)
        self.actionSetDecimalPlace.setObjectName("actionSetDecimalPlace")
        self.actionDeveloper_Info = QtWidgets.QAction(self)
        self.actionDeveloper_Info.setObjectName("actionDeveloper_Info")

        self.menuEdit.addAction(self.actionCopy_Result)
        self.menuEdit.addAction(self.actionSetDecimalPlace)
        self.menuAbout.addAction(self.actionDeveloper_Info)
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        #  The developer info widget as a component in the main widget
        self.theDevInfoWidget = QtWidgets.QWidget(self.MainWidget)
        self.devInfoUI = DevInfoUI()
        self.devInfoUI.setupUi(self.theDevInfoWidget)
        self.theDevInfoWidget.move(115, 98)
        self.theDevInfoWidget.hide()  # Hide at start

        #  The decimal frame as a component in the main widget
        self.theDecimalFrame = QtWidgets.QFrame(self.MainWidget)
        self.decimalFrameUI = DecimalFrameUI()
        self.decimalFrameUI.setupUi(self.theDecimalFrame)
        self.theDecimalFrame.move(95, 140)
        self.theDecimalFrame.hide()


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.pushButton_7.clicked.connect(lambda: self.numButtonClicked(self.pushButton_7.text()))
        self.pushButton_7.clicked.connect(self.resizeDisplay)
        self.pushButton_8.clicked.connect(lambda: self.numButtonClicked(self.pushButton_8.text()))
        self.pushButton_8.clicked.connect(self.resizeDisplay)
        self.pushButton_9.clicked.connect(lambda: self.numButtonClicked(self.pushButton_9.text()))
        self.pushButton_9.clicked.connect(self.resizeDisplay)
        self.pushButton_4.clicked.connect(lambda: self.numButtonClicked(self.pushButton_4.text()))
        self.pushButton_4.clicked.connect(self.resizeDisplay)
        self.pushButton_5.clicked.connect(lambda: self.numButtonClicked(self.pushButton_5.text()))
        self.pushButton_5.clicked.connect(self.resizeDisplay)
        self.pushButton_6.clicked.connect(lambda: self.numButtonClicked(self.pushButton_6.text()))
        self.pushButton_6.clicked.connect(self.resizeDisplay)
        self.pushButton.clicked.connect(lambda: self.numButtonClicked(self.pushButton.text()))
        self.pushButton.clicked.connect(self.resizeDisplay)
        self.pushButton_2.clicked.connect(lambda: self.numButtonClicked(self.pushButton_2.text()))
        self.pushButton_2.clicked.connect(self.resizeDisplay)
        self.pushButton_3.clicked.connect(lambda: self.numButtonClicked(self.pushButton_3.text()))
        self.pushButton_3.clicked.connect(self.resizeDisplay)
        self.pushButton_15.clicked.connect(lambda: self.numButtonClicked(self.pushButton_15.text()))
        self.pushButton_15.clicked.connect(self.resizeDisplay)
        self.pushButton_16.clicked.connect(lambda: self.numButtonClicked(self.pushButton_16.text()))
        self.pushButton_16.clicked.connect(self.resizeDisplay)
        self.pushButton_19.clicked.connect(lambda: self.numButtonClicked(self.pushButton_19.text()))
        self.pushButton_19.clicked.connect(self.resizeDisplay)
        self.pushButton_20.clicked.connect(lambda: self.numButtonClicked(self.pushButton_20.text()))
        self.pushButton_20.clicked.connect(self.resizeDisplay)
        self.pushButton_18.clicked.connect(self.ACButtonClicked)
        self.pushButton_10.clicked.connect(self.plusButtonClicked)
        self.pushButton_11.clicked.connect(self.minusButtonClicked)
        self.pushButton_12.clicked.connect(self.mulButtonClicked)
        self.pushButton_13.clicked.connect(self.divButtonClicked)
        self.pushButton_14.clicked.connect(self.equalButtonClicked)

        self.actionCopy_Result.triggered.connect(lambda: self.copyTextToClipboard(self.label.text()))
        self.actionDeveloper_Info.triggered.connect(lambda: self.theDevInfoWidget.show())
        self.actionSetDecimalPlace.triggered.connect(lambda: self.theDecimalFrame.show())
        self.devInfoUI.pushButton.clicked.connect(lambda: self.theDevInfoWidget.hide())
        self.photoWidgetUI.closeTheImage.clicked.connect(lambda: self.thePhotoWidget.hide())
        self.photoWidgetUI.closeTheImage.clicked.connect(lambda: self.player.stop())
        self.decimalFrameUI.pushButton.clicked.connect(lambda: self.setDecimalPlace(self.getEnteredInt()))
        self.fileEncryptionUI.actionChange_Passcode.triggered.connect(lambda: self.resetPasscode())

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainFrame", "Calculator+"))

        # Everything on the main widget
        self.pushButton.setText(_translate("MainFrame", "7"))
        self.pushButton.setShortcut(_translate("MainFrame", "7"))
        self.pushButton_2.setText(_translate("MainFrame", "8"))
        self.pushButton_2.setShortcut(_translate("MainFrame", "8"))
        self.pushButton_3.setText(_translate("MainFrame", "9"))
        self.pushButton_3.setShortcut(_translate("MainFrame", "9"))
        self.pushButton_4.setText(_translate("MainFrame", "4"))
        self.pushButton_4.setShortcut(_translate("MainFrame", "4"))
        self.pushButton_5.setText(_translate("MainFrame", "5"))
        self.pushButton_5.setShortcut(_translate("MainFrame", "5"))
        self.pushButton_6.setText(_translate("MainFrame", "6"))
        self.pushButton_6.setShortcut(_translate("MainFrame", "6"))
        self.pushButton_7.setText(_translate("MainFrame", "1"))
        self.pushButton_7.setShortcut(_translate("MainFrame", "1"))
        self.pushButton_8.setText(_translate("MainFrame", "2"))
        self.pushButton_8.setShortcut(_translate("MainFrame", "2"))
        self.pushButton_9.setText(_translate("MainFrame", "3"))
        self.pushButton_9.setShortcut(_translate("MainFrame", "3"))
        self.pushButton_10.setText(_translate("MainFrame", "+"))
        self.pushButton_10.setShortcut(_translate("MainFrame", "Shift+="))
        self.pushButton_11.setText(_translate("MainFrame", "−"))
        self.pushButton_11.setShortcut(_translate("MainFrame", "-"))
        self.pushButton_12.setText(_translate("MainFrame", "×"))
        self.pushButton_12.setShortcut(_translate("MainFrame", "Shift+8"))
        self.pushButton_13.setText(_translate("MainFrame", "÷"))
        self.pushButton_13.setShortcut(_translate("MainFrame", "/"))
        self.pushButton_14.setText(_translate("MainFrame", "="))
        self.pushButton_14.setShortcut(_translate("MainFrame", "Return"))
        self.pushButton_15.setText(_translate("MainFrame", "0"))
        self.pushButton_15.setShortcut(_translate("MainFrame", "0"))
        self.pushButton_16.setText(_translate("MainFrame", "."))
        self.pushButton_16.setShortcut(_translate("MainFrame", "."))

        if not os.path.exists(appdataSavefilePath):
            self.settingPasscode = True
            font = QtGui.QFont()
            font.setPointSize(17)
            self.label.setFont(font)
            self.label.setText(_translate("MainFrame", "Please enter your passcode and press \"=\""))
        else:
            saveFile = open(appdataSavefilePath, "r")  # Read the passcode
            tempPasscode = saveFile.read(self.firstPasscode)
            saveFile.close()
            self.thePasscode = tempPasscode
            print("The passcode is: " + self.thePasscode)
            self.label.setText(_translate("MainFrame", "0"))

        self.pushButton_18.setText(_translate("MainFrame", "AC"))
        self.pushButton_19.setText(_translate("MainFrame", "("))
        self.pushButton_20.setText(_translate("MainFrame", ")"))
        self.menuEdit.setTitle(_translate("MainFrame", "Edit"))
        self.menuAbout.setTitle(_translate("MainFrame", "About"))

        # Everything on the main window
        self.actionCopy_Result.setText(_translate("MainFrame", "Copy Result"))
        self.actionCopy_Result.setStatusTip(_translate("MainFrame", "Copy the result"))
        self.actionCopy_Result.setShortcut(_translate("MainFrame", "Ctrl+C"))
        self.actionSetDecimalPlace.setText(_translate("MainFrame", "Set decimal place"))
        self.actionSetDecimalPlace.setStatusTip(_translate("MainFrame", "Choose how many decimal place to keep"))
        self.actionDeveloper_Info.setText(_translate("MainFrame", "Developer Info"))
        self.actionDeveloper_Info.setStatusTip(_translate("MainFrame", "Show developer information"))

    def resetPasscode(self):
        self.theFileEncryptionWidget.hide()
        os.remove(appdataSavefilePath)
        self.settingPasscode = True
        self.firstPasscode = None
        self.secondPasscode = None
        self.isFirstPasscode = True
        self.thePasscode = None
        self.retranslateUi()

    def resizeDisplay(self):
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)

    def numButtonClicked(self, text):
        if not self.equalPressed:
            oldText = self.label.text()
            if oldText == "0":
                if text == ".":
                    newText = oldText + text
                    self.label.setText(newText)
                else:
                    self.label.setText(text)
            elif oldText == "Please enter your passcode and press \"=\"":
                self.label.setText(text)
            elif oldText == "Please enter your passcode again and press \"=\"":
                self.label.setText(text)
            else:
                newText = oldText + text
                self.label.setText(newText)
        else:
            if text == ".":
                if self.label.text() == "Please enter your passcode again and press \"=\"" or self.label.text() == "Passcode doesn't match, please re-enter first passcode":
                    self.label.setText(text)
                    self.equalPressed = False
                else:
                    self.label.setText("0" + text)
                    self.equalPressed = False
            else:
                self.label.setText(text)
                self.equalPressed = False

    def ACButtonClicked(self):
        self.resizeDisplay()
        self.label.setText("0")
        self.equalPressed = False

    def plusButtonClicked(self):
        self.resizeDisplay()
        if self.label.text() == "Please enter your passcode and press \"=\"" or self.label.text() == "Please enter your passcode again and press \"=\""\
                or self.label.text() == "Passcode doesn't match, please re-enter first passcode":
            self.label.setText("+")
        else:
            oldText = self.label.text()
            newText = oldText + "+"
            self.label.setText(newText)
            self.equalPressed = False

    def minusButtonClicked(self):
        self.resizeDisplay()
        if self.label.text() == "Please enter your passcode and press \"=\"" or self.label.text() == "Please enter your passcode again and press \"=\""\
                or self.label.text() == "Passcode doesn't match, please re-enter first passcode":
            self.label.setText("-")
        else:
            oldText = self.label.text()
            newText = oldText + "-"
            self.label.setText(newText)
            self.equalPressed = False

    def mulButtonClicked(self):
        self.resizeDisplay()
        if self.label.text() == "Please enter your passcode and press \"=\"" or self.label.text() == "Please enter your passcode again and press \"=\""\
                or self.label.text() == "Passcode doesn't match, please re-enter first passcode":
            self.label.setText("×")
        else:
            oldText = self.label.text()
            newText = oldText + "×"
            self.label.setText(newText)
            self.equalPressed = False

    def divButtonClicked(self):
        self.resizeDisplay()
        if self.label.text() == "Please enter your passcode and press \"=\"" or self.label.text() == "Please enter your passcode again and press \"=\""\
                or self.label.text() == "Passcode doesn't match, please re-enter first passcode":
            self.label.setText("÷")
        else:
            oldText = self.label.text()
            newText = oldText + "÷"
            self.label.setText(newText)
            self.equalPressed = False

    def equalButtonClicked(self):
        self.resizeDisplay()
        print("Decimal Place: " + str(self.decimalPlace))
        self.equalPressed = True
        oldText = self.label.text()
        mulReplaced = oldText.replace("×", "*")
        divReplaced = mulReplaced.replace("÷", "/")
        result = "Error"
        try:
            result = eval(divReplaced)
        except:
            pass
        if self.settingPasscode == True:
            if self.isFirstPasscode == True:
                self.firstPasscode = self.label.text()
                self.isFirstPasscode = False
                print("First passcode is: " + self.firstPasscode)
                font = QtGui.QFont()
                font.setPointSize(15)
                self.label.setFont(font)
                self.label.setText("Please enter your passcode again and press \"=\"")
            else:
                self.secondPasscode = self.label.text()
                print("Second passcode is: " + self.secondPasscode)
                if self.firstPasscode == self.secondPasscode:
                    saveFile = open(appdataSavefilePath, "w")  # Write the passcode to file
                    saveFile.write(self.firstPasscode)
                    saveFile.close()
                    self.thePasscode = self.firstPasscode
                    font = QtGui.QFont()
                    font.setPointSize(26)
                    self.label.setFont(font)
                    self.label.setText("Passcode set successfully")
                    self.settingPasscode = False
                    self.showMessage()
                else:
                    font = QtGui.QFont()
                    font.setPointSize(13)
                    self.label.setFont(font)
                    self.label.setText("Passcode doesn't match, please re-enter first passcode")
                    self.isFirstPasscode = True
        elif result == "Error":
            self.label.setText("Error")
        elif result == int(self.thePasscode):
            print("Passcode entered!")
            self.theFileEncryptionWidget.show()
        elif result == 5555:
            self.label.setText("Try secret code 191")
        elif result == 191:
            self.label.setText("Now enter 2012")
        elif result == 2012:
            self.player.play()
            QtTest.QTest.qWait(200)  # Wait for 200 milliseconds to coordinate picture with sound
            self.thePhotoWidget.showFullScreen()
            self.label.setText("LOL")
        else:
            self.label.setText(str(round(result, self.decimalPlace)))

    def showMessage(self):
        message = QMessageBox()
        message.setWindowTitle("Passcode set successful!")
        message.setText("Instruction:\n\n"
                        "Enter your passcode at anytime and press \"=\" to enter the secret file vault.\n\n"
                        "The passcode can be changed inside the file vault:\n"
                        "Menu -> Change Passcode")
        message.setWindowIcon(self.icon)
        message.exec_()

    def copyTextToClipboard(self, text):
        pyperclip.copy(text)
        print("The text copied is: ", text)

    def setDecimalPlace(self, dp):
        self.decimalPlace = dp
        self.theDecimalFrame.hide()

    def getEnteredInt(self):
        returnInt = self.decimalPlace
        try:
            returnInt = int(self.decimalFrameUI.lineEdit.text())
        except:
            pass
        return returnInt


if __name__ == "__main__":
    import sys

    userHome = os.path.expanduser("~")
    appdataPath = userHome + "\AppData\Local\CalculatorPlus"
    appdataFilesPath = userHome + "\AppData\Local\CalculatorPlus\TheFiles"
    appdataSavefilePath = appdataPath + "\Save"
    if not os.path.exists(appdataPath):
        os.makedirs(appdataPath)
    if not os.path.exists(appdataFilesPath):
        os.makedirs(appdataFilesPath)


    app = QtWidgets.QApplication(sys.argv)
    ui = MyWindow()
    ui.setupUi()
    ui.show()

    sys.exit(app.exec_())
