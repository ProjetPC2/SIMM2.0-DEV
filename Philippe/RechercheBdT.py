#Difficulté avec le QTextEdit

"""
Nous retrouvons ici l'ébauche de la recherche de bon de travail.
Il manques le menu et le calendrier. Ce dernier ne veut pas s'afficher

"""

import sys
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QTextEdit, QGridLayout, QApplication, QPushButton, QHBoxLayout, QVBoxLayout, QComboBox)

from AbstractWindow import AbstractWindow


class RechercheBdT(AbstractWindow):
    """"Creation de la classe qui va gerer la fenetre
    creation des methodes evenements"""
    def __init__(self):
        #constructeur
        super().__init__()
        self.initUI()

    def initUI(self):
        #creation des labels
        titre = QLabel("Assistant de Recherche - Bon de Travail")
        titre.setFont((QFont('SansSerif', 24)))

        #Critère de Recherche

        categorie = QLabel('Catégorie d''équipement')
        apres = QLabel('Après le')
        avant= QLabel('Avant le')
        etat=QLabel('Etat')
        cds=QLabel('Centre de Service')
        description=QLabel('Description de la situation')
        apresEdit=QLineEdit()
        avantEdit=QLineEdit()
        descriptionEdit=QLineEdit()

        #creation d'un layout horizontal
        hbox = QHBoxLayout()
       # hbox.addStretch(1)
        hbox.setAlignment(Qt.AlignCenter)

        # Ajout du label du titre dans le layout horizontal 2
        hbox.addWidget(titre,0,)

        #creation d'un layout verticale
        vbox = QVBoxLayout()
        #vbox.addStretch(1)

        #creation d'une grid layout
        grid = QGridLayout()
        grid.setSpacing(10)

        #Postionnement des differents elements dans le grid layout

        grid.addWidget(categorie, 1, 0)

        grid.addWidget(apres, 1, 1)
        grid.addWidget(apresEdit, 2,1)

        grid.addWidget(avant,1,2)
        grid.addWidget(avantEdit,2,2)

        grid.addWidget(etat, 1, 3)

        grid.addWidget(cds, 3,0)


        grid.addWidget(description, 3, 1)
        grid.addWidget(descriptionEdit, 4, 1)



        #///CRÉATION DES LISTES DÉROULANTES\\\

        #Catégorie d'équipement
        categorieEdit = QComboBox(self)
        #On ajoute les differents elements pour la liste deroulante
            #Ça serait bien d'avoir une option pour ajouter automatiquement les catégories

        categorieEdit.addItem("Ajouter une catégorie")

        #État

        etatEdit=QComboBox(self)
        etatEdit.addItem("Ajouter une catégorie")

        #Centre de Service

        cdsEdit = QComboBox(self)
        cdsEdit.addItem("Ajouter une catégorie")

        #ajout de la liste deroulante dans la grid layout
        grid.addWidget(categorieEdit, 2, 0)
        grid.addWidget(etatEdit, 2,3)
        grid.addWidget(cdsEdit, 4,0)
        #creation du label qui sera mise a jour lors de la selection de la liste deroulante
        self.label = QLabel("Stylo", self)
        #ajout du label dans la grille
        grid.addWidget(self.label, 5,0)
        #On connecte la mise a jour du texte a la selection de la liste
        categorieEdit.activated[str].connect(self.onActivated)

        #On ajoute la grid layout et le layout horizontal dans le layout vertical
        vbox.addLayout(hbox)
        vbox.addLayout(grid)


        #on met en place le layout
        self.setLayout(vbox)
        #mise a jour des fenetres
     #Il semble avoir un problème avec la bar de menu
      #  menubar = self.menuBar()
      #  fileMenu = menubar.addMenu('&File')
      #  fileMenu.addAction('Ajouter une action')
      #  fileMenu = menubar.addMenu('&Edit')
     #   fileMenu = menubar.addMenu('&View')
     #   fileMenu = menubar.addMenu('&Insert')
     #   fileMenu = menubar.addMenu('&Format')
     #   fileMenu = menubar.addMenu('&Table')
     #   fileMenu = menubar.addMenu('&Tools')
      #  fileMenu = menubar.addMenu('&Window')
      #  fileMenu = menubar.addMenu('&Help')

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('PC2')
        self.setWindowIcon(QIcon('PC2.png'))
        self.show()

    def onActivated(self, text):
        #methode qui fera la mise a jour du label a la selection dans la liste
        self.label.setText(text)
        self.label.adjustSize()
        print(text)

    def keyPressEvent(self, e):
        #methode qui surcharge l'appuie d'une touche du clavier
        if e.key() == Qt.Key_Escape:
            #on ferme la fenetre lors de l'appuie du bouton Esc
            self.close()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = RechercheBdT()
    sys.exit(app.exec_())