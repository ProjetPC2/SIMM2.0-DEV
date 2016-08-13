import datetime
from threading import Thread

import yaml
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QStringListModel
from PyQt5.QtWidgets import QTableWidgetItem

from BDD.BonTravailManager import BonTravailManager
from BDD.EquipementManager import EquipementManager
from BDD.PieceManager import PieceManager
from Interface.FenetresEnPython.PieceUI import Ui_Piece
from Interface.FenetresEnPython.Signaux import Communicate


class Piece(Ui_Piece):
    def __init__(self, widget):
        self.setupUi(widget)
        self.pieceManager = PieceManager()
        self.enregistrement = Communicate()

        self.ajoutPiece()
        # self.finChargement = finChargement
        # self.tableCategoriePiece.setHorizontalHeaderLabels("Nom Piece")
        self.listeAjoutPiece = list()
        self.nombreLigne  = 0


    def ajoutPiece(self):
        self.piece = self.pieceManager._getPiece()
        if(self.piece['CategoriePiece'] is None):
            self.piece['CategoriePiece'] = dict()
        self.pieceSelonCentre = dict(self.piece['CategoriePiece'])
        # self.quantitePiece = dict(self.piece['QuantitePiece'])
        # print(self.pieceSelonCentre)
        # print(self.quantitePiece)
        # self.listeCategoriePiece = list()
        # self.listeCategoriePiece.append("")
        self.listeCategoriePiece = list(self.pieceManager.ObtenirListeCategorie())
        self.listeCategoriePiece.insert(0, "")
        # self.listeCategoriePiece.append(self.pieceManager.ObtenirListeCategorie())
        self.listeCategoriePiece.sort()

        self.comboBoxSelectionCategoriePiece.currentTextChanged.connect(self.recuperationPieceCategorie)
        self.comboBoxSelectionCategoriePiece.addItems(self.listeCategoriePiece)
        self.comboBoxCategorieSelectionnee.addItems(self.listeCategoriePiece)
        self.comboBoxCategorieSelectionnee.currentTextChanged.connect(self.rechercheCategorie)
        # self.
        # self.lineEdit.returnPressed.connect()

        self.colonneClique = None
        self.nombreClique = 0

        self.colonneCliqueResume = None
        self.nombreCliqueResume = 0

        self.listeCleDonnees = list(["Categorie","Nom Piece", "Nombre"])
        self.tableCategoriePiece.setColumnCount(len(self.listeCleDonnees))
        self.tableCategoriePiece.setHorizontalHeaderLabels(self.listeCleDonnees)
        self.listeCleResume = list(["Nom Piece", "Nombre"])
        self.tableResume.setColumnCount(len(self.listeCleResume))
        self.tableResume.setHorizontalHeaderLabels(self.listeCleResume)
        # self.tableCategoriePiece.resizeColumnsToContents()
        # self.tableCategoriePiece.
        self.BoutonValider.clicked.connect(self.ajouterPiece)
        self.BoutonEnregistrerPiece.clicked.connect(self.enregistrerPiece)

        self.tableCategoriePiece.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableCategoriePiece.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableCategoriePiece.horizontalHeader().sectionClicked.connect(self.trier)

        self.tableResume.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableResume.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableResume.horizontalHeader().sectionClicked.connect(self.trierResume)

    def choisirCategorie(self):
        categorie = self.comboBoxCategorieSelectionnee.currentText()
        print(categorie)
        # print(model)
        # self.listViewCategoriePiece.setModel(model)
        # self.pieceManager.AjouterNombrePiece()

    def ajouterPiece(self):
        print("ajout Piece")
        categorie = self.comboBoxSelectionCategoriePiece.currentText()
        print(categorie)
        nomPiece = self.comboBoxNomPiece.currentText()
        nombre = (self.spinBoxNombreEquipement.text())
        self.tableCategoriePiece.setRowCount(self.tableCategoriePiece.rowCount() + 1)

        self.tableCategoriePiece.setItem(self.tableCategoriePiece.rowCount()-1, 0, QTableWidgetItem(categorie))
        self.tableCategoriePiece.setItem(self.tableCategoriePiece.rowCount()-1, 1, QTableWidgetItem(nomPiece))
        self.tableCategoriePiece.setItem(self.tableCategoriePiece.rowCount()-1, 2, QTableWidgetItem((nombre)))

        self.listeAjoutPiece.append((categorie, nomPiece, int(nombre)))
        print(self.listeAjoutPiece)

    def enregistrerPiece(self):
        print("enregistrerPiece")
        print(self.listeAjoutPiece)
        self.tableCategoriePiece.setRowCount(0)
        self.pieceManager.AjouterPiece(self.listeAjoutPiece)
        self.listeAjoutPiece.clear()
        self.enregistrement.enregistrement.emit()
        self.listeCategoriePiece = list(self.pieceManager.ObtenirListeCategorie())
        self.listeCategoriePiece.sort()
        self.listeCategoriePiece.insert(0,"")
        self.comboBoxSelectionCategoriePiece.clear()
        self.comboBoxCategorieSelectionnee.clear()
        self.comboBoxNomPiece.clear()
        self.comboBoxNomPiece.setCurrentText("")
        self.comboBoxCategorieSelectionnee.addItems(self.listeCategoriePiece)
        self.comboBoxSelectionCategoriePiece.addItems(self.listeCategoriePiece)



    def recuperationPieceCategorie(self):
        self.comboBoxNomPiece.clear()
        self.listePiece = self.pieceManager.ObtenirListePiece(self.comboBoxSelectionCategoriePiece.currentText())
        self.comboBoxNomPiece.addItems(self.listePiece)

    def rechercheCategorie(self):
        self.tableResume.setRowCount(0)
        if(self.comboBoxCategorieSelectionnee.currentText() != ""):
            dictPiece = self.pieceManager._getPiece()
            self.tableResume.setRowCount(len(dictPiece['CategoriePiece'][self.comboBoxCategorieSelectionnee.currentText()]))
            ligne = 0
            for piece, nombre in dictPiece['CategoriePiece'][self.comboBoxCategorieSelectionnee.currentText()].items():
                print(piece, nombre)
                self.tableResume.setItem(ligne, 0, QTableWidgetItem(piece))
                self.tableResume.setItem(ligne, 1, QTableWidgetItem(str(nombre)))
                ligne += 1

    def trier(self, numeroColonne):
        """Methode permettant le tri des colonnes lors du clique sur l'une d'entre elle
        Un clic fait un tri croisssant
        Un second clic fera un tri decroissant"""
        print(numeroColonne)
        if numeroColonne == self.colonneClique:
            if self.nombreClique % 2 == 0:
                self.tableCategoriePiece.sortByColumn(numeroColonne, Qt.AscendingOrder)
            else:
                self.tableCategoriePiece.sortByColumn(numeroColonne, Qt.DescendingOrder)
            self.nombreClique += 1
        else:
            self.nombreClique = 1
            self.tableCategoriePiece.sortByColumn(numeroColonne, Qt.AscendingOrder)
            self.colonneClique = numeroColonne

    def trierResume(self, numeroColonne):
        """Methode permettant le tri des colonnes lors du clique sur l'une d'entre elle
        Un clic fait un tri croisssant
        Un second clic fera un tri decroissant"""
        print(numeroColonne)
        if numeroColonne == self.colonneCliqueResume:
            if self.nombreCliqueResume % 2 == 0:
                self.tableResume.sortByColumn(numeroColonne, Qt.AscendingOrder)
            else:
                self.tableResume.sortByColumn(numeroColonne, Qt.DescendingOrder)
            self.nombreCliqueResume += 1
        else:
            self.nombreCliqueResume = 1
            self.tableResume.sortByColumn(numeroColonne, Qt.AscendingOrder)
            self.colonneCliqueResume = numeroColonne

class fonctionPiece (Thread):
    def __init__(self, fonction):
        Thread.__init__(self)
        self.fonction = fonction

    def run(self):
        self.fonction()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    piece = QtWidgets.QWidget()
    pieceUI = Piece(piece)
    piece.show()
    sys.exit(app.exec_())