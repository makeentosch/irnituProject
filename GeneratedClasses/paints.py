# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'paints.ui'
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

class Ui_Paints(object):
    def setupUi(self, Paints):
        if not Paints.objectName():
            Paints.setObjectName(u"Paints")
        Paints.resize(454, 352)
        self.label_8 = QLabel(Paints)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 30, 181, 21))
        font = QFont()
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.typeCmbx = QComboBox(Paints)
        self.typeCmbx.addItem("")
        self.typeCmbx.addItem("")
        self.typeCmbx.addItem("")
        self.typeCmbx.addItem("")
        self.typeCmbx.addItem("")
        self.typeCmbx.addItem("")
        self.typeCmbx.addItem("")
        self.typeCmbx.addItem("")
        self.typeCmbx.addItem("")
        self.typeCmbx.addItem("")
        self.typeCmbx.addItem("")
        self.typeCmbx.addItem("")
        self.typeCmbx.addItem("")
        self.typeCmbx.addItem("")
        self.typeCmbx.addItem("")
        self.typeCmbx.addItem("")
        self.typeCmbx.addItem("")
        self.typeCmbx.setObjectName(u"typeCmbx")
        self.typeCmbx.setGeometry(QRect(20, 110, 231, 22))
        self.btnCalc = QPushButton(Paints)
        self.btnCalc.setObjectName(u"btnCalc")
        self.btnCalc.setGeometry(QRect(20, 160, 93, 28))
        self.label_10 = QLabel(Paints)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 210, 151, 16))
        self.outputPaintsWeight = QLabel(Paints)
        self.outputPaintsWeight.setObjectName(u"outputPaintsWeight")
        self.outputPaintsWeight.setGeometry(QRect(170, 210, 55, 16))
        self.outputPaintsWeight.setTextFormat(Qt.RichText)
        self.label = QLabel(Paints)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 80, 111, 16))

        self.retranslateUi(Paints)

        QMetaObject.connectSlotsByName(Paints)
    # setupUi

    def retranslateUi(self, Paints):
        Paints.setWindowTitle(QCoreApplication.translate("Paints", u"Dialog", None))
        self.label_8.setText(QCoreApplication.translate("Paints", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.typeCmbx.setItemText(0, QCoreApplication.translate("Paints", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.typeCmbx.setItemText(1, QCoreApplication.translate("Paints", u"\u0414\u043b\u044f \u043f\u043e\u0442\u043e\u043b\u043a\u0430", None))
        self.typeCmbx.setItemText(2, QCoreApplication.translate("Paints", u"\u041b\u0430\u0442\u0435\u043a\u0441\u043d\u0430\u044f \u043a\u0440\u0430\u0441\u043a\u0430", None))
        self.typeCmbx.setItemText(3, QCoreApplication.translate("Paints", u"\u041c\u0430\u0441\u043b\u044f\u043d\u0430\u044f \u043a\u0440\u0430\u0441\u043a\u0430", None))
        self.typeCmbx.setItemText(4, QCoreApplication.translate("Paints", u"\u0420\u0435\u0437\u0438\u043d\u043e\u0432\u0430\u044f \u043a\u0440\u0430\u0441\u043a\u0430", None))
        self.typeCmbx.setItemText(5, QCoreApplication.translate("Paints", u"\u041f\u043e\u043b\u0438\u0443\u0440\u0435\u0442\u0430\u043d\u043e\u0432\u0430\u044f \u043a\u0440\u0430\u0441\u043a\u0430", None))
        self.typeCmbx.setItemText(6, QCoreApplication.translate("Paints", u"\u041e\u0433\u043d\u0435\u0437\u0430\u0449\u0438\u0442\u043d\u0430\u044f \u043a\u0440\u0430\u0441\u043a\u0430", None))
        self.typeCmbx.setItemText(7, QCoreApplication.translate("Paints", u"\u0410\u043b\u043a\u0438\u0434\u043d\u0430\u044f \u043a\u0440\u0430\u0441\u043a\u0430", None))
        self.typeCmbx.setItemText(8, QCoreApplication.translate("Paints", u"\u0412\u043e\u0434\u043e\u044d\u043c\u0443\u043b\u044c\u0441\u0438\u043e\u043d\u043d\u0430\u044f \u043a\u0440\u0430\u0441\u043a\u0430", None))
        self.typeCmbx.setItemText(9, QCoreApplication.translate("Paints", u"\u0421\u0438\u043b\u0438\u043a\u0430\u0442\u043d\u0430\u044f \u043a\u0440\u0430\u0441\u043a\u0430", None))
        self.typeCmbx.setItemText(10, QCoreApplication.translate("Paints", u"\u041f\u043e \u0448\u0442\u0443\u043a\u0430\u0442\u0443\u0440\u043a\u0435", None))
        self.typeCmbx.setItemText(11, QCoreApplication.translate("Paints", u"\u041f\u043e \u0448\u043f\u0430\u043a\u043b\u0435\u0432\u043a\u0435", None))
        self.typeCmbx.setItemText(12, QCoreApplication.translate("Paints", u"\u041f\u043e \u043a\u043e\u0440\u043e\u0435\u0434\u0443", None))
        self.typeCmbx.setItemText(13, QCoreApplication.translate("Paints", u"\u041f\u043e \u0440\u0436\u0430\u0432\u0447\u0438\u043d\u0435", None))
        self.typeCmbx.setItemText(14, QCoreApplication.translate("Paints", u"\u041f\u043e \u0434\u0435\u0440\u0435\u0432\u0443", None))
        self.typeCmbx.setItemText(15, QCoreApplication.translate("Paints", u"\u041f\u043e \u0431\u0435\u0442\u043e\u043d\u0443", None))
        self.typeCmbx.setItemText(16, QCoreApplication.translate("Paints", u"\u041f\u043e \u043c\u0435\u0442\u0430\u043b\u043b\u0443", None))

        self.btnCalc.setText(QCoreApplication.translate("Paints", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.label_10.setText(QCoreApplication.translate("Paints", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043a\u0440\u0430\u0441\u043a\u0438 (\u0433):", None))
        self.outputPaintsWeight.setText("")
        self.label.setText(QCoreApplication.translate("Paints", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u0440\u0430\u0441\u043a\u0438", None))
    # retranslateUi

