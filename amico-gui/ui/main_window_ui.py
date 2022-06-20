# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QProgressBar,
    QPushButton, QRadioButton, QSizePolicy, QSlider,
    QWidget)

from line_edits import (DirectoryLineEdit, FileLineEdit)
from pyqtgraph import ImageView

class Ui_window(object):
    def setupUi(self, window):
        if not window.objectName():
            window.setObjectName(u"window")
        window.resize(1500, 870)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(window.sizePolicy().hasHeightForWidth())
        window.setSizePolicy(sizePolicy)
        self.action_new_study = QAction(window)
        self.action_new_study.setObjectName(u"action_new_study")
        self.action_exit = QAction(window)
        self.action_exit.setObjectName(u"action_exit")
        self.action_preferences = QAction(window)
        self.action_preferences.setObjectName(u"action_preferences")
        self.widget = QWidget(window)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBoxModelSelection = QGroupBox(self.widget)
        self.groupBoxModelSelection.setObjectName(u"groupBoxModelSelection")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBoxModelSelection.sizePolicy().hasHeightForWidth())
        self.groupBoxModelSelection.setSizePolicy(sizePolicy1)
        self.groupBoxModelSelection.setStyleSheet(u"")
        self.gridLayout_20 = QGridLayout(self.groupBoxModelSelection)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.groupBoxModel = QGroupBox(self.groupBoxModelSelection)
        self.groupBoxModel.setObjectName(u"groupBoxModel")
        self.groupBoxModel.setStyleSheet(u"QGroupBox\n"
"{\n"
"	border: 0;\n"
"}")
        self.gridLayout_4 = QGridLayout(self.groupBoxModel)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.labelModel = QLabel(self.groupBoxModel)
        self.labelModel.setObjectName(u"labelModel")
        sizePolicy.setHeightForWidth(self.labelModel.sizePolicy().hasHeightForWidth())
        self.labelModel.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.labelModel, 0, 0, 1, 1)

        self.comboBoxModel = QComboBox(self.groupBoxModel)
        self.comboBoxModel.setObjectName(u"comboBoxModel")
        sizePolicy.setHeightForWidth(self.comboBoxModel.sizePolicy().hasHeightForWidth())
        self.comboBoxModel.setSizePolicy(sizePolicy)
        self.comboBoxModel.setMinimumSize(QSize(150, 40))
        self.comboBoxModel.setMaximumSize(QSize(150, 40))

        self.gridLayout_4.addWidget(self.comboBoxModel, 0, 1, 1, 1)


        self.gridLayout_20.addWidget(self.groupBoxModel, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)


        self.gridLayout.addWidget(self.groupBoxModelSelection, 0, 0, 1, 3, Qt.AlignLeft|Qt.AlignTop)

        self.groupBoxData = QGroupBox(self.widget)
        self.groupBoxData.setObjectName(u"groupBoxData")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBoxData.sizePolicy().hasHeightForWidth())
        self.groupBoxData.setSizePolicy(sizePolicy2)
        self.groupBoxData.setStyleSheet(u"")
        self.groupBoxData.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_21 = QGridLayout(self.groupBoxData)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.pushButtonLoadData = QPushButton(self.groupBoxData)
        self.pushButtonLoadData.setObjectName(u"pushButtonLoadData")
        sizePolicy.setHeightForWidth(self.pushButtonLoadData.sizePolicy().hasHeightForWidth())
        self.pushButtonLoadData.setSizePolicy(sizePolicy)
        self.pushButtonLoadData.setMinimumSize(QSize(150, 50))
        self.pushButtonLoadData.setMaximumSize(QSize(150, 50))
        self.pushButtonLoadData.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButtonLoadData.setStyleSheet(u"")
        self.pushButtonLoadData.setAutoDefault(False)
        self.pushButtonLoadData.setFlat(False)

        self.gridLayout_21.addWidget(self.pushButtonLoadData, 2, 0, 1, 1, Qt.AlignHCenter)

        self.groupBoxFiles = QGroupBox(self.groupBoxData)
        self.groupBoxFiles.setObjectName(u"groupBoxFiles")
        sizePolicy.setHeightForWidth(self.groupBoxFiles.sizePolicy().hasHeightForWidth())
        self.groupBoxFiles.setSizePolicy(sizePolicy)
        self.groupBoxFiles.setStyleSheet(u"QGroupBox\n"
"{\n"
"	border: 0;\n"
"}")
        self.gridLayout_2 = QGridLayout(self.groupBoxFiles)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButtonDWI = QPushButton(self.groupBoxFiles)
        self.pushButtonDWI.setObjectName(u"pushButtonDWI")
        sizePolicy.setHeightForWidth(self.pushButtonDWI.sizePolicy().hasHeightForWidth())
        self.pushButtonDWI.setSizePolicy(sizePolicy)
        self.pushButtonDWI.setMinimumSize(QSize(80, 30))
        self.pushButtonDWI.setMaximumSize(QSize(80, 30))

        self.gridLayout_2.addWidget(self.pushButtonDWI, 2, 2, 1, 1)

        self.lineEditMask = FileLineEdit(self.groupBoxFiles)
        self.lineEditMask.setObjectName(u"lineEditMask")
        sizePolicy.setHeightForWidth(self.lineEditMask.sizePolicy().hasHeightForWidth())
        self.lineEditMask.setSizePolicy(sizePolicy)
        self.lineEditMask.setMinimumSize(QSize(200, 30))
        self.lineEditMask.setMaximumSize(QSize(200, 30))
        self.lineEditMask.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.lineEditMask, 3, 1, 1, 1)

        self.pushButtonMask = QPushButton(self.groupBoxFiles)
        self.pushButtonMask.setObjectName(u"pushButtonMask")
        sizePolicy.setHeightForWidth(self.pushButtonMask.sizePolicy().hasHeightForWidth())
        self.pushButtonMask.setSizePolicy(sizePolicy)
        self.pushButtonMask.setMinimumSize(QSize(80, 30))
        self.pushButtonMask.setMaximumSize(QSize(80, 30))

        self.gridLayout_2.addWidget(self.pushButtonMask, 3, 2, 1, 1)

        self.lineEditDWI = FileLineEdit(self.groupBoxFiles)
        self.lineEditDWI.setObjectName(u"lineEditDWI")
        sizePolicy.setHeightForWidth(self.lineEditDWI.sizePolicy().hasHeightForWidth())
        self.lineEditDWI.setSizePolicy(sizePolicy)
        self.lineEditDWI.setMinimumSize(QSize(200, 30))
        self.lineEditDWI.setMaximumSize(QSize(200, 30))

        self.gridLayout_2.addWidget(self.lineEditDWI, 2, 1, 1, 1)

        self.labelStudy = QLabel(self.groupBoxFiles)
        self.labelStudy.setObjectName(u"labelStudy")
        sizePolicy.setHeightForWidth(self.labelStudy.sizePolicy().hasHeightForWidth())
        self.labelStudy.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.labelStudy, 0, 0, 1, 1)

        self.labelSubject = QLabel(self.groupBoxFiles)
        self.labelSubject.setObjectName(u"labelSubject")
        sizePolicy.setHeightForWidth(self.labelSubject.sizePolicy().hasHeightForWidth())
        self.labelSubject.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.labelSubject, 1, 0, 1, 1)

        self.lineEditSubject = DirectoryLineEdit(self.groupBoxFiles)
        self.lineEditSubject.setObjectName(u"lineEditSubject")
        sizePolicy.setHeightForWidth(self.lineEditSubject.sizePolicy().hasHeightForWidth())
        self.lineEditSubject.setSizePolicy(sizePolicy)
        self.lineEditSubject.setMinimumSize(QSize(200, 30))
        self.lineEditSubject.setMaximumSize(QSize(200, 30))

        self.gridLayout_2.addWidget(self.lineEditSubject, 1, 1, 1, 1)

        self.labelDWI = QLabel(self.groupBoxFiles)
        self.labelDWI.setObjectName(u"labelDWI")
        sizePolicy.setHeightForWidth(self.labelDWI.sizePolicy().hasHeightForWidth())
        self.labelDWI.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.labelDWI, 2, 0, 1, 1)

        self.pushButtonStudy = QPushButton(self.groupBoxFiles)
        self.pushButtonStudy.setObjectName(u"pushButtonStudy")
        sizePolicy.setHeightForWidth(self.pushButtonStudy.sizePolicy().hasHeightForWidth())
        self.pushButtonStudy.setSizePolicy(sizePolicy)
        self.pushButtonStudy.setMinimumSize(QSize(80, 30))
        self.pushButtonStudy.setMaximumSize(QSize(80, 30))

        self.gridLayout_2.addWidget(self.pushButtonStudy, 0, 2, 1, 1)

        self.pushButtonSubject = QPushButton(self.groupBoxFiles)
        self.pushButtonSubject.setObjectName(u"pushButtonSubject")
        sizePolicy.setHeightForWidth(self.pushButtonSubject.sizePolicy().hasHeightForWidth())
        self.pushButtonSubject.setSizePolicy(sizePolicy)
        self.pushButtonSubject.setMinimumSize(QSize(80, 30))
        self.pushButtonSubject.setMaximumSize(QSize(80, 30))

        self.gridLayout_2.addWidget(self.pushButtonSubject, 1, 2, 1, 1)

        self.labelMask = QLabel(self.groupBoxFiles)
        self.labelMask.setObjectName(u"labelMask")
        sizePolicy.setHeightForWidth(self.labelMask.sizePolicy().hasHeightForWidth())
        self.labelMask.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.labelMask, 3, 0, 1, 1)

        self.lineEditStudy = DirectoryLineEdit(self.groupBoxFiles)
        self.lineEditStudy.setObjectName(u"lineEditStudy")
        sizePolicy.setHeightForWidth(self.lineEditStudy.sizePolicy().hasHeightForWidth())
        self.lineEditStudy.setSizePolicy(sizePolicy)
        self.lineEditStudy.setMinimumSize(QSize(200, 30))
        self.lineEditStudy.setMaximumSize(QSize(200, 30))

        self.gridLayout_2.addWidget(self.lineEditStudy, 0, 1, 1, 1)


        self.gridLayout_21.addWidget(self.groupBoxFiles, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.groupBoxSchemefile = QGroupBox(self.groupBoxData)
        self.groupBoxSchemefile.setObjectName(u"groupBoxSchemefile")
        sizePolicy.setHeightForWidth(self.groupBoxSchemefile.sizePolicy().hasHeightForWidth())
        self.groupBoxSchemefile.setSizePolicy(sizePolicy)
        self.groupBoxSchemefile.setFlat(True)
        self.gridLayout_17 = QGridLayout(self.groupBoxSchemefile)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.radioButtonGenerateSchemefile = QRadioButton(self.groupBoxSchemefile)
        self.radioButtonGenerateSchemefile.setObjectName(u"radioButtonGenerateSchemefile")
        sizePolicy.setHeightForWidth(self.radioButtonGenerateSchemefile.sizePolicy().hasHeightForWidth())
        self.radioButtonGenerateSchemefile.setSizePolicy(sizePolicy)

        self.gridLayout_17.addWidget(self.radioButtonGenerateSchemefile, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.groupBoxGenerateSchemefile = QGroupBox(self.groupBoxSchemefile)
        self.groupBoxGenerateSchemefile.setObjectName(u"groupBoxGenerateSchemefile")
        self.groupBoxGenerateSchemefile.setStyleSheet(u"QGroupBox\n"
"{\n"
"	border: 0;\n"
"}")
        self.gridLayout_3 = QGridLayout(self.groupBoxGenerateSchemefile)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.labelBvals = QLabel(self.groupBoxGenerateSchemefile)
        self.labelBvals.setObjectName(u"labelBvals")
        sizePolicy.setHeightForWidth(self.labelBvals.sizePolicy().hasHeightForWidth())
        self.labelBvals.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.labelBvals, 0, 0, 1, 1)

        self.lineEditBvals = FileLineEdit(self.groupBoxGenerateSchemefile)
        self.lineEditBvals.setObjectName(u"lineEditBvals")
        sizePolicy.setHeightForWidth(self.lineEditBvals.sizePolicy().hasHeightForWidth())
        self.lineEditBvals.setSizePolicy(sizePolicy)
        self.lineEditBvals.setMinimumSize(QSize(200, 30))
        self.lineEditBvals.setMaximumSize(QSize(200, 30))

        self.gridLayout_3.addWidget(self.lineEditBvals, 0, 1, 1, 2)

        self.pushButtonBvals = QPushButton(self.groupBoxGenerateSchemefile)
        self.pushButtonBvals.setObjectName(u"pushButtonBvals")
        sizePolicy.setHeightForWidth(self.pushButtonBvals.sizePolicy().hasHeightForWidth())
        self.pushButtonBvals.setSizePolicy(sizePolicy)
        self.pushButtonBvals.setMinimumSize(QSize(80, 30))
        self.pushButtonBvals.setMaximumSize(QSize(80, 30))

        self.gridLayout_3.addWidget(self.pushButtonBvals, 0, 3, 1, 1)

        self.labelBvecs = QLabel(self.groupBoxGenerateSchemefile)
        self.labelBvecs.setObjectName(u"labelBvecs")
        sizePolicy.setHeightForWidth(self.labelBvecs.sizePolicy().hasHeightForWidth())
        self.labelBvecs.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.labelBvecs, 1, 0, 1, 1)

        self.lineEditBvecs = FileLineEdit(self.groupBoxGenerateSchemefile)
        self.lineEditBvecs.setObjectName(u"lineEditBvecs")
        sizePolicy.setHeightForWidth(self.lineEditBvecs.sizePolicy().hasHeightForWidth())
        self.lineEditBvecs.setSizePolicy(sizePolicy)
        self.lineEditBvecs.setMinimumSize(QSize(200, 30))
        self.lineEditBvecs.setMaximumSize(QSize(200, 30))

        self.gridLayout_3.addWidget(self.lineEditBvecs, 1, 1, 1, 2)

        self.pushButtonBvecs = QPushButton(self.groupBoxGenerateSchemefile)
        self.pushButtonBvecs.setObjectName(u"pushButtonBvecs")
        sizePolicy.setHeightForWidth(self.pushButtonBvecs.sizePolicy().hasHeightForWidth())
        self.pushButtonBvecs.setSizePolicy(sizePolicy)
        self.pushButtonBvecs.setMinimumSize(QSize(80, 30))
        self.pushButtonBvecs.setMaximumSize(QSize(80, 30))

        self.gridLayout_3.addWidget(self.pushButtonBvecs, 1, 3, 1, 1)

        self.labelBStep = QLabel(self.groupBoxGenerateSchemefile)
        self.labelBStep.setObjectName(u"labelBStep")
        sizePolicy.setHeightForWidth(self.labelBStep.sizePolicy().hasHeightForWidth())
        self.labelBStep.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.labelBStep, 2, 0, 1, 1)

        self.lineEditBStep = QLineEdit(self.groupBoxGenerateSchemefile)
        self.lineEditBStep.setObjectName(u"lineEditBStep")
        sizePolicy.setHeightForWidth(self.lineEditBStep.sizePolicy().hasHeightForWidth())
        self.lineEditBStep.setSizePolicy(sizePolicy)
        self.lineEditBStep.setMinimumSize(QSize(80, 30))
        self.lineEditBStep.setMaximumSize(QSize(80, 30))

        self.gridLayout_3.addWidget(self.lineEditBStep, 2, 1, 1, 1)

        self.labelBStepUnit = QLabel(self.groupBoxGenerateSchemefile)
        self.labelBStepUnit.setObjectName(u"labelBStepUnit")
        self.labelBStepUnit.setEnabled(False)
        sizePolicy.setHeightForWidth(self.labelBStepUnit.sizePolicy().hasHeightForWidth())
        self.labelBStepUnit.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.labelBStepUnit, 2, 2, 1, 2)


        self.gridLayout_17.addWidget(self.groupBoxGenerateSchemefile, 1, 0, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.groupBoxGenerateSchemefileSANDI = QGroupBox(self.groupBoxSchemefile)
        self.groupBoxGenerateSchemefileSANDI.setObjectName(u"groupBoxGenerateSchemefileSANDI")
        self.groupBoxGenerateSchemefileSANDI.setStyleSheet(u"QGroupBox\n"
"{\n"
"	border: 0;\n"
"}")
        self.gridLayout_10 = QGridLayout(self.groupBoxGenerateSchemefileSANDI)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.labelDelta = QLabel(self.groupBoxGenerateSchemefileSANDI)
        self.labelDelta.setObjectName(u"labelDelta")
        sizePolicy.setHeightForWidth(self.labelDelta.sizePolicy().hasHeightForWidth())
        self.labelDelta.setSizePolicy(sizePolicy)

        self.gridLayout_10.addWidget(self.labelDelta, 0, 0, 1, 1)

        self.lineEditDelta = QLineEdit(self.groupBoxGenerateSchemefileSANDI)
        self.lineEditDelta.setObjectName(u"lineEditDelta")
        sizePolicy.setHeightForWidth(self.lineEditDelta.sizePolicy().hasHeightForWidth())
        self.lineEditDelta.setSizePolicy(sizePolicy)
        self.lineEditDelta.setMinimumSize(QSize(80, 30))
        self.lineEditDelta.setMaximumSize(QSize(80, 30))

        self.gridLayout_10.addWidget(self.lineEditDelta, 0, 1, 1, 1)

        self.labelDeltaUnit = QLabel(self.groupBoxGenerateSchemefileSANDI)
        self.labelDeltaUnit.setObjectName(u"labelDeltaUnit")
        self.labelDeltaUnit.setEnabled(False)
        sizePolicy.setHeightForWidth(self.labelDeltaUnit.sizePolicy().hasHeightForWidth())
        self.labelDeltaUnit.setSizePolicy(sizePolicy)

        self.gridLayout_10.addWidget(self.labelDeltaUnit, 0, 2, 1, 1)

        self.labelSmallDelta = QLabel(self.groupBoxGenerateSchemefileSANDI)
        self.labelSmallDelta.setObjectName(u"labelSmallDelta")
        sizePolicy.setHeightForWidth(self.labelSmallDelta.sizePolicy().hasHeightForWidth())
        self.labelSmallDelta.setSizePolicy(sizePolicy)

        self.gridLayout_10.addWidget(self.labelSmallDelta, 1, 0, 1, 1)

        self.lineEditSmallDelta = QLineEdit(self.groupBoxGenerateSchemefileSANDI)
        self.lineEditSmallDelta.setObjectName(u"lineEditSmallDelta")
        sizePolicy.setHeightForWidth(self.lineEditSmallDelta.sizePolicy().hasHeightForWidth())
        self.lineEditSmallDelta.setSizePolicy(sizePolicy)
        self.lineEditSmallDelta.setMinimumSize(QSize(80, 30))
        self.lineEditSmallDelta.setMaximumSize(QSize(80, 30))

        self.gridLayout_10.addWidget(self.lineEditSmallDelta, 1, 1, 1, 1)

        self.labelSmallDeltaUnit = QLabel(self.groupBoxGenerateSchemefileSANDI)
        self.labelSmallDeltaUnit.setObjectName(u"labelSmallDeltaUnit")
        self.labelSmallDeltaUnit.setEnabled(False)
        sizePolicy.setHeightForWidth(self.labelSmallDeltaUnit.sizePolicy().hasHeightForWidth())
        self.labelSmallDeltaUnit.setSizePolicy(sizePolicy)

        self.gridLayout_10.addWidget(self.labelSmallDeltaUnit, 1, 2, 1, 1)

        self.labelTE = QLabel(self.groupBoxGenerateSchemefileSANDI)
        self.labelTE.setObjectName(u"labelTE")
        sizePolicy.setHeightForWidth(self.labelTE.sizePolicy().hasHeightForWidth())
        self.labelTE.setSizePolicy(sizePolicy)

        self.gridLayout_10.addWidget(self.labelTE, 2, 0, 1, 1)

        self.lineEditTE = QLineEdit(self.groupBoxGenerateSchemefileSANDI)
        self.lineEditTE.setObjectName(u"lineEditTE")
        sizePolicy.setHeightForWidth(self.lineEditTE.sizePolicy().hasHeightForWidth())
        self.lineEditTE.setSizePolicy(sizePolicy)
        self.lineEditTE.setMinimumSize(QSize(80, 30))
        self.lineEditTE.setMaximumSize(QSize(80, 30))

        self.gridLayout_10.addWidget(self.lineEditTE, 2, 1, 1, 1)

        self.labelTEUnit = QLabel(self.groupBoxGenerateSchemefileSANDI)
        self.labelTEUnit.setObjectName(u"labelTEUnit")
        self.labelTEUnit.setEnabled(False)
        sizePolicy.setHeightForWidth(self.labelTEUnit.sizePolicy().hasHeightForWidth())
        self.labelTEUnit.setSizePolicy(sizePolicy)

        self.gridLayout_10.addWidget(self.labelTEUnit, 2, 2, 1, 1)


        self.gridLayout_17.addWidget(self.groupBoxGenerateSchemefileSANDI, 2, 0, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.radioButtonLoadSchemefile = QRadioButton(self.groupBoxSchemefile)
        self.radioButtonLoadSchemefile.setObjectName(u"radioButtonLoadSchemefile")
        sizePolicy.setHeightForWidth(self.radioButtonLoadSchemefile.sizePolicy().hasHeightForWidth())
        self.radioButtonLoadSchemefile.setSizePolicy(sizePolicy)

        self.gridLayout_17.addWidget(self.radioButtonLoadSchemefile, 3, 0, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.groupBoxLoadSchemefile = QGroupBox(self.groupBoxSchemefile)
        self.groupBoxLoadSchemefile.setObjectName(u"groupBoxLoadSchemefile")
        self.groupBoxLoadSchemefile.setStyleSheet(u"QGroupBox\n"
"{\n"
"	border: 0;\n"
"}")
        self.gridLayout_14 = QGridLayout(self.groupBoxLoadSchemefile)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.labelSchemefile = QLabel(self.groupBoxLoadSchemefile)
        self.labelSchemefile.setObjectName(u"labelSchemefile")
        sizePolicy.setHeightForWidth(self.labelSchemefile.sizePolicy().hasHeightForWidth())
        self.labelSchemefile.setSizePolicy(sizePolicy)

        self.gridLayout_14.addWidget(self.labelSchemefile, 0, 0, 1, 1)

        self.lineEditSchemefile = FileLineEdit(self.groupBoxLoadSchemefile)
        self.lineEditSchemefile.setObjectName(u"lineEditSchemefile")
        sizePolicy.setHeightForWidth(self.lineEditSchemefile.sizePolicy().hasHeightForWidth())
        self.lineEditSchemefile.setSizePolicy(sizePolicy)
        self.lineEditSchemefile.setMinimumSize(QSize(200, 30))
        self.lineEditSchemefile.setMaximumSize(QSize(200, 30))

        self.gridLayout_14.addWidget(self.lineEditSchemefile, 0, 1, 1, 1)

        self.pushButtonSchemefile = QPushButton(self.groupBoxLoadSchemefile)
        self.pushButtonSchemefile.setObjectName(u"pushButtonSchemefile")
        sizePolicy.setHeightForWidth(self.pushButtonSchemefile.sizePolicy().hasHeightForWidth())
        self.pushButtonSchemefile.setSizePolicy(sizePolicy)
        self.pushButtonSchemefile.setMinimumSize(QSize(80, 30))
        self.pushButtonSchemefile.setMaximumSize(QSize(80, 30))

        self.gridLayout_14.addWidget(self.pushButtonSchemefile, 0, 2, 1, 1)


        self.gridLayout_17.addWidget(self.groupBoxLoadSchemefile, 4, 0, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.groupBoxSchemefileB0 = QGroupBox(self.groupBoxSchemefile)
        self.groupBoxSchemefileB0.setObjectName(u"groupBoxSchemefileB0")
        self.groupBoxSchemefileB0.setStyleSheet(u"QGroupBox\n"
"{\n"
"	border: 0;\n"
"}")
        self.gridLayout_16 = QGridLayout(self.groupBoxSchemefileB0)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.labelB0Threshold = QLabel(self.groupBoxSchemefileB0)
        self.labelB0Threshold.setObjectName(u"labelB0Threshold")
        sizePolicy.setHeightForWidth(self.labelB0Threshold.sizePolicy().hasHeightForWidth())
        self.labelB0Threshold.setSizePolicy(sizePolicy)

        self.gridLayout_16.addWidget(self.labelB0Threshold, 0, 0, 1, 1)

        self.lineEditB0Threshold = QLineEdit(self.groupBoxSchemefileB0)
        self.lineEditB0Threshold.setObjectName(u"lineEditB0Threshold")
        sizePolicy.setHeightForWidth(self.lineEditB0Threshold.sizePolicy().hasHeightForWidth())
        self.lineEditB0Threshold.setSizePolicy(sizePolicy)
        self.lineEditB0Threshold.setMinimumSize(QSize(80, 30))
        self.lineEditB0Threshold.setMaximumSize(QSize(80, 30))

        self.gridLayout_16.addWidget(self.lineEditB0Threshold, 0, 1, 1, 1)

        self.labelB0ThresholdUnit = QLabel(self.groupBoxSchemefileB0)
        self.labelB0ThresholdUnit.setObjectName(u"labelB0ThresholdUnit")
        self.labelB0ThresholdUnit.setEnabled(False)
        sizePolicy.setHeightForWidth(self.labelB0ThresholdUnit.sizePolicy().hasHeightForWidth())
        self.labelB0ThresholdUnit.setSizePolicy(sizePolicy)

        self.gridLayout_16.addWidget(self.labelB0ThresholdUnit, 0, 2, 1, 1)


        self.gridLayout_17.addWidget(self.groupBoxSchemefileB0, 5, 0, 1, 1, Qt.AlignLeft|Qt.AlignTop)


        self.gridLayout_21.addWidget(self.groupBoxSchemefile, 1, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.gridLayout.addWidget(self.groupBoxData, 1, 0, 1, 1)

        self.groupBoxModelSetup = QGroupBox(self.widget)
        self.groupBoxModelSetup.setObjectName(u"groupBoxModelSetup")
        sizePolicy2.setHeightForWidth(self.groupBoxModelSetup.sizePolicy().hasHeightForWidth())
        self.groupBoxModelSetup.setSizePolicy(sizePolicy2)
        self.groupBoxModelSetup.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_22 = QGridLayout(self.groupBoxModelSetup)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.groupBoxNODDISetup = QGroupBox(self.groupBoxModelSetup)
        self.groupBoxNODDISetup.setObjectName(u"groupBoxNODDISetup")
        self.groupBoxNODDISetup.setStyleSheet(u"QGroupBox\n"
"{\n"
"	border: 0;\n"
"}")
        self.gridLayout_12 = QGridLayout(self.groupBoxNODDISetup)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.lineEditDiffPar = QLineEdit(self.groupBoxNODDISetup)
        self.lineEditDiffPar.setObjectName(u"lineEditDiffPar")
        sizePolicy.setHeightForWidth(self.lineEditDiffPar.sizePolicy().hasHeightForWidth())
        self.lineEditDiffPar.setSizePolicy(sizePolicy)
        self.lineEditDiffPar.setMinimumSize(QSize(80, 30))
        self.lineEditDiffPar.setMaximumSize(QSize(80, 30))

        self.gridLayout_12.addWidget(self.lineEditDiffPar, 0, 1, 1, 1)

        self.labelDiffIso = QLabel(self.groupBoxNODDISetup)
        self.labelDiffIso.setObjectName(u"labelDiffIso")
        sizePolicy.setHeightForWidth(self.labelDiffIso.sizePolicy().hasHeightForWidth())
        self.labelDiffIso.setSizePolicy(sizePolicy)

        self.gridLayout_12.addWidget(self.labelDiffIso, 1, 0, 1, 1)

        self.labelDiffParUnit = QLabel(self.groupBoxNODDISetup)
        self.labelDiffParUnit.setObjectName(u"labelDiffParUnit")
        self.labelDiffParUnit.setEnabled(False)
        sizePolicy.setHeightForWidth(self.labelDiffParUnit.sizePolicy().hasHeightForWidth())
        self.labelDiffParUnit.setSizePolicy(sizePolicy)

        self.gridLayout_12.addWidget(self.labelDiffParUnit, 0, 2, 1, 1)

        self.labelDiffIsoUnit = QLabel(self.groupBoxNODDISetup)
        self.labelDiffIsoUnit.setObjectName(u"labelDiffIsoUnit")
        self.labelDiffIsoUnit.setEnabled(False)
        sizePolicy.setHeightForWidth(self.labelDiffIsoUnit.sizePolicy().hasHeightForWidth())
        self.labelDiffIsoUnit.setSizePolicy(sizePolicy)

        self.gridLayout_12.addWidget(self.labelDiffIsoUnit, 1, 2, 1, 1)

        self.lineEditDiffIso = QLineEdit(self.groupBoxNODDISetup)
        self.lineEditDiffIso.setObjectName(u"lineEditDiffIso")
        sizePolicy.setHeightForWidth(self.lineEditDiffIso.sizePolicy().hasHeightForWidth())
        self.lineEditDiffIso.setSizePolicy(sizePolicy)
        self.lineEditDiffIso.setMinimumSize(QSize(80, 30))
        self.lineEditDiffIso.setMaximumSize(QSize(80, 30))

        self.gridLayout_12.addWidget(self.lineEditDiffIso, 1, 1, 1, 1)

        self.labelDiffPar = QLabel(self.groupBoxNODDISetup)
        self.labelDiffPar.setObjectName(u"labelDiffPar")
        sizePolicy.setHeightForWidth(self.labelDiffPar.sizePolicy().hasHeightForWidth())
        self.labelDiffPar.setSizePolicy(sizePolicy)

        self.gridLayout_12.addWidget(self.labelDiffPar, 0, 0, 1, 1)


        self.gridLayout_22.addWidget(self.groupBoxNODDISetup, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pushButtonSetupModel = QPushButton(self.groupBoxModelSetup)
        self.pushButtonSetupModel.setObjectName(u"pushButtonSetupModel")
        sizePolicy.setHeightForWidth(self.pushButtonSetupModel.sizePolicy().hasHeightForWidth())
        self.pushButtonSetupModel.setSizePolicy(sizePolicy)
        self.pushButtonSetupModel.setMinimumSize(QSize(150, 50))
        self.pushButtonSetupModel.setMaximumSize(QSize(150, 50))
        self.pushButtonSetupModel.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButtonSetupModel.setStyleSheet(u"")

        self.gridLayout_22.addWidget(self.pushButtonSetupModel, 5, 0, 1, 1, Qt.AlignHCenter)

        self.checkBoxAdvModelSetup = QCheckBox(self.groupBoxModelSetup)
        self.checkBoxAdvModelSetup.setObjectName(u"checkBoxAdvModelSetup")

        self.gridLayout_22.addWidget(self.checkBoxAdvModelSetup, 4, 0, 1, 1, Qt.AlignLeft|Qt.AlignBottom)

        self.groupBoxAdvSANDISetup = QGroupBox(self.groupBoxModelSetup)
        self.groupBoxAdvSANDISetup.setObjectName(u"groupBoxAdvSANDISetup")
        self.groupBoxAdvSANDISetup.setStyleSheet(u"QGroupBox\n"
"{\n"
"	border: 0;\n"
"}")
        self.gridLayout_8 = QGridLayout(self.groupBoxAdvSANDISetup)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.labelSANDILB = QLabel(self.groupBoxAdvSANDISetup)
        self.labelSANDILB.setObjectName(u"labelSANDILB")
        sizePolicy.setHeightForWidth(self.labelSANDILB.sizePolicy().hasHeightForWidth())
        self.labelSANDILB.setSizePolicy(sizePolicy)

        self.gridLayout_8.addWidget(self.labelSANDILB, 0, 1, 1, 1)

        self.labelSANDIUB = QLabel(self.groupBoxAdvSANDISetup)
        self.labelSANDIUB.setObjectName(u"labelSANDIUB")
        sizePolicy.setHeightForWidth(self.labelSANDIUB.sizePolicy().hasHeightForWidth())
        self.labelSANDIUB.setSizePolicy(sizePolicy)

        self.gridLayout_8.addWidget(self.labelSANDIUB, 0, 3, 1, 1)

        self.labelSANDIN = QLabel(self.groupBoxAdvSANDISetup)
        self.labelSANDIN.setObjectName(u"labelSANDIN")
        sizePolicy.setHeightForWidth(self.labelSANDIN.sizePolicy().hasHeightForWidth())
        self.labelSANDIN.setSizePolicy(sizePolicy)

        self.gridLayout_8.addWidget(self.labelSANDIN, 0, 5, 1, 1)

        self.labelRadius = QLabel(self.groupBoxAdvSANDISetup)
        self.labelRadius.setObjectName(u"labelRadius")
        sizePolicy.setHeightForWidth(self.labelRadius.sizePolicy().hasHeightForWidth())
        self.labelRadius.setSizePolicy(sizePolicy)
        self.labelRadius.setFrameShape(QFrame.NoFrame)
        self.labelRadius.setFrameShadow(QFrame.Plain)
        self.labelRadius.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.labelRadius, 1, 0, 1, 1)

        self.lineEditRadiusLB = QLineEdit(self.groupBoxAdvSANDISetup)
        self.lineEditRadiusLB.setObjectName(u"lineEditRadiusLB")
        sizePolicy.setHeightForWidth(self.lineEditRadiusLB.sizePolicy().hasHeightForWidth())
        self.lineEditRadiusLB.setSizePolicy(sizePolicy)
        self.lineEditRadiusLB.setMinimumSize(QSize(80, 30))
        self.lineEditRadiusLB.setMaximumSize(QSize(80, 30))

        self.gridLayout_8.addWidget(self.lineEditRadiusLB, 1, 1, 1, 1)

        self.labelRadiusLBUnit = QLabel(self.groupBoxAdvSANDISetup)
        self.labelRadiusLBUnit.setObjectName(u"labelRadiusLBUnit")
        self.labelRadiusLBUnit.setEnabled(False)
        sizePolicy.setHeightForWidth(self.labelRadiusLBUnit.sizePolicy().hasHeightForWidth())
        self.labelRadiusLBUnit.setSizePolicy(sizePolicy)

        self.gridLayout_8.addWidget(self.labelRadiusLBUnit, 1, 2, 1, 1)

        self.lineEditRadiusUB = QLineEdit(self.groupBoxAdvSANDISetup)
        self.lineEditRadiusUB.setObjectName(u"lineEditRadiusUB")
        sizePolicy.setHeightForWidth(self.lineEditRadiusUB.sizePolicy().hasHeightForWidth())
        self.lineEditRadiusUB.setSizePolicy(sizePolicy)
        self.lineEditRadiusUB.setMinimumSize(QSize(80, 30))
        self.lineEditRadiusUB.setMaximumSize(QSize(80, 30))

        self.gridLayout_8.addWidget(self.lineEditRadiusUB, 1, 3, 1, 1)

        self.labelRadiusUBUnit = QLabel(self.groupBoxAdvSANDISetup)
        self.labelRadiusUBUnit.setObjectName(u"labelRadiusUBUnit")
        self.labelRadiusUBUnit.setEnabled(False)
        sizePolicy.setHeightForWidth(self.labelRadiusUBUnit.sizePolicy().hasHeightForWidth())
        self.labelRadiusUBUnit.setSizePolicy(sizePolicy)

        self.gridLayout_8.addWidget(self.labelRadiusUBUnit, 1, 4, 1, 1)

        self.lineEditRadiusN = QLineEdit(self.groupBoxAdvSANDISetup)
        self.lineEditRadiusN.setObjectName(u"lineEditRadiusN")
        sizePolicy.setHeightForWidth(self.lineEditRadiusN.sizePolicy().hasHeightForWidth())
        self.lineEditRadiusN.setSizePolicy(sizePolicy)
        self.lineEditRadiusN.setMinimumSize(QSize(80, 30))
        self.lineEditRadiusN.setMaximumSize(QSize(80, 30))

        self.gridLayout_8.addWidget(self.lineEditRadiusN, 1, 5, 1, 1)

        self.labelDiffIN = QLabel(self.groupBoxAdvSANDISetup)
        self.labelDiffIN.setObjectName(u"labelDiffIN")
        sizePolicy.setHeightForWidth(self.labelDiffIN.sizePolicy().hasHeightForWidth())
        self.labelDiffIN.setSizePolicy(sizePolicy)
        self.labelDiffIN.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.labelDiffIN, 2, 0, 1, 1)

        self.lineEditDiffINLB = QLineEdit(self.groupBoxAdvSANDISetup)
        self.lineEditDiffINLB.setObjectName(u"lineEditDiffINLB")
        sizePolicy.setHeightForWidth(self.lineEditDiffINLB.sizePolicy().hasHeightForWidth())
        self.lineEditDiffINLB.setSizePolicy(sizePolicy)
        self.lineEditDiffINLB.setMinimumSize(QSize(80, 30))
        self.lineEditDiffINLB.setMaximumSize(QSize(80, 30))

        self.gridLayout_8.addWidget(self.lineEditDiffINLB, 2, 1, 1, 1)

        self.labelDiffINLBUnit = QLabel(self.groupBoxAdvSANDISetup)
        self.labelDiffINLBUnit.setObjectName(u"labelDiffINLBUnit")
        self.labelDiffINLBUnit.setEnabled(False)
        sizePolicy.setHeightForWidth(self.labelDiffINLBUnit.sizePolicy().hasHeightForWidth())
        self.labelDiffINLBUnit.setSizePolicy(sizePolicy)

        self.gridLayout_8.addWidget(self.labelDiffINLBUnit, 2, 2, 1, 1)

        self.lineEditDiffINUB = QLineEdit(self.groupBoxAdvSANDISetup)
        self.lineEditDiffINUB.setObjectName(u"lineEditDiffINUB")
        sizePolicy.setHeightForWidth(self.lineEditDiffINUB.sizePolicy().hasHeightForWidth())
        self.lineEditDiffINUB.setSizePolicy(sizePolicy)
        self.lineEditDiffINUB.setMinimumSize(QSize(80, 30))
        self.lineEditDiffINUB.setMaximumSize(QSize(80, 30))

        self.gridLayout_8.addWidget(self.lineEditDiffINUB, 2, 3, 1, 1)

        self.labelDiffINUBUnit = QLabel(self.groupBoxAdvSANDISetup)
        self.labelDiffINUBUnit.setObjectName(u"labelDiffINUBUnit")
        self.labelDiffINUBUnit.setEnabled(False)
        sizePolicy.setHeightForWidth(self.labelDiffINUBUnit.sizePolicy().hasHeightForWidth())
        self.labelDiffINUBUnit.setSizePolicy(sizePolicy)

        self.gridLayout_8.addWidget(self.labelDiffINUBUnit, 2, 4, 1, 1)

        self.lineEditDiffINN = QLineEdit(self.groupBoxAdvSANDISetup)
        self.lineEditDiffINN.setObjectName(u"lineEditDiffINN")
        sizePolicy.setHeightForWidth(self.lineEditDiffINN.sizePolicy().hasHeightForWidth())
        self.lineEditDiffINN.setSizePolicy(sizePolicy)
        self.lineEditDiffINN.setMinimumSize(QSize(80, 30))
        self.lineEditDiffINN.setMaximumSize(QSize(80, 30))

        self.gridLayout_8.addWidget(self.lineEditDiffINN, 2, 5, 1, 1)

        self.labelDiffECI = QLabel(self.groupBoxAdvSANDISetup)
        self.labelDiffECI.setObjectName(u"labelDiffECI")
        sizePolicy.setHeightForWidth(self.labelDiffECI.sizePolicy().hasHeightForWidth())
        self.labelDiffECI.setSizePolicy(sizePolicy)
        self.labelDiffECI.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.labelDiffECI, 3, 0, 1, 1)

        self.lineEditDiffECILB = QLineEdit(self.groupBoxAdvSANDISetup)
        self.lineEditDiffECILB.setObjectName(u"lineEditDiffECILB")
        sizePolicy.setHeightForWidth(self.lineEditDiffECILB.sizePolicy().hasHeightForWidth())
        self.lineEditDiffECILB.setSizePolicy(sizePolicy)
        self.lineEditDiffECILB.setMinimumSize(QSize(80, 30))
        self.lineEditDiffECILB.setMaximumSize(QSize(80, 30))

        self.gridLayout_8.addWidget(self.lineEditDiffECILB, 3, 1, 1, 1)

        self.labelDiffECILBUnit = QLabel(self.groupBoxAdvSANDISetup)
        self.labelDiffECILBUnit.setObjectName(u"labelDiffECILBUnit")
        self.labelDiffECILBUnit.setEnabled(False)
        sizePolicy.setHeightForWidth(self.labelDiffECILBUnit.sizePolicy().hasHeightForWidth())
        self.labelDiffECILBUnit.setSizePolicy(sizePolicy)

        self.gridLayout_8.addWidget(self.labelDiffECILBUnit, 3, 2, 1, 1)

        self.lineEditDiffECIUB = QLineEdit(self.groupBoxAdvSANDISetup)
        self.lineEditDiffECIUB.setObjectName(u"lineEditDiffECIUB")
        sizePolicy.setHeightForWidth(self.lineEditDiffECIUB.sizePolicy().hasHeightForWidth())
        self.lineEditDiffECIUB.setSizePolicy(sizePolicy)
        self.lineEditDiffECIUB.setMinimumSize(QSize(80, 30))
        self.lineEditDiffECIUB.setMaximumSize(QSize(80, 30))

        self.gridLayout_8.addWidget(self.lineEditDiffECIUB, 3, 3, 1, 1)

        self.labelDiffECIUBUnit = QLabel(self.groupBoxAdvSANDISetup)
        self.labelDiffECIUBUnit.setObjectName(u"labelDiffECIUBUnit")
        self.labelDiffECIUBUnit.setEnabled(False)
        sizePolicy.setHeightForWidth(self.labelDiffECIUBUnit.sizePolicy().hasHeightForWidth())
        self.labelDiffECIUBUnit.setSizePolicy(sizePolicy)

        self.gridLayout_8.addWidget(self.labelDiffECIUBUnit, 3, 4, 1, 1)

        self.lineEditDiffECIN = QLineEdit(self.groupBoxAdvSANDISetup)
        self.lineEditDiffECIN.setObjectName(u"lineEditDiffECIN")
        sizePolicy.setHeightForWidth(self.lineEditDiffECIN.sizePolicy().hasHeightForWidth())
        self.lineEditDiffECIN.setSizePolicy(sizePolicy)
        self.lineEditDiffECIN.setMinimumSize(QSize(80, 30))
        self.lineEditDiffECIN.setMaximumSize(QSize(80, 30))

        self.gridLayout_8.addWidget(self.lineEditDiffECIN, 3, 5, 1, 1)


        self.gridLayout_22.addWidget(self.groupBoxAdvSANDISetup, 3, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.groupBoxSANDISetup = QGroupBox(self.groupBoxModelSetup)
        self.groupBoxSANDISetup.setObjectName(u"groupBoxSANDISetup")
        self.groupBoxSANDISetup.setStyleSheet(u"QGroupBox\n"
"{\n"
"	border: 0;\n"
"}")
        self.gridLayout_6 = QGridLayout(self.groupBoxSANDISetup)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.labelDiffIS = QLabel(self.groupBoxSANDISetup)
        self.labelDiffIS.setObjectName(u"labelDiffIS")
        sizePolicy.setHeightForWidth(self.labelDiffIS.sizePolicy().hasHeightForWidth())
        self.labelDiffIS.setSizePolicy(sizePolicy)

        self.gridLayout_6.addWidget(self.labelDiffIS, 0, 0, 1, 1)

        self.lineEditDiffIS = QLineEdit(self.groupBoxSANDISetup)
        self.lineEditDiffIS.setObjectName(u"lineEditDiffIS")
        sizePolicy.setHeightForWidth(self.lineEditDiffIS.sizePolicy().hasHeightForWidth())
        self.lineEditDiffIS.setSizePolicy(sizePolicy)
        self.lineEditDiffIS.setMinimumSize(QSize(80, 30))
        self.lineEditDiffIS.setMaximumSize(QSize(80, 30))

        self.gridLayout_6.addWidget(self.lineEditDiffIS, 0, 1, 1, 1)

        self.labelDiffISUnit = QLabel(self.groupBoxSANDISetup)
        self.labelDiffISUnit.setObjectName(u"labelDiffISUnit")
        self.labelDiffISUnit.setEnabled(False)
        sizePolicy.setHeightForWidth(self.labelDiffISUnit.sizePolicy().hasHeightForWidth())
        self.labelDiffISUnit.setSizePolicy(sizePolicy)

        self.gridLayout_6.addWidget(self.labelDiffISUnit, 0, 2, 1, 1)


        self.gridLayout_22.addWidget(self.groupBoxSANDISetup, 2, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.groupBoxAdvNODDISetup = QGroupBox(self.groupBoxModelSetup)
        self.groupBoxAdvNODDISetup.setObjectName(u"groupBoxAdvNODDISetup")
        self.groupBoxAdvNODDISetup.setStyleSheet(u"QGroupBox\n"
"{\n"
"	border: 0;\n"
"}")
        self.gridLayout_5 = QGridLayout(self.groupBoxAdvNODDISetup)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.labelNODDILB = QLabel(self.groupBoxAdvNODDISetup)
        self.labelNODDILB.setObjectName(u"labelNODDILB")
        sizePolicy.setHeightForWidth(self.labelNODDILB.sizePolicy().hasHeightForWidth())
        self.labelNODDILB.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.labelNODDILB, 0, 1, 1, 1)

        self.labelNODDIUB = QLabel(self.groupBoxAdvNODDISetup)
        self.labelNODDIUB.setObjectName(u"labelNODDIUB")
        sizePolicy.setHeightForWidth(self.labelNODDIUB.sizePolicy().hasHeightForWidth())
        self.labelNODDIUB.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.labelNODDIUB, 0, 2, 1, 1)

        self.labelNODDIN = QLabel(self.groupBoxAdvNODDISetup)
        self.labelNODDIN.setObjectName(u"labelNODDIN")
        sizePolicy.setHeightForWidth(self.labelNODDIN.sizePolicy().hasHeightForWidth())
        self.labelNODDIN.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.labelNODDIN, 0, 3, 1, 1)

        self.labelICVF = QLabel(self.groupBoxAdvNODDISetup)
        self.labelICVF.setObjectName(u"labelICVF")
        sizePolicy.setHeightForWidth(self.labelICVF.sizePolicy().hasHeightForWidth())
        self.labelICVF.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.labelICVF, 1, 0, 1, 1)

        self.lineEditICVFLB = QLineEdit(self.groupBoxAdvNODDISetup)
        self.lineEditICVFLB.setObjectName(u"lineEditICVFLB")
        sizePolicy.setHeightForWidth(self.lineEditICVFLB.sizePolicy().hasHeightForWidth())
        self.lineEditICVFLB.setSizePolicy(sizePolicy)
        self.lineEditICVFLB.setMinimumSize(QSize(80, 30))
        self.lineEditICVFLB.setMaximumSize(QSize(80, 30))

        self.gridLayout_5.addWidget(self.lineEditICVFLB, 1, 1, 1, 1)

        self.lineEditICVFUB = QLineEdit(self.groupBoxAdvNODDISetup)
        self.lineEditICVFUB.setObjectName(u"lineEditICVFUB")
        sizePolicy.setHeightForWidth(self.lineEditICVFUB.sizePolicy().hasHeightForWidth())
        self.lineEditICVFUB.setSizePolicy(sizePolicy)
        self.lineEditICVFUB.setMinimumSize(QSize(80, 30))
        self.lineEditICVFUB.setMaximumSize(QSize(80, 30))

        self.gridLayout_5.addWidget(self.lineEditICVFUB, 1, 2, 1, 1)

        self.lineEditICVFN = QLineEdit(self.groupBoxAdvNODDISetup)
        self.lineEditICVFN.setObjectName(u"lineEditICVFN")
        sizePolicy.setHeightForWidth(self.lineEditICVFN.sizePolicy().hasHeightForWidth())
        self.lineEditICVFN.setSizePolicy(sizePolicy)
        self.lineEditICVFN.setMinimumSize(QSize(80, 30))
        self.lineEditICVFN.setMaximumSize(QSize(80, 30))

        self.gridLayout_5.addWidget(self.lineEditICVFN, 1, 3, 1, 1)

        self.labelICOD = QLabel(self.groupBoxAdvNODDISetup)
        self.labelICOD.setObjectName(u"labelICOD")
        sizePolicy.setHeightForWidth(self.labelICOD.sizePolicy().hasHeightForWidth())
        self.labelICOD.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.labelICOD, 2, 0, 1, 1)

        self.lineEditICODLB = QLineEdit(self.groupBoxAdvNODDISetup)
        self.lineEditICODLB.setObjectName(u"lineEditICODLB")
        sizePolicy.setHeightForWidth(self.lineEditICODLB.sizePolicy().hasHeightForWidth())
        self.lineEditICODLB.setSizePolicy(sizePolicy)
        self.lineEditICODLB.setMinimumSize(QSize(80, 30))
        self.lineEditICODLB.setMaximumSize(QSize(80, 30))

        self.gridLayout_5.addWidget(self.lineEditICODLB, 2, 1, 1, 1)

        self.lineEditICODUB = QLineEdit(self.groupBoxAdvNODDISetup)
        self.lineEditICODUB.setObjectName(u"lineEditICODUB")
        sizePolicy.setHeightForWidth(self.lineEditICODUB.sizePolicy().hasHeightForWidth())
        self.lineEditICODUB.setSizePolicy(sizePolicy)
        self.lineEditICODUB.setMinimumSize(QSize(80, 30))
        self.lineEditICODUB.setMaximumSize(QSize(80, 30))

        self.gridLayout_5.addWidget(self.lineEditICODUB, 2, 2, 1, 1)

        self.lineEditICODN = QLineEdit(self.groupBoxAdvNODDISetup)
        self.lineEditICODN.setObjectName(u"lineEditICODN")
        sizePolicy.setHeightForWidth(self.lineEditICODN.sizePolicy().hasHeightForWidth())
        self.lineEditICODN.setSizePolicy(sizePolicy)
        self.lineEditICODN.setMinimumSize(QSize(80, 30))
        self.lineEditICODN.setMaximumSize(QSize(80, 30))

        self.gridLayout_5.addWidget(self.lineEditICODN, 2, 3, 1, 1)


        self.gridLayout_22.addWidget(self.groupBoxAdvNODDISetup, 1, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.gridLayout.addWidget(self.groupBoxModelSetup, 1, 1, 1, 1)

        self.groupBoxModelFit = QGroupBox(self.widget)
        self.groupBoxModelFit.setObjectName(u"groupBoxModelFit")
        sizePolicy2.setHeightForWidth(self.groupBoxModelFit.sizePolicy().hasHeightForWidth())
        self.groupBoxModelFit.setSizePolicy(sizePolicy2)
        self.gridLayout_23 = QGridLayout(self.groupBoxModelFit)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.checkBoxAdvModelFit = QCheckBox(self.groupBoxModelFit)
        self.checkBoxAdvModelFit.setObjectName(u"checkBoxAdvModelFit")

        self.gridLayout_23.addWidget(self.checkBoxAdvModelFit, 1, 0, 1, 1, Qt.AlignLeft|Qt.AlignBottom)

        self.pushButtonFitModel = QPushButton(self.groupBoxModelFit)
        self.pushButtonFitModel.setObjectName(u"pushButtonFitModel")
        sizePolicy.setHeightForWidth(self.pushButtonFitModel.sizePolicy().hasHeightForWidth())
        self.pushButtonFitModel.setSizePolicy(sizePolicy)
        self.pushButtonFitModel.setMinimumSize(QSize(150, 50))
        self.pushButtonFitModel.setMaximumSize(QSize(150, 50))
        self.pushButtonFitModel.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButtonFitModel.setStyleSheet(u"")

        self.gridLayout_23.addWidget(self.pushButtonFitModel, 2, 0, 1, 1, Qt.AlignHCenter)

        self.groupBoxImagePreview = QGroupBox(self.groupBoxModelFit)
        self.groupBoxImagePreview.setObjectName(u"groupBoxImagePreview")
        self.groupBoxImagePreview.setFlat(True)
        self.gridLayout_19 = QGridLayout(self.groupBoxImagePreview)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.graphicsView = ImageView(self.groupBoxImagePreview)
        self.graphicsView.setObjectName(u"graphicsView")
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setMinimumSize(QSize(400, 300))
        self.graphicsView.setMaximumSize(QSize(400, 350))

        self.gridLayout_19.addWidget(self.graphicsView, 1, 0, 1, 3)

        self.comboBoxImagePreview = QComboBox(self.groupBoxImagePreview)
        self.comboBoxImagePreview.setObjectName(u"comboBoxImagePreview")
        self.comboBoxImagePreview.setMinimumSize(QSize(300, 40))
        self.comboBoxImagePreview.setMaximumSize(QSize(300, 40))

        self.gridLayout_19.addWidget(self.comboBoxImagePreview, 0, 0, 1, 1)

        self.pushButtonPreviewExternal = QPushButton(self.groupBoxImagePreview)
        self.pushButtonPreviewExternal.setObjectName(u"pushButtonPreviewExternal")
        self.pushButtonPreviewExternal.setMinimumSize(QSize(100, 30))
        self.pushButtonPreviewExternal.setMaximumSize(QSize(100, 30))
        self.pushButtonPreviewExternal.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_19.addWidget(self.pushButtonPreviewExternal, 0, 1, 1, 1)

        self.groupBoxPreviewButtons = QGroupBox(self.groupBoxImagePreview)
        self.groupBoxPreviewButtons.setObjectName(u"groupBoxPreviewButtons")
        self.groupBoxPreviewButtons.setStyleSheet(u"QGroupBox\n"
"{\n"
"	border: 0;\n"
"}")
        self.gridLayout_11 = QGridLayout(self.groupBoxPreviewButtons)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.pushButtonView1 = QPushButton(self.groupBoxPreviewButtons)
        self.pushButtonView1.setObjectName(u"pushButtonView1")
        self.pushButtonView1.setMinimumSize(QSize(100, 30))
        self.pushButtonView1.setMaximumSize(QSize(100, 30))
        self.pushButtonView1.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_11.addWidget(self.pushButtonView1, 0, 1, 1, 1)

        self.pushButtonView2 = QPushButton(self.groupBoxPreviewButtons)
        self.pushButtonView2.setObjectName(u"pushButtonView2")
        self.pushButtonView2.setMinimumSize(QSize(100, 30))
        self.pushButtonView2.setMaximumSize(QSize(100, 30))
        self.pushButtonView2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_11.addWidget(self.pushButtonView2, 0, 2, 1, 1)

        self.pushButtonView3 = QPushButton(self.groupBoxPreviewButtons)
        self.pushButtonView3.setObjectName(u"pushButtonView3")
        self.pushButtonView3.setMinimumSize(QSize(100, 30))
        self.pushButtonView3.setMaximumSize(QSize(100, 30))
        self.pushButtonView3.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_11.addWidget(self.pushButtonView3, 0, 0, 1, 1)


        self.gridLayout_19.addWidget(self.groupBoxPreviewButtons, 3, 0, 1, 2)

        self.horizontalSlider = QSlider(self.groupBoxImagePreview)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_19.addWidget(self.horizontalSlider, 2, 0, 1, 1)


        self.gridLayout_23.addWidget(self.groupBoxImagePreview, 3, 0, 1, 1, Qt.AlignHCenter|Qt.AlignBottom)

        self.groupBoxFitSetup = QGroupBox(self.groupBoxModelFit)
        self.groupBoxFitSetup.setObjectName(u"groupBoxFitSetup")
        sizePolicy.setHeightForWidth(self.groupBoxFitSetup.sizePolicy().hasHeightForWidth())
        self.groupBoxFitSetup.setSizePolicy(sizePolicy)
        self.groupBoxFitSetup.setStyleSheet(u"QGroupBox\n"
"{\n"
"	border: 0;\n"
"}")
        self.gridLayout_7 = QGridLayout(self.groupBoxFitSetup)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.labelLambda1 = QLabel(self.groupBoxFitSetup)
        self.labelLambda1.setObjectName(u"labelLambda1")
        sizePolicy.setHeightForWidth(self.labelLambda1.sizePolicy().hasHeightForWidth())
        self.labelLambda1.setSizePolicy(sizePolicy)

        self.gridLayout_7.addWidget(self.labelLambda1, 0, 0, 1, 1)

        self.lineEditLambda1 = QLineEdit(self.groupBoxFitSetup)
        self.lineEditLambda1.setObjectName(u"lineEditLambda1")
        sizePolicy.setHeightForWidth(self.lineEditLambda1.sizePolicy().hasHeightForWidth())
        self.lineEditLambda1.setSizePolicy(sizePolicy)
        self.lineEditLambda1.setMinimumSize(QSize(80, 30))
        self.lineEditLambda1.setMaximumSize(QSize(80, 30))
        self.lineEditLambda1.setFrame(False)
        self.lineEditLambda1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.lineEditLambda1, 0, 1, 1, 1)

        self.labelLambda2 = QLabel(self.groupBoxFitSetup)
        self.labelLambda2.setObjectName(u"labelLambda2")
        sizePolicy.setHeightForWidth(self.labelLambda2.sizePolicy().hasHeightForWidth())
        self.labelLambda2.setSizePolicy(sizePolicy)

        self.gridLayout_7.addWidget(self.labelLambda2, 1, 0, 1, 1)

        self.lineEditLambda2 = QLineEdit(self.groupBoxFitSetup)
        self.lineEditLambda2.setObjectName(u"lineEditLambda2")
        sizePolicy.setHeightForWidth(self.lineEditLambda2.sizePolicy().hasHeightForWidth())
        self.lineEditLambda2.setSizePolicy(sizePolicy)
        self.lineEditLambda2.setMinimumSize(QSize(80, 30))
        self.lineEditLambda2.setMaximumSize(QSize(80, 30))
        self.lineEditLambda2.setFrame(False)
        self.lineEditLambda2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.lineEditLambda2, 1, 1, 1, 1)


        self.gridLayout_23.addWidget(self.groupBoxFitSetup, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.gridLayout.addWidget(self.groupBoxModelFit, 1, 2, 1, 1)

        self.progressBar = QProgressBar(self.widget)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy3)
        self.progressBar.setStyleSheet(u"")
        self.progressBar.setMaximum(0)
        self.progressBar.setValue(-1)
        self.progressBar.setTextVisible(False)

        self.gridLayout.addWidget(self.progressBar, 2, 1, 1, 1)

        window.setCentralWidget(self.widget)
        self.menubar = QMenuBar(window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1500, 22))
        self.menu_file = QMenu(self.menubar)
        self.menu_file.setObjectName(u"menu_file")
        self.menu_recent_studies = QMenu(self.menu_file)
        self.menu_recent_studies.setObjectName(u"menu_recent_studies")
        self.menu_Settings = QMenu(self.menubar)
        self.menu_Settings.setObjectName(u"menu_Settings")
        window.setMenuBar(self.menubar)
        QWidget.setTabOrder(self.comboBoxModel, self.lineEditStudy)
        QWidget.setTabOrder(self.lineEditStudy, self.pushButtonStudy)
        QWidget.setTabOrder(self.pushButtonStudy, self.lineEditSubject)
        QWidget.setTabOrder(self.lineEditSubject, self.pushButtonSubject)
        QWidget.setTabOrder(self.pushButtonSubject, self.lineEditDWI)
        QWidget.setTabOrder(self.lineEditDWI, self.pushButtonDWI)
        QWidget.setTabOrder(self.pushButtonDWI, self.lineEditMask)
        QWidget.setTabOrder(self.lineEditMask, self.pushButtonMask)
        QWidget.setTabOrder(self.pushButtonMask, self.radioButtonGenerateSchemefile)
        QWidget.setTabOrder(self.radioButtonGenerateSchemefile, self.lineEditBvals)
        QWidget.setTabOrder(self.lineEditBvals, self.pushButtonBvals)
        QWidget.setTabOrder(self.pushButtonBvals, self.lineEditBvecs)
        QWidget.setTabOrder(self.lineEditBvecs, self.pushButtonBvecs)
        QWidget.setTabOrder(self.pushButtonBvecs, self.lineEditBStep)
        QWidget.setTabOrder(self.lineEditBStep, self.lineEditDelta)
        QWidget.setTabOrder(self.lineEditDelta, self.lineEditSmallDelta)
        QWidget.setTabOrder(self.lineEditSmallDelta, self.lineEditTE)
        QWidget.setTabOrder(self.lineEditTE, self.radioButtonLoadSchemefile)
        QWidget.setTabOrder(self.radioButtonLoadSchemefile, self.lineEditSchemefile)
        QWidget.setTabOrder(self.lineEditSchemefile, self.pushButtonSchemefile)
        QWidget.setTabOrder(self.pushButtonSchemefile, self.lineEditB0Threshold)
        QWidget.setTabOrder(self.lineEditB0Threshold, self.pushButtonLoadData)
        QWidget.setTabOrder(self.pushButtonLoadData, self.lineEditDiffPar)
        QWidget.setTabOrder(self.lineEditDiffPar, self.lineEditDiffIso)
        QWidget.setTabOrder(self.lineEditDiffIso, self.lineEditICVFLB)
        QWidget.setTabOrder(self.lineEditICVFLB, self.lineEditICVFUB)
        QWidget.setTabOrder(self.lineEditICVFUB, self.lineEditICVFN)
        QWidget.setTabOrder(self.lineEditICVFN, self.lineEditICODLB)
        QWidget.setTabOrder(self.lineEditICODLB, self.lineEditICODUB)
        QWidget.setTabOrder(self.lineEditICODUB, self.lineEditICODN)
        QWidget.setTabOrder(self.lineEditICODN, self.lineEditDiffIS)
        QWidget.setTabOrder(self.lineEditDiffIS, self.lineEditRadiusLB)
        QWidget.setTabOrder(self.lineEditRadiusLB, self.lineEditRadiusUB)
        QWidget.setTabOrder(self.lineEditRadiusUB, self.lineEditRadiusN)
        QWidget.setTabOrder(self.lineEditRadiusN, self.lineEditDiffINLB)
        QWidget.setTabOrder(self.lineEditDiffINLB, self.lineEditDiffINUB)
        QWidget.setTabOrder(self.lineEditDiffINUB, self.lineEditDiffINN)
        QWidget.setTabOrder(self.lineEditDiffINN, self.lineEditDiffECILB)
        QWidget.setTabOrder(self.lineEditDiffECILB, self.lineEditDiffECIUB)
        QWidget.setTabOrder(self.lineEditDiffECIUB, self.lineEditDiffECIN)
        QWidget.setTabOrder(self.lineEditDiffECIN, self.checkBoxAdvModelSetup)
        QWidget.setTabOrder(self.checkBoxAdvModelSetup, self.pushButtonSetupModel)
        QWidget.setTabOrder(self.pushButtonSetupModel, self.lineEditLambda1)
        QWidget.setTabOrder(self.lineEditLambda1, self.lineEditLambda2)
        QWidget.setTabOrder(self.lineEditLambda2, self.checkBoxAdvModelFit)
        QWidget.setTabOrder(self.checkBoxAdvModelFit, self.pushButtonFitModel)
        QWidget.setTabOrder(self.pushButtonFitModel, self.comboBoxImagePreview)
        QWidget.setTabOrder(self.comboBoxImagePreview, self.pushButtonPreviewExternal)
        QWidget.setTabOrder(self.pushButtonPreviewExternal, self.graphicsView)
        QWidget.setTabOrder(self.graphicsView, self.horizontalSlider)
        QWidget.setTabOrder(self.horizontalSlider, self.pushButtonView3)
        QWidget.setTabOrder(self.pushButtonView3, self.pushButtonView1)
        QWidget.setTabOrder(self.pushButtonView1, self.pushButtonView2)

        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_Settings.menuAction())
        self.menu_file.addAction(self.action_new_study)
        self.menu_file.addAction(self.menu_recent_studies.menuAction())
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_exit)
        self.menu_Settings.addAction(self.action_preferences)

        self.retranslateUi(window)

        QMetaObject.connectSlotsByName(window)
    # setupUi

    def retranslateUi(self, window):
        window.setWindowTitle(QCoreApplication.translate("window", u"AMICO Graphical Interface", None))
        self.action_new_study.setText(QCoreApplication.translate("window", u"&New study", None))
        self.action_exit.setText(QCoreApplication.translate("window", u"Exit", None))
        self.action_preferences.setText(QCoreApplication.translate("window", u"&Preferences...", None))
        self.groupBoxModelSelection.setTitle(QCoreApplication.translate("window", u"Model selection", None))
        self.labelModel.setText(QCoreApplication.translate("window", u"Model", None))
        self.groupBoxData.setTitle(QCoreApplication.translate("window", u"Data", None))
        self.pushButtonLoadData.setText(QCoreApplication.translate("window", u"Load data", None))
        self.pushButtonDWI.setText(QCoreApplication.translate("window", u"...", None))
        self.lineEditMask.setPlaceholderText(QCoreApplication.translate("window", u"optional", None))
        self.pushButtonMask.setText(QCoreApplication.translate("window", u"...", None))
