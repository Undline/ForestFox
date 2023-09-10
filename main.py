from PyQt6.QtWidgets import QApplication, QLabel

app = QApplication([])

label = QLabel("Something will happen soon...")
label.show()

app.exec()
