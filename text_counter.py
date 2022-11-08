import re

from PySide6 import QtWidgets
from interface import Ui_MainWindow

class Programm(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(Programm, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnCounter.clicked.connect(self.counter)

    def counter(self):
        txt = self.ui.textEdit.toPlainText()

        # Символы
        symb = re.findall(r"\S", txt)
        self.ui.lblSymb.setText(f"Символов в тексте: {len(symb)}")

        # Слова
        word = re.split(r"\W|\d|_", txt)
        word = [i for i in word if not i == ""]
        self.ui.lblWord.setText(f"Слов в тексте: {len(word)}")

        # Цифры
        value = re.findall(r"\d", txt)
        self.ui.lblValue.setText(f"Цифр в тексте: {len(value)}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication()
    window = Programm()
    window.show()
    sys.exit(app.exec())
