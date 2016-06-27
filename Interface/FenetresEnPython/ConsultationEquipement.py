from Interface.FenetresEnPython.ConsultationEquipementUI import Ui_ConsultationEquipement
import yaml
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout

from BDD.BonTravailManager import BonTravailManager
from BDD.EquipementManager import EquipementManager
from Interface.FenetresEnPython.ModificationEquipement import ModificationEquipement


class ConsultationEquipement(Ui_ConsultationEquipement):
    def __init__(self, widget):
        self.setupUi(widget)
        self.ajoutConsultationEquipement()


    def ajoutConsultationEquipement(self):
        #Creation de la liste pour manipuler les labels
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


        # A voir pour les bons de travaux
        self.listeLabel.append(self.labelCommentaires)
        #Efface le contenu des differents champs par defaut
        for label in self.listeLabel:
            label.clear()
        #Recuperation des differents attributs d''un equipement
        self.equipementManager = EquipementManager("DataBase_Equipement.json")
        self.bonDeTravailManager = BonTravailManager('DataBase_BDT.json', 'DataBase_Equipement.json')
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
        self.boutonModifierEquipement.setEnabled(False)
        self.boutonAjouterUnBon.setEnabled(False)
        self.boutonConsulterBon.setEnabled(False)
        self.comboBoxBons.clear()

        # self.comboBoxBons.addItem(icon2, "")

    def rechercherEquipement(self):
        '''
            Methode permettant la recherche de l'equipement par son ID
            Affichage des informations de l'equipement dans les labels correspondants
            :param: None
            :return:
        '''
        #Recuperation du dictionnaire de resultat
        equipementRecherche = dict()
        equipementRecherche["ID"] = self.lineEditId.text()
        listeEquipement = self.equipementManager.RechercherEquipement(equipementRecherche)

        if(any(listeEquipement)):
            #Cas ou l'equipement existe
            self.boutonModifierEquipement.setEnabled(True)
            self.boutonAjouterUnBon.setEnabled(True)
            self.boutonConsulterBon.setEnabled(False)
            self.equipement = listeEquipement[0]
            i = 0
            for cle in self.listeCleDonnees:
                #Recuperation des donnees sous forme de string
                self.listeLabel[i].setText(str(self.equipement[cle]))
                i += 1
            self.rechercherBonDeTravailAssocie()
        else:
            #Cas ou l'equipement n'existe pas
            self.boutonModifierEquipement.setEnabled(False)

    def rechercherBonDeTravailAssocie(self):
        '''
            Recuperation des bons de travails associe a un equipement
            Affichage des numeros des bons dans la liste deroulantes
            :param: None
            :return:
        '''
        #Recuperation des bons associees a l'equipement
        dictionnaireBDTRecherche = dict()
        #TODO : verifier que l'ID-EQ recupere bien que cet ID
        dictionnaireBDTRecherche["ID-EQ"] = self.lineEditId.text()
        listeBonDeTravail = self.bonDeTravailManager.RechercherBonTravail(dictionnaireBDTRecherche)
        self.comboBoxBons.clear()
        if(any(listeBonDeTravail)):
            #Dans le cas ou on a trouve des bons de travail, on les affiche
            self.boutonConsulterBon.setEnabled(True)
            icon2 = QtGui.QIcon()
            icon2.addPixmap(
                QtGui.QPixmap("../../../SIMM-2.0/Apprentissage Python/exercices/Hatim/Accueil/view-icon.png"),
                QtGui.QIcon.Normal, QtGui.QIcon.Off)
            for bdt in listeBonDeTravail:
                affichage = self.lineEditId.text() + "-" + bdt["ID-BDT"]
                self.comboBoxBons.addItem(icon2, affichage)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    consultationEquipement = QtWidgets.QWidget()
    consultationEquipementUI = ConsultationEquipement(consultationEquipement)
    consultationEquipement.show()
    sys.exit(app.exec_())
