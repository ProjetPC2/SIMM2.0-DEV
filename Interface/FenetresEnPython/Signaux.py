from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSignal, QObject


class Communicate(QObject):
    closeApp = pyqtSignal()
    finProcessus = pyqtSignal()