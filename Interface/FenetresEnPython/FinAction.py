import sys
from threading import Thread

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget, QMainWindow, QTextEdit, QPushButton, QGridLayout


class FinAction(QWidget):
    def __init__(self, parent=None):

        QWidget.__init__(self, parent)
        palette = QPalette(self.palette())
        self.text = "Aucun Resultat"

    def paintEvent(self, event):

        qp = QPainter()
        qp.begin(self)
        qp.fillRect(event.rect(), QBrush(QColor(255, 255, 255, 127)))

        self.drawText(event, qp)
        qp.end()

    def drawText(self, event, qp):

        qp.setPen(QColor(0, 0, 0))
        qp.setFont(QFont('Decorative', 12, QFont.Bold))
        qp.drawText(event.rect(), Qt.AlignCenter, self.text)

    def showEvent(self, event):

        self.timer = self.startTimer(20)
        self.counter = 0

    def timerEvent(self, event):

        self.counter += 1
        self.update()
        if self.counter == 60:
            self.killTimer(self.timer)
            self.hide()

    def termine(self):
        self.killTimer(self.timer)
        self.hide()

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        widget = QWidget(self)
        self.editor = QTextEdit()
        self.editor.setPlainText("0123456789" * 100)
        layout = QGridLayout(widget)
        layout.addWidget(self.editor, 0, 0, 1, 3)
        button = QPushButton("Wait")
        layout.addWidget(button, 1, 1, 1, 1)

        self.setCentralWidget(widget)
        self.overlay = FinAction(self.centralWidget())
        print(widget.size())
        self.overlay.hide()
        button.clicked.connect(self.overlay.show)

    def resizeEvent(self, event):
        print(event)
        print("size", event.size())
        self.overlay.resize(event.size())
        event.accept()

class AttenteThread(Thread):
    def __init__(self, finAction):
        Thread.__init__(self)
        self.overlay = finAction


    def run(self):
        self.overlay.raise_()
        self.overlay.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())