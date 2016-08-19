from PyQt5.QtCore import pyqtSignal, QObject


class Communicate(QObject):
    #classe permettant la gestion des differents signaux
    aucunResultat = pyqtSignal()
    finChargement = pyqtSignal()
    sauvegardeTermine = pyqtSignal()
    enregistrementTermine = pyqtSignal()
    suppressionTermine = pyqtSignal()
    rechercheTermine = pyqtSignal()
    supportCree = pyqtSignal()
    motDePasseCorrect = pyqtSignal()