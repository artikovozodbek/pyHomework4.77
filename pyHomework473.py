import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class Office(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ofis")

        self.data = {"Dilshod": "Direktor", "Aziza": "Hisobchi"}

        layout = QVBoxLayout()

        self.name = QLineEdit()
        self.name.setPlaceholderText("Ism kiriting")

        self.job = QLineEdit()
        self.job.setPlaceholderText("Lavozim")

        self.label = QLabel("Natija")

        btn1 = QPushButton("Tekshirish")
        btn1.clicked.connect(self.check)

        btn2 = QPushButton("Qo'shish")
        btn2.clicked.connect(self.add)

        layout.addWidget(self.name)
        layout.addWidget(self.job)
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def check(self):
        ism = self.name.text()
        self.label.setText(self.data.get(ism, "Topilmadi"))

    def add(self):
        self.data[self.name.text()] = self.job.text()
        self.label.setText("Qo'shildi")

app = QApplication(sys.argv)
win = Office()
win.show()
app.exec_()
