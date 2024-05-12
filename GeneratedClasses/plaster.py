# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plaster.ui'
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

class Ui_Plaster(object):
    def setupUi(self, Plaster):
        if not Plaster.objectName():
            Plaster.setObjectName(u"Plaster")
        Plaster.resize(458, 334)
        self.label_9 = QLabel(Plaster)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 30, 351, 31))
        font = QFont()
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_2 = QLabel(Plaster)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 70, 141, 16))
        self.typeCmbx = QComboBox(Plaster)
        self.typeCmbx.addItem("")
        self.typeCmbx.addItem("")
        self.typeCmbx.addItem("")
        self.typeCmbx.setObjectName(u"typeCmbx")
        self.typeCmbx.setGeometry(QRect(20, 100, 231, 22))
        self.label_3 = QLabel(Plaster)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 150, 121, 16))
        self.inputLayerWidth = QLineEdit(Plaster)
        self.inputLayerWidth.setObjectName(u"inputLayerWidth")
        self.inputLayerWidth.setGeometry(QRect(20, 180, 61, 21))
        self.label_5 = QLabel(Plaster)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 270, 171, 16))
        self.outputPlasterCount = QLabel(Plaster)
        self.outputPlasterCount.setObjectName(u"outputPlasterCount")
        self.outputPlasterCount.setGeometry(QRect(190, 270, 101, 16))
        self.outputPlasterCount.setTextFormat(Qt.RichText)
        self.btnCalc = QPushButton(Plaster)
        self.btnCalc.setObjectName(u"btnCalc")
        self.btnCalc.setGeometry(QRect(20, 220, 93, 28))

        self.retranslateUi(Plaster)

        QMetaObject.connectSlotsByName(Plaster)
    # setupUi

    def retranslateUi(self, Plaster):
        Plaster.setWindowTitle(QCoreApplication.translate("Plaster", u"Dialog", None))
        self.label_9.setText(QCoreApplication.translate("Plaster", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0448\u0442\u0443\u043a\u0430\u0442\u0443\u0440\u043a\u0438", None))
        self.label_2.setText(QCoreApplication.translate("Plaster", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0448\u0442\u0443\u043a\u0430\u0442\u0443\u0440\u043a\u0438", None))
        self.typeCmbx.setItemText(0, QCoreApplication.translate("Plaster", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.typeCmbx.setItemText(1, QCoreApplication.translate("Plaster", u"\u0413\u0438\u043f\u0441\u043e\u0432\u0430\u044f", None))
        self.typeCmbx.setItemText(2, QCoreApplication.translate("Plaster", u"\u0426\u0435\u043c\u0435\u043d\u0442\u043d\u0430\u044f", None))

        self.label_3.setText(QCoreApplication.translate("Plaster", u"\u0422\u043e\u043b\u0449\u0438\u043d\u0430 \u0441\u043b\u043e\u044f (\u043c\u043c)", None))
        self.label_5.setText(QCoreApplication.translate("Plaster", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0448\u0442\u0443\u043a\u0430\u0442\u0443\u0440\u043a\u0438 (\u0433):", None))
        self.outputPlasterCount.setText("")
        self.btnCalc.setText(QCoreApplication.translate("Plaster", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
    # retranslateUi

