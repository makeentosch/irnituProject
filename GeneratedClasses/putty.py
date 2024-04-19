# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'putty.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QSizePolicy, QWidget)

class Ui_Putty(object):
    def setupUi(self, Putty):
        if not Putty.objectName():
            Putty.setObjectName(u"Putty")
        Putty.resize(403, 333)
        self.label_10 = QLabel(Putty)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 30, 181, 21))
        font = QFont()
        font.setPointSize(13)
        self.label_10.setFont(font)
        self.label_5 = QLabel(Putty)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 190, 151, 16))
        self.inputLayerWidth = QLineEdit(Putty)
        self.inputLayerWidth.setObjectName(u"inputLayerWidth")
        self.inputLayerWidth.setGeometry(QRect(20, 110, 61, 21))
        self.outputSquare = QLabel(Putty)
        self.outputSquare.setObjectName(u"outputSquare")
        self.outputSquare.setGeometry(QRect(230, 160, 55, 16))
        self.outputSquare.setTextFormat(Qt.RichText)
        self.label_4 = QLabel(Putty)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 160, 201, 16))
        self.label_3 = QLabel(Putty)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 80, 101, 16))
        self.outputPuttyCount = QLabel(Putty)
        self.outputPuttyCount.setObjectName(u"outputPuttyCount")
        self.outputPuttyCount.setGeometry(QRect(180, 190, 55, 16))
        self.outputPuttyCount.setTextFormat(Qt.RichText)

        self.retranslateUi(Putty)

        QMetaObject.connectSlotsByName(Putty)
    # setupUi

    def retranslateUi(self, Putty):
        Putty.setWindowTitle(QCoreApplication.translate("Putty", u"Dialog", None))
        self.label_10.setText(QCoreApplication.translate("Putty", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.label_5.setText(QCoreApplication.translate("Putty", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0448\u0442\u0443\u043a\u0430\u0442\u0443\u0440\u043a\u0438:", None))
        self.outputSquare.setText("")
        self.label_4.setText(QCoreApplication.translate("Putty", u"\u041f\u043b\u043e\u0449\u0430\u0434\u044c \u0440\u0430\u0431\u043e\u0447\u0435\u0439 \u043f\u043e\u0432\u0435\u0440\u0445\u043d\u043e\u0441\u0442\u0438:", None))
        self.label_3.setText(QCoreApplication.translate("Putty", u"\u0422\u043e\u043b\u0449\u0438\u043d\u0430 \u0441\u043b\u043e\u044f", None))
        self.outputPuttyCount.setText("")
    # retranslateUi

