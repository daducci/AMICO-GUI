from xmlrpc.client import Boolean, boolean
from PySide6.QtGui import QValidator, QIntValidator, QDoubleValidator, QAction, QScreen
from PySide6.QtWidgets import QMainWindow, QFileDialog, QLineEdit, QMessageBox, QApplication
from PySide6.QtCore import Slot, QLocale
from ui.main_window_ui import Ui_window
import configparser
from multiprocessing import cpu_count
from os import path, listdir
from workers import LoadDataWorker, SetupModelWorker, FitModelWorker
import nibabel as nib
import numpy as np
from preview_window import PreviewWindow
from preferences_dialog import PreferencesDialog
from validators import *

amico_config_file = path.abspath(path.join(path.dirname(__file__), 'amico_gui.cfg'))

def load_config():
    config = configparser.ConfigParser()
    config.read(amico_config_file)
    return config

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_window()
        self.ui.setupUi(self)
        
        self.init()
        
        # TESTS

    def init(self):
        # Load config file
        self.config = load_config()

        self.load_options()
        self.setup_sections()
        self.setup_slots()
        self.setup_validators()

    def adjust_window_size(self):
        self.adjustSize()
        self.ui.widget.adjustSize()
        # self.ui.groupBoxModelSelection.adjustSize()
        # self.ui.groupBoxData.adjustSize()
        # self.ui.groupBoxModelSetup.adjustSize()
        # self.ui.groupBoxModelFit.adjustSize()
        self.center_window()
    
    def center_window(self):
        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geo = self.frameGeometry()
        geo.moveCenter(center)
        self.move(geo.topLeft())

    def load_options(self):
        # Menubar
        n = int(self.config['N_RECENTS']['n_recents'])
        self.recents = []
        for i in range(n, 0, -1):
            section = 'RECENT_' + str(i)
            if section in self.config:
                study = self.config[section]['study']
                subject = self.config[section]['subject']
                if study != '':
                    self.recents.append(
                        {
                            'section': section,
                            'action': QAction(path.basename(study) + ' --> ' + path.basename(subject), self)
                        }
                    )
        for recent in self.recents:
            self.ui.menu_recent_studies.addAction(recent['action'])
            # Slot that must be reloaded when new project is triggered
            recent['action'].triggered.connect(lambda checked=True, section=recent['section']: self.load_recent(section) if self.confirm_dialog('Load this recent?') else None)
        self.ui.menu_recent_studies.addSeparator()
        self.ui.menu_recent_studies.addAction('Clear all', self.clear_recents)

        # Models
        self.ui.comboBoxModel.addItems(self.config['DEFAULT']['models'].split(', '))
        self.ui.comboBoxModel.setCurrentText(self.config['DEFAULT']['model_default'])
        self.switch_model()

        # Schemefile
        self.ui.radioButtonGenerateSchemefile.setChecked(True)
        self.switch_schemefile()
        self.ui.lineEditBStep.setText(self.config['DEFAULT']['b_step'])
        self.ui.lineEditB0Threshold.setText(self.config['DEFAULT']['b0_threshold'])

        # Global options
        self.load_preferences(
            self.config['GLOBAL']['lmax'],
            self.config['GLOBAL']['ndirs_selected'],
            self.config['GLOBAL']['openblas_num_threads'],
            self.config['GLOBAL']['joblib_backend_selected'],
            self.config['GLOBAL']['joblib_num_threads']
        )

        # NODDI options
        self.ui.lineEditDiffPar.setText(self.config['DEFAULT_NODDI']['diff_par'])
        self.ui.lineEditDiffIso.setText(self.config['DEFAULT_NODDI']['diff_iso'])
        self.ui.lineEditICVFLB.setText(self.config['DEFAULT_NODDI']['ic_vf_lb'])
        self.ui.lineEditICVFUB.setText(self.config['DEFAULT_NODDI']['ic_vf_ub'])
        self.ui.lineEditICVFN.setText(self.config['DEFAULT_NODDI']['ic_vf_n'])
        self.ui.lineEditICODLB.setText(self.config['DEFAULT_NODDI']['ic_od_lb'])
        self.ui.lineEditICODUB.setText(self.config['DEFAULT_NODDI']['ic_od_ub'])
        self.ui.lineEditICODN.setText(self.config['DEFAULT_NODDI']['ic_od_n'])

        # SANDI options
        self.ui.lineEditDiffIS.setText(self.config['DEFAULT_SANDI']['diff_is'])
        self.ui.lineEditRadiusLB.setText(self.config['DEFAULT_SANDI']['radius_lb'])
        self.ui.lineEditRadiusUB.setText(self.config['DEFAULT_SANDI']['radius_ub'])
        self.ui.lineEditRadiusN.setText(self.config['DEFAULT_SANDI']['radius_n'])
        self.ui.lineEditDiffINLB.setText(self.config['DEFAULT_SANDI']['diff_in_lb'])
        self.ui.lineEditDiffINUB.setText(self.config['DEFAULT_SANDI']['diff_in_ub'])
        self.ui.lineEditDiffINN.setText(self.config['DEFAULT_SANDI']['diff_in_n'])
        self.ui.lineEditDiffECILB.setText(self.config['DEFAULT_SANDI']['diff_iso_lb'])
        self.ui.lineEditDiffECIUB.setText(self.config['DEFAULT_SANDI']['diff_iso_ub'])
        self.ui.lineEditDiffECIN.setText(self.config['DEFAULT_SANDI']['diff_iso_n'])

    def setup_sections(self):
        self.ui.groupBoxModelSetup.setEnabled(False)
        self.ui.groupBoxModelFit.setEnabled(False)
        self.ui.comboBoxImagePreview.clear()
        self.ui.graphicsView.hide()
        self.ui.graphicsView.setPredefinedGradient('grey')
        self.ui.progressBar.setMinimum(0)
        self.ui.progressBar.setMaximum(0)
        self.ui.progressBar.hide()

    def setup_slots(self):
        # Menubar
        self.ui.action_exit.triggered.connect(self.close)
        self.ui.action_new_study.triggered.connect(lambda checked=True: self.new_project() if self.confirm_dialog('New project?') else None)
        self.ui.action_preferences.triggered.connect(self.show_preferences)

        # Model selection
        self.ui.comboBoxModel.currentTextChanged.connect(self.switch_model)

        # Advanced options
        self.ui.checkBoxAdvModelSetup.stateChanged.connect(self.switch_advanced_setup_options)
        self.ui.checkBoxAdvModelFit.stateChanged.connect(self.switch_advanced_fit_options)

        # Schemefile
        self.ui.radioButtonGenerateSchemefile.toggled.connect(self.switch_schemefile)
        self.ui.radioButtonLoadSchemefile.toggled.connect(self.switch_schemefile)

        # Input buttons
        self.ui.pushButtonStudy.clicked.connect(lambda: self.load_directory(self.ui.lineEditStudy, 'Select study directory'))
        self.ui.pushButtonSubject.clicked.connect(lambda: self.load_directory(self.ui.lineEditSubject, 'Select subject directory', self.ui.lineEditStudy.text()))
        self.ui.pushButtonDWI.clicked.connect(lambda: self.load_file(self.ui.lineEditDWI, 'Select DWI file', 'Image files (*.nii *.nii.gz *.img)'))
        self.ui.pushButtonMask.clicked.connect(lambda: self.load_file(self.ui.lineEditMask, 'Select mask file', 'Image files (*.nii *.nii.gz *.img)'))
        self.ui.pushButtonBvals.clicked.connect(lambda: self.load_file(self.ui.lineEditBvals, 'Select bval file', 'Bval files (*.bval *.bvals *.txt)'))
        self.ui.pushButtonBvecs.clicked.connect(lambda: self.load_file(self.ui.lineEditBvecs, 'Select bvec file', 'Bvec files (*.bvec *.bvecs *.txt)'))
        self.ui.pushButtonSchemefile.clicked.connect(lambda: self.load_file(self.ui.lineEditSchemefile, 'Select schemefile', 'Scheme files (*.scheme *.txt)'))

        # Run buttons
        self.ui.pushButtonLoadData.clicked.connect(self.load_data)
        self.ui.pushButtonSetupModel.clicked.connect(self.setup_model)
        self.ui.pushButtonFitModel.clicked.connect(self.fit_model)

        # Reset stylesheets
        self.ui.lineEditStudy.textChanged.connect(self.reset_stylesheets)
        self.ui.lineEditSubject.textChanged.connect(self.reset_stylesheets)
        self.ui.lineEditDWI.textChanged.connect(self.reset_stylesheets)
        self.ui.lineEditMask.textChanged.connect(self.reset_stylesheets)
        self.ui.lineEditBvals.textChanged.connect(self.reset_stylesheets)
        self.ui.lineEditBvecs.textChanged.connect(self.reset_stylesheets)
        self.ui.lineEditSchemefile.textChanged.connect(self.reset_stylesheets)
        self.ui.lineEditBStep.textChanged.connect(self.reset_stylesheets)
        self.ui.lineEditB0Threshold.textChanged.connect(self.reset_stylesheets)
        self.ui.lineEditDelta.textChanged.connect(self.reset_stylesheets)
        self.ui.lineEditSmallDelta.textChanged.connect(self.reset_stylesheets)
        self.ui.lineEditTE.textChanged.connect(self.reset_stylesheets)
        self.ui.lineEditDiffPar.textChanged.connect(self.reset_stylesheets)
        self.ui.lineEditDiffIso.textChanged.connect(self.reset_stylesheets)
        self.ui.lineEditICVFLB.textChanged.connect(self.reset_stylesheets)
        self.ui.lineEditICVFUB.textChanged.connect(self.reset_stylesheets)
        self.ui.lineEditICVFN.textChanged.connect(self.reset_stylesheets)
        self.ui.lineEditICODLB.textChanged.connect(self.reset_stylesheets)
        self.ui.lineEditICODUB.textChanged.connect(self.reset_stylesheets)
        self.ui.lineEditICODN.textChanged.connect(self.reset_stylesheets)
        self.ui.lineEditDiffIS.textChanged.connect(self.reset_stylesheets)
        self.ui.lineEditRadiusLB.textChanged.connect(self.reset_stylesheets)
        self.ui.lineEditRadiusUB.textChanged.connect(self.reset_stylesheets)
        self.ui.lineEditRadiusN.textChanged.connect(self.reset_stylesheets)
        self.ui.lineEditDiffINLB.textChanged.connect(self.reset_stylesheets)
        self.ui.lineEditDiffINUB.textChanged.connect(self.reset_stylesheets)
        self.ui.lineEditDiffINN.textChanged.connect(self.reset_stylesheets)
        self.ui.lineEditDiffECILB.textChanged.connect(self.reset_stylesheets)
        self.ui.lineEditDiffECIUB.textChanged.connect(self.reset_stylesheets)
        self.ui.lineEditDiffECIN.textChanged.connect(self.reset_stylesheets)
        self.ui.lineEditLambda1.textChanged.connect(self.reset_stylesheets)
        self.ui.lineEditLambda2.textChanged.connect(self.reset_stylesheets)

        self.ui.comboBoxModel.currentTextChanged.connect(self.reset_stylesheets)
        self.ui.radioButtonGenerateSchemefile.toggled.connect(self.reset_stylesheets)
        self.ui.radioButtonLoadSchemefile.toggled.connect(self.reset_stylesheets)

        # Preview section
        self.ui.pushButtonView1.clicked.connect(lambda: self.switch_view('sagittal'))
        self.ui.pushButtonView2.clicked.connect(lambda: self.switch_view('coronal'))
        self.ui.pushButtonView3.clicked.connect(lambda: self.switch_view('axial'))
        self.ui.horizontalSlider.valueChanged.connect(self.update_slice)
        self.ui.comboBoxImagePreview.currentTextChanged.connect(self.switch_image)
        self.ui.pushButtonPreviewExternal.clicked.connect(self.open_full_preview)

    def reset_stylesheets(self):
        self.ui.labelStudy.setStyleSheet('')
        self.ui.lineEditStudy.setStyleSheet('')
        self.ui.labelSubject.setStyleSheet('')
        self.ui.lineEditSubject.setStyleSheet('')
        self.ui.labelDWI.setStyleSheet('')
        self.ui.lineEditDWI.setStyleSheet('')
        self.ui.labelMask.setStyleSheet('')
        self.ui.lineEditMask.setStyleSheet('')
        self.ui.labelBvals.setStyleSheet('')
        self.ui.lineEditBvals.setStyleSheet('')
        self.ui.labelBvecs.setStyleSheet('')
        self.ui.lineEditBvecs.setStyleSheet('')
        self.ui.labelSchemefile.setStyleSheet('')
        self.ui.lineEditSchemefile.setStyleSheet('')
        self.ui.labelBStep.setStyleSheet('')
        self.ui.lineEditBStep.setStyleSheet('')
        self.ui.labelB0Threshold.setStyleSheet('')
        self.ui.lineEditB0Threshold.setStyleSheet('')
        self.ui.labelDelta.setStyleSheet('')
        self.ui.lineEditDelta.setStyleSheet('')
        self.ui.labelSmallDelta.setStyleSheet('')
        self.ui.lineEditSmallDelta.setStyleSheet('')
        self.ui.labelTE.setStyleSheet('')
        self.ui.lineEditTE.setStyleSheet('')
        self.ui.labelDiffPar.setStyleSheet('')
        self.ui.lineEditDiffPar.setStyleSheet('')
        self.ui.labelDiffIso.setStyleSheet('')
        self.ui.lineEditDiffIso.setStyleSheet('')
        self.ui.labelICVF.setStyleSheet('')
        self.ui.lineEditICVFLB.setStyleSheet('')
        self.ui.lineEditICVFUB.setStyleSheet('')
        self.ui.lineEditICVFN.setStyleSheet('')
        self.ui.labelICOD.setStyleSheet('')
        self.ui.lineEditICODLB.setStyleSheet('')
        self.ui.lineEditICODUB.setStyleSheet('')
        self.ui.lineEditICODN.setStyleSheet('')
        self.ui.labelDiffIS.setStyleSheet('')
        self.ui.labelRadius.setStyleSheet('')
        self.ui.lineEditRadiusLB.setStyleSheet('')
        self.ui.lineEditRadiusUB.setStyleSheet('')
        self.ui.lineEditRadiusN.setStyleSheet('')
        self.ui.labelDiffIN.setStyleSheet('')
        self.ui.lineEditDiffINLB.setStyleSheet('')
        self.ui.lineEditDiffINUB.setStyleSheet('')
        self.ui.lineEditDiffINN.setStyleSheet('')
        self.ui.labelDiffECI.setStyleSheet('')
        self.ui.lineEditDiffECILB.setStyleSheet('')
        self.ui.lineEditDiffECIUB.setStyleSheet('')
        self.ui.lineEditDiffECIN.setStyleSheet('')
        self.ui.labelLambda1.setStyleSheet('')
        self.ui.lineEditLambda1.setStyleSheet('')
        self.ui.labelLambda2.setStyleSheet('')
        self.ui.lineEditLambda2.setStyleSheet('')

    def setup_validators(self):
        QLocale.setDefault(QLocale('en_US'))
        directory_validator = DirectoryValidator(parent=self)
        file_validator = FileValidator(parent=self)
        optional_file_validator = OptionalFileValidator(parent=self)
        major_zero_int_validator = MajorZeroIntValidator()
        non_negative_double_validator = NonNegativeDoubleValidator(parent=self)
        major_zero_double_validator = MajorZeroDoubleValidator()
        optional_major_zero_double_validator = OptionalMajorZeroDoubleValidator(parent=self)

        self.ui.lineEditStudy.setValidator(directory_validator)
        self.ui.lineEditSubject.setValidator(directory_validator)
        self.ui.lineEditDWI.setValidator(file_validator)
        self.ui.lineEditMask.setValidator(optional_file_validator)
        self.ui.lineEditBvals.setValidator(file_validator)
        self.ui.lineEditBvecs.setValidator(file_validator)
        self.ui.lineEditSchemefile.setValidator(file_validator)
        self.ui.lineEditBStep.setValidator(non_negative_double_validator)
        self.ui.lineEditB0Threshold.setValidator(non_negative_double_validator)
        self.ui.lineEditDelta.setValidator(major_zero_double_validator)
        self.ui.lineEditSmallDelta.setValidator(major_zero_double_validator)
        self.ui.lineEditTE.setValidator(optional_major_zero_double_validator)
        self.ui.lineEditDiffPar.setValidator(major_zero_double_validator)
        self.ui.lineEditDiffIso.setValidator(major_zero_double_validator)
        self.ui.lineEditICVFLB.setValidator(major_zero_double_validator)
        self.ui.lineEditICVFUB.setValidator(major_zero_double_validator)
        self.ui.lineEditICVFN.setValidator(major_zero_int_validator)
        self.ui.lineEditICODLB.setValidator(major_zero_double_validator)
        self.ui.lineEditICODUB.setValidator(major_zero_double_validator)
        self.ui.lineEditICODN.setValidator(major_zero_int_validator)
        self.ui.lineEditDiffIS.setValidator(major_zero_double_validator)
        self.ui.lineEditRadiusLB.setValidator(major_zero_double_validator)
        self.ui.lineEditRadiusUB.setValidator(major_zero_double_validator)
        self.ui.lineEditRadiusN.setValidator(major_zero_int_validator)
        self.ui.lineEditDiffINLB.setValidator(major_zero_double_validator)
        self.ui.lineEditDiffINUB.setValidator(major_zero_double_validator)
        self.ui.lineEditDiffINN.setValidator(major_zero_int_validator)
        self.ui.lineEditDiffECILB.setValidator(major_zero_double_validator)
        self.ui.lineEditDiffECIUB.setValidator(major_zero_double_validator)
        self.ui.lineEditDiffECIN.setValidator(major_zero_int_validator)
        self.ui.lineEditLambda1.setValidator(non_negative_double_validator)
        self.ui.lineEditLambda2.setValidator(non_negative_double_validator)

    def check_validators(self):
        if self.ui.lineEditStudy.validator().validate(self.ui.lineEditStudy.text(), 0)[0] != QValidator.Acceptable:
            self.ui.labelStudy.setStyleSheet('QLabel {color: red;}')
            self.ui.lineEditStudy.setStyleSheet('QLineEdit {border: 1px solid red}')
            raise ValueError('Study directory not exists')
        if self.ui.lineEditSubject.validator().validate(self.ui.lineEditSubject.text(), 0)[0] != QValidator.Acceptable:
            self.ui.labelSubject.setStyleSheet('QLabel {color: red}')
            self.ui.lineEditSubject.setStyleSheet('QLineEdit {border: 1px solid red}')
            raise ValueError('Subject directory not exists')
        if self.ui.lineEditDWI.validator().validate(self.ui.lineEditDWI.text(), 0)[0] != QValidator.Acceptable:
            self.ui.labelDWI.setStyleSheet('QLabel {color: red}')
            self.ui.lineEditDWI.setStyleSheet('QLineEdit {border: 1px solid red}')
            raise ValueError('DWI file not exists')
        if self.ui.lineEditMask.validator().validate(self.ui.lineEditMask.text(), 0)[0] != QValidator.Acceptable:
            self.ui.labelMask.setStyleSheet('QLabel {color: red}')
            self.ui.lineEditMask.setStyleSheet('QLineEdit {border: 1px solid red}')
            raise ValueError('Mask file not exists')
        if self.ui.lineEditB0Threshold.validator().validate(self.ui.lineEditB0Threshold.text(), 0)[0] != QValidator.Acceptable:
            self.ui.labelB0Threshold.setStyleSheet('QLabel {color: red}')
            self.ui.lineEditB0Threshold.setStyleSheet('QLineEdit {border: 1px solid red}')
            raise ValueError('b0 threshold not valid')

        if self.ui.radioButtonGenerateSchemefile.isChecked():
            if self.ui.lineEditBvals.validator().validate(self.ui.lineEditBvals.text(), 0)[0] != QValidator.Acceptable:
                self.ui.labelBvals.setStyleSheet('QLabel {color: red}')
                self.ui.lineEditBvals.setStyleSheet('QLineEdit {border: 1px solid red}')
                raise ValueError('Bvals file not exists')
            if self.ui.lineEditBvecs.validator().validate(self.ui.lineEditBvecs.text(), 0)[0] != QValidator.Acceptable:
                self.ui.labelBvecs.setStyleSheet('QLabel {color: red}')
                self.ui.lineEditBvecs.setStyleSheet('QLineEdit {border: 1px solid red}')
                raise ValueError('Bvecs file not exists')
            if self.ui.lineEditBStep.validator().validate(self.ui.lineEditBStep.text(), 0)[0] != QValidator.Acceptable:
                self.ui.labelBStep.setStyleSheet('QLabel {color: red}')
                self.ui.lineEditBStep.setStyleSheet('QLineEdit {border: 1px solid red}')
                raise ValueError('b-value step not valid')
            if self.ui.comboBoxModel.currentText() == 'SANDI':
                if self.ui.lineEditDelta.validator().validate(self.ui.lineEditDelta.text(), 0)[0] != QValidator.Acceptable:
                    self.ui.labelDelta.setStyleSheet('QLabel { color: red }')
                    self.ui.lineEditDelta.setStyleSheet('QLineEdit { border: 1px solid red }')
                    raise ValueError('Delta must be a positive number')
                if self.ui.lineEditSmallDelta.validator().validate(self.ui.lineEditSmallDelta.text(), 0)[0] != QValidator.Acceptable:
                    self.ui.labelSmallDelta.setStyleSheet('QLabel { color: red }')
                    self.ui.lineEditSmallDelta.setStyleSheet('QLineEdit { border: 1px solid red }')
                    raise ValueError('Small delta must be a positive number')

        if self.ui.radioButtonLoadSchemefile.isChecked():
            if self.ui.lineEditSchemefile.validator().validate(self.ui.lineEditSchemefile.text(), 0)[0] != QValidator.Acceptable:
                self.ui.labelSchemefile.setStyleSheet('QLabel {color: red}')
                self.ui.lineEditSchemefile.setStyleSheet('QLineEdit {border: 1px solid red}')
                raise ValueError('Scheme file not exists')

        if self.ui.comboBoxModel.currentText() == 'NODDI':
            if self.ui.lineEditDiffPar.validator().validate(self.ui.lineEditDiffPar.text(), 0)[0] != QValidator.Acceptable:
                self.ui.labelDiffPar.setStyleSheet('QLabel { color: red }')
                self.ui.lineEditDiffPar.setStyleSheet('QLineEdit { border: 1px solid red }')
                raise ValueError('Diffusion parameter not valid')
            if self.ui.lineEditDiffIso.validator().validate(self.ui.lineEditDiffIso.text(), 0)[0] != QValidator.Acceptable:
                self.ui.labelDiffIso.setStyleSheet('QLabel { color: red }')
                self.ui.lineEditDiffIso.setStyleSheet('QLineEdit { border: 1px solid red }')
                raise ValueError('Diffusion parameter not valid')
            if self.ui.lineEditICVFLB.validator().validate(self.ui.lineEditICVFLB.text(), 0)[0] != QValidator.Acceptable:
                self.ui.labelICVF.setStyleSheet('QLabel { color: red }')
                self.ui.lineEditICVFLB.setStyleSheet('QLineEdit { border: 1px solid red }')
                raise ValueError('ICVF lower bound not valid')
            if self.ui.lineEditICVFUB.validator().validate(self.ui.lineEditICVFUB.text(), 0)[0] != QValidator.Acceptable:
                self.ui.labelICVF.setStyleSheet('QLabel { color: red }')
                self.ui.lineEditICVFUB.setStyleSheet('QLineEdit { border: 1px solid red }')
                raise ValueError('ICVF upper bound not valid')
            if self.ui.lineEditICVFN.validator().validate(self.ui.lineEditICVFN.text(), 0)[0] != QValidator.Acceptable:
                self.ui.labelICVF.setStyleSheet('QLabel { color: red }')
                self.ui.lineEditICVFN.setStyleSheet('QLineEdit { border: 1px solid red }')
                raise ValueError('ICVF number of points not valid')
            if self.ui.lineEditICODLB.validator().validate(self.ui.lineEditICODLB.text(), 0)[0] != QValidator.Acceptable:
                self.ui.labelICOD.setStyleSheet('QLabel { color: red }')
                self.ui.lineEditICODLB.setStyleSheet('QLineEdit { border: 1px solid red }')
                raise ValueError('ICOD lower bound not valid')
            if self.ui.lineEditICODUB.validator().validate(self.ui.lineEditICODUB.text(), 0)[0] != QValidator.Acceptable:
                self.ui.labelICOD.setStyleSheet('QLabel { color: red }')
                self.ui.lineEditICODUB.setStyleSheet('QLineEdit { border: 1px solid red }')
                raise ValueError('ICOD upper bound not valid')
            if self.ui.lineEditICODN.validator().validate(self.ui.lineEditICODN.text(), 0)[0] != QValidator.Acceptable:
                self.ui.labelICOD.setStyleSheet('QLabel { color: red }')
                self.ui.lineEditICODN.setStyleSheet('QLineEdit { border: 1px solid red }')
                raise ValueError('ICOD number of points not valid')

        if self.ui.comboBoxModel.currentText() == 'SANDI':
            if self.ui.lineEditDiffIS.validator().validate(self.ui.lineEditDiffIS.text(), 0)[0] != QValidator.Acceptable:
                self.ui.labelDiffIS.setStyleSheet('QLabel { color: red }')
                self.ui.lineEditDiffIS.setStyleSheet('QLineEdit { border: 1px solid red }')
                raise ValueError('Diffusion parameter not valid')
            if self.ui.lineEditRadiusLB.validator().validate(self.ui.lineEditRadiusLB.text(), 0)[0] != QValidator.Acceptable:
                self.ui.labelRadius.setStyleSheet('QLabel { color: red }')
                self.ui.lineEditRadiusLB.setStyleSheet('QLineEdit { border: 1px solid red }')
                raise ValueError('Radius lower bound not valid')
            if self.ui.lineEditRadiusUB.validator().validate(self.ui.lineEditRadiusUB.text(), 0)[0] != QValidator.Acceptable:
                self.ui.labelRadius.setStyleSheet('QLabel { color: red }')
                self.ui.lineEditRadiusUB.setStyleSheet('QLineEdit { border: 1px solid red }')
                raise ValueError('Radius upper bound not valid')
            if self.ui.lineEditRadiusN.validator().validate(self.ui.lineEditRadiusN.text(), 0)[0] != QValidator.Acceptable:
                self.ui.labelRadius.setStyleSheet('QLabel { color: red }')
                self.ui.lineEditRadiusN.setStyleSheet('QLineEdit { border: 1px solid red }')
                raise ValueError('Radius number of points not valid')
            if self.ui.lineEditDiffINLB.validator().validate(self.ui.lineEditDiffINLB.text(), 0)[0] != QValidator.Acceptable:
                self.ui.labelDiffIN.setStyleSheet('QLabel { color: red }')
                self.ui.lineEditDiffINLB.setStyleSheet('QLineEdit { border: 1px solid red }')
                raise ValueError('Diffusion lower bound not valid')
            if self.ui.lineEditDiffINUB.validator().validate(self.ui.lineEditDiffINUB.text(), 0)[0] != QValidator.Acceptable:
                self.ui.labelDiffIN.setStyleSheet('QLabel { color: red }')
                self.ui.lineEditDiffINUB.setStyleSheet('QLineEdit { border: 1px solid red }')
                raise ValueError('Diffusion upper bound not valid')
            if self.ui.lineEditDiffINN.validator().validate(self.ui.lineEditDiffINN.text(), 0)[0] != QValidator.Acceptable:
                self.ui.labelDiffIN.setStyleSheet('QLabel { color: red }')
                self.ui.lineEditDiffINN.setStyleSheet('QLineEdit { border: 1px solid red }')
                raise ValueError('Diffusion number of points not valid')
            if self.ui.lineEditDiffECILB.validator().validate(self.ui.lineEditDiffECILB.text(), 0)[0] != QValidator.Acceptable:
                self.ui.labelDiffECI.setStyleSheet('QLabel { color: red }')
                self.ui.lineEditDiffECILB.setStyleSheet('QLineEdit { border: 1px solid red }')
                raise ValueError('Diffusion lower bound not valid')
            if self.ui.lineEditDiffECIUB.validator().validate(self.ui.lineEditDiffECIUB.text(), 0)[0] != QValidator.Acceptable:
                self.ui.labelDiffECI.setStyleSheet('QLabel { color: red }')
                self.ui.lineEditDiffECIUB.setStyleSheet('QLineEdit { border: 1px solid red }')
                raise ValueError('Diffusion upper bound not valid')
            if self.ui.lineEditDiffECIN.validator().validate(self.ui.lineEditDiffECIN.text(), 0)[0] != QValidator.Acceptable:
                self.ui.labelDiffECI.setStyleSheet('QLabel { color: red }')
                self.ui.lineEditDiffECIN.setStyleSheet('QLineEdit { border: 1px solid red }')
                raise ValueError('Diffusion number of points not valid')

        if self.ui.lineEditLambda1.validator().validate(self.ui.lineEditLambda1.text(), 0)[0] != QValidator.Acceptable:
            self.ui.labelLambda1.setStyleSheet('QLabel { color: red }')
            self.ui.lineEditLambda1.setStyleSheet('QLineEdit { border: 1px solid red }')
            raise ValueError('Sparsity not valid')
        if self.ui.lineEditLambda2.validator().validate(self.ui.lineEditLambda2.text(), 0)[0] != QValidator.Acceptable:
            self.ui.labelLambda2.setStyleSheet('QLabel { color: red }')
            self.ui.lineEditLambda2.setStyleSheet('QLineEdit { border: 1px solid red }')
            raise ValueError('Smoothness not valid')

    ### NEW CODE HERE
    @Slot()
    def show_preferences(self):
        self.preferences_dialog = PreferencesDialog()
        self.preferences_dialog.show()

        self.preferences_dialog.closeEvent = lambda event: (
            self.load_preferences(
                self.preferences_dialog.lmax,
                self.preferences_dialog.ndirs_selected,
                self.preferences_dialog.openblas_num_threads,
                self.preferences_dialog.joblib_backend_selected,
                self.preferences_dialog.joblib_num_threads,
            ),
            event.accept()
        )

    def load_preferences(self, lmax, ndirs_selected, openblas_num_threads, joblib_backend_selected, joblib_num_threads):
        self.lmax = lmax
        self.ndirs_selected = ndirs_selected
        self.openblas_num_threads = openblas_num_threads
        self.joblib_backend_selected = joblib_backend_selected
        self.joblib_num_threads = str(cpu_count()) if joblib_num_threads == 'auto' else joblib_num_threads

    @Slot()
    def open_full_preview(self):
        preview_window = PreviewWindow(self.preview_path)
        preview_window.showMaximized()

    def clear_recents(self):
        self.ui.menu_recent_studies.clear()
        self.ui.menu_recent_studies.addSeparator()
        self.ui.menu_recent_studies.addAction('Clear all', self.clear_recents)

        config = configparser.ConfigParser()
        config.read(amico_config_file)
        n_max = int(config['N_RECENTS']['max_recents'])
        config['N_RECENTS']['n_recents'] = '0'
        for i in range(1, n_max+1):
            section = 'RECENT_' + str(i)
            if section in config:
                config.remove_section(section)
        with open(amico_config_file, 'w') as configfile:
                config.write(configfile)

    @Slot()
    def new_project(self):
        self.ui.comboBoxModel.clear()
        self.ui.lineEditStudy.setText('')
        self.ui.lineEditSubject.setText('')
        self.ui.lineEditDWI.setText('')
        self.ui.lineEditMask.setText('')
        self.ui.lineEditBvals.setText('')
        self.ui.lineEditBvecs.setText('')
        self.ui.lineEditSchemefile.setText('')
        self.ui.lineEditBStep.setText('')
        self.ui.lineEditB0Threshold.setText('')
        self.ui.lineEditDelta.setText('')
        self.ui.lineEditSmallDelta.setText('')
        self.ui.lineEditTE.setText('')

        self.ui.menu_recent_studies.clear()

        self.load_options()
        self.setup_sections()

    def confirm_dialog(self, message):
        response = QMessageBox.question(self, 'Confirm', message, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if response == QMessageBox.Yes:
            return True
        else:
            return False

    @Slot()
    def load_recent(self, recent_section):
        if recent_section != '':
            self.ui.comboBoxModel.setCurrentText(self.config[recent_section]['model'])
            self.ui.lineEditStudy.setText(self.config[recent_section]['study'])
            self.ui.lineEditSubject.setText(self.config[recent_section]['subject'])
            self.ui.lineEditDWI.setText(self.config[recent_section]['dwi'])
            self.ui.lineEditMask.setText(self.config[recent_section]['mask'])
            self.ui.lineEditBvals.setText(self.config[recent_section]['bvals'])
            self.ui.lineEditBvecs.setText(self.config[recent_section]['bvecs'])
            self.ui.lineEditBStep.setText(self.config[recent_section]['b_step'])
            self.ui.lineEditB0Threshold.setText(self.config[recent_section]['b0_threshold'])
            self.ui.lineEditDelta.setText(self.config[recent_section]['delta'])
            self.ui.lineEditSmallDelta.setText(self.config[recent_section]['small_delta'])
            self.ui.lineEditTE.setText(self.config[recent_section]['te'])
            self.ui.lineEditSchemefile.setText(self.config[recent_section]['schemefile'])
            self.ui.radioButtonGenerateSchemefile.setChecked(True if self.config[recent_section]['generate_schemefile'] == 'True' else False)
            self.ui.radioButtonLoadSchemefile.setChecked(False if self.config[recent_section]['generate_schemefile'] == 'True' else True)

            self.ui.lineEditDiffPar.setText(self.config[recent_section]['diff_par'])
            self.ui.lineEditDiffIso.setText(self.config[recent_section]['diff_iso'])
            self.ui.lineEditICVFLB.setText(self.config[recent_section]['ic_vf_lb'])
            self.ui.lineEditICVFUB.setText(self.config[recent_section]['ic_vf_ub'])
            self.ui.lineEditICVFN.setText(self.config[recent_section]['ic_vf_n'])
            self.ui.lineEditICODLB.setText(self.config[recent_section]['ic_od_lb'])
            self.ui.lineEditICODUB.setText(self.config[recent_section]['ic_od_ub'])
            self.ui.lineEditICODN.setText(self.config[recent_section]['ic_od_n'])
            self.ui.lineEditDiffIS.setText(self.config[recent_section]['diff_is'])
            self.ui.lineEditRadiusLB.setText(self.config[recent_section]['radius_lb'])
            self.ui.lineEditRadiusUB.setText(self.config[recent_section]['radius_ub'])
            self.ui.lineEditRadiusN.setText(self.config[recent_section]['radius_n'])
            self.ui.lineEditDiffINLB.setText(self.config[recent_section]['diff_in_lb'])
            self.ui.lineEditDiffINUB.setText(self.config[recent_section]['diff_in_ub'])
            self.ui.lineEditDiffINN.setText(self.config[recent_section]['diff_in_n'])
            self.ui.lineEditDiffECILB.setText(self.config[recent_section]['diff_iso_lb'])
            self.ui.lineEditDiffECIUB.setText(self.config[recent_section]['diff_iso_ub'])
            self.ui.lineEditDiffECIN.setText(self.config[recent_section]['diff_iso_n'])
            self.ui.lineEditLambda1.setText(self.config[recent_section]['lambda1'])
            self.ui.lineEditLambda2.setText(self.config[recent_section]['lambda2'])

            self.setup_sections()

    def save_data(self):
        config = configparser.ConfigParser()
        config.read(amico_config_file)
        n_max = int(config['N_RECENTS']['max_recents'])
        n = int(config['N_RECENTS']['n_recents'])
        saved = False
        if self.ui.lineEditStudy.text() != '':
            for i in range(1, n+1):
                section = 'RECENT_' + str(i)
                if section in config and config[section]['study'] == self.ui.lineEditStudy.text() and config[section]['subject'] == self.ui.lineEditSubject.text():
                    config.remove_section(section)
                    config.add_section(section)
                    config[section] = {
                        'model': self.ui.comboBoxModel.currentText(),
                        'study': self.ui.lineEditStudy.text(),
                        'subject': self.ui.lineEditSubject.text(),
                        'dwi': self.ui.lineEditDWI.text(),
                        'mask': self.ui.lineEditMask.text(),
                        'bvals': self.ui.lineEditBvals.text(),
                        'bvecs': self.ui.lineEditBvecs.text(),
                        'b_step': self.ui.lineEditBStep.text(),
                        'b0_threshold': self.ui.lineEditB0Threshold.text(),
                        'delta': self.ui.lineEditDelta.text(),
                        'small_delta': self.ui.lineEditSmallDelta.text(),
                        'te': self.ui.lineEditTE.text(),
                        'schemefile': self.ui.lineEditSchemefile.text(),
                        'generate_schemefile': self.ui.radioButtonGenerateSchemefile.isChecked(),
                        'diff_par': self.ui.lineEditDiffPar.text(),
                        'diff_iso': self.ui.lineEditDiffIso.text(),
                        'ic_vf_lb': self.ui.lineEditICVFLB.text(),
                        'ic_vf_ub': self.ui.lineEditICVFUB.text(),
                        'ic_vf_n': self.ui.lineEditICVFN.text(),
                        'ic_od_lb': self.ui.lineEditICODLB.text(),
                        'ic_od_ub': self.ui.lineEditICODUB.text(),
                        'ic_od_n': self.ui.lineEditICODN.text(),
                        'diff_is': self.ui.lineEditDiffIS.text(),
                        'radius_lb': self.ui.lineEditRadiusLB.text(),
                        'radius_ub': self.ui.lineEditRadiusUB.text(),
                        'radius_n': self.ui.lineEditRadiusN.text(),
                        'diff_in_lb': self.ui.lineEditDiffINLB.text(),
                        'diff_in_ub': self.ui.lineEditDiffINUB.text(),
                        'diff_in_n': self.ui.lineEditDiffINN.text(),
                        'diff_iso_lb': self.ui.lineEditDiffECILB.text(),
                        'diff_iso_ub': self.ui.lineEditDiffECIUB.text(),
                        'diff_iso_n': self.ui.lineEditDiffECIN.text(),
                        'lambda1': self.ui.lineEditLambda1.text(),
                        'lambda2': self.ui.lineEditLambda2.text()
                    }
                    saved = True
                    break
            if not saved:
                if 'RECENT_'+str(n_max) in config:
                    config.remove_section('RECENT_1')
                    for i in range(2, n+1):
                        section = 'RECENT_' + str(i)
                        items = config.items(section)
                        config.remove_section(section)
                        config.add_section('RECENT_' + str(i-1))
                        for item in items:
                            config.set('RECENT_' + str(i-1), item[0], item[1])
                    config['RECENT_'+str(n)] = {
                        'model': str(self.ui.comboBoxModel.currentText()),
                        'study': self.ui.lineEditStudy.text(),
                        'subject': self.ui.lineEditSubject.text(),
                        'dwi': self.ui.lineEditDWI.text(),
                        'mask': self.ui.lineEditMask.text(),
                        'bvals': self.ui.lineEditBvals.text(),
                        'bvecs': self.ui.lineEditBvecs.text(),
                        'b_step': self.ui.lineEditBStep.text(),
                        'b0_threshold': self.ui.lineEditB0Threshold.text(),
                        'delta': self.ui.lineEditDelta.text(),
                        'small_delta': self.ui.lineEditSmallDelta.text(),
                        'te': self.ui.lineEditTE.text(),
                        'schemefile': self.ui.lineEditSchemefile.text(),
                        'generate_schemefile': self.ui.radioButtonGenerateSchemefile.isChecked(),
                        'diff_par': self.ui.lineEditDiffPar.text(),
                        'diff_iso': self.ui.lineEditDiffIso.text(),
                        'ic_vf_lb': self.ui.lineEditICVFLB.text(),
                        'ic_vf_ub': self.ui.lineEditICVFUB.text(),
                        'ic_vf_n': self.ui.lineEditICVFN.text(),
                        'ic_od_lb': self.ui.lineEditICODLB.text(),
                        'ic_od_ub': self.ui.lineEditICODUB.text(),
                        'ic_od_n': self.ui.lineEditICODN.text(),
                        'diff_is': self.ui.lineEditDiffIS.text(),
                        'radius_lb': self.ui.lineEditRadiusLB.text(),
                        'radius_ub': self.ui.lineEditRadiusUB.text(),
                        'radius_n': self.ui.lineEditRadiusN.text(),
                        'diff_in_lb': self.ui.lineEditDiffINLB.text(),
                        'diff_in_ub': self.ui.lineEditDiffINUB.text(),
                        'diff_in_n': self.ui.lineEditDiffINN.text(),
                        'diff_iso_lb': self.ui.lineEditDiffECILB.text(),
                        'diff_iso_ub': self.ui.lineEditDiffECIUB.text(),
                        'diff_iso_n': self.ui.lineEditDiffECIN.text(),
                        'lambda1': self.ui.lineEditLambda1.text(),
                        'lambda2': self.ui.lineEditLambda2.text()
                    }
                else:
                    for i in range(1, n_max+1):
                        section = 'RECENT_' + str(i)
                        if section not in config:
                            config[section] = {
                                'model': str(self.ui.comboBoxModel.currentText()),
                                'study': self.ui.lineEditStudy.text(),
                                'subject': self.ui.lineEditSubject.text(),
                                'dwi': self.ui.lineEditDWI.text(),
                                'mask': self.ui.lineEditMask.text(),
                                'bvals': self.ui.lineEditBvals.text(),
                                'bvecs': self.ui.lineEditBvecs.text(),
                                'b_step': self.ui.lineEditBStep.text(),
                                'b0_threshold': self.ui.lineEditB0Threshold.text(),
                                'delta': self.ui.lineEditDelta.text(),
                                'small_delta': self.ui.lineEditSmallDelta.text(),
                                'te': self.ui.lineEditTE.text(),
                                'schemefile': self.ui.lineEditSchemefile.text(),
                                'generate_schemefile': self.ui.radioButtonGenerateSchemefile.isChecked(),
                                'diff_par': self.ui.lineEditDiffPar.text(),
                                'diff_iso': self.ui.lineEditDiffIso.text(),
                                'ic_vf_lb': self.ui.lineEditICVFLB.text(),
                                'ic_vf_ub': self.ui.lineEditICVFUB.text(),
                                'ic_vf_n': self.ui.lineEditICVFN.text(),
                                'ic_od_lb': self.ui.lineEditICODLB.text(),
                                'ic_od_ub': self.ui.lineEditICODUB.text(),
                                'ic_od_n': self.ui.lineEditICODN.text(),
                                'diff_is': self.ui.lineEditDiffIS.text(),
                                'radius_lb': self.ui.lineEditRadiusLB.text(),
                                'radius_ub': self.ui.lineEditRadiusUB.text(),
                                'radius_n': self.ui.lineEditRadiusN.text(),
                                'diff_in_lb': self.ui.lineEditDiffINLB.text(),
                                'diff_in_ub': self.ui.lineEditDiffINUB.text(),
                                'diff_in_n': self.ui.lineEditDiffINN.text(),
                                'diff_iso_lb': self.ui.lineEditDiffECILB.text(),
                                'diff_iso_ub': self.ui.lineEditDiffECIUB.text(),
                                'diff_iso_n': self.ui.lineEditDiffECIN.text(),
                                'lambda1': self.ui.lineEditLambda1.text(),
                                'lambda2': self.ui.lineEditLambda2.text()
                            }
                            break
                config['N_RECENTS']['n_recents'] = str(n+1) if n+1 <= n_max else str(n_max)
            with open(amico_config_file, 'w') as configfile:
                config.write(configfile)

    def closeEvent(self, event):
        self.save_data()
        event.accept()

    def init_image_preview(self):
        self.ui.graphicsView.show()
        self.images = [file for file in listdir(self.preview_path) if file.endswith('.nii.gz')]
        self.ui.comboBoxImagePreview.addItems(self.images)
        self.switch_image()

    def set_enabled_sections(self, enabled):
        self.ui.groupBoxModelSelection.setEnabled(enabled)
        self.ui.groupBoxData.setEnabled(enabled)
        self.ui.groupBoxModelSetup.setEnabled(enabled)
        self.ui.groupBoxModelFit.setEnabled(enabled)

    @Slot()
    def switch_image(self):
        if self.ui.comboBoxImagePreview.currentText() != '':
            img = nib.load(path.join(self.preview_path, self.ui.comboBoxImagePreview.currentText()))
            img_data = img.get_fdata()
            
            self.sagittal_coronal = np.flip(img_data, axis=1)
            self.sagittal_coronal = np.flip(self.sagittal_coronal, axis=2)
            self.axial = np.flip(img_data, axis=1)

            self.view = 'axial'
            slice = self.axial.shape[2] // 2
            self.ui.horizontalSlider.setMinimum(0)
            self.ui.horizontalSlider.setMaximum(self.axial.shape[2]-1)
            self.ui.horizontalSlider.setValue(slice)
            self.ui.graphicsView.setImage(self.axial[:, :, slice])

    @Slot()
    def switch_view(self, view):
        if view == 'sagittal' and self.view != 'sagittal':
            self.view = 'sagittal'
            slice = self.sagittal_coronal.shape[0] // 2
            self.ui.horizontalSlider.setMaximum(self.sagittal_coronal.shape[0]-1)
            self.ui.horizontalSlider.setValue(slice)
            self.ui.graphicsView.setImage(self.sagittal_coronal[slice, :, :])
        elif view == 'coronal' and self.view != 'coronal':
            self.view = 'coronal'
            slice = self.sagittal_coronal.shape[1] // 2
            self.ui.horizontalSlider.setMaximum(self.sagittal_coronal.shape[1]-1)
            self.ui.horizontalSlider.setValue(slice)
            self.ui.graphicsView.setImage(self.sagittal_coronal[:, slice, :])
        elif view == 'axial' and self.view != 'axial':
            self.view = 'axial'
            slice = self.axial.shape[2] // 2
            self.ui.horizontalSlider.setMaximum(self.axial.shape[2]-1)
            self.ui.horizontalSlider.setValue(slice)
            self.ui.graphicsView.setImage(self.axial[:, :, slice])
            
    @Slot()
    def update_slice(self):
        slice = self.ui.horizontalSlider.value()
        if self.view == 'sagittal':
            self.ui.graphicsView.setImage(self.sagittal_coronal[slice, :, :])
        elif self.view == 'coronal':
            self.ui.graphicsView.setImage(self.sagittal_coronal[:, slice, :])
        elif self.view == 'axial':
            self.ui.graphicsView.setImage(self.axial[:, :, slice])

    @Slot()
    def load_data(self):
        try:
            self.check_validators()
        except ValueError as e:
            QMessageBox.critical(self, 'Error', str(e))
            return

        self.setup_sections()

        # Save data for the preview
        self.preview_path = path.join(self.ui.lineEditSubject.text(), 'AMICO', self.ui.comboBoxModel.currentText())

        # self.ui.widget.setEnabled(False)
        self.set_enabled_sections(False)
        self.ui.progressBar.reset()
        self.ui.progressBar.show()

        self.load_data_worker = LoadDataWorker(
            self.ui.comboBoxModel.currentText(),
            self.ui.lineEditStudy.text(),
            self.ui.lineEditSubject.text(),
            self.ui.lineEditDWI.text(),
            self.ui.lineEditB0Threshold.text(),
            self.ui.lineEditMask.text(),
            self.ui.lineEditBvals.text() if self.ui.radioButtonGenerateSchemefile.isChecked() else None,
            self.ui.lineEditBvecs.text() if self.ui.radioButtonGenerateSchemefile.isChecked() else None,
            self.ui.lineEditBStep.text() if self.ui.radioButtonGenerateSchemefile.isChecked() else None,
            self.ui.lineEditDelta.text() if self.ui.comboBoxModel.currentText() == 'SANDI' and self.ui.radioButtonGenerateSchemefile.isChecked() else None,
            self.ui.lineEditSmallDelta.text() if self.ui.comboBoxModel.currentText() == 'SANDI' and self.ui.radioButtonGenerateSchemefile.isChecked() else None,
            self.ui.lineEditTE.text() if self.ui.comboBoxModel.currentText() == 'SANDI' and self.ui.radioButtonGenerateSchemefile.isChecked() else None,
            self.ui.lineEditSchemefile.text() if self.ui.radioButtonLoadSchemefile.isChecked() else None,
        )

        self.load_data_worker.complete_signal.connect(self.load_data_complete)
        self.load_data_worker.error_signal.connect(self.load_data_error)
        self.load_data_worker.start()

    @Slot()
    def load_data_complete(self):
        self.ui.progressBar.hide()
        # self.ui.widget.setEnabled(True)
        self.set_enabled_sections(True)
        self.ui.groupBoxModelSelection.setEnabled(True)
        self.ui.groupBoxData.setEnabled(True)
        self.ui.groupBoxModelSetup.setEnabled(True)
        self.ui.groupBoxModelFit.setEnabled(False)

    @Slot()
    def load_data_error(self, message):
        self.ui.progressBar.hide()
        # self.ui.widget.setEnabled(True)
        self.set_enabled_sections(True)
        self.ui.groupBoxModelSelection.setEnabled(True)
        self.ui.groupBoxData.setEnabled(True)

        QMessageBox.critical(self, 'Error', message)

    @Slot()
    def setup_model(self):
        try:
            self.check_validators()
        except ValueError as e:
            QMessageBox.critical(self, 'Error', str(e))
            return
        
        # TODO reset_preview()
        self.ui.comboBoxImagePreview.clear()
        self.ui.graphicsView.hide()
        self.ui.graphicsView.setPredefinedGradient('grey')

        # self.ui.widget.setEnabled(False)
        self.set_enabled_sections(False)
        self.ui.progressBar.reset()
        self.ui.progressBar.show()

        self.setup_model_worker = SetupModelWorker(
            model=self.load_data_worker.model,
            evaluation=self.load_data_worker.evaluation,
            lmax=self.lmax,
            ndirs=self.ndirs_selected,
            openblas_num_threads=self.openblas_num_threads,
            diff_par=self.ui.lineEditDiffPar.text() if self.load_data_worker.model == 'NODDI' else None,
            diff_iso=self.ui.lineEditDiffIso.text() if self.load_data_worker.model == 'NODDI' else None,
            ic_vf_lb=self.ui.lineEditICVFLB.text() if self.load_data_worker.model == 'NODDI' else None,
            ic_vf_ub=self.ui.lineEditICVFUB.text() if self.load_data_worker.model == 'NODDI' else None,
            ic_vf_n=self.ui.lineEditICVFN.text() if self.load_data_worker.model == 'NODDI' else None,
            ic_od_lb=self.ui.lineEditICODLB.text() if self.load_data_worker.model == 'NODDI' else None,
            ic_od_ub=self.ui.lineEditICODUB.text() if self.load_data_worker.model == 'NODDI' else None,
            ic_od_n=self.ui.lineEditICODN.text() if self.load_data_worker.model == 'NODDI' else None,
            diff_is=self.ui.lineEditDiffIS.text() if self.load_data_worker.model == 'SANDI' else None,
            radius_lb=self.ui.lineEditRadiusLB.text() if self.load_data_worker.model == 'SANDI' else None,
            radius_ub=self.ui.lineEditRadiusUB.text() if self.load_data_worker.model == 'SANDI' else None,
            radius_n=self.ui.lineEditRadiusN.text() if self.load_data_worker.model == 'SANDI' else None,
            diff_in_lb=self.ui.lineEditDiffINLB.text() if self.load_data_worker.model == 'SANDI' else None,
            diff_in_ub=self.ui.lineEditDiffINUB.text() if self.load_data_worker.model == 'SANDI' else None,
            diff_in_n=self.ui.lineEditDiffINN.text() if self.load_data_worker.model == 'SANDI' else None,
            diff_eciso_lb=self.ui.lineEditDiffECILB.text() if self.load_data_worker.model == 'SANDI' else None,
            diff_eciso_ub=self.ui.lineEditDiffECIUB.text() if self.load_data_worker.model == 'SANDI' else None,
            diff_eciso_n=self.ui.lineEditDiffECIN.text() if self.load_data_worker.model == 'SANDI' else None
        )

        self.setup_model_worker.complete_signal.connect(self.setup_model_complete)
        self.setup_model_worker.error_signal.connect(self.setup_model_error)
        self.setup_model_worker.start()

    @Slot()
    def setup_model_complete(self):
        self.ui.progressBar.hide()
        # self.ui.widget.setEnabled(True)
        self.set_enabled_sections(True)
        self.ui.groupBoxModelSelection.setEnabled(True)
        self.ui.groupBoxData.setEnabled(True)
        self.ui.groupBoxModelSetup.setEnabled(True)
        self.ui.groupBoxModelFit.setEnabled(True)
        self.ui.groupBoxImagePreview.setEnabled(False)

    @Slot()
    def setup_model_error(self, message):
        self.ui.progressBar.hide()
        # self.ui.widget.setEnabled(True)
        self.set_enabled_sections(True)
        self.ui.groupBoxModelSelection.setEnabled(True)
        self.ui.groupBoxData.setEnabled(True)
        self.ui.groupBoxModelSetup.setEnabled(True)

        QMessageBox.critical(self, 'Error', message)

    @Slot()
    def fit_model(self):
        try:
            self.check_validators()
        except ValueError as e:
            QMessageBox.critical(self, 'Error', str(e))
            return

        # self.ui.widget.setEnabled(False)
        self.set_enabled_sections(False)
        self.ui.progressBar.reset()
        self.ui.progressBar.show()

        self.fit_model_worker = FitModelWorker(
            evaluation=self.load_data_worker.evaluation,
            joblib_backend=self.joblib_backend_selected,
            joblib_num_threads=self.joblib_num_threads,
            lambda1=self.ui.lineEditLambda1.text(),
            lambda2=self.ui.lineEditLambda2.text()
        )
        self.fit_model_worker.complete_signal.connect(self.fit_model_complete)
        self.fit_model_worker.error_signal.connect(self.fit_model_error)
        self.fit_model_worker.start()

    @Slot()
    def fit_model_complete(self):
        self.ui.progressBar.hide()
        # self.ui.widget.setEnabled(True)
        self.set_enabled_sections(True)
        self.ui.groupBoxModelSelection.setEnabled(True)
        self.ui.groupBoxData.setEnabled(True)
        self.ui.groupBoxModelSetup.setEnabled(True)
        self.ui.groupBoxModelFit.setEnabled(True)
        self.ui.groupBoxImagePreview.setEnabled(True)
        self.init_image_preview()

    @Slot()
    def fit_model_error(self, message):
        self.ui.progressBar.hide()
        # self.ui.widget.setEnabled(True)
        self.set_enabled_sections(True)
        self.ui.groupBoxModelSelection.setEnabled(True)
        self.ui.groupBoxData.setEnabled(True)
        self.ui.groupBoxModelSetup.setEnabled(True)
        self.ui.groupBoxModelFit.setEnabled(True)

        QMessageBox.critical(self, 'Error', message)

    @Slot()
    def switch_model(self):
        self.setup_sections()

        if self.ui.comboBoxModel.currentText() == 'NODDI':
            # Schemefile
            self.ui.groupBoxGenerateSchemefileSANDI.hide()
            
            # Model setup
            self.ui.groupBoxNODDISetup.show()
            self.ui.groupBoxSANDISetup.hide()
            self.ui.checkBoxAdvModelSetup.setChecked(False)
            self.ui.groupBoxAdvNODDISetup.hide()
            self.ui.groupBoxAdvSANDISetup.hide()

            # Remember current options
            # if self.ui.checkBoxAdvModelSetup.isChecked():
            #     self.ui.groupBoxAdvNODDISetup.show()
            # else:
            #     self.ui.groupBoxAdvNODDISetup.hide()
            # self.ui.groupBoxSANDISetup.hide()
            # self.ui.groupBoxAdvSANDISetup.hide()

            # Model fit
            self.ui.lineEditLambda1.setText(self.config.get('DEFAULT_NODDI', 'lambda1'))
            self.ui.lineEditLambda2.setText(self.config.get('DEFAULT_NODDI', 'lambda2'))
            self.ui.checkBoxAdvModelFit.setChecked(False)
        elif self.ui.comboBoxModel.currentText() == 'SANDI':
            # Schemefile
            self.ui.groupBoxGenerateSchemefileSANDI.show()

            # Model setup
            self.ui.groupBoxSANDISetup.show()
            self.ui.groupBoxNODDISetup.hide()
            self.ui.checkBoxAdvModelSetup.setChecked(False)
            self.ui.groupBoxAdvSANDISetup.show()
            self.ui.groupBoxAdvNODDISetup.hide()

            # Remember current options
            # self.ui.groupBoxSANDISetup.show()
            # if self.ui.checkBoxAdvModelSetup.isChecked():
            #     self.ui.groupBoxAdvSANDISetup.show()
            # else:
            #     self.ui.groupBoxAdvSANDISetup.hide()
            # self.ui.groupBoxNODDISetup.hide()
            # self.ui.groupBoxAdvNODDISetup.hide()

            # Model fit
            self.ui.lineEditLambda1.setText(self.config.get('DEFAULT_SANDI', 'lambda1'))
            self.ui.lineEditLambda2.setText(self.config.get('DEFAULT_SANDI', 'lambda2'))
            self.ui.checkBoxAdvModelFit.setChecked(True)
        self.switch_advanced_fit_options()

    @Slot()
    def switch_advanced_setup_options(self):
        if self.ui.comboBoxModel.currentText() == 'NODDI':
            if self.ui.checkBoxAdvModelSetup.isChecked():
                self.ui.groupBoxAdvNODDISetup.show()
            else:
                self.ui.groupBoxAdvNODDISetup.hide()
        # elif self.ui.comboBoxModel.currentText() == 'SANDI':
        #     if self.ui.checkBoxAdvModelSetup.isChecked():
        #         self.ui.groupBoxAdvSANDISetup.show()
        #     else:
        #         self.ui.groupBoxAdvSANDISetup.hide()

    @Slot()
    def switch_advanced_fit_options(self):
        if self.ui.checkBoxAdvModelFit.isChecked():
            self.ui.groupBoxFitSetup.show()
        else:
            self.ui.groupBoxFitSetup.hide()

    @Slot()
    def switch_schemefile(self):
        if self.ui.radioButtonGenerateSchemefile.isChecked():
            self.ui.groupBoxGenerateSchemefile.setEnabled(True)
            self.ui.groupBoxGenerateSchemefileSANDI.setEnabled(True)
            self.ui.groupBoxLoadSchemefile.setEnabled(False)
        elif self.ui.radioButtonLoadSchemefile.isChecked():
            self.ui.groupBoxLoadSchemefile.setEnabled(True)
            self.ui.groupBoxGenerateSchemefile.setEnabled(False)
            self.ui.groupBoxGenerateSchemefileSANDI.setEnabled(False)

    @Slot()
    def load_directory(self, line_edit: QLineEdit, caption='Select directory', current_directory=None):
        if current_directory and path.isdir(current_directory):
            directory = QFileDialog.getExistingDirectory(self, caption, current_directory)
        else:
            directory = QFileDialog.getExistingDirectory(self, caption, None)
        if directory:
            line_edit.setText(directory)

    @Slot()
    def load_file(self, line_edit: QLineEdit, caption='Select file', filter=None):
        filter = filter + ';;All Files (*)' if filter else 'All Files (*)'
        if path.isdir(self.ui.lineEditSubject.text()):
            filename = QFileDialog.getOpenFileName(self, caption, self.ui.lineEditSubject.text(), filter)
        elif path.isdir(self.ui.lineEditStudy.text()):
            filename = QFileDialog.getOpenFileName(self, caption, self.ui.lineEditStudy.text(), filter)
        else:
            filename = QFileDialog.getOpenFileName(self, caption, None, filter)
        if filename[0]:
            line_edit.setText(filename[0])
