# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        MainWindow.setStyleSheet("background-color: rgb(24,24,26);")
        MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_bar = QtWidgets.QFrame(self.centralwidget)
        self.top_bar.setMaximumSize(QtCore.QSize(16777215, 32))
        self.top_bar.setStyleSheet("background-color: rgb(38, 38, 38);")
        self.top_bar.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.top_bar.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.top_bar.setLineWidth(0)
        self.top_bar.setObjectName("top_bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.top_bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.toggle_menu = QtWidgets.QFrame(self.top_bar)
        self.toggle_menu.setMaximumSize(QtCore.QSize(70, 32))
        self.toggle_menu.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.toggle_menu.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.toggle_menu.setLineWidth(0)
        self.toggle_menu.setObjectName("toggle_menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.toggle_menu)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_menu = QtWidgets.QPushButton(self.toggle_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_menu.sizePolicy().hasHeightForWidth())
        self.btn_menu.setSizePolicy(sizePolicy)
        self.btn_menu.setMinimumSize(QtCore.QSize(45, 0))
        self.btn_menu.setMaximumSize(QtCore.QSize(45, 32))
        self.btn_menu.setStyleSheet("QPushButton:pressed {\n"
"    border-style: inset;\n"
"}")
        self.btn_menu.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/menu_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_menu.setIcon(icon)
        self.btn_menu.setIconSize(QtCore.QSize(32, 32))
        self.btn_menu.setAutoDefault(False)
        self.btn_menu.setDefault(False)
        self.btn_menu.setFlat(True)
        self.btn_menu.setObjectName("btn_menu")
        self.verticalLayout_2.addWidget(self.btn_menu)
        self.horizontalLayout.addWidget(self.toggle_menu)
        self.frame = QtWidgets.QFrame(self.top_bar)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 32))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.horizontalLayout.addWidget(self.frame)
        self.verticalLayout.addWidget(self.top_bar)
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.content.setLineWidth(0)
        self.content.setObjectName("content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.slide_menu = QtWidgets.QFrame(self.content)
        self.slide_menu.setMinimumSize(QtCore.QSize(0, 300))
        self.slide_menu.setMaximumSize(QtCore.QSize(48, 1000))
        self.slide_menu.setStyleSheet("background-color: rgb(64, 64, 64);")
        self.slide_menu.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.slide_menu.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.slide_menu.setLineWidth(0)
        self.slide_menu.setObjectName("slide_menu")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.slide_menu)
        self.horizontalLayout_4.setContentsMargins(0, 0, 2, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.icons_frame = QtWidgets.QFrame(self.slide_menu)
        self.icons_frame.setMinimumSize(QtCore.QSize(0, 300))
        self.icons_frame.setMaximumSize(QtCore.QSize(46, 1000))
        self.icons_frame.setStyleSheet("background-color: rgb(38, 38, 38);")
        self.icons_frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.icons_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.icons_frame.setLineWidth(0)
        self.icons_frame.setObjectName("icons_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.icons_frame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_serial = QtWidgets.QPushButton(self.icons_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_serial.sizePolicy().hasHeightForWidth())
        self.btn_serial.setSizePolicy(sizePolicy)
        self.btn_serial.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_serial.setAutoFillBackground(False)
        self.btn_serial.setStyleSheet("QPushButton {\n"
"    background-color: rgb(50, 50, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(55, 55, 55);\n"
"    border-style: inset;\n"
"}")
        self.btn_serial.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/arduino_logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_serial.setIcon(icon1)
        self.btn_serial.setIconSize(QtCore.QSize(32, 32))
        self.btn_serial.setCheckable(False)
        self.btn_serial.setChecked(False)
        self.btn_serial.setAutoDefault(False)
        self.btn_serial.setDefault(False)
        self.btn_serial.setFlat(True)
        self.btn_serial.setObjectName("btn_serial")
        self.verticalLayout_4.addWidget(self.btn_serial)
        self.btn_database = QtWidgets.QPushButton(self.icons_frame)
        self.btn_database.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_database.sizePolicy().hasHeightForWidth())
        self.btn_database.setSizePolicy(sizePolicy)
        self.btn_database.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_database.setAutoFillBackground(False)
        self.btn_database.setStyleSheet("QPushButton {\n"
"    background-color: rgb(50, 50, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(55, 55, 55);\n"
"    border-style: inset;\n"
"}")
        self.btn_database.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resources/database_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_database.setIcon(icon2)
        self.btn_database.setIconSize(QtCore.QSize(32, 32))
        self.btn_database.setFlat(True)
        self.btn_database.setObjectName("btn_database")
        self.verticalLayout_4.addWidget(self.btn_database)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout_4.addWidget(self.icons_frame)
        self.horizontalLayout_2.addWidget(self.slide_menu)
        self.frame_3 = QtWidgets.QFrame(self.content)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_3.setLineWidth(0)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.page_widgets = QtWidgets.QStackedWidget(self.frame_3)
        self.page_widgets.setEnabled(True)
        self.page_widgets.setAutoFillBackground(False)
        self.page_widgets.setLineWidth(0)
        self.page_widgets.setObjectName("page_widgets")
        self.serial_page = QtWidgets.QWidget()
        self.serial_page.setObjectName("serial_page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.serial_page)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_2 = QtWidgets.QFrame(self.serial_page)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_2.setLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.serialInput = QtWidgets.QLineEdit(self.frame_2)
        self.serialInput.setMinimumSize(QtCore.QSize(0, 40))
        self.serialInput.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.serialInput.setFont(font)
        self.serialInput.setAutoFillBackground(False)
        self.serialInput.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"padding-left: 10px;")
        self.serialInput.setFrame(True)
        self.serialInput.setCursorPosition(0)
        self.serialInput.setClearButtonEnabled(False)
        self.serialInput.setObjectName("serialInput")
        self.verticalLayout_6.addWidget(self.serialInput)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_4.setAutoFillBackground(False)
        self.frame_4.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"border-radius:20px")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_4.setLineWidth(0)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_3.setSpacing(7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_4)
        self.scrollArea.setEnabled(True)
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1164, 599))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.serialOutput = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serialOutput.sizePolicy().hasHeightForWidth())
        self.serialOutput.setSizePolicy(sizePolicy)
        self.serialOutput.setMinimumSize(QtCore.QSize(0, 0))
        self.serialOutput.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.serialOutput.setFont(font)
        self.serialOutput.setAutoFillBackground(False)
        self.serialOutput.setStyleSheet("color: rgb(255, 255, 255);")
        self.serialOutput.setLineWidth(0)
        self.serialOutput.setText("")
        self.serialOutput.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.serialOutput.setObjectName("serialOutput")
        self.verticalLayout_7.addWidget(self.serialOutput)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.addWidget(self.scrollArea)
        self.verticalScrollBar = QtWidgets.QScrollBar(self.frame_4)
        self.verticalScrollBar.setMaximumSize(QtCore.QSize(20, 16777215))
        self.verticalScrollBar.setStyleSheet("QScrollBar::handle:vertical {\n"
"    background-color: rgb(32, 32, 32);\n"
"    border-radius: 4px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{\n"
"    background-color: rgb(204, 120, 50);\n"
"    border-radius: 4px;\n"
"}\n"
"QScrollBar::handle:vertical:pressed {\n"
"    background-color: rgb(237, 131, 43);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical{\n"
"    background: rgb(38, 38, 38);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical{\n"
"    background: rgb(38, 38, 38);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
" QScrollBar:vertical {\n"
"    border: 1px solid rgb(38, 38, 38);\n"
"    background-color: rgb(38, 38, 38);\n"
"    border-radius: 4px;\n"
" }\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"     border-radius: 4px;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"     border-radius: 4px;\n"
"}")
        self.verticalScrollBar.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.horizontalLayout_3.addWidget(self.verticalScrollBar)
        self.verticalLayout_6.addWidget(self.frame_4)
        self.verticalLayout_5.addWidget(self.frame_2)
        self.page_widgets.addWidget(self.serial_page)
        self.database_page = QtWidgets.QWidget()
        self.database_page.setObjectName("database_page")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.database_page)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.page_widgets.addWidget(self.database_page)
        self.verticalLayout_3.addWidget(self.page_widgets)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.content)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.page_widgets.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cadeira"))
        self.serialInput.setPlaceholderText(_translate("MainWindow", "Digite:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
