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
        # palette.setColor(palette.Background, Qt.transparent)
        # self.setPalette(palette)

    # def paintEvent(self, event):
    #
    #     painter = QPainter()
    #     painter.begin(self)
    #     painter.setRenderHint(QPainter.Antialiasing)
    #     painter.fillRect(event.rect(), QBrush(QColor(255, 255, 255, 127)))
    #     painter.setPen(QPen(Qt.NoPen))
    #
    #     for i in range(6):
    #         # if (self.counter / 5) % 6 == i:
    #         #     painter.setBrush(QBrush(QColor(127 + (self.counter % 5) * 32, 0, 0)))
    #         if (self.counter) % 6 == i:
    #             painter.setBrush(QBrush(QColor(200 , 0, 0)))
    #         else:
    #             painter.setBrush(QBrush(QColor(127, 127, 127)))
    #         painter.drawEllipse(
    #             self.width() / 2 + 30 * math.cos(2 * math.pi * i / 6.0) - 10,
    #             self.height() / 2 + 30 * math.sin(2 * math.pi * i / 6.0) - 10,
    #             20, 20)
    #         painter.drawText(self.width() / 2 + 30 * math.cos(2 * math.pi * i / 6.0) - 10,self.height() / 2 + 30 * math.sin(2 * math.pi * i / 6.0) - 10, "Aucun resultat")
    #
    #     painter.end()
    #     # print(self.width(), self.height())

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