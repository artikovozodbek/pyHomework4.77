import sys, random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

class RandomPick(QWidget):
    def __init__(self):
        super().__init__()
        self.students = ["Ali", "Vali", "Hasan"]

        layout = QVBoxLayout()
        self.label = QLabel("Ism")
        btn = QPushButton("Tanlash")
        btn.clicked.connect(self.pick)

        layout.addWidget(btn)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def pick(self):
        self.label.setText(random.choice(self.students))

app = QApplication(sys.argv)
win = RandomPick()
win.show()
app.exec_()
