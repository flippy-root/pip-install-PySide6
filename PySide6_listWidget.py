from PySide6 import QtWidgets
import interface

class Programm(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(Programm, self).__init__(parent)
        self.ui = interface.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnAdd.clicked.connect(self.add_data)
        self.ui.btnDel.clicked.connect(self.del_data)

    def add_data(self):
        if not self.ui.lineEdit.text():
            return
        txt = self.ui.lineEdit.text()
        self.ui.listWidget.addItem(txt)
        self.ui.lineEdit.clear()

    def del_data(self):
        if self.ui.listWidget.currentItem():
            item = self.ui.listWidget.currentItem()
            self.ui.listWidget.takeItem(self.ui.listWidget.row(item))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication()
    window = Programm()
    window.show()
    sys.exit(app.exec())
