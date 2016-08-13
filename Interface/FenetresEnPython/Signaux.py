from PyQt5.QtCore import pyqtSignal, QObject


class Communicate(QObject):

    aucunResultat = pyqtSignal()
    finChargement = pyqtSignal()
    sauvegardeTermine = pyqtSignal()
    enregistrement = pyqtSignal()
    suppressionTermine = pyqtSignal()