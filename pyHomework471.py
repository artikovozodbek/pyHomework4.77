import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox

class PhoneBook(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Telefon kitobi")

        self.data = {
            "Ali": "99890 111 11 11",
            "Vali": "99891 222 22 22"
        }

        layout = QVBoxLayout()

        self.combo = QComboBox()
        self.combo.addItems(self.data.keys())
        self.combo.currentTextChanged.connect(self.show_number)

        self.label = QLabel("Raqam shu yerda chiqadi")

        layout.addWidget(self.combo)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def show_number(self, name):
        self.label.setText(self.data[name])

app = QApplication(sys.argv)
win = PhoneBook()
win.show()
app.exec_()
