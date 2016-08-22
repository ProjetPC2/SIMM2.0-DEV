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

    #Fenetre Ajout Equipement

    signalVerificationEquipement = pyqtSignal()
    signalNouvelEquipement = pyqtSignal()
    signalModifierEquipement = pyqtSignal()


    #Fenetre Bon de travail
    chargerBonTravail = pyqtSignal()
    choisirCategoriePiecce = pyqtSignal()
    editionBonTravail = pyqtSignal()
    chercherEquipement = pyqtSignal()
    nouveauBonTravail = pyqtSignal()
    consultationBonTravail = pyqtSignal()
    #Fenetre support
    motDePasseCorrect = pyqtSignal()