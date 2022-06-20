from PySide6.QtGui import QValidator
from os.path import isdir, isfile

# Directory
class DirectoryValidator(QValidator):
    def __init__(self, parent=None):
        super().__init__(parent)

    def validate(self, directory, position):
        validator = QValidator.Invalid
        if directory or not directory:
            validator = QValidator.Intermediate
        if isdir(directory):
            validator = QValidator.Acceptable
        return validator, directory, position

# File
class FileValidator(QValidator):
    def __init__(self, parent=None):
        super().__init__(parent)

    def validate(self, filename, position):
        validator = QValidator.Invalid
        if filename or not filename:
            validator = QValidator.Intermediate
        if isfile(filename):
            validator = QValidator.Acceptable
        return validator, filename, position

class OptionalFileValidator(QValidator):
    def __init__(self, parent=None):
        super().__init__(parent)

    def validate(self, filename, position):
        validator = QValidator.Invalid
        if filename:
            validator = QValidator.Intermediate
        if not filename:
            validator = QValidator.Acceptable
        if isfile(filename):
            validator = QValidator.Acceptable
        return validator, filename, position

# Integer
class MajorZeroIntValidator(QValidator):
    def __init__(self, parent=None):
        super().__init__(parent)

    def validate(self, text, position):
        validator = QValidator.Invalid
        if text.isdigit():
            if int(text) > 0:
                validator = QValidator.Acceptable
        if not text:
            validator = QValidator.Intermediate
        return validator, text, position
        # if text == '':
        #     return QValidator.Intermediate, text, position
        # elif text.isdigit():
        #     if int(text) > 0:
        #         return QValidator.Acceptable, text, position
        #     else:
        #         return QValidator.Intermediate, text, position
        # else:
        #     return QValidator.Invalid, text, position

# Float
class NonNegativeDoubleValidator(QValidator):
    def __init__(self, parent=None):
        super().__init__(parent)

    def validate(self, text, position):
        validator = QValidator.Invalid
        if not text:
            validator = QValidator.Intermediate
        if text.replace('.', '', 1).isdigit():
            if float(text) >= 0:
                validator = QValidator.Acceptable
        return validator, text, position
        # if text == '':
        #     return QValidator.Intermediate, text, position
        # elif text.replace('.', '', 1).isdigit():
        #     if int(text) >= 0:
        #         return QValidator.Acceptable, text, position
        #     else:
        #         return QValidator.Intermediate, text, position
        # else:
        #     return QValidator.Invalid, text, position

class MajorZeroDoubleValidator(QValidator):
    def __init__(self, parent=None):
        super().__init__(parent)

    def validate(self, text, position):
        validator = QValidator.Invalid
        if not text:
            validator = QValidator.Intermediate
        if text.replace('.', '', 1).isdigit():
            if float(text) > 0:
                validator = QValidator.Acceptable
            else:
                validator = QValidator.Intermediate
        return validator, text, position
        # if text == '':
        #     return QValidator.Intermediate, text, position
        # elif text.replace('.', '', 1).isdigit():
        #     if float(text) > 0:
        #         return QValidator.Acceptable, text, position
        #     else:
        #         return QValidator.Intermediate, text, position
        # else:
        #     return QValidator.Invalid, text, position

class OptionalMajorZeroDoubleValidator(QValidator):
    def __init__(self, parent=None):
        super().__init__(parent)

    def validate(self, text, position):
        validator = QValidator.Invalid
        if not text:
            validator = QValidator.Intermediate
        if text.replace('.', '', 1).isdigit():
            if float(text) > 0:
                validator = QValidator.Acceptable
            else:
                validator = QValidator.Intermediate
        return validator, text, position
        # if text == '':
        #     return QValidator.Acceptable, text, position
        # elif text.replace('.', '', 1).isdigit():
        #     if float(text) > 0:
        #         return QValidator.Acceptable, text, position
        #     else:
        #         return QValidator.Intermediate, text, position
        # else:
        #     return QValidator.Invalid, text, position
