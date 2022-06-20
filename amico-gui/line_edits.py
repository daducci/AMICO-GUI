from PySide6.QtWidgets import QLineEdit
from os.path import isdir, isfile

class DirectoryLineEdit(QLineEdit):
    def dragEnterEvent(self, event):
        if len(event.mimeData().urls()) == 1 and isdir(event.mimeData().urls()[0].toLocalFile()):
            event.acceptProposedAction()

    def dropEvent(self, event):
        if len(event.mimeData().urls()) == 1 and isdir(event.mimeData().urls()[0].toLocalFile()):
            self.setText(event.mimeData().urls()[0].toLocalFile())
            event.acceptProposedAction()

class FileLineEdit(QLineEdit):
    def dragEnterEvent(self, event):
        if len(event.mimeData().urls()) == 1 and isfile(event.mimeData().urls()[0].toLocalFile()):
            event.acceptProposedAction()

    def dropEvent(self, event):
        if len(event.mimeData().urls()) == 1 and isfile(event.mimeData().urls()[0].toLocalFile()):
            self.setText(event.mimeData().urls()[0].toLocalFile())
            event.acceptProposedAction()
