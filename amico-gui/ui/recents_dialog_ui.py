# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recents_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QGroupBox,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QWidget)

class Ui_dialog(object):
    def setupUi(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"dialog")
        dialog.resize(400, 300)
        dialog.setModal(False)
        self.gridLayout_2 = QGridLayout(dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.listWidgetRecents = QListWidget(dialog)
        self.listWidgetRecents.setObjectName(u"listWidgetRecents")

        self.gridLayout_2.addWidget(self.listWidgetRecents, 0, 0, 1, 1)

        self.groupBoxButtons = QGroupBox(dialog)
        self.groupBoxButtons.setObjectName(u"groupBoxButtons")
        self.groupBoxButtons.setStyleSheet(u"QGroupBox\n"
"{\n"
"	border: 0;\n"
"}")
        self.gridLayout = QGridLayout(self.groupBoxButtons)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButtonLoad = QPushButton(self.groupBoxButtons)
        self.pushButtonLoad.setObjectName(u"pushButtonLoad")
        self.pushButtonLoad.setMinimumSize(QSize(100, 30))
        self.pushButtonLoad.setMaximumSize(QSize(100, 30))
        self.pushButtonLoad.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButtonLoad, 0, 0, 1, 1)

        self.pushButtonClose = QPushButton(self.groupBoxButtons)
        self.pushButtonClose.setObjectName(u"pushButtonClose")
        self.pushButtonClose.setMinimumSize(QSize(100, 30))
        self.pushButtonClose.setMaximumSize(QSize(100, 30))
        self.pushButtonClose.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButtonClose, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBoxButtons, 1, 0, 1, 1, Qt.AlignRight|Qt.AlignBottom)

        QWidget.setTabOrder(self.listWidgetRecents, self.pushButtonLoad)
        QWidget.setTabOrder(self.pushButtonLoad, self.pushButtonClose)

        self.retranslateUi(dialog)

        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(QCoreApplication.translate("dialog", u"Recent data", None))
        self.pushButtonLoad.setText(QCoreApplication.translate("dialog", u"Load", None))
        self.pushButtonClose.setText(QCoreApplication.translate("dialog", u"New", None))
    # retranslateUi

