# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fenetreRechercheEquipement2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import datetime
import yaml
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem

from BDD.EquipementManager import EquipementManager


class RechercheEquipementUI(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1314, 1128)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Images/magnifier.png"))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        self.labelTitre = QtWidgets.QLabel(Form)
        self.labelTitre.setMinimumSize(QtCore.QSize(400, 0))
        self.labelTitre.setMaximumSize(QtCore.QSize(1000, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        self.labelTitre.setFont(font)
        self.labelTitre.setObjectName("labelTitre")
        self.gridLayout.addWidget(self.labelTitre, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.textEditNumeroSerie_2 = QtWidgets.QLineEdit(Form)
        self.textEditNumeroSerie_2.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.textEditNumeroSerie_2.setFont(font)
        self.textEditNumeroSerie_2.setStyleSheet("padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247, 247, 247)")
        self.textEditNumeroSerie_2.setObjectName("textEditNumeroSerie_2")
        self.gridLayout_3.addWidget(self.textEditNumeroSerie_2, 1, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.comboBoxCategorieEquipement_2 = QtWidgets.QComboBox(Form)
        self.comboBoxCategorieEquipement_2.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBoxCategorieEquipement_2.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.comboBoxCategorieEquipement_2.setFont(font)
        self.comboBoxCategorieEquipement_2.setStyleSheet("padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247, 247, 247)")
        self.comboBoxCategorieEquipement_2.setObjectName("comboBoxCategorieEquipement_2")
        self.comboBoxCategorieEquipement_2.addItem("")
        self.comboBoxCategorieEquipement_2.addItem("")
        self.comboBoxCategorieEquipement_2.addItem("")
        self.gridLayout_3.addWidget(self.comboBoxCategorieEquipement_2, 1, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.labelCategorieEquipement_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.labelCategorieEquipement_2.setFont(font)
        self.labelCategorieEquipement_2.setObjectName("labelCategorieEquipement_2")
        self.gridLayout_3.addWidget(self.labelCategorieEquipement_2, 0, 0, 1, 1)
        self.labelNumeroSerie_2 = QtWidgets.QLabel(Form)
        self.labelNumeroSerie_2.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.labelNumeroSerie_2.setFont(font)
        self.labelNumeroSerie_2.setObjectName("labelNumeroSerie_2")
        self.gridLayout_3.addWidget(self.labelNumeroSerie_2, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.comboBoxEtatService = QtWidgets.QComboBox(Form)
        self.comboBoxEtatService.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBoxEtatService.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.comboBoxEtatService.setFont(font)
        self.comboBoxEtatService.setStyleSheet("padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247, 247, 247)")
        self.comboBoxEtatService.setObjectName("comboBoxEtatService")
        self.comboBoxEtatService.addItem("")
        self.comboBoxEtatService.addItem("")
        self.comboBoxEtatService.addItem("")
        self.gridLayout_5.addWidget(self.comboBoxEtatService, 1, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.labelCentreService = QtWidgets.QLabel(Form)
        self.labelCentreService.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.labelCentreService.setFont(font)
        self.labelCentreService.setObjectName("labelCentreService")
        self.gridLayout_5.addWidget(self.labelCentreService, 0, 1, 1, 1)
        self.labelEtatService = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.labelEtatService.setFont(font)
        self.labelEtatService.setObjectName("labelEtatService")
        self.gridLayout_5.addWidget(self.labelEtatService, 0, 0, 1, 1)
        self.comboBoxCentreService = QtWidgets.QComboBox(Form)
        self.comboBoxCentreService.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBoxCentreService.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.comboBoxCentreService.setFont(font)
        self.comboBoxCentreService.setStyleSheet("padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247, 247, 247)")
        self.comboBoxCentreService.setObjectName("comboBoxCentreService")
        self.comboBoxCentreService.addItem("")
        self.comboBoxCentreService.addItem("")
        self.comboBoxCentreService.addItem("")
        self.gridLayout_5.addWidget(self.comboBoxCentreService, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.labelSalle = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.labelSalle.setFont(font)
        self.labelSalle.setObjectName("labelSalle")
        self.gridLayout_6.addWidget(self.labelSalle, 0, 0, 1, 1)
        self.labelProvenance = QtWidgets.QLabel(Form)
        self.labelProvenance.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.labelProvenance.setFont(font)
        self.labelProvenance.setObjectName("labelProvenance")
        self.gridLayout_6.addWidget(self.labelProvenance, 0, 1, 1, 1)
        self.comboBoxProvenance = QtWidgets.QComboBox(Form)
        self.comboBoxProvenance.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.comboBoxProvenance.setFont(font)
        self.comboBoxProvenance.setStyleSheet("padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247, 247, 247)")
        self.comboBoxProvenance.setObjectName("comboBoxProvenance")
        self.comboBoxProvenance.addItem("")
        self.comboBoxProvenance.addItem("")
        self.comboBoxProvenance.addItem("")
        self.gridLayout_6.addWidget(self.comboBoxProvenance, 1, 1, 1, 1)
        self.comboBoxSalle = QtWidgets.QComboBox(Form)
        self.comboBoxSalle.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBoxSalle.setMaximumSize(QtCore.QSize(1000, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.comboBoxSalle.setFont(font)
        self.comboBoxSalle.setStyleSheet("padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247, 247, 247)")
        self.comboBoxSalle.setObjectName("comboBoxSalle")
        self.comboBoxSalle.addItem("")
        self.comboBoxSalle.addItem("")
        self.comboBoxSalle.addItem("")
        self.gridLayout_6.addWidget(self.comboBoxSalle, 1, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.horizontalLayout_2.addLayout(self.gridLayout_6)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.boutonActualiser = QtWidgets.QPushButton(Form)
        self.boutonActualiser.setMaximumSize(QtCore.QSize(50, 50))
        self.boutonActualiser.setStyleSheet("padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247, 247, 247)")
        self.boutonActualiser.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Images/refresh-button-2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonActualiser.setIcon(icon)
        self.boutonActualiser.setIconSize(QtCore.QSize(50, 50))
        self.boutonActualiser.setObjectName("boutonActualiser")
        self.horizontalLayout_2.addWidget(self.boutonActualiser)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableResultats = QtWidgets.QTableWidget(Form)
        self.tableResultats.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.tableResultats.setFont(font)
        self.tableResultats.setStyleSheet("padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247, 247, 247)")
        self.tableResultats.setLineWidth(10)
        self.tableResultats.setMidLineWidth(9)
        self.tableResultats.setObjectName("tableResultats")
        self.tableResultats.setColumnCount(3)
        self.tableResultats.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableResultats.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultats.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultats.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableResultats.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultats.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultats.setHorizontalHeaderItem(2, item)
        self.tableResultats.horizontalHeader().setDefaultSectionSize(250)
        self.tableResultats.horizontalHeader().setMinimumSectionSize(20)
        self.tableResultats.verticalHeader().setDefaultSectionSize(30)
        self.tableResultats.verticalHeader().setMinimumSectionSize(20)
        self.tableResultats.verticalHeader().setSortIndicatorShown(False)
        self.tableResultats.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.tableResultats)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.labelTitre.setText(_translate("Form", "Assistant de recherche - Équipement"))
        self.comboBoxCategorieEquipement_2.setItemText(0, _translate("Form", "Catégorie 1"))
        self.comboBoxCategorieEquipement_2.setItemText(1, _translate("Form", "Catégorie 2"))
        self.comboBoxCategorieEquipement_2.setItemText(2, _translate("Form", "Catégorie 3"))
        self.labelCategorieEquipement_2.setText(_translate("Form", "Catégorie d\'équipement"))
        self.labelNumeroSerie_2.setText(_translate("Form", "Numéro de série"))
        self.comboBoxEtatService.setItemText(0, _translate("Form", "En service"))
        self.comboBoxEtatService.setItemText(1, _translate("Form", "En maintenance"))
        self.comboBoxEtatService.setItemText(2, _translate("Form", "Au rebus"))
        self.labelCentreService.setText(_translate("Form", "Centre de service"))
        self.labelEtatService.setText(_translate("Form", "État de service"))
        self.comboBoxCentreService.setItemText(0, _translate("Form", "Centre 1"))
        self.comboBoxCentreService.setItemText(1, _translate("Form", "Centre 2"))
        self.comboBoxCentreService.setItemText(2, _translate("Form", "Centre 3"))
        self.labelSalle.setText(_translate("Form", "Salle"))
        self.labelProvenance.setText(_translate("Form", "Provenance"))
        self.comboBoxProvenance.setItemText(0, _translate("Form", "Provenance 1"))
        self.comboBoxProvenance.setItemText(1, _translate("Form", "Provenance 2"))
        self.comboBoxProvenance.setItemText(2, _translate("Form", "Provenance 3"))
        self.comboBoxSalle.setItemText(0, _translate("Form", "Chambre patient"))
        self.comboBoxSalle.setItemText(1, _translate("Form", "Salle d\'opération"))
        self.comboBoxSalle.setItemText(2, _translate("Form", "Salle de réunion"))
        item = self.tableResultats.verticalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.tableResultats.verticalHeaderItem(1)
        item.setText(_translate("Form", "2"))
        item = self.tableResultats.verticalHeaderItem(2)
        item.setText(_translate("Form", "3"))
        item = self.tableResultats.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.tableResultats.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Catégorie d\'équipement"))
        item = self.tableResultats.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Marque"))

        self.ajoutRechercheBonDeTravail()

    def ajoutRechercheBonDeTravail(self):
        #Recuperation des differents attributs d'un equipement
        self.equipementManager = EquipementManager("DataBase_Equipement.json")
        self.listeCleDonnees = list()
        conf_file = 'fichier_conf.yaml'  # pathname du fichier de configuration
        try:
            fichierConf = open(conf_file, 'r')  # try: ouvrir le fichier et le lire
            with fichierConf:
                self._conf = yaml.load(fichierConf)
        except IOError:  # attrape l'erreur IOError si elle se présente et renvoie
            print("Could not read file: ", conf_file)  # définir ce qu'il faut faire pour corriger
        # récupère la liste des 'accepted keys' dans le fichier de configuration
        self.listeCleDonnees.append("ID")
        for element in self._conf['champsAcceptes-Equipement']:
            self.listeCleDonnees.append(element)
        # self.listeCleDonnees = ()
        self.listeCategorieEquipement = list(self._conf['CategorieEquipement'])
        self.listeEtatService = list(self._conf['EtatService'])
        self.listeCentreService = list(self._conf['CentreService'])
        self.listeSalle = list(self._conf['Salle'])
        self.listeProvenance = list(self._conf['Provenance'])

        #Mise a jour des listes avec les bons elements
        self.comboBoxCategorieEquipement_2.clear()
        self.comboBoxCategorieEquipement_2.addItem("")
        self.comboBoxCategorieEquipement_2.addItems(self.listeCategorieEquipement)
        self.comboBoxEtatService.clear()
        self.comboBoxEtatService.addItem("")
        self.comboBoxEtatService.addItems(self.listeEtatService)
        self.comboBoxCentreService.clear()
        self.comboBoxCentreService.addItem("")
        self.comboBoxCentreService.addItems(self.listeCentreService)
        self.comboBoxSalle.clear()
        self.comboBoxSalle.addItem("")
        self.comboBoxSalle.addItems(self.listeSalle)
        self.comboBoxProvenance.clear()
        self.comboBoxProvenance.addItems(self.listeProvenance)

        fichierConf.close()

        #Mise en forme de la page d'accueil
        self.tableResultats.setColumnCount(len(self.listeCleDonnees))
        # self.tableResultats.setHorizontalHeaderLabels("ID")
        self.tableResultats.setHorizontalHeaderLabels(self.listeCleDonnees)
        self.tableResultats.resizeColumnsToContents()

        self.dictionnaireRecherche = dict()

        #Connexion des differents champs de selections
        self.comboBoxCategorieEquipement_2.currentTextChanged.connect(self.rechercheCategorieEquipement)
        self.comboBoxEtatService.currentTextChanged.connect(self.rechercheEtatDeService)
        self.comboBoxCentreService.currentTextChanged.connect(self.rechercheCentreService)
        self.comboBoxSalle.currentTextChanged.connect(self.rechercheSalle)
        self.comboBoxProvenance.currentTextChanged.connect(self.rechercheProvenance)
        self.textEditNumeroSerie_2.returnPressed.connect(self.rechercheNumeroSerie)
        self.tableResultats.horizontalHeader().sectionClicked.connect(self.tableResultats.sortItems)

        self.tableResultats.horizontalHeader().sectionClicked.connect(self.trier)
        self.colonneClique = None
        self.nombreClique = 0
        #Empeche la modification de la table
        self.tableResultats.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers );
        self.tableResultats.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableResultats.cellDoubleClicked.connect(self.choisirEquipement)
        self.listeResultat = list()
        self.modificationEquipement = None
        self.equipementSelectionne = None

    def choisirEquipement(self, ligne, colonne):
        print("ligne", ligne)
        print("colonne", colonne)
        print(self.tableResultats.item(ligne,0).data(0))
        self.equipementSelectionne = dict()
        indice = 0
        for cle in self.listeCleDonnees:
            if(cle == "ID"):
                self.equipementSelectionne[cle] = int(self.tableResultats.item(ligne,indice).data(0))
            elif cle == "DateAcquisition" or cle == "DateDernierEntretien":
                self.equipementSelectionne[cle] = datetime.datetime.strptime(self.tableResultats.item(ligne,indice).data(0) , '%Y-%m-%d')
            else:
                self.equipementSelectionne[cle] = self.tableResultats.item(ligne,indice).data(0)
            indice += 1
        # self.modificationEquipement = QtWidgets.QWidget()
        # self.modificationEquipementUI = ModificationEquipementUI()
        # self.modificationEquipementUI.setupUi(self.modificationEquipement, equipement)
        # # self.modificationEquipement.setStyleSheet("background: white;")
        print (self.equipementSelectionne)
        # self.hide()

    def trier(self, numeroColonne):
        """Methode permettant le tri des colonnes lors du clique sur l'une d'entre elle
        Un clic fait un tri croisssant
        Un second clic fera un tri decroissant"""
        print(numeroColonne)
        if numeroColonne == self.colonneClique:
            if self.nombreClique % 2 == 0:
                self.tableResultats.sortByColumn(numeroColonne, Qt.AscendingOrder)
            else:
                self.tableResultats.sortByColumn(numeroColonne, Qt.DescendingOrder)
            self.nombreClique += 1
        else:
            self.nombreClique = 1
            self.tableResultats.sortByColumn(numeroColonne, Qt.AscendingOrder)
            self.colonneClique = numeroColonne

    def rechercheCategorieEquipement(self):
        """Methode permettant la recherche par rapport au champ de recherche
        de categorie d'equipement"""
        if(self.comboBoxCategorieEquipement_2.currentText() != ""):
            self.dictionnaireRecherche["CategorieEquipement"] = self.comboBoxCategorieEquipement_2.currentText()

        else:
            self.dictionnaireRecherche.pop("CategorieEquipement")
        self.remplirTableau()


    def rechercheEtatDeService(self):
        """Methode permettant la recherche par rapport au champ de recherche
            d'etat de service d'equipement"""
        if (self.comboBoxEtatService.currentText() != ""):
            self.dictionnaireRecherche["EtatService"] = self.comboBoxEtatService.currentText()

        else:
            self.dictionnaireRecherche.pop("EtatService")
        self.remplirTableau()

    def rechercheCentreService(self):
        """Methode permettant la recherche par rapport au champ de recherche
            d'etat de centre de service d'equipement"""
        if (self.comboBoxCentreService.currentText() != ""):
            self.dictionnaireRecherche["CentreService"] = self.comboBoxCentreService.currentText()

        else:
            self.dictionnaireRecherche.pop("CentreService")
        self.remplirTableau()

    def rechercheSalle(self):
        """Methode permettant la recherche par rapport au champ de recherche
            de salle """
        if (self.comboBoxSalle.currentText() != ""):
            self.dictionnaireRecherche["Salle"] = self.comboBoxSalle.currentText()

        else:
            self.dictionnaireRecherche.pop("Salle")
        self.remplirTableau()

    def rechercheProvenance(self):
        """Methode permettant la recherche par rapport au champ de recherche
           Provenance"""
        if (self.comboBoxProvenance.currentText() != ""):
            self.dictionnaireRecherche["Provenance"] = self.comboBoxProvenance.currentText()
        else:
            self.dictionnaireRecherche.pop("Provenance")
        self.remplirTableau()

    def rechercheNumeroSerie(self):
        """Methode permettant la recherche par rapport au champ de recherche
            Numero de Serie"""
        print("recherche numero de serie")
        if (self.textEditNumeroSerie_2.text() != ""):
            self.dictionnaireRecherche["NumeroSerie"] = self.textEditNumeroSerie_2.text()

        else:

            self.dictionnaireRecherche.pop("NumeroSerie")
        self.remplirTableau()

    def remplirTableau(self):
        """Methode permettant de remplir la table des resultats
        Le remplissage se fait avec le resultat des donnees"""
        if(any(self.dictionnaireRecherche)):
            self.listeResultat = self.equipementManager.RechercherEquipement(self.dictionnaireRecherche)
            self.tableResultats.setRowCount(len(self.listeResultat))
            for i, dictionnaire in enumerate(self.listeResultat):
                # Creation des QTableWidgetItem
                colonne = 0
                # print(dictionnaire)
                # print(self.listeCleDonnees)
                for cle in self.listeCleDonnees:
                    self.tableResultats.setItem(i, colonne, QTableWidgetItem(str(dictionnaire[cle])))
                    colonne += 1
        else:
            print("dictionnaire de recherche vide")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    rechercheEquipement = QtWidgets.QWidget()
    rechercheEquipementUI = RechercheEquipementUI()
    rechercheEquipementUI.setupUi(rechercheEquipement)
    rechercheEquipement.show()
    sys.exit(app.exec_())

