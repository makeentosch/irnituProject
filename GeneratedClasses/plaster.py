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
    QLineEdit, QSizePolicy, QWidget)

class Ui_Plaster(object):
    def setupUi(self, Plaster):
        if not Plaster.objectName():
            Plaster.setObjectName(u"Plaster")
        Plaster.resize(458, 347)
        self.label_9 = QLabel(Plaster)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 30, 181, 21))
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
        self.label_3.setGeometry(QRect(20, 150, 101, 16))
        self.label_4 = QLabel(Plaster)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 230, 201, 16))
        self.outputSquare = QLabel(Plaster)
        self.outputSquare.setObjectName(u"outputSquare")
        self.outputSquare.setGeometry(QRect(220, 230, 55, 16))
        self.outputSquare.setTextFormat(Qt.RichText)
        self.inputLayerWidth = QLineEdit(Plaster)
        self.inputLayerWidth.setObjectName(u"inputLayerWidth")
        self.inputLayerWidth.setGeometry(QRect(20, 180, 61, 21))
        self.label_5 = QLabel(Plaster)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 260, 151, 16))
        self.outputPlasterCount = QLabel(Plaster)
        self.outputPlasterCount.setObjectName(u"outputPlasterCount")
        self.outputPlasterCount.setGeometry(QRect(180, 260, 55, 16))
        self.outputPlasterCount.setTextFormat(Qt.RichText)

        self.retranslateUi(Plaster)

        QMetaObject.connectSlotsByName(Plaster)
    # setupUi

    def retranslateUi(self, Plaster):
        Plaster.setWindowTitle(QCoreApplication.translate("Plaster", u"Dialog", None))
        self.label_9.setText(QCoreApplication.translate("Plaster", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.label_2.setText(QCoreApplication.translate("Plaster", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0448\u0442\u0443\u043a\u0430\u0442\u0443\u0440\u043a\u0438", None))
        self.typeCmbx.setItemText(0, QCoreApplication.translate("Plaster", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.typeCmbx.setItemText(1, QCoreApplication.translate("Plaster", u"\u0413\u0438\u043f\u0441\u043e\u0432\u0430\u044f", None))
        self.typeCmbx.setItemText(2, QCoreApplication.translate("Plaster", u"\u0426\u0435\u043c\u0435\u043d\u0442\u043d\u0430\u044f", None))

        self.label_3.setText(QCoreApplication.translate("Plaster", u"\u0422\u043e\u043b\u0449\u0438\u043d\u0430 \u0441\u043b\u043e\u044f", None))
        self.label_4.setText(QCoreApplication.translate("Plaster", u"\u041f\u043b\u043e\u0449\u0430\u0434\u044c \u0440\u0430\u0431\u043e\u0447\u0435\u0439 \u043f\u043e\u0432\u0435\u0440\u0445\u043d\u043e\u0441\u0442\u0438:", None))
        self.outputSquare.setText("")
        self.label_5.setText(QCoreApplication.translate("Plaster", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0448\u0442\u0443\u043a\u0430\u0442\u0443\u0440\u043a\u0438:", None))
        self.outputPlasterCount.setText("")
    # retranslateUi

