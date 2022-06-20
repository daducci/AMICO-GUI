# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preview_window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QWidget)

from pyqtgraph import ImageView

class Ui_window(object):
    def setupUi(self, window):
        if not window.objectName():
            window.setObjectName(u"window")
        window.resize(1186, 709)
        self.widget = QWidget(window)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBoxImagePreview = QGroupBox(self.widget)
        self.groupBoxImagePreview.setObjectName(u"groupBoxImagePreview")
        self.groupBoxImagePreview.setStyleSheet(u"QGroupBox\n"
"{\n"
"	border: 0;\n"
"}")
        self.gridLayout_19 = QGridLayout(self.groupBoxImagePreview)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.groupBoxPreviewButtons = QGroupBox(self.groupBoxImagePreview)
        self.groupBoxPreviewButtons.setObjectName(u"groupBoxPreviewButtons")
        self.gridLayout_11 = QGridLayout(self.groupBoxPreviewButtons)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.pushButtonView2 = QPushButton(self.groupBoxPreviewButtons)
        self.pushButtonView2.setObjectName(u"pushButtonView2")
        self.pushButtonView2.setMinimumSize(QSize(200, 60))
        self.pushButtonView2.setMaximumSize(QSize(200, 60))
        self.pushButtonView2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_11.addWidget(self.pushButtonView2, 0, 2, 1, 1)

        self.pushButtonView1 = QPushButton(self.groupBoxPreviewButtons)
        self.pushButtonView1.setObjectName(u"pushButtonView1")
        self.pushButtonView1.setMinimumSize(QSize(200, 60))
        self.pushButtonView1.setMaximumSize(QSize(200, 60))
        self.pushButtonView1.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_11.addWidget(self.pushButtonView1, 0, 1, 1, 1)

        self.pushButtonView3 = QPushButton(self.groupBoxPreviewButtons)
        self.pushButtonView3.setObjectName(u"pushButtonView3")
        self.pushButtonView3.setMinimumSize(QSize(200, 60))
        self.pushButtonView3.setMaximumSize(QSize(200, 60))
        self.pushButtonView3.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_11.addWidget(self.pushButtonView3, 0, 0, 1, 1)


        self.gridLayout_19.addWidget(self.groupBoxPreviewButtons, 3, 0, 1, 1, Qt.AlignHCenter|Qt.AlignBottom)

        self.graphicsView = ImageView(self.groupBoxImagePreview)
        self.graphicsView.setObjectName(u"graphicsView")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setMinimumSize(QSize(0, 0))
        self.graphicsView.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_19.addWidget(self.graphicsView, 1, 0, 1, 1)

        self.horizontalSlider = QSlider(self.groupBoxImagePreview)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_19.addWidget(self.horizontalSlider, 2, 0, 1, 1, Qt.AlignBottom)

        self.comboBoxImagePreview = QComboBox(self.groupBoxImagePreview)
        self.comboBoxImagePreview.setObjectName(u"comboBoxImagePreview")
        self.comboBoxImagePreview.setMinimumSize(QSize(300, 40))
        self.comboBoxImagePreview.setMaximumSize(QSize(300, 40))

        self.gridLayout_19.addWidget(self.comboBoxImagePreview, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignTop)


        self.gridLayout.addWidget(self.groupBoxImagePreview, 0, 0, 1, 1)

        window.setCentralWidget(self.widget)
        QWidget.setTabOrder(self.comboBoxImagePreview, self.graphicsView)
        QWidget.setTabOrder(self.graphicsView, self.horizontalSlider)
        QWidget.setTabOrder(self.horizontalSlider, self.pushButtonView1)
        QWidget.setTabOrder(self.pushButtonView1, self.pushButtonView2)

        self.retranslateUi(window)

        QMetaObject.connectSlotsByName(window)
    # setupUi

    def retranslateUi(self, window):
        window.setWindowTitle(QCoreApplication.translate("window", u"Inspect results", None))
        self.groupBoxImagePreview.setTitle("")
        self.pushButtonView2.setText(QCoreApplication.translate("window", u"Coronal", None))
        self.pushButtonView1.setText(QCoreApplication.translate("window", u"Sagittal", None))
        self.pushButtonView3.setText(QCoreApplication.translate("window", u"Axial", None))
    # retranslateUi

