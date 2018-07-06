from threading import Thread

import yaml
from PyQt5 import QtGui, QtWidgets

from BDD.BonTravailManagerSQLite import BonTravailManager
from BDD.EquipementManagerSQLite import EquipementManager
from Interface.FenetresEnPython.Fichiers import pathEquipementDatabase, pathBonTravailDatabase, pathFichierConf
from Interface.FenetresEnPython.Signaux import Communicate
from Interface.FenetresEnPython.SuppressionEquipementUI import Ui_SuppressionEquipement



class SuppressionEquipement(Ui_SuppressionEquipement):
    #Classe permettant la gestion de la suppression des equipements
    def __init__(self, widget):
        self.setupUi(widget)
        self.ajoutSuppressionEquipement()
        self.suppression = Communicate()

    def ajoutSuppressionEquipement(self):
        # Creation de la liste pour manipuler les labels
        self.listeLabel = list()
        self.listeLabel.append(self.labelId)
        self.listeLabel.append(self.labelCategorie)
        self.listeLabel.append(self.labelMarque)
        self.listeLabel.append(self.labelModele)
        self.listeLabel.append(self.labelNoDeSerie)
        self.listeLabel.append(self.labelSalle)
        self.listeLabel.append(self.labelUnite)
        self.listeLabel.append(self.labelDateDaquisition)
        self.listeLabel.append(self.labelDateDuDernierEntretien)
        self.listeLabel.append(self.labelFreqEntretien)
        self.listeLabel.append(self.labelProvenance)
        self.listeLabel.append(self.labelVoltage)
        self.listeLabel.append(self.labelEtatDeService)
        self.listeLabel.append(self.labelEtatDeConservation)

        # A voir pour les bons de travaux
        self.listeLabel.append(self.labelCommentaires)
 #       self.listeLabel.append(self.labelPDFPath)
        # Efface le contenu des differents champs par defaut
        for label in self.listeLabel:
            label.clear()
        # Recuperation des differents attributs d''un equipement
        self.equipementManager = EquipementManager(pathEquipementDatabase)
        self.bonDeTravailManager = BonTravailManager(pathBonTravailDatabase)
        try:
            fichierConf = open(pathFichierConf, 'r')  # try: ouvrir le fichier et le lire
            with fichierConf:
                self._conf = yaml.load(fichierConf)
        except IOError:  # attrape l'erreur IOError si elle se présente et renvoie
            print("Could not read file: ", pathFichierConf)  # définir ce qu'il faut faire pour corriger
        # récupère la liste des 'accepted keys' dans le fichier de configuration
        self.listeCleDonnees = list(self._conf['champsAcceptes-Equipement'])
        fichierConf.close()

        self.listeEdit = list()
        self.equipement = None

        self.signalSuppresion = Communicate()
        self.signalSuppresion.chargerEquipement.connect(self.chargerEquipement)
        self.signalSuppresion.nouvelleRecherche.connect(self.nouvelleRecherche)
        self.signalSuppresion.chargerBonTravail.connect(self.chargerBonTravail)

        self.boutonAfficherEquipement.clicked.connect(self.rechercherEquipementThread)
        self.lineEditId.returnPressed.connect(self.rechercherEquipementThread)
        self.boutonConsulterBon.setEnabled(False)
        self.boutonSupprimerEquipement.setEnabled(False)
        self.boutonSupprimerEquipement.clicked.connect(self.supprimerEquipementThread)
        self.comboBoxBons.clear()


    def rechercherEquipement(self):
        '''
            Methode permettant la recherche de l'equipement par son ID
            Affichage des informations de l'equipement dans les labels correspondants
            :param: None
            :return:
        '''
        # Recuperation du dictionnaire de resultat
        self.signalSuppresion.nouvelleRecherche.emit()
        if (self.lineEditId.text() != ""):
            equipementRecherche = dict()
            equipementRecherche["Id"] = self.lineEditId.text()
            listeEquipement = self.equipementManager.RechercherEquipement(equipementRecherche)

            if (any(listeEquipement)):
                # Cas ou l'equipement existe

                self.equipement = listeEquipement[0]
                self.signalSuppresion.chargerEquipement.emit()
                self.rechercherBonDeTravailAssocie()
                self.suppression.finChargement.emit()
            else:
                # Cas ou l'equipement n'existe pas
                self.boutonSupprimerEquipement.setEnabled(False)
                self.suppression.finChargement.emit()
                self.suppression.aucunResultat.emit()
        else:
            print("Champ ID null")
            self.suppression.finChargement.emit()


    def chargerEquipement(self):
        self.boutonSupprimerEquipement.setEnabled(True)
        self.boutonConsulterBon.setEnabled(False)
        i = 0
        for cle in self.listeCleDonnees:
            # Recuperation des donnees sous forme de string
            if cle == "PdfPath":
                pass
            else:
                self.listeLabel[i].setText(str(self.equipement[cle]))
            i += 1

    def nouvelleRecherche(self):
        for label in self.listeLabel:
            label.clear()
        self.boutonSupprimerEquipement.setEnabled(False)
        self.boutonConsulterBon.setEnabled(False)
        self.comboBoxBons.clear()

    def rechercherBonDeTravailAssocie(self):
        '''
            Recuperation des bons de travails associe a un equipement
            Affichage des numeros des bons dans la liste deroulantes
            :param: None
            :return:
        '''
        # Recuperation des bons associees a l'equipement
        dictionnaireBDTRecherche = dict()
        dictionnaireBDTRecherche["IdEquipement"] = self.lineEditId.text()
        self.listeBonDeTravail = self.bonDeTravailManager.RechercherBonTravail(dictionnaireBDTRecherche)
        if (any(self.listeBonDeTravail)):
            self.signalSuppresion.chargerBonTravail.emit()

    def chargerBonTravail(self):
        # Dans le cas ou on a trouve des bons de travail, on les affiche
        self.boutonConsulterBon.setEnabled(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap("Images/view-icon.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        for bdt in self.listeBonDeTravail:
            affichage = self.lineEditId.text() + "-" + str(bdt["NumeroBonTravail"])
            self.comboBoxBons.addItem(icon2, affichage)

    def supprimerEquipement(self):
        self.equipementManager.SupprimerEquipement(self.equipement["Id"])
        self.suppression.suppressionTermine.emit()

    def rechercherEquipementThread(self):
        a = fonctionThread(self.rechercherEquipement)
        a.start()

    def supprimerEquipementThread(self):
        thread = fonctionThread(self.supprimerEquipement)
        thread.start()

class fonctionThread(Thread):
    def __init__(self, fonction):
        Thread.__init__(self)
        self.fonction = fonction

    def run(self):
        self.fonction()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainFrame = QtWidgets.QWidget()
    ui = SuppressionEquipement(MainFrame)
    MainFrame.show()
    sys.exit(app.exec_())
