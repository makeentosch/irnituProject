# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'panels.ui'
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
    QPushButton, QSizePolicy, QWidget)

class Ui_Panels(object):
    def setupUi(self, Panels):
        if not Panels.objectName():
            Panels.setObjectName(u"Panels")
        Panels.resize(400, 300)
        self.label_8 = QLabel(Panels)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 30, 181, 21))
        font = QFont()
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.typeCmbx = QComboBox(Panels)
        self.typeCmbx.addItem("")
        self.typeCmbx.addItem("")
        self.typeCmbx.addItem("")
        self.typeCmbx.addItem("")
        self.typeCmbx.addItem("")
        self.typeCmbx.addItem("")
        self.typeCmbx.setObjectName(u"typeCmbx")
        self.typeCmbx.setGeometry(QRect(20, 100, 231, 22))
        self.label = QLabel(Panels)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 70, 111, 16))
        self.btnCalc = QPushButton(Panels)
        self.btnCalc.setObjectName(u"btnCalc")
        self.btnCalc.setGeometry(QRect(20, 140, 93, 28))
        self.label_11 = QLabel(Panels)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 190, 171, 16))
        self.outputCnt = QLabel(Panels)
        self.outputCnt.setObjectName(u"outputCnt")
        self.outputCnt.setGeometry(QRect(190, 190, 55, 16))
        self.outputCnt.setTextFormat(Qt.RichText)

        self.retranslateUi(Panels)

        QMetaObject.connectSlotsByName(Panels)
    # setupUi

    def retranslateUi(self, Panels):
        Panels.setWindowTitle(QCoreApplication.translate("Panels", u"Dialog", None))
        self.label_8.setText(QCoreApplication.translate("Panels", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.typeCmbx.setItemText(0, QCoreApplication.translate("Panels", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.typeCmbx.setItemText(1, QCoreApplication.translate("Panels", u"3000\u0445250", None))
        self.typeCmbx.setItemText(2, QCoreApplication.translate("Panels", u"3000\u0445100", None))
        self.typeCmbx.setItemText(3, QCoreApplication.translate("Panels", u"2700\u0445250", None))
        self.typeCmbx.setItemText(4, QCoreApplication.translate("Panels", u"2700\u0445350", None))
        self.typeCmbx.setItemText(5, QCoreApplication.translate("Panels", u"2600\u0445240", None))

        self.label.setText(QCoreApplication.translate("Panels", u"\u0420\u0430\u0437\u043c\u0435\u0440\u044b \u043f\u0430\u043d\u0435\u043b\u0435\u0439", None))
        self.btnCalc.setText(QCoreApplication.translate("Panels", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.label_11.setText(QCoreApplication.translate("Panels", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0430\u043d\u0435\u043b\u0435\u0439 (\u0448\u0442):", None))
        self.outputCnt.setText("")
    # retranslateUi

