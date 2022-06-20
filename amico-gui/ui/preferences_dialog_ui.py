# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preferences_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTabWidget, QWidget)

class Ui_dialog(object):
    def setupUi(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"dialog")
        dialog.resize(400, 300)
        dialog.setStyleSheet(u"QGroupBox\n"
"{\n"
"	border: 0;\n"
"}")
        self.gridLayout_2 = QGridLayout(dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabSetup = QWidget()
        self.tabSetup.setObjectName(u"tabSetup")
        self.gridLayout_5 = QGridLayout(self.tabSetup)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupBoxSetup = QGroupBox(self.tabSetup)
        self.groupBoxSetup.setObjectName(u"groupBoxSetup")
        self.groupBoxSetup.setStyleSheet(u"QGroupBox\n"
"{\n"
"	border: 0;\n"
"}")
        self.gridLayout_3 = QGridLayout(self.groupBoxSetup)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.labelLmax = QLabel(self.groupBoxSetup)
        self.labelLmax.setObjectName(u"labelLmax")

        self.gridLayout_3.addWidget(self.labelLmax, 1, 0, 1, 1)

        self.labelNdirs = QLabel(self.groupBoxSetup)
        self.labelNdirs.setObjectName(u"labelNdirs")

        self.gridLayout_3.addWidget(self.labelNdirs, 0, 0, 1, 1)

        self.comboBoxNdirs = QComboBox(self.groupBoxSetup)
        self.comboBoxNdirs.setObjectName(u"comboBoxNdirs")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxNdirs.sizePolicy().hasHeightForWidth())
        self.comboBoxNdirs.setSizePolicy(sizePolicy)
        self.comboBoxNdirs.setMinimumSize(QSize(150, 40))
        self.comboBoxNdirs.setMaximumSize(QSize(150, 40))

        self.gridLayout_3.addWidget(self.comboBoxNdirs, 0, 1, 1, 1)

        self.lineEditLmax = QLineEdit(self.groupBoxSetup)
        self.lineEditLmax.setObjectName(u"lineEditLmax")
        self.lineEditLmax.setMinimumSize(QSize(80, 30))
        self.lineEditLmax.setMaximumSize(QSize(80, 30))

        self.gridLayout_3.addWidget(self.lineEditLmax, 1, 1, 1, 1)


        self.gridLayout_5.addWidget(self.groupBoxSetup, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.tabWidget.addTab(self.tabSetup, "")
        self.tabGlobal = QWidget()
        self.tabGlobal.setObjectName(u"tabGlobal")
        self.gridLayout_6 = QGridLayout(self.tabGlobal)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.groupBoxGlobal = QGroupBox(self.tabGlobal)
        self.groupBoxGlobal.setObjectName(u"groupBoxGlobal")
        self.groupBoxGlobal.setStyleSheet(u"QGroupBox\n"
"{\n"
"	border: 0;\n"
"}")
        self.gridLayout_4 = QGridLayout(self.groupBoxGlobal)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.labelJoblibBacked = QLabel(self.groupBoxGlobal)
        self.labelJoblibBacked.setObjectName(u"labelJoblibBacked")

        self.gridLayout_4.addWidget(self.labelJoblibBacked, 1, 0, 1, 1)

        self.comboBoxJoblibBackend = QComboBox(self.groupBoxGlobal)
        self.comboBoxJoblibBackend.setObjectName(u"comboBoxJoblibBackend")
        self.comboBoxJoblibBackend.setMinimumSize(QSize(150, 40))
        self.comboBoxJoblibBackend.setMaximumSize(QSize(150, 40))

        self.gridLayout_4.addWidget(self.comboBoxJoblibBackend, 1, 1, 1, 1)

        self.comboBoxOpenBLAS = QComboBox(self.groupBoxGlobal)
        self.comboBoxOpenBLAS.setObjectName(u"comboBoxOpenBLAS")
        self.comboBoxOpenBLAS.setMinimumSize(QSize(80, 40))
        self.comboBoxOpenBLAS.setMaximumSize(QSize(80, 40))

        self.gridLayout_4.addWidget(self.comboBoxOpenBLAS, 0, 1, 1, 1)

        self.labelOpenBLAS = QLabel(self.groupBoxGlobal)
        self.labelOpenBLAS.setObjectName(u"labelOpenBLAS")

        self.gridLayout_4.addWidget(self.labelOpenBLAS, 0, 0, 1, 1)

        self.labelJoblibNumThreads = QLabel(self.groupBoxGlobal)
        self.labelJoblibNumThreads.setObjectName(u"labelJoblibNumThreads")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelJoblibNumThreads.sizePolicy().hasHeightForWidth())
        self.labelJoblibNumThreads.setSizePolicy(sizePolicy1)

        self.gridLayout_4.addWidget(self.labelJoblibNumThreads, 2, 0, 1, 1)

        self.comboBoxJoblibNumThreads = QComboBox(self.groupBoxGlobal)
        self.comboBoxJoblibNumThreads.setObjectName(u"comboBoxJoblibNumThreads")
        sizePolicy1.setHeightForWidth(self.comboBoxJoblibNumThreads.sizePolicy().hasHeightForWidth())
        self.comboBoxJoblibNumThreads.setSizePolicy(sizePolicy1)
        self.comboBoxJoblibNumThreads.setMinimumSize(QSize(80, 40))
        self.comboBoxJoblibNumThreads.setMaximumSize(QSize(80, 40))

        self.gridLayout_4.addWidget(self.comboBoxJoblibNumThreads, 2, 1, 1, 1)


        self.gridLayout_6.addWidget(self.groupBoxGlobal, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.tabWidget.addTab(self.tabGlobal, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.groupBoxButtons = QGroupBox(dialog)
        self.groupBoxButtons.setObjectName(u"groupBoxButtons")
        self.gridLayout = QGridLayout(self.groupBoxButtons)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButtonConfirm = QPushButton(self.groupBoxButtons)
        self.pushButtonConfirm.setObjectName(u"pushButtonConfirm")
        self.pushButtonConfirm.setMinimumSize(QSize(100, 30))
        self.pushButtonConfirm.setMaximumSize(QSize(100, 30))
        self.pushButtonConfirm.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButtonConfirm, 0, 0, 1, 1)

        self.pushButtonCancel = QPushButton(self.groupBoxButtons)
        self.pushButtonCancel.setObjectName(u"pushButtonCancel")
        self.pushButtonCancel.setMinimumSize(QSize(100, 30))
        self.pushButtonCancel.setMaximumSize(QSize(100, 30))
        self.pushButtonCancel.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButtonCancel, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBoxButtons, 1, 0, 1, 1, Qt.AlignRight|Qt.AlignBottom)

        QWidget.setTabOrder(self.tabWidget, self.comboBoxNdirs)
        QWidget.setTabOrder(self.comboBoxNdirs, self.lineEditLmax)
        QWidget.setTabOrder(self.lineEditLmax, self.comboBoxOpenBLAS)
        QWidget.setTabOrder(self.comboBoxOpenBLAS, self.comboBoxJoblibBackend)
        QWidget.setTabOrder(self.comboBoxJoblibBackend, self.comboBoxJoblibNumThreads)
        QWidget.setTabOrder(self.comboBoxJoblibNumThreads, self.pushButtonConfirm)
        QWidget.setTabOrder(self.pushButtonConfirm, self.pushButtonCancel)

        self.retranslateUi(dialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(QCoreApplication.translate("dialog", u"Settings", None))
        self.groupBoxSetup.setTitle("")
        self.labelLmax.setText(QCoreApplication.translate("dialog", u"lmax", None))
        self.labelNdirs.setText(QCoreApplication.translate("dialog", u"ndirs", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSetup), QCoreApplication.translate("dialog", u"Response functions", None))
        self.groupBoxGlobal.setTitle("")
        self.labelJoblibBacked.setText(QCoreApplication.translate("dialog", u"joblib backend", None))
        self.labelOpenBLAS.setText(QCoreApplication.translate("dialog", u"OpenBLAS n threads", None))
        self.labelJoblibNumThreads.setText(QCoreApplication.translate("dialog", u"joblib threads", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGlobal), QCoreApplication.translate("dialog", u"Parallel execution", None))
        self.pushButtonConfirm.setText(QCoreApplication.translate("dialog", u"Ok", None))
        self.pushButtonCancel.setText(QCoreApplication.translate("dialog", u"Cancel", None))
    # retranslateUi

