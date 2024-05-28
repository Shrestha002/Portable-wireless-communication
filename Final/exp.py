# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PortabletgqnFn.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSplitter, QTextEdit, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1153, 554)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 50))
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setStyleSheet(u"background-color: #800080;\n"
"font: 700 18pt \"Segoe Script\" ;\n"
"color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 0, 9, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"padding:0px;\n"
"margin:0px;")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 2)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(100, 0))
        self.frame_3.setMaximumSize(QSize(400, 16777215))
        self.frame_3.setStyleSheet(u"background-color: rgb(216, 199, 230);\n"
"padding:0px;\n"
"margin-left:0px;\n"
"border: 2px solid rgb(170, 0, 255)")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_3.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 1)
        self.widget_4 = QWidget(self.frame_3)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setEnabled(True)
        self.widget_4.setMaximumSize(QSize(16777215, 60))
        self.widget_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.widget_4.setStyleSheet(u"margin: 0px;\n"
"background-color: rgb(192,132,252);\n"
"color: rgb(126,34,206);\n"
"border:  2px solid rgb(170, 85, 255);\n"
"	")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 9, -1, -1)
        self.horizontalSpacer = QSpacerItem(3, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"border: none")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(3, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.widget_3 = QWidget(self.frame_3)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 70))
        self.widget_3.setMaximumSize(QSize(16777215, 70))
        self.widget_3.setStyleSheet(u"border:  none;\n"
"background-color: rgb(170, 85, 255);\n"
"color: #ffffff;\n"
"font: 12pt \"Bodoni MT\" ;\n"
"")
        self.layoutWidget = QWidget(self.widget_3)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 10, 171, 51))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_5.addWidget(self.label_6)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_5.addWidget(self.label_7)


        self.horizontalLayout_7.addLayout(self.verticalLayout_5)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.widget = QWidget(self.frame_3)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 70))
        self.widget.setStyleSheet(u"border: none;\n"
"background-color: rgb(170, 85, 255);\n"
"font: 12pt \"Bodoni MT\" ;\n"
"color: #ffffff")
        self.layoutWidget1 = QWidget(self.widget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 10, 171, 51))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_4.addWidget(self.label_5)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignVCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.frame_3, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.frame_4)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 40))
        self.widget_2.setMaximumSize(QSize(16777215, 50))
        self.widget_2.setStyleSheet(u"background-color: rgb(255, 215, 252);\n"
"font: 700 15pt \"System\";")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setSpacing(9)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(342, 19, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.DevName = QLabel(self.widget_2)
        self.DevName.setObjectName(u"DevName")
        font1 = QFont()
        font1.setFamilies([u"System"])
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setItalic(False)
        self.DevName.setFont(font1)

        self.horizontalLayout_4.addWidget(self.DevName)

        self.horizontalSpacer_4 = QSpacerItem(342, 19, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.ShowProgress = QLabel(self.widget_2)
        self.ShowProgress.setObjectName(u"ShowProgress")

        self.horizontalLayout_4.addWidget(self.ShowProgress)

        self.Microphone = QPushButton(self.widget_2)
        self.Microphone.setObjectName(u"Microphone")
        self.Microphone.setMinimumSize(QSize(30, 30))
        self.Microphone.setMaximumSize(QSize(60, 60))
        self.Microphone.setStyleSheet(u"image: url(:/Assets/assets/mic.png);\n"
"border: none;\n"
"background-color: rgba(255, 255, 255, 0)\n"
"")

        self.horizontalLayout_4.addWidget(self.Microphone)

        self.Files = QPushButton(self.widget_2)
        self.Files.setObjectName(u"Files")
        self.Files.setMinimumSize(QSize(30, 30))
        self.Files.setMaximumSize(QSize(60, 60))
        self.Files.setFont(font1)
        self.Files.setStyleSheet(u"image: url(:/Assets/assets/clip.png);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border: none;")

        self.horizontalLayout_4.addWidget(self.Files)


        self.verticalLayout_3.addWidget(self.widget_2)

        self.scrollArea = QScrollArea(self.frame_4)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(0, 0))
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setStyleSheet(u"background-color: rgb(63, 7, 79);\n"
"")
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 873, 384))
        self.splitter = QSplitter(self.scrollAreaWidgetContents)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(720, 220, 99, 80))
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 60))
        self.frame_5.setMaximumSize(QSize(16777215, 60))
        self.frame_5.setStyleSheet(u"background-color: rgba(124, 83, 124, 200)")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setSpacing(9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.MessageBox = QTextEdit(self.frame_5)
        self.MessageBox.setObjectName(u"MessageBox")
        self.MessageBox.setMaximumSize(QSize(16777215, 40))
        self.MessageBox.setStyleSheet(u"font: 12pt \"Segoe Print\";\n"
"border-radius: 10px; /* Rounded corners */\n"
"border: 1px solid #ccc; /* Border */\n"
"background-color: rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_5.addWidget(self.MessageBox)

        self.Send = QPushButton(self.frame_5)
        self.Send.setObjectName(u"Send")
        self.Send.setMinimumSize(QSize(40, 40))
        self.Send.setMaximumSize(QSize(60, 60))
        font2 = QFont()
        font2.setPointSize(12)
        self.Send.setFont(font2)
        self.Send.setAcceptDrops(True)
        self.Send.setStyleSheet(u"border-radius: 16px; /* Rounded corners */\n"
"background-color: #e6daff; /* Light purple background */\n"
"\n"
"\n"
"   image: url(:/Assets/assets/send (1).png); /* Replace 'path_to_your_icon.png' with the path to your icon */\n"
"padding: 5px;\n"
"")
        self.Send.setFlat(False)

        self.horizontalLayout_5.addWidget(self.Send)


        self.verticalLayout_3.addWidget(self.frame_5)


        self.horizontalLayout_2.addWidget(self.frame_4)

        self.widget_5 = QWidget(self.frame_2)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(100, 500))
        self.widget_5.setStyleSheet(u"background-color: rgb(216, 199, 230);\n"
"padding:0px;\n"
"margin-left:0px;\n"
"")
        self.layoutWidget2 = QWidget(self.widget_5)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(0, 0, 101, 431))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.layoutWidget2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"border:  4px solid rgb(170, 85, 255);\n"
