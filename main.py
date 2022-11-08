from PySide6 import QtWidgets
import interface

class Programm(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Programm, self).__init__(parent)
        self.ui = interface.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(lambda:self.ui.label.setText("Привет, мир!"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication()
    window = Programm()
    window.show()
    sys.exit(app.exec())
