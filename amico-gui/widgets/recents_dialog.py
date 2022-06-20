from PySide6.QtWidgets import QDialog, QListWidgetItem
from PySide6.QtCore import Slot
from ui.recents_dialog_ui import Ui_dialog
import configparser

from os import path
amico_config_file = path.abspath(path.join(path.dirname(__file__), 'amico_gui.cfg'))

class RecentsDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_dialog()
        self.ui.setupUi(self)

        self.init()

    def init(self):
        self.setModal(True)

        self.setup_recents()
        self.setup_slots()

        self.recent_section = ''

    def get_recents(self):
        config = configparser.ConfigParser()
        config.read(amico_config_file)
        n = int(config['N_RECENTS']['n_recents'])
        self.recents = []
        for i in range(n, 0, -1):
            section = 'RECENT_' + str(i)
            if section in config:
                study = config[section]['study']
                subject = config[section]['subject']
                if study != '':
                    self.recents.append(
                        {
                            'section': section,
                            'item': QListWidgetItem(study + ' --> ' + subject) # TODO os.path.basename(study) + ' --> ' + os.path.basename(subject)
                        }
                    )

    def setup_recents(self):
        self.get_recents()
        for recent in self.recents:
            self.ui.listWidgetRecents.addItem(recent['item'])

    def setup_slots(self):
        self.ui.pushButtonLoad.clicked.connect(self.load_recent)
        self.ui.listWidgetRecents.itemDoubleClicked.connect(self.load_recent)
        self.ui.pushButtonClose.clicked.connect(self.close)

    @Slot()
    def load_recent(self):
        self.recent_section = self.recents[self.ui.listWidgetRecents.currentRow()]['section']
        self.close()