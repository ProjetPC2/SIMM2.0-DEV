from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSignal, QObject


class Communicate(QObject):

    aucunResultat = pyqtSignal()
    finProcessus = pyqtSignal()
    sauvegardeTermine = pyqtSignal()
    enregistrement = pyqtSignal()