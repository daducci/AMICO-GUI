# TODO to remove
from os import environ
from os.path import pathsep, abspath, dirname, join as path_join
environ['PATH'] += pathsep + abspath(path_join(dirname(__file__), 'jdk', 'bin'))
environ['PATH'] += pathsep + abspath(path_join(dirname(__file__), 'camino', 'bin'))
environ['CAMINO_HEAP_SIZE'] = '4000'

import sys
from PySide6.QtWidgets import QApplication
from widgets.main_window import MainWindow
from widgets.recents_dialog import RecentsDialog
import configparser

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open(abspath(path_join(dirname(__file__), 'log.txt')), 'w')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(
            str(message)
            .replace('\033[0;32m', '')
            .replace('\033[0m', '')
            .replace('\033[0;30;44m', '')
            .replace('\033[0;34m', '')
            .replace('\033[0;30;43m', '')
            .replace('\033[0;33m', '')
            .replace('\033[0;30;41m', '')
            .replace('\033[0;31m', '')
        )

    def flush(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    # main_window.setFixedSize(1500, 870)
    main_window.show()

    config = configparser.ConfigParser()
    # config.read('amico_gui.cfg')
    config.read(abspath(path_join(dirname(__file__), 'amico_gui.cfg')))
    if int(config['N_RECENTS']['n_recents']) > 0:
        recents_dialog = RecentsDialog()
        recents_dialog.show()
        recents_dialog.closeEvent = lambda event: (main_window.load_recent(recents_dialog.recent_section), event.accept())

    # Styling
    # with open('style.qss', 'r') as style_file:
    with open(abspath(path_join(dirname(__file__), 'style.qss')), 'r') as style_file:
        _style = style_file.read()
        app.setStyleSheet(_style)

    sys.stdout = Logger()

    sys.exit(app.exec())