# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpinBox, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(564, 515)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 331, 31))
        font = QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 70, 81, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 70, 61, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(240, 70, 121, 16))
        self.inputLength = QLineEdit(self.centralwidget)
        self.inputLength.setObjectName(u"inputLength")
        self.inputLength.setGeometry(QRect(20, 90, 91, 21))
        self.inputWidth = QLineEdit(self.centralwidget)
        self.inputWidth.setObjectName(u"inputWidth")
        self.inputWidth.setGeometry(QRect(130, 90, 91, 21))
        self.inputHeight = QLineEdit(self.centralwidget)
        self.inputHeight.setObjectName(u"inputHeight")
        self.inputHeight.setGeometry(QRect(240, 90, 91, 21))
        self.btnCalc = QPushButton(self.centralwidget)
        self.btnCalc.setObjectName(u"btnCalc")
        self.btnCalc.setGeometry(QRect(20, 330, 271, 24))
        self.outputSquare = QLabel(self.centralwidget)
        self.outputSquare.setObjectName(u"outputSquare")
        self.outputSquare.setGeometry(QRect(310, 330, 111, 21))
        font1 = QFont()
        font1.setPointSize(12)
        self.outputSquare.setFont(font1)
        self.outputSquare.setFrameShadow(QFrame.Plain)
        self.outputSquare.setTextFormat(Qt.RichText)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 380, 311, 21))
        font2 = QFont()
        font2.setPointSize(10)
        self.label_5.setFont(font2)
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem(u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(20, 420, 231, 22))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 130, 321, 31))
        self.label_7.setFont(font2)
        self.doorsCount = QSpinBox(self.centralwidget)
        self.doorsCount.setObjectName(u"doorsCount")
        self.doorsCount.setGeometry(QRect(220, 180, 42, 22))
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 230, 321, 21))
        self.label_10.setFont(font2)
        self.windowsCount = QSpinBox(self.centralwidget)
        self.windowsCount.setObjectName(u"windowsCount")
        self.windowsCount.setGeometry(QRect(310, 270, 42, 22))
        self.doorCmbx = QComboBox(self.centralwidget)
        self.doorCmbx.addItem("")
        self.doorCmbx.addItem("")
        self.doorCmbx.addItem("")
        self.doorCmbx.addItem("")
        self.doorCmbx.addItem("")
        self.doorCmbx.setObjectName(u"doorCmbx")
        self.doorCmbx.setGeometry(QRect(20, 180, 171, 22))
        self.windowCmbx = QComboBox(self.centralwidget)
        self.windowCmbx.addItem("")
        self.windowCmbx.addItem("")
        self.windowCmbx.addItem("")
        self.windowCmbx.addItem("")
        self.windowCmbx.setObjectName(u"windowCmbx")
        self.windowCmbx.setGeometry(QRect(20, 270, 271, 22))
        self.btnAdd1 = QPushButton(self.centralwidget)
        self.btnAdd1.setObjectName(u"btnAdd1")
        self.btnAdd1.setGeometry(QRect(290, 180, 141, 24))
        self.btnAdd2 = QPushButton(self.centralwidget)
        self.btnAdd2.setObjectName(u"btnAdd2")
        self.btnAdd2.setGeometry(QRect(380, 270, 141, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 564, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043a\u043e\u043c\u043d\u0430\u0442\u044b", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0440\u0438\u043d\u0430, \u043c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u043d\u0430, \u043c", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u0442\u0430 \u043f\u043e\u0442\u043e\u043b\u043a\u0430, \u043c", None))
        self.btnCalc.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c \u043f\u043b\u043e\u0449\u0430\u0434\u044c \u0440\u0430\u0431\u043e\u0447\u0435\u0439 \u043f\u043e\u0432\u0435\u0440\u0445\u043d\u043e\u0441\u0442\u0438", None))
        self.outputSquare.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b \u0434\u043b\u044f \u043e\u0442\u0434\u0435\u043b\u043a\u0438 \u0441\u0442\u0435\u043d", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043e\u0438", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041a\u0440\u0430\u0441\u043a\u0430", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043d\u0435\u043b\u0438", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"\u0428\u0442\u0443\u043a\u0430\u0442\u0443\u0440\u043a\u0430", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0440\u0430\u0437\u043c\u0435\u0440 \u0438 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0434\u0432\u0435\u0440\u0435\u0439", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0440\u0430\u0437\u043c\u0435\u0440 \u0438 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043e\u043a\u043e\u043d", None))
        self.doorCmbx.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.doorCmbx.setItemText(1, QCoreApplication.translate("MainWindow", u"800 \u0445 2000 \u043c\u043c", None))
        self.doorCmbx.setItemText(2, QCoreApplication.translate("MainWindow", u"1300 \u0445 2000 \u043c\u043c", None))
        self.doorCmbx.setItemText(3, QCoreApplication.translate("MainWindow", u"600 x 2000 \u043c\u043c", None))
        self.doorCmbx.setItemText(4, QCoreApplication.translate("MainWindow", u"700 \u0445 1900 \u043c\u043c", None))

        self.windowCmbx.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.windowCmbx.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041e\u0434\u043d\u043e\u0441\u0442\u0432\u043e\u0440\u0447\u0430\u0442\u044b\u0435 - 700 \u0445 1350 \u043c\u043c", None))
        self.windowCmbx.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0443\u0445\u0441\u0442\u0432\u043e\u0440\u0447\u0430\u0442\u044b\u0435 - 1300 \u0445 1400 \u043c\u043c", None))
        self.windowCmbx.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0435\u0445\u0441\u0442\u0432\u043e\u0440\u0447\u0430\u0442\u044b\u0435 - 2050 \u0445 1400 \u043c\u043c", None))

        self.btnAdd1.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0434\u0432\u0435\u0440\u044c", None))
        self.btnAdd2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043e\u043a\u043d\u043e", None))
    # retranslateUi

