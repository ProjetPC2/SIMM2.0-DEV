from BDD.BonTravailManager import BonTravailManager
from BDD.EquipementManager import EquipementManager
from BDD.PieceManager import PieceManager
from Interface.FenetresEnPython.SuppressionBonDeTravailUI import Ui_SuppressionBonDeTravail
from PyQt5 import QtWidgets


class SuppressionBonDeTravail(Ui_SuppressionBonDeTravail):
    def __init__(self, widget):
        self.setupUi(widget)
        self.ajoutSuppressionBonDeTravail()

    def ajoutSuppressionBonDeTravail(self):

            self.lineEditID.setText("")
            # Connexion de l'appuie de la touche entree
            self.lineEditID.returnPressed.connect(self.chercherEquipement)

            # Creation des differents elements utiles pour la sauvegarde
            self.equipementManager = EquipementManager('DataBase_Equipement.yaml', 'DataBase_BDT.yaml')
            self.bonDeTravailManager = BonTravailManager('DataBase_BDT.yaml', 'DataBase_Equipement.yaml')
            self.pieceManager = PieceManager()

            self.equipementDictionnaire = dict()
            self.listeBonDeTravail = list()
            self.indiceBonDeTravail = 0

            self.listeLabelCache = list()
            self.listeLabelCache.append(self.labelCacheNomTech)
            self.listeLabelCache.append(self.labelCacheDate)
            self.listeLabelCache.append(self.labelCacheTemps)
            self.listeLabelCache.append(self.labelCacheDescSit)
            self.listeLabelCache.append(self.labelCacheDescInt)

            for label in self.listeLabelCache:
                label.hide()

            self.listeWidget = list()
            self.listeWidget.append(self.textEditDescIntervention)
            self.listeWidget.append(self.textEditDescSituation)
            self.listeWidget.append(self.timeEditTempsEstime)
            self.listeWidget.append(self.labelEcritureBonTravail)
            self.listeWidget.append(self.dateEdit)

            # Connexion des differents boutons
            self.boutonFlecheGauche.clicked.connect(self.bonTravailPrecedent)
            self.boutonFlecheDroite.clicked.connect(self.bonTravailSuivant)
            self.boutonFlecheDoubleDroite.clicked.connect(self.bonTravailDernier)
            self.boutonFlecheDoubleGauche.clicked.connect(self.bonTravailPremier)
            self.comboBoxOuvertFerme.currentTextChanged.connect(self.editionBonDeTravail)
            self.boutonSupprimerBon.clicked.connect(self.supprimerBonDeTravail
                                                    )
    def chercherEquipement(self):
        '''
            Recuperation de l'equipement associe a l'ID dans le cas ou il existe
            Affichage des informations de l'equipement dans les champs existants
            Recuperation des bons de travail associes a cet equipement
            :param: None
            :return:
        '''
        # On fait la requete a la BDD
        print("recherche equipement")
        dic_request = dict()
        dic_request['ID'] = self.lineEditID.text()
        listeTrouve = self.equipementManager.RechercherEquipement(dic_request)
        # On efface les bons de travail deja affiche
        self.listeBonDeTravail.clear()
        if (any(listeTrouve)):
            # Si on a trouve un equipement correspondant, on affiche les informations correspondantes
            self.equipementDictionnaire = listeTrouve[0]
            self.labelEcritureCatEquip.setText(self.equipementDictionnaire["CategorieEquipement"])
            self.labelEcritureCentreService.setText(self.equipementDictionnaire["CentreService"])
            self.labelEcritureMarque.setText(self.equipementDictionnaire["Marque"])
            self.labelEcritureSalle.setText(self.equipementDictionnaire["Salle"])
            self.labelEcritureModele.setText(self.equipementDictionnaire["Modele"])
            # On fait la recheche des bons de travail
            self.listeBonDeTravail = self.bonDeTravailManager.RechercherBonTravail({"ID-EQ": self.lineEditID.text()})
            self.indiceBonDeTravail = 0
            self.chargerBonTravail()
        else:
            # Dans le cas ou on ne trouve pas d'equipement associe a cet ID
            self.equipementDictionnaire = None
            self.labelEcritureCatEquip.clear()
            self.labelEcritureCentreService.clear()
            self.labelEcritureMarque.clear()
            self.labelEcritureSalle.clear()
            self.labelEcritureModele.clear()
            self.labelEcritureBonTravail.clear()
            self.dateEdit.clear()
            self.timeEditTempsEstime.clear()
            self.textEditDescSituation.clear()
            self.textEditDescIntervention.clear()

    def supprimerBonDeTravail(self):
        '''
           Methode permettant la sauvegarde du bon de travail
           Recuperation des informations des differents champs
           Puis sauvegarde dans la BDD
            :param: None
            :return:
        '''
        # Recuperation des differentes informations dans les champs de BDT
        dictionnaireDonnees = dict()
        dictionnaireDonnees["Date"] = self.dateEdit.date().toPyDate()
        dictionnaireDonnees["TempsEstime"] = str(self.timeEditTempsEstime.time().toPyTime())
        dictionnaireDonnees["DescriptionSituation"] = self.textEditDescSituation.toPlainText()
        dictionnaireDonnees["DescriptionIntervention"] = self.textEditDescIntervention.toPlainText()
        dictionnaireDonnees["EtatBDT"] = self.comboBoxOuvertFerme.currentText()
        if (any(self.equipementDictionnaire)):
            # On ajoute le bon de travail a un equipement existant
            self.bonDeTravailManager.SupprimerBonTravail(self.equipementDictionnaire["ID"], self.listeBonDeTravail[self.indiceBonDeTravail]["ID-BDT"])

    def chargerBonTravail(self):
        '''
            Methode permettant le chargement des informations d'un bon de travail
            Mise des informations du bon de travall dans les differents champs
             :param: None
             :return:
         '''
        if (any(self.listeBonDeTravail)):
            # Si un bon de travail a ete trouve, on remplit les differents champs associes
            self.dateEdit.setDate(self.listeBonDeTravail[self.indiceBonDeTravail]["Date"])
            self.textEditDescSituation.setText(self.listeBonDeTravail[self.indiceBonDeTravail]["DescriptionSituation"])
            self.textEditDescSituation.wordWrapMode()
            self.textEditDescIntervention.setText(
                self.listeBonDeTravail[self.indiceBonDeTravail]["DescriptionIntervention"])
            self.textEditDescIntervention.wordWrapMode()
            # Remplir le temps estime
            # TODO: Remplir la date associe au bon de travail
            # self.timeEditTempsEstime.setTime(self.listeBonDeTravail[self.indiceBonDeTravail]["TempsEstime"])
            if self.listeBonDeTravail[self.indiceBonDeTravail]["EtatBDT"] != "Ouvert":
                self.comboBoxOuvertFerme.setCurrentText("Fermé")
            idBDT = str(self.equipementDictionnaire["ID"]) + "-" + str(self.indiceBonDeTravail + 1)
            self.labelEcritureBonTravail.setText(idBDT)

    def bonTravailSuivant(self):
        '''
            Methode permettant d'afficher le bon de travail suivant
             :param: None
             :return:
         '''
        if (self.indiceBonDeTravail < len(self.listeBonDeTravail) - 1):
            self.indiceBonDeTravail += 1
            self.chargerBonTravail()

    def bonTravailPrecedent(self):
        '''
            Methode permettant d'afficher le bon de travail precedent
             :param: None
             :return:
         '''
        if (self.indiceBonDeTravail > 0):
            self.indiceBonDeTravail -= 1
            self.chargerBonTravail()

    def bonTravailPremier(self):
        '''
            Methode permettant de retourner au premier bon de travail
             :param: None
             :return:
         '''
        self.indiceBonDeTravail = 0
        self.chargerBonTravail()

    def bonTravailDernier(self):
        '''
            Methode permettant d'aller au dernier bon de travail
             :param: None
             :return:
         '''
        self.indiceBonDeTravail = len(self.listeBonDeTravail) - 1
        self.chargerBonTravail()

    def editionBonDeTravail(self):
        print("edition")
        if (self.comboBoxOuvertFerme.currentText() == "Ouvert"):
            self.dateEdit.setDisabled(False)
            self.timeEditTempsEstime.setDisabled(False)
            self.textEditDescSituation.setDisabled(False)
            self.textEditDescIntervention.setDisabled(False)
        else:
            self.dateEdit.setDisabled(True)
            self.timeEditTempsEstime.setDisabled(True)
            self.textEditDescSituation.setDisabled(True)
            self.textEditDescIntervention.setDisabled(True)
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainFrame = QtWidgets.QWidget()
    ui = SuppressionBonDeTravail(MainFrame)
    MainFrame.show()
    sys.exit(app.exec_())