"padding:5px;\n"
"font: 700 12pt \"Segoe UI\" ;\n"
"background-color: rgb(192,132,252);\n"
"color: rgb(126,34,206);")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_9)

        self.splitter_2 = QSplitter(self.layoutWidget2)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Orientation.Vertical)
        self.ChannelInpt = QLineEdit(self.splitter_2)
        self.ChannelInpt.setObjectName(u"ChannelInpt")
        self.ChannelInpt.setMinimumSize(QSize(0, 30))
        self.ChannelInpt.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.ChannelInpt.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly)
        self.ChannelInpt.setMaxLength(2)
        self.splitter_2.addWidget(self.ChannelInpt)
        self.label_3 = QLabel(self.splitter_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(160, 120))
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3.setWordWrap(True)
        self.splitter_2.addWidget(self.label_3)
        self.BaudInpt = QComboBox(self.splitter_2)
        self.BaudInpt.addItem("")
        self.BaudInpt.addItem("")
        self.BaudInpt.addItem("")
        self.BaudInpt.addItem("")
        self.BaudInpt.addItem("")
        self.BaudInpt.addItem("")
        self.BaudInpt.addItem("")
        self.BaudInpt.addItem("")
        self.BaudInpt.setObjectName(u"BaudInpt")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BaudInpt.sizePolicy().hasHeightForWidth())
        self.BaudInpt.setSizePolicy(sizePolicy)
        self.BaudInpt.setMaximumSize(QSize(100, 70))
        font3 = QFont()
        font3.setFamilies([u"Yu Gothic UI Semibold"])
        font3.setPointSize(11)
        font3.setWeight(QFont.DemiBold)
        font3.setItalic(False)
        self.BaudInpt.setFont(font3)
        self.BaudInpt.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.BaudInpt.setStyleSheet(u"font: 600 11pt \"Yu Gothic UI Semibold\";")
        self.splitter_2.addWidget(self.BaudInpt)

        self.verticalLayout_6.addWidget(self.splitter_2)

        self.Discoveribility = QPushButton(self.layoutWidget2)
        self.Discoveribility.setObjectName(u"Discoveribility")
        self.Discoveribility.setMinimumSize(QSize(40, 40))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.Discoveribility.setFont(font4)
        self.Discoveribility.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.Discoveribility.setStyleSheet(u"QPushButton{\n"
"image: url(:/Assets/assets/wifi.png);\n"
"padding: 2px;\n"
"border: none;\n"
"text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 255, 255, 64);\n"
"}")
        self.Discoveribility.setIconSize(QSize(40, 40))

        self.verticalLayout_6.addWidget(self.Discoveribility)

        self.Search = QPushButton(self.layoutWidget2)
        self.Search.setObjectName(u"Search")
        self.Search.setMinimumSize(QSize(40, 40))
        font5 = QFont()
        font5.setFamilies([u"Segoe Script"])
        font5.setPointSize(18)
        font5.setBold(True)
        font5.setItalic(False)
        self.Search.setFont(font5)
        self.Search.setStyleSheet(u"QPushButton{\n"
"image: url(:/Assets/assets/search.png);\n"
"padding:3px;\n"
"border: none;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255, 64);}")

        self.verticalLayout_6.addWidget(self.Search)

        self.Refresh = QPushButton(self.layoutWidget2)
        self.Refresh.setObjectName(u"Refresh")
        self.Refresh.setMinimumSize(QSize(40, 40))
        self.Refresh.setStyleSheet(u"QPushButton{ \n"
"border:none;\n"
"image: url(:/Assets/assets/refresh.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 255, 255, 60);\n"
"}")

        self.verticalLayout_6.addWidget(self.Refresh)

        self.ComList = QComboBox(self.layoutWidget2)
        self.ComList.setObjectName(u"ComList")
        self.ComList.setStyleSheet(u"border-radius: 20px;\n"
"background-color: rgba(255, 170, 255, 150);\n"
"font: 11pt \"Segoe UI\";")

        self.verticalLayout_6.addWidget(self.ComList)

        self.ConnectComPort = QPushButton(self.layoutWidget2)
        self.ConnectComPort.setObjectName(u"ConnectComPort")
        self.ConnectComPort.setMinimumSize(QSize(40, 40))
        self.ConnectComPort.setStyleSheet(u"QPushButton{ \n"
"border:none;\n"
"	image: url(:/Assets/assets/hotspot.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 255, 255, 60);\n"
"}")

        self.verticalLayout_6.addWidget(self.ConnectComPort)

        self.checkBox = QCheckBox(self.layoutWidget2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMaximumSize(QSize(100, 100))
        self.checkBox.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.checkBox.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")

        self.verticalLayout_6.addWidget(self.checkBox)


        self.horizontalLayout_2.addWidget(self.widget_5, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Send.setDefault(False)
        self.BaudInpt.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Portable Wireless Communication", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nearby Devices", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.DevName.setText(QCoreApplication.translate("MainWindow", u"Device 1", None))
        self.ShowProgress.setText("")
#if QT_CONFIG(tooltip)
        self.Microphone.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Voice messege</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Microphone.setText("")
#if QT_CONFIG(tooltip)
        self.Files.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>attach</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Files.setText("")
#if QT_CONFIG(tooltip)
        self.MessageBox.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">qww</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.Send.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Send </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Send.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Setup", None))
