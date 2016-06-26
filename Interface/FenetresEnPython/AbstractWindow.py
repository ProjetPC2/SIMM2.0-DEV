from PyQt5.QtWidgets import *

class AbstractWindow(QWidget):

    def closeEvent(self, event):
        """Fonction gerant la creation d'une fenetre de verification
        lors de la fermeture de la fenetre"""
        reply = QMessageBox.question(self, 'Message',
                                     "Etes-vous sur de vouloir quitter ?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        # Selon le choix on fait une action precise
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


    def quitter(self):
        # reply = QMessageBox.question(self, 'Message',
        #                              "Etes-vous sur de vouloir quitter ?", QMessageBox.Yes |
        #                              QMessageBox.No, QMessageBox.No)
        # if reply == QMessageBox.Yes:
        #     # self.hide()
        #     # self.close()
        self.destroy()

    def center(self):
        """Methode permettant de centrer la fenetre"""
        # Nous recuperons la geometrie de la fenetre principale
        qr = self.frameGeometry()
        # Nous recuperons la definition de l'ecran et nous recuperons le point central
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        # self.move(qr.center)