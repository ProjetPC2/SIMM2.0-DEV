import yaml
from PyQt5 import QtGui, QtWidgets

from BDD.BonTravailManager import BonTravailManager
from BDD.EquipementManager import EquipementManager
from Interface.FenetresEnPython.Fichiers import pathEquipementDatabase, pathBonTravailDatabase
from Interface.FenetresEnPython.SuppressionEquipementUI import Ui_SuppressionEquipement


class SuppressionEquipement(Ui_SuppressionEquipement):
    def __init__(self, widget):
        self.setupUi(widget)
        self.ajoutSuppressionEquipement()

    def ajoutSuppressionEquipement(self):
        # Creation de la liste pour manipuler les labels
        self.listeLabel = list()
        self.listeLabel.append(self.labelCategorie)
        self.listeLabel.append(self.labelMarque)
        self.listeLabel.append(self.labelModele)
        self.listeLabel.append(self.labelNoDeSerie)
        self.listeLabel.append(self.labelSalle)
        self.listeLabel.append(self.labelCentreDeService)
        self.listeLabel.append(self.labelDateDaquisition)
        self.listeLabel.append(self.labelDateDuDernierEntretien)
        self.listeLabel.append(self.labelProvenance)
        self.listeLabel.append(self.labelEtatDeService)
        self.listeLabel.append(self.labelEtatDeConservation)
        self.listeLabel.append(self.labelCodeASSET)

        # A voir pour les bons de travaux
        self.listeLabel.append(self.labelCommentaires)
        # Efface le contenu des differents champs par defaut
        for label in self.listeLabel:
            label.clear()
        # Recuperation des differents attributs d''un equipement
        self.equipementManager = EquipementManager(pathEquipementDatabase, pathBonTravailDatabase)
        self.bonDeTravailManager = BonTravailManager(pathBonTravailDatabase, pathEquipementDatabase)
        # self.listeCleDonnees = list()
        conf_file = 'fichier_conf.yaml'  # pathname du fichier de configuration
        try:
            fichierConf = open(conf_file, 'r')  # try: ouvrir le fichier et le lire
            with fichierConf:
                self._conf = yaml.load(fichierConf)
        except IOError:  # attrape l'erreur IOError si elle se présente et renvoie
            print("Could not read file: ", conf_file)  # définir ce qu'il faut faire pour corriger
        # récupère la liste des 'accepted keys' dans le fichier de configuration
        self.listeCleDonnees = list(self._conf['champsAcceptes-Equipement'])
        fichierConf.close()

        self.listeEdit = list()
        self.equipement = None
        self.boutonAfficherEquipement.clicked.connect(self.rechercherEquipement)
        self.lineEditId.returnPressed.connect(self.rechercherEquipement)
        self.boutonConsulterBon.setEnabled(False)
        self.boutonSupprimerEquipement.setEnabled(False)
        self.boutonSupprimerEquipement.clicked.connect(self.supprimerEquipement)
        self.comboBoxBons.clear()


    def rechercherEquipement(self):
        '''
            Methode permettant la recherche de l'equipement par son ID
            Affichage des informations de l'equipement dans les labels correspondants
            :param: None
            :return:
        '''
        # Recuperation du dictionnaire de resultat
        if (self.lineEditId.text() != ""):
            equipementRecherche = dict()
            equipementRecherche["ID"] = self.lineEditId.text()
            listeEquipement = self.equipementManager.RechercherEquipement(equipementRecherche)

            if (any(listeEquipement)):
                # Cas ou l'equipement existe
                self.boutonSupprimerEquipement.setEnabled(True)
                self.boutonConsulterBon.setEnabled(False)
                self.equipement = listeEquipement[0]
                i = 0
                for cle in self.listeCleDonnees:
                    # Recuperation des donnees sous forme de string
                    self.listeLabel[i].setText(str(self.equipement[cle]))
                    i += 1
                self.rechercherBonDeTravailAssocie()
                self.rechercherBonDeTravailAssocie()
            else:
                # Cas ou l'equipement n'existe pas
                self.boutonSupprimerEquipement.setEnabled(False)
        else:
            print("Champ ID null")

    def rechercherBonDeTravailAssocie(self):
        '''
            Recuperation des bons de travails associe a un equipement
            Affichage des numeros des bons dans la liste deroulantes
            :param: None
            :return:
        '''
        # Recuperation des bons associees a l'equipement
        dictionnaireBDTRecherche = dict()
        # TODO : verifier que l'ID-EQ recupere bien que cet ID
        dictionnaireBDTRecherche["ID-EQ"] = self.lineEditId.text()
        listeBonDeTravail = self.bonDeTravailManager.RechercherBonTravail(dictionnaireBDTRecherche)
        self.comboBoxBons.clear()
        if (any(listeBonDeTravail)):
            # Dans le cas ou on a trouve des bons de travail, on les affiche
            self.boutonConsulterBon.setEnabled(True)
            icon2 = QtGui.QIcon()
            icon2.addPixmap(
                QtGui.QPixmap("../../../SIMM-2.0/Apprentissage Python/exercices/Hatim/Accueil/view-icon.png"),
                QtGui.QIcon.Normal, QtGui.QIcon.Off)
            for bdt in listeBonDeTravail:
                affichage = self.lineEditId.text() + "-" + bdt["ID-BDT"]
                self.comboBoxBons.addItem(icon2, affichage)

    def supprimerEquipement(self):
        self.equipementManager.SupprimerEquipement(self.equipement["ID"])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainFrame = QtWidgets.QWidget()
    ui = SuppressionEquipement(MainFrame)
    MainFrame.show()
    sys.exit(app.exec_())
