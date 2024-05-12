# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wallpaper.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Wallpapers(object):
    def setupUi(self, Wallpapers):
        if not Wallpapers.objectName():
            Wallpapers.setObjectName(u"Wallpapers")
        Wallpapers.resize(455, 371)
        self.label = QLabel(Wallpapers)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 291, 31))
        font = QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label_2 = QLabel(Wallpapers)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 80, 71, 16))
        self.label_3 = QLabel(Wallpapers)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(120, 80, 101, 16))
        self.label_4 = QLabel(Wallpapers)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(250, 80, 71, 16))
        self.label_5 = QLabel(Wallpapers)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(350, 80, 55, 16))
        self.inputWidth = QLineEdit(Wallpapers)
        self.inputWidth.setObjectName(u"inputWidth")
        self.inputWidth.setGeometry(QRect(20, 100, 71, 21))
        self.inputLength = QLineEdit(Wallpapers)
        self.inputLength.setObjectName(u"inputLength")
        self.inputLength.setGeometry(QRect(110, 100, 111, 21))
        self.inputRapport = QLineEdit(Wallpapers)
        self.inputRapport.setObjectName(u"inputRapport")
        self.inputRapport.setGeometry(QRect(240, 100, 81, 21))
        self.inputReserve = QLineEdit(Wallpapers)
        self.inputReserve.setObjectName(u"inputReserve")
        self.inputReserve.setGeometry(QRect(340, 100, 71, 21))
        self.label_6 = QLabel(Wallpapers)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 140, 121, 31))
        font1 = QFont()
        font1.setPointSize(10)
        self.label_6.setFont(font1)
        self.comboBox = QComboBox(Wallpapers)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(20, 180, 231, 22))
        self.label_9 = QLabel(Wallpapers)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 310, 131, 16))
        self.outputWpCount = QLabel(Wallpapers)
        self.outputWpCount.setObjectName(u"outputWpCount")
        self.outputWpCount.setGeometry(QRect(160, 280, 55, 16))
        self.outputWpCount.setTextFormat(Qt.RichText)
        self.btnCalc = QPushButton(Wallpapers)
        self.btnCalc.setObjectName(u"btnCalc")
        self.btnCalc.setGeometry(QRect(20, 230, 93, 28))
        self.label_7 = QLabel(Wallpapers)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 280, 131, 16))
        self.outputGlueCount = QLabel(Wallpapers)
        self.outputGlueCount.setObjectName(u"outputGlueCount")
        self.outputGlueCount.setGeometry(QRect(140, 310, 121, 16))
        self.outputGlueCount.setTextFormat(Qt.RichText)

        self.retranslateUi(Wallpapers)

        QMetaObject.connectSlotsByName(Wallpapers)
    # setupUi

    def retranslateUi(self, Wallpapers):
        Wallpapers.setWindowTitle(QCoreApplication.translate("Wallpapers", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Wallpapers", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043e\u0431\u043e\u0435\u0432", None))
        self.label_2.setText(QCoreApplication.translate("Wallpapers", u"\u0428\u0438\u0440\u0438\u043d\u0430, \u043c", None))
        self.label_3.setText(QCoreApplication.translate("Wallpapers", u"\u0414\u043b\u0438\u043d\u0430 \u0440\u0443\u043b\u043e\u043d\u0430, \u043c", None))
        self.label_4.setText(QCoreApplication.translate("Wallpapers", u"\u0420\u0430\u043f\u043f\u043e\u0440\u0442, \u043c", None))
        self.label_5.setText(QCoreApplication.translate("Wallpapers", u"\u0417\u0430\u043f\u0430\u0441, \u043c", None))
        self.label_6.setText(QCoreApplication.translate("Wallpapers", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u043b\u0435\u0439", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Wallpapers", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Wallpapers", u"\u041e\u0431\u043e\u0438 \u0424\u043b\u0438\u0437\u0435\u043b\u0438\u043d\u043e\u0432\u044b\u0435, \u0441\u0442\u0430\u043d\u0434\u0430\u0440\u0442", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Wallpapers", u"\u041e\u0431\u043e\u0438 \u0424\u043b\u0438\u0437\u0435\u043b\u0438\u043d\u043e\u0432\u044b\u0435, \u043b\u0435\u0433\u043a\u0438\u0435", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Wallpapers", u"\u041e\u0431\u043e\u0438 \u0411\u0443\u043c\u0430\u0436\u043d\u044b\u0435, \u0441\u0442\u0430\u043d\u0434\u0430\u0440\u0442", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Wallpapers", u"\u041e\u0431\u043e\u0438 \u0411\u0443\u043c\u0430\u0436\u043d\u044b\u0435, \u043b\u0435\u0433\u043a\u0438\u0435", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Wallpapers", u"\u041e\u0431\u043e\u0438 \u0412\u0438\u043d\u0438\u043b\u043e\u0432\u044b\u0435, \u0441\u0442\u0430\u043d\u0434\u0430\u0440\u0442", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("Wallpapers", u"\u041e\u0431\u043e\u0438 \u0412\u0438\u043d\u0438\u043b\u043e\u0432\u044b\u0435, \u0442\u044f\u0436\u0435\u043b\u044b\u0435", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("Wallpapers", u"\u041e\u0431\u043e\u0438 \u0421\u0442\u0435\u043a\u043b\u043e\u043e\u0431\u043e\u0438", None))

        self.label_9.setText(QCoreApplication.translate("Wallpapers", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043a\u043b\u0435\u044f (\u0433):", None))
        self.outputWpCount.setText("")
        self.btnCalc.setText(QCoreApplication.translate("Wallpapers", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.label_7.setText(QCoreApplication.translate("Wallpapers", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0440\u0443\u043b\u043e\u043d\u043e\u0432:", None))
        self.outputGlueCount.setText("")
    # retranslateUi

