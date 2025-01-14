# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1457, 912)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addPixmap(QPixmap("image/web.png"), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QSize(24, 24))
        MainWindow.setToolButtonStyle(Qt.ToolButtonTextOnly)
        MainWindow.setAnimated(True)
        self.centralwidget = QWidget(MainWindow)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QFrame(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("QFrame {    \n"
"    background-color: rgb(0, 85, 127);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(4)
        self.frame.setObjectName("frame")
        self.cctv = QLabel(self.frame)
        self.cctv.setGeometry(QRect(20, 30, 441, 331))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cctv.sizePolicy().hasHeightForWidth())
        self.cctv.setSizePolicy(sizePolicy)
        self.cctv.setStyleSheet("QLabel{\n"
"    background-color: rgb(186, 162, 27);\n"
"    border-radius: 10px;\n"
"    \n"
"    border-color: rgb(255, 170, 0);\n"
"}")
        self.cctv.setFrameShape(QFrame.Box)
        self.cctv.setFrameShadow(QFrame.Raised)
        self.cctv.setLineWidth(2)
        self.cctv.setText("")
        self.cctv.setObjectName("cctv")
        self.handSign = QLabel(self.frame)
        self.handSign.setGeometry(QRect(20, 390, 700, 491))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.handSign.sizePolicy().hasHeightForWidth())
        self.handSign.setSizePolicy(sizePolicy)
        self.handSign.setFocusPolicy(Qt.StrongFocus)
        self.handSign.setStyleSheet("QLabel{\n"
"background-color: rgb(165, 104, 93);\n"
"border-radius: 10px;\n"
"}")
        self.handSign.setFrameShape(QFrame.Box)
        self.handSign.setFrameShadow(QFrame.Raised)
        self.handSign.setLineWidth(2)
        self.handSign.setText("")
        self.handSign.setObjectName("handSign")
        self.rccarCam = QLabel(self.frame)
        self.rccarCam.setGeometry(QRect(490, 30, 451, 331))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rccarCam.sizePolicy().hasHeightForWidth())
        self.rccarCam.setSizePolicy(sizePolicy)
        self.rccarCam.setStyleSheet("QLabel{\n"
"background-color: rgb(186, 162, 27);\n"
"border-radius: 10px;\n"
"}")
        self.rccarCam.setFrameShape(QFrame.Box)
        self.rccarCam.setFrameShadow(QFrame.Raised)
        self.rccarCam.setLineWidth(2)
        self.rccarCam.setText("")
        self.rccarCam.setObjectName("rccarCam")
        self.cap_img = QLabel(self.frame)
        self.cap_img.setGeometry(QRect(970, 30, 451, 331))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cap_img.sizePolicy().hasHeightForWidth())
        self.cap_img.setSizePolicy(sizePolicy)
        self.cap_img.setStyleSheet("QLabel{\n"
"background-color: rgb(186, 162, 27);\n"
"border-radius: 10px;\n"
"}")
        self.cap_img.setFrameShape(QFrame.Box)
        self.cap_img.setFrameShadow(QFrame.Raised)
        self.cap_img.setLineWidth(2)
        self.cap_img.setText("")
        self.cap_img.setObjectName("cap_img")
        self.sr_img = QLabel(self.frame)
        self.sr_img.setGeometry(QRect(750, 390, 451, 331))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sr_img.sizePolicy().hasHeightForWidth())
        self.sr_img.setSizePolicy(sizePolicy)
        self.sr_img.setStyleSheet("QLabel{\n"
"background-color: rgb(186, 162, 27);\n"
"border-radius: 10px;\n"
"}")
        self.sr_img.setFrameShape(QFrame.Box)
        self.sr_img.setFrameShadow(QFrame.Raised)
        self.sr_img.setLineWidth(2)
        self.sr_img.setText("")
        self.sr_img.setObjectName("sr_img")
        self.warning = QLabel(self.frame)
        self.warning.setGeometry(QRect(490, 160, 451, 51))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.warning.sizePolicy().hasHeightForWidth())
        self.warning.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.warning.setFont(font)
        self.warning.setStyleSheet("QLabel{\n"
"    background-color: rgba(170, 85, 127, 170);\n"
"    border-radius: 10px;\n"
"}")
        self.warning.setAlignment(Qt.AlignCenter)
        self.warning.setObjectName("warning")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setGeometry(QRect(1230, 500, 191, 221))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setStyleSheet("QPushButton{\n"
"font: 75 18pt \"Segoe UI\";\n"
"background-color: rgb(103, 149, 255);\n"
"border-radius: 10px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.cctv_name = QLabel(self.frame)
        self.cctv_name.setGeometry(QRect(30, 8, 200, 21))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cctv_name.sizePolicy().hasHeightForWidth())
        self.cctv_name.setSizePolicy(sizePolicy)
        self.cctv_name.setStyleSheet("QLabel{\n"
"    font: 16pt \"Segoe UI\";\n"
"    background-color: rgb(85, 170, 127);\n"
"}")
        self.cctv_name.setAlignment(Qt.AlignCenter)
        self.cctv_name.setObjectName("cctv_name")
        self.rccar_name = QLabel(self.frame)
        self.rccar_name.setGeometry(QRect(500, 8, 200, 21))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rccar_name.sizePolicy().hasHeightForWidth())
        self.rccar_name.setSizePolicy(sizePolicy)
        self.rccar_name.setStyleSheet("QLabel{\n"
"    font: 16pt \"Segoe UI\";\n"
"    background-color: rgb(85, 170, 127);\n"
"}")
        self.rccar_name.setAlignment(Qt.AlignCenter)
        self.rccar_name.setObjectName("rccar_name")
        self.cap_name = QLabel(self.frame)
        self.cap_name.setGeometry(QRect(980, 8, 200, 21))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cap_name.sizePolicy().hasHeightForWidth())
        self.cap_name.setSizePolicy(sizePolicy)
        self.cap_name.setStyleSheet("QLabel{\n"
"    font: 16pt \"Segoe UI\";\n"
"    background-color: rgb(85, 170, 127);\n"
"}")
        self.cap_name.setAlignment(Qt.AlignCenter)
        self.cap_name.setObjectName("cap_name")
        self.hs_name = QLabel(self.frame)
        self.hs_name.setGeometry(QRect(30, 368, 220, 21))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hs_name.sizePolicy().hasHeightForWidth())
        self.hs_name.setSizePolicy(sizePolicy)
        self.hs_name.setStyleSheet("QLabel{\n"
"    font: 16pt \"Segoe UI\";\n"
"    background-color: rgb(85, 170, 127);\n"
"}")
        self.hs_name.setAlignment(Qt.AlignCenter)
        self.hs_name.setObjectName("hs_name")
        self.sr_name = QLabel(self.frame)
        self.sr_name.setGeometry(QRect(760, 368, 200, 21))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sr_name.sizePolicy().hasHeightForWidth())
        self.sr_name.setSizePolicy(sizePolicy)
        self.sr_name.setStyleSheet("QLabel{\n"
"    font: 16pt \"Segoe UI\";\n"
"    background-color: rgb(85, 170, 127);\n"
"}")
        self.sr_name.setAlignment(Qt.AlignCenter)
        self.sr_name.setObjectName("sr_name")
        self.lcdNumber = QLCDNumber(self.frame)
        self.lcdNumber.setGeometry(QRect(1230, 390, 191, 91))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy)
        self.lcdNumber.setStyleSheet("QLCDNumber{\n"
"background-color: rgb(208, 139, 0);\n"
"border-radius: 10px;\n"
"}")
        self.lcdNumber.setObjectName("lcdNumber")
        self.case_name = QLabel(self.frame)
        self.case_name.setGeometry(QRect(1240, 368, 171, 21))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.case_name.sizePolicy().hasHeightForWidth())
        self.case_name.setSizePolicy(sizePolicy)
        self.case_name.setStyleSheet("QLabel{\n"
"    font: 16pt \"Segoe UI\";\n"
"    background-color: rgb(85, 170, 127);\n"
"}")
        self.case_name.setAlignment(Qt.AlignCenter)
        self.case_name.setObjectName("case_name")
        self.cmd = QLabel(self.frame)
        self.cmd.setGeometry(QRect(750, 740, 671, 141))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmd.sizePolicy().hasHeightForWidth())
        self.cmd.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.cmd.setFont(font)
        self.cmd.setStyleSheet("QLabel{\n"
"background-color: rgb(193, 193, 193);\n"
"border-radius: 10px;\n"
"}")
        self.cmd.setText("")
        self.cmd.setObjectName("cmd")
        self.wait = QLabel(self.frame)
        self.wait.setGeometry(QRect(750, 530, 451, 50))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wait.sizePolicy().hasHeightForWidth())
        self.wait.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.wait.setFont(font)
        self.wait.setStyleSheet("QLabel{\n"
"    background-color: rgba(100, 162, 27, 170);\n"
"    border-radius: 10px;\n"
"}")
        self.wait.setAlignment(Qt.AlignCenter)
        self.wait.setObjectName("wait")
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Handsign Project"))
        self.warning.setText(_translate("MainWindow", "Warning"))
        self.pushButton.setText(_translate("MainWindow", "CCTV\n"
"BUTTON"))
        self.cctv_name.setText(_translate("MainWindow", "RC-CAR CAM"))
        self.rccar_name.setText(_translate("MainWindow", "CCTV"))
        self.cap_name.setText(_translate("MainWindow", "CAPTURE IMAGE"))
        self.hs_name.setText(_translate("MainWindow", "HAND SIGN"))
        self.sr_name.setText(_translate("MainWindow", "SR IMAGE"))
        self.case_name.setText(_translate("MainWindow", "CASE SOLVED"))
        self.wait.setText(_translate("MainWindow", "Wait..."))


# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     MainWindow = QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())