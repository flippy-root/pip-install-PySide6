# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(332, 189)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.rBtnPlus = QRadioButton(self.frame)
        self.rBtnPlus.setObjectName(u"rBtnPlus")

        self.verticalLayout.addWidget(self.rBtnPlus)

        self.rBtnMinus = QRadioButton(self.frame)
        self.rBtnMinus.setObjectName(u"rBtnMinus")

        self.verticalLayout.addWidget(self.rBtnMinus)

        self.rBtnMult = QRadioButton(self.frame)
        self.rBtnMult.setObjectName(u"rBtnMult")

        self.verticalLayout.addWidget(self.rBtnMult)

        self.rBtnDel = QRadioButton(self.frame)
        self.rBtnDel.setObjectName(u"rBtnDel")

        self.verticalLayout.addWidget(self.rBtnDel)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.value1 = QLineEdit(self.frame_2)
        self.value1.setObjectName(u"value1")

        self.verticalLayout_2.addWidget(self.value1)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.value2 = QLineEdit(self.frame_2)
        self.value2.setObjectName(u"value2")

        self.verticalLayout_2.addWidget(self.value2)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_4)

        self.BtnRes = QPushButton(self.frame_2)
        self.BtnRes.setObjectName(u"BtnRes")

        self.verticalLayout_2.addWidget(self.BtnRes)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440", None))
        self.rBtnPlus.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u043e\u0436\u0435\u043d\u0438\u0435", None))
        self.rBtnMinus.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0447\u0438\u0442\u0430\u043d\u0438\u0435", None))
        self.rBtnMult.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043c\u043d\u043e\u0436\u0435\u043d\u0438\u0435", None))
        self.rBtnDel.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u043b\u0435\u043d\u0438\u0435", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0432\u043e\u0435 \u0447\u0438\u0441\u043b\u043e", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0442\u043e\u0440\u043e\u0435 \u0447\u0438\u0441\u043b\u043e", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
        self.label_4.setText("")
        self.BtnRes.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
    # retranslateUi