#if QT_CONFIG(tooltip)
        self.lineEditDWI.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.labelStudy.setText(QCoreApplication.translate("window", u"Study", None))
        self.labelSubject.setText(QCoreApplication.translate("window", u"Subject", None))
#if QT_CONFIG(tooltip)
        self.labelDWI.setToolTip(QCoreApplication.translate("window", u"The file name of the DWI data", None))
#endif // QT_CONFIG(tooltip)
        self.labelDWI.setText(QCoreApplication.translate("window", u"DWI", None))
        self.pushButtonStudy.setText(QCoreApplication.translate("window", u"...", None))
        self.pushButtonSubject.setText(QCoreApplication.translate("window", u"...", None))
        self.labelMask.setText(QCoreApplication.translate("window", u"Mask", None))
        self.groupBoxSchemefile.setTitle(QCoreApplication.translate("window", u"Acquisition scheme", None))
        self.radioButtonGenerateSchemefile.setText(QCoreApplication.translate("window", u"Generate", None))
        self.labelBvals.setText(QCoreApplication.translate("window", u"Bvals", None))
        self.pushButtonBvals.setText(QCoreApplication.translate("window", u"...", None))
        self.labelBvecs.setText(QCoreApplication.translate("window", u"Bvecs", None))
        self.pushButtonBvecs.setText(QCoreApplication.translate("window", u"...", None))
        self.labelBStep.setText(QCoreApplication.translate("window", u"bStep", None))
        self.labelBStepUnit.setText(QCoreApplication.translate("window", u"[s/mm\u00b2]", None))
        self.labelDelta.setText(QCoreApplication.translate("window", u"Delta", None))
        self.labelDeltaUnit.setText(QCoreApplication.translate("window", u"[s]", None))
        self.labelSmallDelta.setText(QCoreApplication.translate("window", u"Small Delta", None))
        self.labelSmallDeltaUnit.setText(QCoreApplication.translate("window", u"[s]", None))
        self.labelTE.setText(QCoreApplication.translate("window", u"TE", None))
        self.lineEditTE.setPlaceholderText(QCoreApplication.translate("window", u"optional", None))
        self.labelTEUnit.setText(QCoreApplication.translate("window", u"[s]", None))
        self.radioButtonLoadSchemefile.setText(QCoreApplication.translate("window", u"Load existing", None))
        self.labelSchemefile.setText(QCoreApplication.translate("window", u"Schemefile", None))
        self.pushButtonSchemefile.setText(QCoreApplication.translate("window", u"...", None))
        self.labelB0Threshold.setText(QCoreApplication.translate("window", u"b0 threshold", None))
        self.labelB0ThresholdUnit.setText(QCoreApplication.translate("window", u"[s/mm\u00b2]", None))
        self.groupBoxModelSetup.setTitle(QCoreApplication.translate("window", u"Model setup", None))
        self.lineEditDiffPar.setPlaceholderText("")
        self.labelDiffIso.setText(QCoreApplication.translate("window", u"Isotropic diff.", None))
        self.labelDiffParUnit.setText(QCoreApplication.translate("window", u"\u00d710\u00af\u00b3 [mm\u00b2/s]", None))
        self.labelDiffIsoUnit.setText(QCoreApplication.translate("window", u"\u00d710\u00af\u00b3 [mm\u00b2/s]", None))
        self.labelDiffPar.setText(QCoreApplication.translate("window", u"Parallel diff.", None))
        self.pushButtonSetupModel.setText(QCoreApplication.translate("window", u"Setup model", None))
        self.checkBoxAdvModelSetup.setText(QCoreApplication.translate("window", u"Show advanced options", None))
        self.labelSANDILB.setText(QCoreApplication.translate("window", u"Lower bound", None))
        self.labelSANDIUB.setText(QCoreApplication.translate("window", u"Upper bound", None))
        self.labelSANDIN.setText(QCoreApplication.translate("window", u"N", None))
        self.labelRadius.setText(QCoreApplication.translate("window", u"Soma radius", None))
        self.labelRadiusLBUnit.setText(QCoreApplication.translate("window", u"\u00d710\u00af\u2076 [m]", None))
        self.labelRadiusUBUnit.setText(QCoreApplication.translate("window", u"\u00d710\u00af\u2076 [m]", None))
        self.labelDiffIN.setText(QCoreApplication.translate("window", u"Intra-neurite diff.", None))
        self.labelDiffINLBUnit.setText(QCoreApplication.translate("window", u"\u00d710\u00af\u00b3 [mm\u00b2/s]", None))
        self.labelDiffINUBUnit.setText(QCoreApplication.translate("window", u"\u00d710\u00af\u00b3 [mm\u00b2/s]", None))
        self.labelDiffECI.setText(QCoreApplication.translate("window", u"Extra-cellular isotropic diff.", None))
        self.labelDiffECILBUnit.setText(QCoreApplication.translate("window", u"\u00d710\u00af\u00b3 [mm\u00b2/s]", None))
        self.labelDiffECIUBUnit.setText(QCoreApplication.translate("window", u"\u00d710\u00af\u00b3 [mm\u00b2/s]", None))
        self.labelDiffIS.setText(QCoreApplication.translate("window", u"Intra-soma diff.", None))
        self.lineEditDiffIS.setInputMask("")
        self.lineEditDiffIS.setPlaceholderText("")
        self.labelDiffISUnit.setText(QCoreApplication.translate("window", u"\u00d710\u00af\u00b3 [mm\u00b2/s]", None))
        self.labelNODDILB.setText(QCoreApplication.translate("window", u"Lower bound", None))
        self.labelNODDIUB.setText(QCoreApplication.translate("window", u"Upper bound", None))
        self.labelNODDIN.setText(QCoreApplication.translate("window", u"N", None))
