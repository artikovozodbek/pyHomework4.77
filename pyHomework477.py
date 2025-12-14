import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QListWidget

class Library(QWidget):
    def __init__(self):
        super().__init__()
        self.books = ["Python Asoslari", "Flask Dasturlash", "Sun'iy Intellekt"]

        layout = QVBoxLayout()
        self.search = QLineEdit()
        self.search.textChanged.connect(self.find)

        self.list = QListWidget()
        self.list.addItems(self.books)

        layout.addWidget(self.search)
        layout.addWidget(self.list)
        self.setLayout(layout)

    def find(self, text):
        self.list.clear()
        for book in self.books:
            if text.lower() in book.lower():
                self.list.addItem(book)

app = QApplication(sys.argv)
win = Library()
win.show()
app.exec_()
