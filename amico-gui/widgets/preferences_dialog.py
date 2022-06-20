from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Slot
from ui.preferences_dialog_ui import Ui_dialog
import configparser
from multiprocessing import cpu_count

from os import path
amico_config_file = path.abspath(path.join(path.dirname(__file__), 'amico_gui.cfg'))

class PreferencesDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_dialog()
        self.ui.setupUi(self)

        # self.ndirs_default = ndirs_default
        # self.lmax = lmax
        # self.openblas_num_threads = openblas_num_threads
        # self.joblib_backend_default = joblib_backend_default

        self.init()

    def init(self):
        self.setModal(True)
        self.setup_options()
        self.setup_slots()

    def setup_options(self):
        self.config = configparser.ConfigParser()
        self.config.read(amico_config_file)
        self.lmax = self.config['GLOBAL']['lmax']
        self.ndirs = self.config['GLOBAL']['ndirs'].split(', ')
        self.ndirs_selected = self.config['GLOBAL']['ndirs_selected']
        self.openblas_num_threads = self.config['GLOBAL']['openblas_num_threads']
        self.joblib_backends = self.config['GLOBAL']['joblib_backends'].split(', ')
        self.joblib_backend_selected = self.config['GLOBAL']['joblib_backend_selected']
        self.joblib_num_threads = self.config['GLOBAL']['joblib_num_threads']

        self.ui.lineEditLmax.setText(self.lmax)
        self.ui.comboBoxNdirs.addItems(self.ndirs)
        self.ui.comboBoxNdirs.setCurrentText(self.ndirs_selected)
        self.ui.comboBoxOpenBLAS.addItems([str(i) for i in range(1, cpu_count() + 1)])
        self.ui.comboBoxOpenBLAS.setCurrentText(self.openblas_num_threads)
        self.ui.comboBoxJoblibBackend.addItems(self.joblib_backends)
        self.ui.comboBoxJoblibBackend.setCurrentText(self.joblib_backend_selected)
        self.ui.comboBoxJoblibNumThreads.addItems([str(i) for i in range(1, cpu_count() + 1)])
        if self.joblib_num_threads == 'auto':
            self.ui.comboBoxJoblibNumThreads.setCurrentText(str(cpu_count()))
        else:
            self.ui.comboBoxJoblibNumThreads.setCurrentText(self.joblib_num_threads)

    def setup_slots(self):
        self.ui.pushButtonConfirm.clicked.connect(self.setup_preferences)
        self.ui.pushButtonCancel.clicked.connect(self.close)

    @Slot()
    def setup_preferences(self):
        self.lmax = self.ui.lineEditLmax.text()
        self.ndirs_selected = self.ui.comboBoxNdirs.currentText()
        self.openblas_num_threads = self.ui.comboBoxOpenBLAS.currentText()
        self.joblib_backend_selected = self.ui.comboBoxJoblibBackend.currentText()
        self.joblib_num_threads = self.ui.comboBoxJoblibNumThreads.currentText()

        with open(amico_config_file, 'w') as configfile:
            self.config['GLOBAL']['lmax'] = self.lmax
            self.config['GLOBAL']['ndirs_selected'] = self.ndirs_selected
            self.config['GLOBAL']['openblas_num_threads'] = self.openblas_num_threads
            self.config['GLOBAL']['joblib_backend_selected'] = self.joblib_backend_selected
            self.config['GLOBAL']['joblib_num_threads'] = self.joblib_num_threads
            self.config.write(configfile)

        self.close()
