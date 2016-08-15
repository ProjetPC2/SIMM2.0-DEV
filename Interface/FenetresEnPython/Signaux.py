from PyQt5.QtCore import pyqtSignal, QObject


class Communicate(QObject):

    aucunResultat = pyqtSignal()
    finChargement = pyqtSignal()
    sauvegardeTermine = pyqtSignal()
    enregistrementTermine = pyqtSignal()
    suppressionTermine = pyqtSignal()
    rechercheTermine = pyqtSignal()
