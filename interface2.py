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
    QMainWindow, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(655, 524)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_3.addWidget(self.textEdit)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblSymb = QLabel(self.frame)
        self.lblSymb.setObjectName(u"lblSymb")

        self.verticalLayout.addWidget(self.lblSymb)

        self.lblWord = QLabel(self.frame)
        self.lblWord.setObjectName(u"lblWord")

        self.verticalLayout.addWidget(self.lblWord)

        self.lblValue = QLabel(self.frame)
        self.lblValue.setObjectName(u"lblValue")

        self.verticalLayout.addWidget(self.lblValue)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btnCounter = QPushButton(self.frame_2)
        self.btnCounter.setObjectName(u"btnCounter")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCounter.sizePolicy().hasHeightForWidth())
        self.btnCounter.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.btnCounter)


        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout_3.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lblSymb.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043c\u0432\u043e\u043b\u043e\u0432 \u0432 \u0442\u0435\u043a\u0441\u0442\u0435:", None))
        self.lblWord.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u043e\u0432 \u0432 \u0442\u0435\u043a\u0441\u0442\u0435:", None))
        self.lblValue.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0438\u0444\u0440 \u0432 \u0442\u0435\u043a\u0441\u0442\u0435:", None))
        self.btnCounter.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
    # retranslateUi
