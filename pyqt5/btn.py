import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.btnUI()

    def btnUI(self):
        btn1=QPushButton('Button&1',self)
        btn1.setCheckable(True)
        btn1.toggle()

        btn2=QPushButton(self)
        btn2.setText('button&2')

        btn3=QPushButton('Button&3',self)
        btn3.setEnabled(False)

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        self.setLayout(vbox)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())