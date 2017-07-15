from threading import Thread

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem

from BDD.PieceManagerSQLite import PieceManager
from Interface.FenetresEnPython.Fichiers import pathPieceDatabase
from Interface.FenetresEnPython.PieceUI import Ui_Piece
from Interface.FenetresEnPython.Signaux import Communicate


class Piece(Ui_Piece):
    #Classe permettant de gerer la fenetre permettant l'ajout de pieces dans la base de donnees
    def __init__(self, widget):
        self.setupUi(widget)
        self.pieceManager = PieceManager(pathPieceDatabase)
        self.enregistrement = Communicate()
        self.ajoutPiece()
        self.listeAjoutPiece = list()
        self.nombreLigne  = 0


    def ajoutPiece(self):
        self.listeCategoriePiece = list(self.pieceManager.ObtenirListeCategorie())
        self.listeCategoriePiece.insert(0, "")
        self.listeCategoriePiece.sort()

        self.comboBoxSelectionCategoriePiece.currentTextChanged.connect(self.recuperationPieceCategorie)
        self.comboBoxSelectionCategoriePiece.addItems(self.listeCategoriePiece)
        self.comboBoxCategorieSelectionnee.addItems(self.listeCategoriePiece)
        self.comboBoxCategorieSelectionnee.currentTextChanged.connect(self.rechercheCategorie)

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
        self.BoutonValider.clicked.connect(self.ajouterPiece)
        self.BoutonEnregistrerPiece.clicked.connect(self.enregistrerPieceThread)

        self.tableCategoriePiece.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableCategoriePiece.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableCategoriePiece.horizontalHeader().sectionClicked.connect(self.trier)

        self.tableResume.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableResume.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableResume.horizontalHeader().sectionClicked.connect(self.trierResume)

    def ajouterPiece(self):
        print("ajout Piece")
        categorie = self.comboBoxSelectionCategoriePiece.currentText()
        print(categorie)
        nomPiece = self.comboBoxNomPiece.currentText()
        nombre = (self.spinBoxNombreEquipement.text())
        if(int(nombre)>0):
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
        print("Obtention de la liste de categorie")
        self.listeCategoriePiece = list(self.pieceManager.ObtenirListeCategorie())
        self.listeCategoriePiece.sort()
        self.listeCategoriePiece.insert(0,"")
        self.comboBoxSelectionCategoriePiece.clear()
        self.comboBoxCategorieSelectionnee.clear()
        self.comboBoxNomPiece.clear()
        self.comboBoxNomPiece.setCurrentText("")
        self.comboBoxCategorieSelectionnee.addItems(self.listeCategoriePiece)
        self.comboBoxSelectionCategoriePiece.addItems(self.listeCategoriePiece)
        self.enregistrement.enregistrementTermine.emit()



    def recuperationPieceCategorie(self):
        self.comboBoxNomPiece.clear()
        self.listePiece = self.pieceManager.ObtenirListePiece(self.comboBoxSelectionCategoriePiece.currentText())
        self.comboBoxNomPiece.addItems(self.listePiece)

    def rechercheCategorie(self):
        self.tableResume.setRowCount(0)
        if(self.comboBoxCategorieSelectionnee.currentText() != ""):
            dictPiece = self.pieceManager.ObtenirCategorie(self.comboBoxCategorieSelectionnee.currentText())
            self.tableResume.setRowCount(len(dictPiece))
            ligne = 0
            for piece, nombre in dictPiece.items():
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

    def enregistrerPieceThread(self):
        thread = fonctionPiece(self.enregistrerPiece)
        thread.start()

class fonctionPiece(Thread):
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