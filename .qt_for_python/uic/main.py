# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import Resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.bg = QFrame(self.centralwidget)
        self.bg.setObjectName(u"bg")
        self.bg.setStyleSheet(u"/* /////////////////////////////////////////\n"
"BACKGROUND COLOR OF THE APP */\n"
"#bg{background-color: rgb(40, 44, 52)}\n"
"\n"
"/* /////////////////////////////////////////\n"
"LABEL STYLESHEET */\n"
"QLabel{\n"
"	color: rgb(230, 230, 230);\n"
"	font-family: \"Segoe UI\";\n"
"	font-size: 15px\n"
"}\n"
"/* /////////////////////////////////////////\n"
"TOOL TIP */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}")
        self.bg.setFrameShape(QFrame.StyledPanel)
        self.bg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.bg)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.topBar = QFrame(self.bg)
        self.topBar.setObjectName(u"topBar")
        self.topBar.setMaximumSize(QSize(16777215, 50))
        self.topBar.setSizeIncrement(QSize(0, 50))
        self.topBar.setStyleSheet(u"QFrame{background-color: rgb(33, 37, 43);}\n"
"\n"
"/* /////////////////////////////////////////\n"
"TOP BAR BUTTONS STYLE SHEET*/\n"
"QPushButton{\n"
"	border: none;\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:hover{	\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(14, 16, 18)\n"
"}\n"
"")
        self.topBar.setFrameShape(QFrame.StyledPanel)
        self.topBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.topBar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.titleBar = QLabel(self.topBar)
        self.titleBar.setObjectName(u"titleBar")
        self.titleBar.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.titleBar)

        self.zoomOutBtn = QPushButton(self.topBar)
        self.zoomOutBtn.setObjectName(u"zoomOutBtn")
        self.zoomOutBtn.setMinimumSize(QSize(25, 25))
        self.zoomOutBtn.setMaximumSize(QSize(25, 25))
        icon = QIcon()
        icon.addFile(u":/Icons/img/icons/cil-zoom-out.png", QSize(), QIcon.Normal, QIcon.Off)
        self.zoomOutBtn.setIcon(icon)

        self.horizontalLayout.addWidget(self.zoomOutBtn)

        self.zoomInBtn = QPushButton(self.topBar)
        self.zoomInBtn.setObjectName(u"zoomInBtn")
        self.zoomInBtn.setMinimumSize(QSize(25, 25))
        self.zoomInBtn.setMaximumSize(QSize(25, 25))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/img/icons/cil-zoom-in.png", QSize(), QIcon.Normal, QIcon.Off)
        self.zoomInBtn.setIcon(icon1)

        self.horizontalLayout.addWidget(self.zoomInBtn)

        self.runFileBtn = QPushButton(self.topBar)
        self.runFileBtn.setObjectName(u"runFileBtn")
        self.runFileBtn.setMinimumSize(QSize(25, 25))
        self.runFileBtn.setMaximumSize(QSize(25, 25))
        icon2 = QIcon()
        icon2.addFile(u":/Icons/img/icons/cil-media-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.runFileBtn.setIcon(icon2)

        self.horizontalLayout.addWidget(self.runFileBtn)

        self.openFileBtn = QPushButton(self.topBar)
        self.openFileBtn.setObjectName(u"openFileBtn")
        self.openFileBtn.setMinimumSize(QSize(25, 25))
        self.openFileBtn.setMaximumSize(QSize(25, 25))
        icon3 = QIcon()
        icon3.addFile(u":/Icons/img/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.openFileBtn.setIcon(icon3)

        self.horizontalLayout.addWidget(self.openFileBtn)

        self.saveAsBtn = QPushButton(self.topBar)
        self.saveAsBtn.setObjectName(u"saveAsBtn")
        self.saveAsBtn.setMinimumSize(QSize(25, 25))
        self.saveAsBtn.setMaximumSize(QSize(25, 25))
        icon4 = QIcon()
        icon4.addFile(u":/Icons/img/icons/cil-notes.png", QSize(), QIcon.Normal, QIcon.Off)
        self.saveAsBtn.setIcon(icon4)

        self.horizontalLayout.addWidget(self.saveAsBtn)

        self.saveFileBtn = QPushButton(self.topBar)
        self.saveFileBtn.setObjectName(u"saveFileBtn")
        self.saveFileBtn.setMinimumSize(QSize(25, 25))
        self.saveFileBtn.setMaximumSize(QSize(25, 25))
        icon5 = QIcon()
        icon5.addFile(u":/Icons/img/icons/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.saveFileBtn.setIcon(icon5)

        self.horizontalLayout.addWidget(self.saveFileBtn)

        self.minimizeBtn = QPushButton(self.topBar)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        self.minimizeBtn.setMinimumSize(QSize(25, 25))
        self.minimizeBtn.setMaximumSize(QSize(25, 25))
        icon6 = QIcon()
        icon6.addFile(u":/Icons/img/icons/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon6)

        self.horizontalLayout.addWidget(self.minimizeBtn)

        self.maxBtn = QPushButton(self.topBar)
        self.maxBtn.setObjectName(u"maxBtn")
        self.maxBtn.setMinimumSize(QSize(25, 25))
        self.maxBtn.setMaximumSize(QSize(25, 25))
        icon7 = QIcon()
        icon7.addFile(u":/Icons/img/icons/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maxBtn.setIcon(icon7)

        self.horizontalLayout.addWidget(self.maxBtn)

        self.closeBtn = QPushButton(self.topBar)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setMinimumSize(QSize(25, 25))
        self.closeBtn.setMaximumSize(QSize(25, 25))
        self.closeBtn.setStyleSheet(u"#closeBtn:pressed{\n"
"	background-color: \"#ff5555\"\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/Icons/img/icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon8)

        self.horizontalLayout.addWidget(self.closeBtn)


        self.verticalLayout_2.addWidget(self.topBar)

        self.frame = QFrame(self.bg)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.textEdit = QTextEdit(self.frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(40, 44, 52);\n"
"	border: 1px solid white;\n"
"	color: white;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
""
                        "     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar:"
                        ":down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }")

        self.horizontalLayout_2.addWidget(self.textEdit)


        self.verticalLayout_2.addWidget(self.frame)

        self.bottomframe = QFrame(self.bg)
        self.bottomframe.setObjectName(u"bottomframe")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottomframe.sizePolicy().hasHeightForWidth())
        self.bottomframe.setSizePolicy(sizePolicy)
        self.bottomframe.setMaximumSize(QSize(16777215, 25))
        self.bottomframe.setSizeIncrement(QSize(0, 25))
        self.bottomframe.setFrameShape(QFrame.StyledPanel)
        self.bottomframe.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.bottomframe)


        self.verticalLayout.addWidget(self.bg)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.zoomInBtn.clicked.connect(self.textEdit.zoomIn)
        self.zoomOutBtn.clicked.connect(self.textEdit.zoomOut)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Python Code Editor", None))
        self.titleBar.setText(QCoreApplication.translate("MainWindow", u"Python Code Editor", None))
        self.zoomOutBtn.setText("")
#if QT_CONFIG(shortcut)
        self.zoomOutBtn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+-", None))
#endif // QT_CONFIG(shortcut)
        self.zoomInBtn.setText("")
#if QT_CONFIG(shortcut)
        self.zoomInBtn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+=", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.runFileBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Run File in Terminal (F5)", None))
#endif // QT_CONFIG(tooltip)
        self.runFileBtn.setText("")
#if QT_CONFIG(shortcut)
        self.runFileBtn.setShortcut(QCoreApplication.translate("MainWindow", u"F5", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.openFileBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Open File (ctrl + o)", None))
#endif // QT_CONFIG(tooltip)
        self.openFileBtn.setText("")
#if QT_CONFIG(shortcut)
        self.openFileBtn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.saveAsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Save As (ctrl + Shit + s)", None))
#endif // QT_CONFIG(tooltip)
        self.saveAsBtn.setText("")
#if QT_CONFIG(shortcut)
        self.saveAsBtn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.saveFileBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Save File (ctrl + s)", None))
#endif // QT_CONFIG(tooltip)
        self.saveFileBtn.setText("")
#if QT_CONFIG(shortcut)
        self.saveFileBtn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.minimizeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maxBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maxBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
    # retranslateUi

