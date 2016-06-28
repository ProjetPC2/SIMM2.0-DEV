import sys
from PyQt5 import QtWidgets

from Interface.FenetresEnPython.AccueilUI import Ui_Accueil

from Interface.FenetresEnPython.AjoutEquipement import AjoutEquipement
from Interface.FenetresEnPython.BonDeTravail import BonDeTravail
from Interface.FenetresEnPython.ConsultationEquipement import ConsultationEquipement
from Interface.FenetresEnPython.ModificationEquipement import ModificationEquipement
from Interface.FenetresEnPython.RechercheBonDeTravail import RechercheBonDeTravail
from Interface.FenetresEnPython.RechercheEquipement import RechercheEquipement
from Interface.FenetresEnPython.Statistique import Statistique
from Interface.FenetresEnPython.SupportPC2 import SupportPC2

from Interface.FenetresEnPython.PDF import PDF
from Interface.FenetresEnPython.SuppressionBonDeTravail import SuppressionBonDeTravail
from Interface.FenetresEnPython.SuppressionEquipement import SuppressionEquipement


class Accueil(Ui_Accueil):
    '''
        Fonction de lancement de la page d'accueil de SIMM
        :param: None
        :return:
    '''
    # On masque les autres elements
    def __init__(self, Accueil):
        self.setupUi(Accueil)
        self.ajoutAccueil()
        self.BoutonFlecheNavigation.hide()
        self.frameFleche.hide()

    def ajoutAccueil(self):
        '''
            Ajout des differents elements a la page d'accueil
            :param:
            :return:
        '''
        # Creation d'une liste contenant les elements destines
        # A l'affichage dans la partie centrale
        self.listeElementParDefaut = list()
        self.listeElementParDefaut.append(self.LabelSIMM20HopitalSaintMichel)
        # Rajouter le logo de SIMM
        self.listeElementParDefaut.append(self.logo)
        self.listeElementParDefaut.append(self.LabelDefinitionSIMM)

              # Creation des differents conteneur pour les widgets a afficher
        # Partie Equipement
        self.ajoutEquipement = None
        self.consultationEquipement = None
        self.rechercheEquipement = None
        self.modificationEquipement = None
        self.ajoutBonDeTravailEquipement = None
        self.consultationBonDeTravail = None

        # Partie Bon de Travail
        self.ajoutBonDeTravail = None
        self.rechercheBonDeTravail = None
        self.modificationEquipementRecherche = None
        # Connexion des actions aux cliques des boutons de la partie Bon de Travail
        # Creation du conteneur de la page statistique
        self.statistique = None

        # Creation de la partie Support
        self.support = None
        self.supprimeEquipement = None
        self.supprimeBonDeTravail = None
        #Connexion des differents elements
        self.connectionBouton()

        self.listeNavigation = list()
        self.selectionOption()
        self.BoutonFlecheNavigation.clicked.connect(self.naviguer)

    def connectionBouton(self):
        '''
            Methode qui va faire la connection des differents boutons
            :param:
            :return:
        '''
        self.BoutonAccueil.clicked.connect(self.afficherAccueil)
        self.BoutonAjouterEquipement.clicked.connect(self.afficherAjoutEquipement)
        self.BoutonModifierConsulterEquipement.clicked.connect(self.afficherConsultationEquipement)
        self.BoutonRechercherEquipement.clicked.connect(self.afficherRechercheEquipement)

        self.BoutonAjouterBonTravail.clicked.connect(self.afficherAjoutBonDeTravail)
        self.BoutonRechercherBonTravail.clicked.connect(self.afficherRechercheBonDeTravail)

        self.BoutonImprimerInventaire.clicked.connect(self.imprimerInventaire)
        self.BoutonStatistiques.clicked.connect(self.afficherStatistique)

        self.BoutonSuportTecnique.clicked.connect(self.afficherSupport)

    def afficherAjoutEquipement(self):
        '''
            Affichage du widget permet l'ajout d'un equipement
            Masquage des autres elements graphiques de la partie principale
            :param: None
            :return:
        '''
        # On masque les autres elements
        self.masquerElementGraphique()

        if self.ajoutEquipement is None:
            # Creation du widget s'il n'existe pas deja

            self.ajoutEquipement = QtWidgets.QWidget()
            self.ajoutEquipementUI = AjoutEquipement(self.ajoutEquipement)
            self.ajoutEquipement.setStyleSheet("background: white;")

            self.listeElementParDefaut.append(self.ajoutEquipement)
            self.layoutAffichagePrincipal.addWidget(self.ajoutEquipement)
        else:
            # Affichage du widget s'il existe deja
            self.ajoutEquipement.show()
        self.BoutonFlecheNavigation.hide()
        self.frameFleche.hide()
        self.listeNavigation.clear()

    def afficherConsultationEquipement(self):
        '''
            Affichage du widget permet la consultation d'un equipement
            Masquage des autres elements graphiques de la partie principale
            :param: None
            :return:
        '''
        # On masque les autres elements
        self.masquerElementGraphique()
        if self.consultationEquipement is None:
            # Creation du widget s'il n'existe pas encore
            self.consultationEquipement = QtWidgets.QWidget()
            self.consultationEquipementUI = ConsultationEquipement(self.consultationEquipement)
            self.consultationEquipement.setStyleSheet("background: white;")

            # connexion de l'action a l'appuye du bouton modification equipement
            self.consultationEquipementUI.boutonModifierEquipement.clicked.connect(self.modifierEquipement)

            self.consultationEquipementUI.boutonAjouterUnBon.clicked.connect(self.ajouterBonDeTravailEquipement)
            self.consultationEquipementUI.boutonConsulterBon.clicked.connect(self.consulterBonDeTravail)
            self.listeElementParDefaut.append(self.consultationEquipement)
            self.layoutAffichagePrincipal.addWidget(self.consultationEquipement)
        else:
            # Affichage de l'element s'il existe deja
            self.consultationEquipement.show()
        self.BoutonFlecheNavigation.hide()
        self.frameFleche.hide()
        self.listeNavigation.clear()
        self.listeNavigation.append(self.consultationEquipement)

    def afficherRechercheEquipement(self):
        '''
            Affichage du widget permet la recherche d'un equipement
            Masquage des autres elements graphiques de la partie principale
            :param: None
            :return:
        '''
        # On masque les autres elements
        self.masquerElementGraphique()
        if self.rechercheEquipement is None:
            # Creation du widget s'il n'existe pas
            self.rechercheEquipement = QtWidgets.QWidget()
            self.rechercheEquipementUI = RechercheEquipement(self.rechercheEquipement)
            self.rechercheEquipement.setStyleSheet("background: white;")
            self.listeElementParDefaut.append(self.rechercheEquipement)
            self.layoutAffichagePrincipal.addWidget(self.rechercheEquipement)
            self.rechercheEquipementUI.tableResultats.doubleClicked.connect(self.choisirEquipement)
        else:
            # Affichage du widget s'il existe deja
            self.rechercheEquipement.show()
        self.BoutonFlecheNavigation.hide()
        self.frameFleche.hide()
        self.listeNavigation.clear()
        self.listeNavigation.append(self.rechercheEquipement)

    def choisirEquipement(self):
        # On masque les autres elements
        self.masquerElementGraphique()
        self.frameFleche.show()
        self.BoutonFlecheNavigation.show()
        equipement = self.rechercheEquipementUI.equipementSelectionne
        if self.modificationEquipementRecherche is None:
            # Creation du widget s'il n'existe pas
            self.modificationEquipementRecherche = QtWidgets.QWidget()
            self.modificationEquipementRechercheUI = ModificationEquipement(self.modificationEquipementRecherche, equipement)
            self.modificationEquipementRecherche.setStyleSheet("background: white;")

            self.listeElementParDefaut.append(self.modificationEquipementRecherche)
            self.layoutAffichagePrincipal.addWidget(self.modificationEquipementRecherche)
        else:
            # Affichage du widget s'il existe deja
            self.modificationEquipementRecherche.show()
            self.modificationEquipementRechercheUI.equipementRecherche = equipement
            self.modificationEquipementRechercheUI.remplirEquipement()
        self.listeNavigation.append(self.modificationEquipementRecherche)

    def supprimerEquipement(self):
        # On masque les autres elements
        self.masquerElementGraphique()
        self.frameFleche.show()
        self.BoutonFlecheNavigation.show()
        if self.supprimeEquipement is None:
            # Creation du widget s'il n'existe pas
            self.supprimeEquipement = QtWidgets.QWidget()
            self.supprimeEquipementUI = SuppressionEquipement(self.supprimeEquipement)
            self.supprimeEquipement.setStyleSheet("background: white;")

            self.listeElementParDefaut.append(self.supprimeEquipement)
            self.layoutAffichagePrincipal.addWidget(self.supprimeEquipement)
        else:
            # Affichage du widget s'il existe deja
            self.supprimeEquipement.show()
        self.listeNavigation.append(self.supprimeEquipement)

    def supprimerBonDeTravail(self):
        # On masque les autres elements
        self.masquerElementGraphique()
        self.frameFleche.show()
        self.BoutonFlecheNavigation.show()
        if self.supprimeBonDeTravail is None:
            # Creation du widget s'il n'existe pas
            self.supprimeBonDeTravail = QtWidgets.QWidget()
            self.supprimeBonDeTravailUI = SuppressionBonDeTravail(self.supprimeBonDeTravail)
            self.supprimeBonDeTravail.setStyleSheet("background: white;")

            self.listeElementParDefaut.append(self.supprimeBonDeTravail)
            self.layoutAffichagePrincipal.addWidget(self.supprimeBonDeTravail)
        else:
            # Affichage du widget s'il existe deja
            self.supprimeBonDeTravail.show()
        self.listeNavigation.append(self.supprimeBonDeTravail)

    def afficherAjoutBonDeTravail(self):
        '''
            Affichage du widget permet l'ajout d'un bon de travail
            Masquage des autres elements graphiques de la partie principale
            :param: None
            :return:
        '''
        # On masque les autres elements
        self.masquerElementGraphique()
        if self.ajoutBonDeTravail is None:
            # Creation du widget s'il n'existe pas
            self.ajoutBonDeTravail = QtWidgets.QWidget()
            self.bonDeTravailUI = BonDeTravail(self.ajoutBonDeTravail)
            self.ajoutBonDeTravail.setStyleSheet("background: white;")

            self.listeElementParDefaut.append(self.ajoutBonDeTravail)
            self.layoutAffichagePrincipal.addWidget(self.ajoutBonDeTravail)
        else:
            # Affichage de l'element s'il existe deja
            self.ajoutBonDeTravail.show()
        self.BoutonFlecheNavigation.hide()
        self.frameFleche.hide()
        self.listeNavigation.clear()

    #TODO : Creer une methode ajouterBonDeTravail
    #Cette methode va masquer les autres elements graphiques du layout principal
    #Elle va creer un nouveau widget ajouterBonDeTravailEquipement

    #TODO : Creer une methode pour consulter le bon de travail selectionnee
    def afficherRechercheBonDeTravail(self):
        '''
            Affichage du widget permet la recherche d'un bon de travail
            Masquage des autres elements graphiques de la partie principale
            :param: None
            :return:
        '''
        # On masque les autres elements
        self.masquerElementGraphique()
        if self.rechercheBonDeTravail is None:
            # Creation du widget s'il n'existe pas
            self.rechercheBonDeTravail = QtWidgets.QWidget()
            self.rechercheBonDeTravailUI = RechercheBonDeTravail(self.rechercheBonDeTravail)
            self.rechercheBonDeTravail.setStyleSheet("background: white;")

            self.listeElementParDefaut.append(self.rechercheBonDeTravail)
            self.layoutAffichagePrincipal.addWidget(self.rechercheBonDeTravail)
        else:
            # Affichage du widget s'il existe deja
            self.rechercheBonDeTravail.show()
        self.BoutonFlecheNavigation.hide()
        self.frameFleche.hide()
        self.listeNavigation.clear()

    def afficherStatistique(self):
        '''
            Affichage du widget Statistique
            Masquage des autres elements graphiques de la partie principale
            :param: None
            :return:
        '''
        # On masque les autres elements
        self.masquerElementGraphique()

        if self.statistique is None:
            # Creation du widget Statistique s'il n'existe pas
            self.statistique = QtWidgets.QWidget()
            statistique = Statistique(self.statistique)
            self.statistique.setStyleSheet("background: white;")
            self.listeElementParDefaut.append(self.statistique)
            self.layoutAffichagePrincipal.addWidget(self.statistique)
        else:
            # Affichage du widget s'il existe deja
            self.statistique.show()
        self.BoutonFlecheNavigation.hide()
        self.frameFleche.hide()
        self.listeNavigation.clear()

    def afficherSupport(self):
        '''
            Affichage du widget Support
            Masquage des autres elements graphiques de la partie principale
            :param: None
            :return:
        '''
        # On masque les autres elements
        self.masquerElementGraphique()
        if self.support is None:
            # Creation du widget support s'il n'existe pas
            self.support = QtWidgets.QWidget()
            self.supportPC2UI = SupportPC2(self.support)
            self.support.setStyleSheet("background: white;")
            self.supportPC2UI.boutonSupprimerEquipement.clicked.connect(self.supprimerEquipement)
            self.supportPC2UI.boutonSupprimerBon.clicked.connect(self.supprimerBonDeTravail)
            self.listeElementParDefaut.append(self.support)
            self.layoutAffichagePrincipal.addWidget(self.support)
        else:
            # Affichage du widget support
            self.support.show()
        self.BoutonFlecheNavigation.hide()
        self.frameFleche.hide()
        self.listeNavigation.clear()
        self.listeNavigation.append(self.support)

    def afficherAccueil(self):
        '''
            Affichage du widget Support
            Masquage des autres elements graphiques de la partie principale
            :param: None
            :return:
        '''
        # On masque les autres elements
        self.masquerElementGraphique()
        self.LabelSIMM20HopitalSaintMichel.show()
        self.logo.show()
        self.LabelDefinitionSIMM.show()
        self.BoutonFlecheNavigation.hide()
        self.frameFleche.hide()
        self.listeNavigation.clear()

    def masquerElementGraphique(self):
        '''
            Masquage les elements graphiques de listeELementParDefaut
            :param: None
            :return:
        '''
        # On masque les autres elements
        for elementGraphique in self.listeElementParDefaut:
            elementGraphique.hide()

    def modifierEquipement(self):
        '''
            Affichage du widget recapitulant l'equipement que l'on souhaite ajouter
            Masquage des autres elements graphiques de la partie principale
            :param: None
            :return:
        '''
        # On masque les autres elements
        self.BoutonFlecheNavigation.show()
        self.frameFleche.show()
        self.masquerElementGraphique()
        equipement = self.consultationEquipementUI.equipement
        if self.modificationEquipement is None:
            # Creation du widget s'il n'existe pas
            self.modificationEquipement = QtWidgets.QWidget()
            self.modificationEquipementUI = ModificationEquipement(self.modificationEquipement, equipement)
            self.modificationEquipement.setStyleSheet("background: white;")
            self.listeElementParDefaut.append(self.modificationEquipement)
            self.layoutAffichagePrincipal.addWidget(self.modificationEquipement)
        else:
            # Affichage du widget s'il existe deja
            self.modificationEquipement.show()
            self.modificationEquipementUI.equipementRecherche = equipement
            self.modificationEquipementUI.remplirEquipement()
        self.listeNavigation.append(self.modificationEquipement)

    def ajouterBonDeTravailEquipement(self):
        '''
            Affichage du widget permettant l'ajout d'un bon de travail par rapport a un equipement
            Masquage des autres elements graphiques de la partie principale
            :param: None
            :return:
        '''
        #TODO passer les informations a la nouvelle fenetre
        # On masque les autres elements
        self.BoutonFlecheNavigation.show()
        self.frameFleche.show()
        self.masquerElementGraphique()
        equipement = self.consultationEquipementUI.equipement
        if self.ajoutBonDeTravailEquipement is None:
            # Creation du widget s'il n'existe pas
            self.ajoutBonDeTravailEquipement = QtWidgets.QWidget()
            self.ajoutBonDeTravailEquipementUI = BonDeTravail(self.ajoutBonDeTravailEquipement)
            self.ajoutBonDeTravailEquipement.setStyleSheet("background: white;")
            self.listeElementParDefaut.append(self.ajoutBonDeTravailEquipement)
            self.layoutAffichagePrincipal.addWidget(self.ajoutBonDeTravailEquipement)
        else:
            # Affichage du widget s'il existe deja
            self.ajoutBonDeTravailEquipement.show()
            self.ajoutBonDeTravailEquipementUI.equipementRecherche = equipement
            self.ajoutBonDeTravailEquipement.remplirEquipement()
        self.listeNavigation.append(self.ajoutBonDeTravailEquipement)

    def consulterBonDeTravail(self):
        '''
            Affichage du widget permettant de voir le bon de travail selectionne
            Masquage des autres elements graphiques de la partie principale
            :param: None
            :return:
        '''
        #TODO passer les informations a la nouvelle fenetre
        # On masque les autres elements
        self.BoutonFlecheNavigation.show()
        self.frameFleche.show()
        self.masquerElementGraphique()
        equipement = self.consultationEquipementUI.equipement
        if self.ajoutBonDeTravailEquipement is None:
            # Creation du widget s'il n'existe pas
            self.consultationBonDeTravail = QtWidgets.QWidget()
            self.consultationBonDeTravailUI = BonDeTravail(self.consultationBonDeTravail)
            self.consultationBonDeTravail.setStyleSheet("background: white;")
            self.listeElementParDefaut.append(self.consultationBonDeTravail)
            self.layoutAffichagePrincipal.addWidget(self.consultationBonDeTravail)
        else:
            # Affichage du widget s'il existe deja
            self.consultationBonDeTravail.show()
            self.consultationBonDeTravailUI.equipementRecherche = equipement
            self.consultationBonDeTravail.remplirEquipement()
        self.listeNavigation.append(self.consultationBonDeTravail)


    def imprimerInventaire(self):
        pdf = PDF()
        # pdf.creationPDF(pdf.fileName[0])
        pdf.start()
        # On attend la fin du thread, on annule le lancement en parallele pour l'instant car le logiciel repond mal
        pdf.join()

    def naviguer(self):
        if (len(self.listeNavigation) > 1):
            widget = self.listeNavigation.pop(len(self.listeNavigation) - 1)
            widget.hide()
            self.listeNavigation[len(self.listeNavigation) - 1].show()
            if (len(self.listeNavigation) == 1):
                self.BoutonFlecheNavigation.hide()
                self.frameFleche.hide()
        else:
            print("Il n'y a qu'un seul element")
            self.BoutonFlecheNavigation.hide()
            self.frameFleche.hide()



    def selectionOption(self):
        # self.BoutonAjouterEquipement.setStyleSheet("background-color: white")
        pass


class SIMM():
    '''
        Fonction de lancement de la page d'accueil de SIMM
        :param: None
        :return:
    '''
    # On masque les autres elements
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainFrame = QtWidgets.QMainWindow()
        ui = Accueil(MainFrame)
        MainFrame.show()
        sys.exit(app.exec_())
        os.system("pause")

if __name__ == "__main__":
    SIMM()
