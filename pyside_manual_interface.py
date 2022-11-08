from PySide6 import QtWidgets, QtCore

class Programm(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(Programm, self).__init__(parent)

        self.label = QtWidgets.QLabel()
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setText("Привет мир!")
        self.button = QtWidgets.QPushButton()
        self.button.setText("Выход из программы")

        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.button)
        self.setLayout(self.vbox)

        self.button.clicked.connect(lambda: app.quit())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication()
    window = Programm()
    window.setWindowTitle("Моя первая программа")
    window.resize(300, 100)
    window.show()
    sys.exit(app.exec())
