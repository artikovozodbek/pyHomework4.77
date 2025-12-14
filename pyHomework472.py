import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox

class Budget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Byudjet")

        self.data = {
            "Yanvar": [1200000, 500000],
            "Fevral": [2000000, 800000]
        }

        layout = QVBoxLayout()
        self.combo = QComboBox()
        self.combo.addItems(self.data.keys())
        self.combo.currentTextChanged.connect(self.calc)

        self.label = QLabel("Jami xarajat")

        layout.addWidget(self.combo)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def calc(self, oy):
        self.label.setText(f"Jami: {sum(self.data[oy])} so'm")

app = QApplication(sys.argv)
win = Budget()
win.show()
app.exec_()
