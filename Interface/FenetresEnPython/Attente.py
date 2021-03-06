import math
import sys
from threading import Thread

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget, QMainWindow, QTextEdit, QPushButton, QGridLayout


class Attente(QWidget):
    '''
        Classe permettant l'affichage d'un message pour faire patienter l'utilisateur
        lors du traitement de certaines requetes
    '''
    def __init__(self, texte, parent=None):
        QWidget.__init__(self, parent)
        palette = QPalette(self.palette())
        # palette.setColor(palette.Background, Qt.transparent)
        # self.setPalette(palette)
        self.text = texte

    def paintEvent(self, event):
        '''
            Methode gerant la creation de l'affichage graphique
        '''

        painter = QPainter()
        painter.begin(self)
        painter.setPen(QPen(Qt.NoPen))

        for i in range(6):
            if (self.counter) % 6 == i:
                painter.setBrush(QBrush(QColor(200 , 0, 0)))
            else:
                painter.setBrush(QBrush(QColor(127, 127, 127)))
            painter.drawEllipse(
                self.width() / 2 + 30 * math.cos(2 * math.pi * i / 6.0) - 10,
                self.height() / 2 + 30 * math.sin(2 * math.pi * i / 6.0) - 60,
                20, 20)
        painter.setPen(QColor(0, 0, 0))
        painter.setFont(QFont('Decorative', 12, QFont.Bold))
        painter.drawText(event.rect(), Qt.AlignCenter, self.text)
        painter.end()

    def showEvent(self, event):

        self.timer = self.startTimer(180)
        self.counter = 0

    def timerEvent(self, event):

        self.counter += 1
        self.update()
        if self.counter == 6000:
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
        self.overlay = Attente("Chargement", self.centralWidget())
        print(widget.size())
        self.overlay.hide()
        button.clicked.connect(self.overlay.show)

    def resizeEvent(self, event):
        print(event)
        print("size", event.size())
        self.overlay.resize(event.size())
        event.accept()

class AttenteThread(Thread):
    def __init__(self, Overlay):
        Thread.__init__(self)
        self.overlay = Overlay


    def run(self):
        self.overlay.raise_()
        self.overlay.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())