#if QT_CONFIG(tooltip)
        self.labelICVF.setToolTip(QCoreApplication.translate("window", u"Intra-cellular Volum Fraction", None))
#endif // QT_CONFIG(tooltip)
        self.labelICVF.setText(QCoreApplication.translate("window", u"IC_VF", None))
        self.labelICOD.setText(QCoreApplication.translate("window", u"IC_OD", None))
        self.groupBoxModelFit.setTitle(QCoreApplication.translate("window", u"Model fit", None))
        self.checkBoxAdvModelFit.setText(QCoreApplication.translate("window", u"Show advanced options", None))
        self.pushButtonFitModel.setText(QCoreApplication.translate("window", u"Fit model", None))
        self.groupBoxImagePreview.setTitle(QCoreApplication.translate("window", u"Output preview", None))
        self.pushButtonPreviewExternal.setText(QCoreApplication.translate("window", u"Full view", None))
        self.pushButtonView1.setText(QCoreApplication.translate("window", u"Sagittal", None))
        self.pushButtonView2.setText(QCoreApplication.translate("window", u"Coronal", None))
        self.pushButtonView3.setText(QCoreApplication.translate("window", u"Axial", None))
        self.labelLambda1.setText(QCoreApplication.translate("window", u"Sparsity", None))
        self.labelLambda2.setText(QCoreApplication.translate("window", u"Smoothness", None))
        self.menu_file.setTitle(QCoreApplication.translate("window", u"&File", None))
        self.menu_recent_studies.setTitle(QCoreApplication.translate("window", u"&Recent studies", None))
        self.menu_Settings.setTitle(QCoreApplication.translate("window", u"&Settings", None))
    # retranslateUi

