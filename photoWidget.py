from PyQt5 import QtCore, QtGui, QtWidgets


class PhotoWidgetUI(object):
    def setupUi(self, Form, app):

        # Get user screen size
        screen = app.primaryScreen()
        size = screen.size()
        width = size.width()
        height = size.height()
        print("Monitor width is: " + str(width) + " Monitor height is:" + str(height))

        Form.setObjectName("Form")
        Form.resize(1296, 730)

        self.picOfAlien = QtWidgets.QLabel(Form)
        self.picOfAlien.setGeometry(QtCore.QRect(0, 0, width, height))
        self.picOfAlien.setText("")
        self.picOfAlien.setPixmap(QtGui.QPixmap("D:\Python Projects\DesignerProject\Alien.jpg"))
        self.picOfAlien.setObjectName("picOfAlien")
        self.picOfAlien.setScaledContents(True)  # Make the picture scale with label

        self.closeTheImage = QtWidgets.QPushButton(Form)
        self.closeTheImage.setGeometry(QtCore.QRect(0, 0, width, height))
        self.closeTheImage.setStyleSheet("border : 0;\n""background: transparent;")  # Make button transparent
        self.closeTheImage.setText("")
        self.closeTheImage.setObjectName("closeTheImage")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = PhotoWidgetUI()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
