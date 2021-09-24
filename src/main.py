from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

# Metin Düzenleyici

class Window(QWidget):
    def __init__(self, title, shape, icon):
        super().__init__()
        self.title = title
        self.x, self.y, self.w, self.h = shape
        self.icon = QIcon(icon)
        self.file = ""
        self.vbox = QVBoxLayout()
        self.initUI()
        self.setLayout(self.vbox)
        self.show()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(self.icon)
        self.setGeometry(self.x, self.y, self.w, self.h)
        self.setFont(QFont("Arial", 11))

        hbox = QHBoxLayout()
        
        self.todo_text = QTextEdit()

        self.btns = QVBoxLayout()

        self.open_file = QPushButton(text="Open Folder", clicked=self.OpenFile)
        self.open_file.setFixedWidth(200)
        self.btns.addWidget(self.open_file)

        self.save_file = QPushButton(text="Save", clicked=self.SaveFile)
        self.save_file.setFixedWidth(200)
        self.btns.addWidget(self.save_file)
        self.btns.addStretch()

        hbox.addLayout(self.btns)
        hbox.addWidget(self.todo_text)

        self.vbox.addLayout(hbox)

    def OpenFile(self):
        dlg = QFileDialog()
        dlg.exec_()
        self.file = dlg.selectedFiles()[0]
        
        with open(self.file, "r") as f:
            data = f.read()
            self.todo_text.setText(data)

    def SaveFile(self):
        if self.file != "":
            with open(self.file, "w") as f:
                f.write(self.todo_text.toPlainText())
                QMessageBox.information(self, self.title, "File saved!")
        else:
            QMessageBox.information(self, self.title, "File can't saved!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window("Text Editor", (100, 100, 1300, 800), "../img/icon.jpg")
    app.setStyle("Windows")
    app.exec_()