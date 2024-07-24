# app.py

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class SimpleApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Simple PyQt App')
        
        self.button = QPushButton('Click me', self)
        self.button.resize(100, 50)
        self.button.move(100, 100)
        self.button.clicked.connect(self.show_message)
        
        self.setGeometry(300, 300, 300, 200)
    
    def show_message(self):
        QMessageBox.information(self, 'Message', "Well, ain’t this place a geographical oddity. Two weeks from everywhere!")
        
def main():
    app = QApplication(sys.argv)
    ex = SimpleApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
