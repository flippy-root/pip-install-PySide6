from PySide6 import QtWidgets
import interface
from PySide6.QtWidgets import QButtonGroup

class Programm(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Programm, self).__init__(parent)
        self.ui = interface.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.BtnRes.clicked.connect(self.calc)

    def calc(self):
        if self.ui.rBtnPlus.isChecked():
            value_one = int(self.ui.value1.text())
            value_two = int(self.ui.value2.text())
            res = value_one + value_two
            self.ui.label_4.setText(str(res))
            group = QButtonGroup()
            group.addButton(self.ui.rBtnPlus)
            group.setExclusive(False)
            self.ui.rBtnPlus.setChecked(False)
            del group
        elif self.ui.rBtnMinus.isChecked():
            value_one = int(self.ui.value1.text())
            value_two = int(self.ui.value2.text())
            res = value_one - value_two
            self.ui.label_4.setText(str(res))
            group = QButtonGroup()
            group.addButton(self.ui.rBtnMinus)
            group.setExclusive(False)
            self.ui.rBtnMinus.setChecked(False)
            del group
        elif self.ui.rBtnMult.isChecked():
            value_one = int(self.ui.value1.text())
            value_two = int(self.ui.value2.text())
            res = value_one * value_two
            self.ui.label_4.setText(str(res))
            group = QButtonGroup()
            group.addButton(self.ui.rBtnMult)
            group.setExclusive(False)
            self.ui.rBtnMult.setChecked(False)
            del group
        elif self.ui.rBtnDel.isChecked():
            value_one = int(self.ui.value1.text())
            value_two = int(self.ui.value2.text())
            res = value_one / value_two
            if value_one == 0:
                self.ui.label_4.setText("На ноль делить нельзя!")
            else:
                self.ui.label_4.setText(str(res))
            group = QButtonGroup()
            group.addButton(self.ui.rBtnDel)
            group.setExclusive(False)
            self.ui.rBtnDel.setChecked(False)
            del group



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication()
    window = Programm()
    window.show()
    sys.exit(app.exec())
