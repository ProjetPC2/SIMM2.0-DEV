from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

class AbstractWindow(QWidget):
    '''
        Class permettant la demande de confirmation pour fermer la fenetre
    '''

    def closeEvent(self, event):
        """Fonction gerant la creation d'une fenetre de verification
        lors de la fermeture de la fenetre"""
        self.messageBox = QMessageBox()
        self.messageBox.setStyleSheet("QPushButton {\n"
                                        "color: black;\n"
                                        "background-color:rgb(245, 245, 245);\n"
                                        "border-width: 1px;\n"
                                        "border-color: grey;\n"
                                        "border-style: solid;\n"
                                        "border-radius: 4px;\n"
                                        "padding: 3px;\n"
                                        "font: bold 12px;\n"
                                        "padding-left: 5px;\n"
                                        "padding-right: 5px;\n"
                                        "min-width: 80px;\n"
                                        "max-width:220px;\n"
                                        "min-height: 30px;\n"
                                        "max-height: 30px;\n"
                                        "}\n")
        self.messageBox.setText("Etes-vous sûr de vouloir quitter ?")
        self.messageBox.setWindowTitle("SIMM 2.0")
        self.messageBox.setWindowIcon(QIcon('Images/SIMM2.0.png'))
        self.boutonOk = QPushButton("Oui")
        self.boutonAnnuler = QPushButton("Annuler")
        self.messageBox.addButton(self.boutonOk, QMessageBox.AcceptRole)
        self.messageBox.addButton(self.boutonAnnuler, QMessageBox.RejectRole)
        retour = self.messageBox.exec()
        print(retour)
        if(retour == QMessageBox.AcceptRole):
            event.accept()
        else:
            event.ignore()




    def center(self):
        """Methode permettant de centrer la fenetre"""
        # Nous recuperons la geometrie de la fenetre principale
        qr = self.frameGeometry()
        # Nous recuperons la definition de l'ecran et nous recuperons le point central
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        # self.move(qr.center)

