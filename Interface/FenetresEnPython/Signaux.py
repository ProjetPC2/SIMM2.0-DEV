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

    sauvegardePDF = pyqtSignal()
    signalVerificationEquipement = pyqtSignal()
    signalNouvelEquipement = pyqtSignal()
    signalModifierEquipement = pyqtSignal()

    #Fenetre Consultation Equipement
    afficherBonDeTravailAssocie = pyqtSignal()


    #Fenetre Bon de travail
    chargerBonTravail = pyqtSignal()
    choisirCategoriePiecce = pyqtSignal()
    editionBonTravail = pyqtSignal()
    chargerEquipement = pyqtSignal()
    nouveauBonTravail = pyqtSignal()
    consultationBonTravail = pyqtSignal()
    validerChoixPiece = pyqtSignal()
    aucunEquipement = pyqtSignal()
    confirmation = pyqtSignal()
    trier = pyqtSignal()
    chargerEquipementAPartirBon = pyqtSignal()
    aucunBon = pyqtSignal()
    #Fenetre Recherche Bon De Travail

    remplirTableau = pyqtSignal()
    nouvelleRecherche = pyqtSignal()

    #Statistique
    affichageProvenance = pyqtSignal()
    affichageCentreService = pyqtSignal()
    #Fenetre support
    motDePasseCorrect = pyqtSignal()