#if QT_CONFIG(tooltip)
        self.ChannelInpt.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Select Channel</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ChannelInpt.setPlaceholderText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Select channel from 1-99", None))
        self.BaudInpt.setItemText(0, QCoreApplication.translate("MainWindow", u"1200", None))
        self.BaudInpt.setItemText(1, QCoreApplication.translate("MainWindow", u"2400", None))
        self.BaudInpt.setItemText(2, QCoreApplication.translate("MainWindow", u" 4800", None))
        self.BaudInpt.setItemText(3, QCoreApplication.translate("MainWindow", u" 9600", None))
        self.BaudInpt.setItemText(4, QCoreApplication.translate("MainWindow", u"19200", None))
        self.BaudInpt.setItemText(5, QCoreApplication.translate("MainWindow", u" 38400", None))
        self.BaudInpt.setItemText(6, QCoreApplication.translate("MainWindow", u" 57600", None))
        self.BaudInpt.setItemText(7, QCoreApplication.translate("MainWindow", u"115200", None))

#if QT_CONFIG(tooltip)
        self.BaudInpt.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Baudrate</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.BaudInpt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Baud-Rate", None))
        self.Discoveribility.setText("")
#if QT_CONFIG(tooltip)
        self.Search.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Search</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Search.setText("")
#if QT_CONFIG(tooltip)
        self.Refresh.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Refresh</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Refresh.setText("")
        self.ConnectComPort.setText("")
#if QT_CONFIG(tooltip)
        self.checkBox.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Encryption on/off</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Encryption", None))
    # retranslateUi

