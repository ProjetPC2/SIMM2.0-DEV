import subprocess
import yaml
from PyQt5 import QtGui, QtWidgets

from BDD.BonTravailManagerSQLite import BonTravailManager
from BDD.EquipementManagerSQLite import EquipementManager
from Interface.FenetresEnPython.ConsultationEquipementUI import Ui_ConsultationEquipement
from threading import Thread

from Interface.FenetresEnPython.Fichiers import pathEquipementDatabase, pathBonTravailDatabase, pathFichierConf
from Interface.FenetresEnPython.Signaux import Communicate


class ConsultationEquipement(Ui_ConsultationEquipement):
    def __init__(self, widget):
        self.setupUi(widget)
        self.ajoutConsultationEquipement()
        self.chargement = Communicate()


    def ajoutConsultationEquipement(self):
        #Creation de la liste pour manipuler les labels
        self.listeBonDeTravail = list()
        self.listeLabel = list()
        self.listeLabel.append(self.labelID)
        self.listeLabel.append(self.labelCategorie)
        self.listeLabel.append(self.labelEtatDeService)
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
        self.listeLabel.append(self.labelEtatDeConservation)



        # A voir pour les bons de travaux
        self.listeLabel.append(self.labelCommentaires)
        self.listeLabel.append(self.labelConsultPDF)

        #Efface le contenu des differents champs par defaut
        for label in self.listeLabel:
            label.clear()
        #Recuperation des differents attributs d''un equipement
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

        self.signalFenetreConsultation = Communicate()
        self.signalFenetreConsultation.afficherBonDeTravailAssocie.connect(self.rechercherBonDeTravailAssocie)

        self.listeEdit = list()
        self.equipement = None
        self.boutonAfficherEquipement.clicked.connect(self.rechercherEquipementThread)
        self.lineEditId.returnPressed.connect(self.rechercherEquipementThread)
        self.boutonModifierEquipement.setEnabled(False)
        self.boutonAjouterUnBon.setEnabled(False)
        self.boutonConsulterBon.setEnabled(False)
        self.BoutonPDF.setEnabled(False)
        self.comboBoxBons.clear()
        self.BoutonPDF.clicked.connect(self.ouvrirPDF)

    def rechercherEquipement(self):
        '''
            Methode permettant la recherche de l'equipement par son ID
            Affichage des informations de l'equipement dans les labels correspondants
            :param: None
            :return:
        '''
        #Recuperation du dictionnaire de resultat
        if(self.lineEditId.text() != ""):
            self.nouvelleRecherche()
            equipementRecherche = dict()
            equipementRecherche["Id"] = self.lineEditId.text()
            listeEquipement = self.equipementManager.RechercherEquipement(equipementRecherche)
            print(listeEquipement)
            if(any(listeEquipement)):
                #Cas ou l'equipement existe
                self.equipement = listeEquipement[0]
                i = 0
                for cle in self.listeCleDonnees:
                    #Recuperation des donnees sous forme de string

                    if(cle == "DateAcquisition" or cle == "DateDernierEntretien"):
                        newDate = self.equipement[cle]
                        index = self.equipement[cle].find(" ")
                        if index > -1:
                            newDate = self.equipement[cle].split(" ")[0]
                        self.listeLabel[i].setText(str(newDate))
                    else:
                        print(i)
                        self.listeLabel[i].setText(str(self.equipement[cle]))

                    i += 1
                if (self.equipement["PdfPath"] != ""):
                    self.BoutonPDF.setEnabled(True)
                else:
                    self.BoutonPDF.setEnabled(False)
                self.boutonModifierEquipement.setEnabled(True)
                self.boutonAjouterUnBon.setEnabled(True)
                self.boutonConsulterBon.setEnabled(False)
                dictionnaireBDTRecherche = dict()
                dictionnaireBDTRecherche["IdEquipement"] = self.lineEditId.text()
                self.listeBonDeTravail = self.bonDeTravailManager.RechercherBonTravail(dictionnaireBDTRecherche)

                self.signalFenetreConsultation.afficherBonDeTravailAssocie.emit()
                # self.chargement.finChargement.emit()
            else:
                #Cas ou l'equipement n'existe pas
                self.boutonModifierEquipement.setEnabled(False)
                # self.chargement.finChargement.emit()
                self.chargement.aucunResultat.emit()
        else:
            print("Champ ID null")
        self.chargement.finChargement.emit()

    def nouvelleRecherche(self):
        for label in self.listeLabel:
            label.clear()
        self.boutonModifierEquipement.setEnabled(False)
        self.boutonConsulterBon.setEnabled(False)
        self.comboBoxBons.clear()

    def rechercherBonDeTravailAssocie(self):
        '''
            Recuperation des bons de travails associe a un equipement
            Affichage des numeros des bons dans la liste deroulantes
            :param: None
            :return:
        '''
        #Recuperation des bons associees a l'equipement
        self.comboBoxBons.clear()
        if(any(self.listeBonDeTravail)):
            #Dans le cas ou on a trouve des bons de travail, on les affiche
            self.boutonConsulterBon.setEnabled(True)
            icon2 = QtGui.QIcon()
            icon2.addPixmap(
                QtGui.QPixmap("Images/view-icon.png"),
                QtGui.QIcon.Normal, QtGui.QIcon.Off)
            for bdt in self.listeBonDeTravail:
                affichage = self.lineEditId.text() + "-" + str(bdt["NumeroBonTravail"])
                self.comboBoxBons.addItem(icon2, affichage)

    def rechercherEquipementThread(self):
        a = RechercherEquipement(self.rechercherEquipement)
        a.start()

    def ouvrirPDF(self):
        if(self.equipement is not None):
            if(self.equipement["PdfPath"] != ""):
                subprocess.Popen(self.equipement["PdfPath"], shell=True)

class RechercherEquipement(Thread):
    def __init__(self, fonction):
        Thread.__init__(self)
        self.fonction = fonction


    def run(self):
        self.fonction()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    consultationEquipement = QtWidgets.QWidget()
    consultationEquipementUI = ConsultationEquipement(consultationEquipement)
    consultationEquipement.show()
    sys.exit(app.exec_())
