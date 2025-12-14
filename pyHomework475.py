import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox

class Schedule(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dars jadvali")

        self.data = {
            "Dushanba": ["Matematika", "Fizika"],
            "Seshanba": ["Ingliz tili", "Tarix"]
        }

        layout = QVBoxLayout()
        self.combo = QComboBox()
        self.combo.addItems(self.data.keys())
        self.combo.currentTextChanged.connect(self.show)

        self.label = QLabel()

        layout.addWidget(self.combo)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def show(self, day):
        self.label.setText(", ".join(self.data[day]))

app = QApplication(sys.argv)
win = Schedule()
win.show()
app.exec_()
