import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton

class Shop(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Savatcha")

        self.data = {"Olma": 5000, "Banan": 7000, "Sut": 12000}

        layout = QVBoxLayout()
        self.combo = QComboBox()
        self.combo.addItems(self.data.keys())

        self.count = QLineEdit()
        self.count.setPlaceholderText("Miqdor")

        self.label = QLabel("Summa")

        btn = QPushButton("Hisoblash")
        btn.clicked.connect(self.calc)

        layout.addWidget(self.combo)
        layout.addWidget(self.count)
        layout.addWidget(btn)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def calc(self):
        total = self.data[self.combo.currentText()] * int(self.count.text())
        text = f"{total} so'm"
        if total > 100000:
            text += " (Chegirma qo'llandi)"
        self.label.setText(text)

app = QApplication(sys.argv)
win = Shop()
win.show()
app.exec_()
