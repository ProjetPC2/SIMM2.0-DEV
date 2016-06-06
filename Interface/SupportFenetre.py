"""

"""

import sys

from PyQt5.QtCore import QDate
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Support(QDialog):
    """"""
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)

        # Création des differents éléments
        self.titre = QLabel("Support PC2 - Projet SIMM")
        self.titre.setFont((QFont('SansSerif', 24)))
        #Creation des differents composants de la fenetre
        self.logoPC2 = QLabel()

        self.logoPC2.setPixmap(QPixmap("Images\PC2.png"))
        self.logoPC2.setAlignment(Qt.AlignCenter)
        self.descriptionPC2 = QLabel("Projet PC2 est un organisme à but non-lucratif fondé \n"
                                     "et dirigé par des étudiants de Polytechnique Montréal. \n"
                                     "Notre mission est de se rendre dans différents pays en développement pour outiller\n"
                                     " nos bénéficiaires afin qu’ils puissent eux-mêmes contribuer à l’amélioration\n "
                                     "de la santé, de l’éducation et de l’environnement dans leur pays. Nous tentons de\n "
                                     "donner une seconde vie au matériel informatique et médical en se rendant sur \n"
                                     "place pour offrir des formations sur l’utilisation et la maintenance de ces\n "
                                     "équipements. Notre stratégie est axée sur la maximisation des ressources déjà \n"
                                     "disponibles et le partage de connaissances. C’est en travaillant en collaboration \n"
                                     "avec nos bénéficiaires que nous pouvons y arriver.")
        self.descriptionPC2.wordWrap()
        self.calque = QVBoxLayout()
        self.calque.addWidget(self.titre)
        self.calque.addWidget(self.logoPC2)

        self.calque.addWidget(self.descriptionPC2)



        #Mise en place de la forme de la fenetre
        self.setLayout(self.calque)
        # self.setGeometry(200, 100, 200, 1000)
        self.resize(1000,1000)
        self.setWindowTitle("SIMM 2.0")
        self.setWindowIcon(QIcon('Images\PC2.png'))

    def center(self):
        """Methode permettant de centrer la fenetre"""
        # Nous recuperons la geometrie de la fenetre principale
        qr = self.frameGeometry()
        # Nous recuperons la definition de l'ecran et nous recuperons le point central
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        # self.move(qr.topLeft())
        # self.move(qr.center)

    def closeEvent(self, event):
        """Fonction gerant la creation d'une fenetre de verification
        lors de la fermeture de la fenetre"""
        reply = QMessageBox.question(self, 'Message',
                                     "Etes-vous sur de vouloir quitter ?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        #Selon le choix on fait une action precise
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def quitter(self):
        reply = QMessageBox.question(self, 'Message',
                                     "Etes-vous sur de vouloir quitter ?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            # self.hide()
            # self.close()
            self.destroy()


    def valider(self):
        """Methode valider qui va changer le contenu de la fenetre une fois l'equipement valider
        Cette methode va tout d'abord declancher une fenetre de confirmation
        Puis si la confirmation est valide, elle va mettre les informations sous forme de Qlabel
        Les informations ne seront donc plus modifiables, on passe en mode consultatble"""
        self.formulaire.hide()
        self.validerBouton.hide()
        self.formulaireRempli.show()
        self.modifierBouton.show()
        self.donnees()
        self.remplissageFormulaire()
        self.listeTemp.clear()
        self.resize(1000,1000)

    def modifier(self):
        """Methode modifier permet de passer du mode consultable au mode modifiable
        Cette methode donne la possibilite a l'utilisateur de changer les differents champs
        On retourne dans le meme version que l'ajout d'un equipement"""
        self.formulaireRempli.hide()
        self.modifierBouton.hide()
        self.formulaire.show()
        self.validerBouton.show()

    def afficheMessage(self, event):
        """Methode affichant une fenetre de confirmation pour l'ajout d'un equipement
        Cette fenetre va nous faire passer dans le mode consultable
        Les champs ne seront plus modifiables"""
        message = QMessageBox()
        #On met le texte en gras avec les bases <b> </b>
        message.setText("<b>Sauvegarde de l'equipement</b>")
        message.setInformativeText("Vous allez sauvegarder un nouvel equipement")
        message.setWindowTitle("Confirmation")
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.buttonClicked.connect(self.confirmation)
        message.exec()

    def miseAJourStatutBar(self, text):
        #methode mettant a jour le texte dans la status bar
        pass

    def confirmation(self,i):
        #Methode qui va faire appel a la methode valider
        #Cette methode est appelee une fois que l'ajout d'un element a ete confirme
        if i.text() == "OK":
            self.valider()

    def donnees(self):
        """Methode permettant la recuperation des donnees dans les differents widgets
        On parcours la liste des widgets et on recupere les differentes informations utiles
        Les informations sont recuperees de facon specifique selon le type du widget"""
        for widget in self.formulaire.widgetList:
            # self.stockage.dictionnaire
            if type(widget) is QLineEdit:
                self.listeTemp.append(widget.text())
            elif type(widget) is QDateEdit:
                self.listeTemp.append(str(widget.date()))
                print(widget.date())
                print(QDate.currentDate())
            elif type(widget) is QComboBox:
                self.listeTemp.append(widget.currentText())
                print(widget.currentText())
            elif type(widget) is QGroupBox:
                self.listeTemp.append(self.formulaire.etatService)
            else:
                self.listeTemp.append(widget.toPlainText())
                print(widget.toPlainText())

    def remplissageFormulaire(self):
        """Methode permettant de remplir le formulaire dans le mode consultable"""
        i = 0
        for text in self.listeTemp:
            self.formulaireRempli.widgetList[i].setText(text)
            i += 1


if __name__ == "__main__": #Si le fichier est lancé tout seul

    app = QApplication(sys.argv)
    window = Support()
    # window.center()
    window.show()
    sys.exit(app.exec_())