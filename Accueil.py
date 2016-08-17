import locale
import os
import sys
from multiprocessing import Process

from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Interface.FenetresEnPython.AbstractWindow import AbstractWindow
from Interface.FenetresEnPython.AccueilUI import Ui_Accueil
from Interface.FenetresEnPython.AffichageMessage import AffichageMessage
from Interface.FenetresEnPython.AjoutEquipement import AjoutEquipement
from Interface.FenetresEnPython.Attente import Attente
from Interface.FenetresEnPython.BonDeTravail import BonDeTravail
from Interface.FenetresEnPython.ConsultationEquipement import ConsultationEquipement
from Interface.FenetresEnPython.ModificationEquipement import ModificationEquipement
from Interface.FenetresEnPython.PDF2 import PDF
from Interface.FenetresEnPython.Piece import Piece
from Interface.FenetresEnPython.RechercheBonDeTravail import RechercheBonDeTravail
from Interface.FenetresEnPython.RechercheEquipement import RechercheEquipement
from Interface.FenetresEnPython.Signaux import Communicate
from Interface.FenetresEnPython.Statistique import Statistique
from Interface.FenetresEnPython.SupportPC2 import SupportPC2
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
        self.attente = Accueil.attente
        self.aucunResultat = Accueil.aucunResultat
        self.sauvegarde = Accueil.sauvegarde
        self.Accueil = Accueil
        # Mise en francais des calendriers
        locale.setlocale(locale.LC_ALL, "fra")
        self.enregistrementReussi =  AffichageMessage("Enregistrement réussie", Accueil)
        self.enregistrementReussi.hide()
        self.suppression = Attente("Suppression en cours...", Accueil)
        self.suppression.hide()
        self.suppressionTermine = AffichageMessage("Suppression réussie", Accueil)
        self.suppressionTermine.hide()
        self.sauvegardeReussi = AffichageMessage("Sauvegarde réussie", Accueil)
        self.sauvegardeReussi.hide()
        self.creation = Communicate()

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
        self.ajoutPiece = None
        self.ajoutBonDeTravail = None
        self.rechercheBonDeTravail = None
        self.modificationEquipementRecherche = None
        self.modificationBonDeTravailRecherche = None
        # Connexion des actions aux cliques des boutons de la partie Bon de Travail
        # Creation du conteneur de la page statistique
        self.statistique = None

        # Creation de la partie Support
        self.support = None
        #self.supportPC2UI = None

        self.supprimeEquipement = None
        self.supprimeBonDeTravail = None
        #Connexion des differents elements
        self.connectionBouton()

        self.listeNavigation = list()

        self.boutonSelectionne = None




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

        self.BoutonAjouterPiece.clicked.connect(self.afficherAjoutPiece)
        self.BoutonAjouterBonTravail.clicked.connect(self.afficherAjoutBonDeTravail)
        self.BoutonRechercherBonTravail.clicked.connect(self.afficherRechercheBonDeTravail)

        self.BoutonImprimerInventaire.clicked.connect(self.imprimerInventaire)
        self.BoutonStatistiques.clicked.connect(self.afficherStatistique)

        self.BoutonSupportTecnique.clicked.connect(self.afficherSupport)

        self.BoutonFlecheNavigation.clicked.connect(self.naviguer)


    def afficherAjoutEquipement(self):
        '''
            Affichage du widget permet l'ajout d'un equipement
            Masquage des autres elements graphiques de la partie principale
            :param: None
            :return:
        '''
        # On masque les autres elements
        self.masquerElementGraphique()
        self.selectionnerBouton(self.BoutonAjouterEquipement)
        if self.ajoutEquipement is None:
            # Creation du widget s'il n'existe pas deja
            self.ajoutEquipement = QtWidgets.QWidget()
            self.ajoutEquipementUI = AjoutEquipement(self.ajoutEquipement)
            self.ajoutEquipementUI.BoutonEnregistrer.clicked.connect(self.sauvegardeEnCours)
            self.listeElementParDefaut.append(self.ajoutEquipement)
            self.ajoutEquipementUI.sauvegarde.sauvegardeTermine.connect(self.sauvegardeTermine)
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
        self.selectionnerBouton(self.BoutonModifierConsulterEquipement)
        if self.consultationEquipement is None:
            # Creation du widget s'il n'existe pas encore
            self.consultationEquipement = QtWidgets.QWidget()
            self.consultationEquipementUI = ConsultationEquipement(self.consultationEquipement)
            # connexion de l'action a l'appuye du bouton modification equipement
            self.consultationEquipementUI.boutonAfficherEquipement.clicked.connect(self.afficherChargement)
            self.consultationEquipementUI.lineEditId.returnPressed.connect(self.afficherChargement)
            self.consultationEquipementUI.boutonModifierEquipement.clicked.connect(self.modifierEquipement)
            #self.consultationEquipementUI.boutonModifierEquipement.clicked.connect(self.afficherChargement)

            self.consultationEquipementUI.boutonAjouterUnBon.clicked.connect(self.ajouterBonDeTravailEquipement)
            self.consultationEquipementUI.boutonConsulterBon.clicked.connect(self.consulterBonDeTravail)
            self.consultationEquipementUI.chargement.finChargement.connect(self.finChargement)
            self.consultationEquipementUI.chargement.aucunResultat.connect(self.afficherAucunResultat)
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
        self.selectionnerBouton(self.BoutonRechercherEquipement)
        if self.rechercheEquipement is None:
            # Creation du widget s'il n'existe pas
            self.rechercheEquipement = QtWidgets.QWidget()
            self.rechercheEquipementUI = RechercheEquipement(self.rechercheEquipement)
            # self.rechercheEquipement.setStyleSheet("background: white;")
            self.rechercheEquipementUI.comboBoxCategorieEquipement.currentTextChanged.connect(self.afficherChargement)
            self.rechercheEquipementUI.comboBoxProvenance.currentTextChanged.connect(self.afficherChargement)
            self.rechercheEquipementUI.comboBoxSalle.currentTextChanged.connect(self.afficherChargement)
            self.rechercheEquipementUI.comboBoxCentreService.currentTextChanged.connect(self.afficherChargement)
            self.rechercheEquipementUI.comboBoxEtatService.currentTextChanged.connect(self.afficherChargement)
            self.rechercheEquipementUI.lineEditNumeroSerie.returnPressed.connect(self.afficherChargement)
            self.rechercheEquipementUI.boutonActualiser.clicked.connect(self.afficherChargement)
            self.rechercheEquipementUI.tableResultats.doubleClicked.connect(self.choisirEquipement)
            self.rechercheEquipementUI.chargement.finChargement.connect(self.finChargement)
            self.rechercheEquipementUI.chargement.aucunResultat.connect(self.afficherAucunResultat)
            self.listeElementParDefaut.append(self.rechercheEquipement)
            self.layoutAffichagePrincipal.addWidget(self.rechercheEquipement)
        else:
            # Affichage du widget s'il existe deja
            self.rechercheEquipement.show()
        self.BoutonFlecheNavigation.hide()
        self.frameFleche.hide()
        self.listeNavigation.clear()
        self.listeNavigation.append(self.rechercheEquipement)

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
            self.modificationEquipementUI.BoutonEnregistrer.clicked.connect(self.sauvegardeEnCours)
            self.modificationEquipementUI.sauvegarde.sauvegardeTermine.connect(self.sauvegardeTermine)
            self.modificationEquipementUI.sauvegarde.sauvegardeTermine.connect(self.modificationTermine)
            # self.modificationEquipement.setStyleSheet("background: white;")
            self.listeElementParDefaut.append(self.modificationEquipement)
            self.layoutAffichagePrincipal.addWidget(self.modificationEquipement)
        else:
            # Affichage du widget s'il existe deja
            self.modificationEquipement.show()
            self.modificationEquipementUI.equipementRecherche = equipement
            self.modificationEquipementUI.remplirEquipement()
        self.listeNavigation.append(self.modificationEquipement)

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
            self.modificationEquipementRechercheUI.BoutonEnregistrer.clicked.connect(self.sauvegardeEnCours)
            self.modificationEquipementRechercheUI.sauvegarde.sauvegardeTermine.connect(self.sauvegardeTermine)
            self.modificationEquipementRechercheUI.sauvegarde.sauvegardeTermine.connect(self.modificationTermine)
            self.listeElementParDefaut.append(self.modificationEquipementRecherche)
            self.layoutAffichagePrincipal.addWidget(self.modificationEquipementRecherche)
        else:
            # Affichage du widget s'il existe deja
            self.modificationEquipementRecherche.show()
            self.modificationEquipementRechercheUI.equipementRecherche = equipement
            self.modificationEquipementRechercheUI.remplirEquipement()
        self.listeNavigation.append(self.modificationEquipementRecherche)


    def afficherAjoutPiece(self):
        '''
            Affichage du widget permet l'ajout d'une piece et le resume des categories de pieces
            Masquage des autres elements graphiques de la partie principale
            :param: None
            :return:
        '''
        self.masquerElementGraphique()
        self.selectionnerBouton(self.BoutonAjouterPiece)
        if self.ajoutPiece is None:
            self.ajoutPiece = QtWidgets.QWidget()
            self.pieceUI = Piece(self.ajoutPiece)
            self.pieceUI.BoutonEnregistrerPiece.clicked.connect(self.enregistrer)
            self.pieceUI.enregistrement.enregistrementTermine.connect(self.enregistrementTermine)
            self.listeElementParDefaut.append(self.ajoutPiece)
            self.layoutAffichagePrincipal.addWidget(self.ajoutPiece)
        else:
            self.ajoutPiece.show()
        self.BoutonFlecheNavigation.hide()
        self.frameFleche.hide()
        self.listeNavigation.clear()


    def afficherAjoutBonDeTravail(self):
        '''
            Affichage du widget permet l'ajout d'un bon de travail
            Masquage des autres elements graphiques de la partie principale
            :param: None
            :return:
        '''
        # On masque les autres elements
        self.masquerElementGraphique()
        self.selectionnerBouton(self.BoutonAjouterBonTravail)
        if self.ajoutBonDeTravail is None:
            #TODO: Verifier la partie confirmation pour l'ajout d'un bon de travail
            # Creation du widget s'il n'existe pas
            self.ajoutBonDeTravail = QtWidgets.QWidget()
            self.bonDeTravailUI = BonDeTravail(self.ajoutBonDeTravail)
            # self.ajoutBonDeTravail.setStyleSheet("background: white;")
            self.bonDeTravailUI.boutonActualiser.clicked.connect(self.afficherChargement)
            self.bonDeTravailUI.lineEditID.returnPressed.connect(self.afficherChargement)
            self.bonDeTravailUI.chargement.finChargement.connect(self.finChargement)
            self.bonDeTravailUI.boutonSauvegarde.clicked.connect(self.sauvegardeEnCours)
            self.bonDeTravailUI.chargement.sauvegardeTermine.connect(self.sauvegardeTermine)
            self.listeElementParDefaut.append(self.ajoutBonDeTravail)
            self.layoutAffichagePrincipal.addWidget(self.ajoutBonDeTravail)
        else:
            # Affichage de l'element s'il existe deja
            self.ajoutBonDeTravail.show()
        self.BoutonFlecheNavigation.hide()
        self.frameFleche.hide()
        self.listeNavigation.clear()


    def afficherRechercheBonDeTravail(self):
        '''
            Affichage du widget permet la recherche d'un bon de travail
            Masquage des autres elements graphiques de la partie principale
            :param: None
            :return:
        '''
        # On masque les autres elements
        self.masquerElementGraphique()
        self.selectionnerBouton(self.BoutonRechercherBonTravail)
        if self.rechercheBonDeTravail is None:
            # Creation du widget s'il n'existe pas
            self.rechercheBonDeTravail = QtWidgets.QWidget()
            self.rechercheBonDeTravailUI = RechercheBonDeTravail(self.rechercheBonDeTravail)
            self.rechercheBonDeTravailUI.comboBoxCategorieEquipement.currentTextChanged.connect(self.afficherChargement)
            self.rechercheBonDeTravailUI.comboBoxCentreService.currentTextChanged.connect(self.afficherChargement)
            self.rechercheBonDeTravailUI.comboBoxEtat.currentTextChanged.connect(self.afficherChargement)
            self.rechercheBonDeTravailUI.calendrierApres.dateChanged.connect(self.afficherChargement)
            self.rechercheBonDeTravailUI.calendrierAvant.dateChanged.connect(self.afficherChargement)
            self.rechercheBonDeTravailUI.chargement.finChargement.connect(self.finChargement)
            self.rechercheBonDeTravailUI.chargement.aucunResultat.connect(self.afficherAucunResultat)
            self.rechercheBonDeTravailUI.tableResultats.doubleClicked.connect(self.choisirBonDeTravailTableau)
            self.listeElementParDefaut.append(self.rechercheBonDeTravail)
            self.layoutAffichagePrincipal.addWidget(self.rechercheBonDeTravail)
        else:
            # Affichage du widget s'il existe deja
            self.rechercheBonDeTravail.show()
        self.BoutonFlecheNavigation.hide()
        self.frameFleche.hide()
        self.listeNavigation.clear()
        self.listeNavigation.append(self.rechercheBonDeTravail)

    def choisirBonDeTravailTableau(self):
        '''
            Affichage du widget permettant de voir le bon de travail selectionne
            Masquage des autres elements graphiques de la partie principale
            :param: None
            :return:
        '''
        # TODO passer les informations a la nouvelle fenetreMDP
        # TODO : Faire un retour sur la page d'accueil
        # TODO: La fonction ne fonctionne pas pour l'instant

        # On masque les autres elements
        self.BoutonFlecheNavigation.show()
        self.frameFleche.show()
        self.masquerElementGraphique()
        if self.ajoutBonDeTravailEquipement is None:
            # Creation du widget s'il n'existe pas
            self.modificationBonDeTravailRecherche = QtWidgets.QWidget()
            self.modificationBonDeTravailRechercheUI = BonDeTravail(self.modificationBonDeTravailRecherche, consulterBDT=self.rechercheBonDeTravailUI.bonDeTravailSelectionne)
            self.modificationBonDeTravailRechercheUI.boutonActualiser.clicked.connect(self.afficherChargement)
            self.modificationBonDeTravailRechercheUI.lineEditID.returnPressed.connect(self.afficherChargement)
            self.modificationBonDeTravailRechercheUI.chargement.finChargement.connect(self.finChargement)
            self.modificationBonDeTravailRechercheUI.boutonSauvegarde.clicked.connect(self.sauvegardeEnCours)
            self.modificationBonDeTravailRechercheUI.chargement.sauvegardeTermine.connect(self.sauvegardeTermine)
            self.listeElementParDefaut.append(self.modificationBonDeTravailRecherche)
            self.layoutAffichagePrincipal.addWidget(self.modificationBonDeTravailRecherche)
        else:
            # Affichage du widget s'il existe deja
            self.modificationBonDeTravailRecherche.show()
            self.modificationBonDeTravailRechercheUI.consulterBonTravailSpecifique(self.rechercheBonDeTravailUI.bonDeTravailSelectionne)
        self.listeNavigation.append(self.modificationBonDeTravailRecherche)

    def afficherStatistique(self):
        '''
            Affichage du widget Statistique
            Masquage des autres elements graphiques de la partie principale
            :param: None
            :return:
        '''
        # On masque les autres elements
        self.masquerElementGraphique()
        self.selectionnerBouton(self.BoutonStatistiques)
        if self.statistique is None:
            # Creation du widget Statistique s'il n'existe pas
            self.statistique = QtWidgets.QWidget()
            self.statistiqueUI = Statistique(self.statistique)
            self.listeElementParDefaut.append(self.statistique)
            self.layoutAffichagePrincipal.addWidget(self.statistique)
        else:
            # Affichage du widget s'il existe deja
            self.statistiqueUI.miseAJourStats()
            self.statistique.show()

        self.BoutonFlecheNavigation.hide()
        self.frameFleche.hide()
        self.listeNavigation.clear()



    def afficherAccueil(self):
        '''
            Affichage du widget Support
            Masquage des autres elements graphiques de la partie principale
            :param: None
            :return:
        '''
        # On masque les autres elements
        self.selectionnerBouton(self.BoutonAccueil)
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
        # print("salut", self.horizontalLayout_2.minimumSize())
        for elementGraphique in self.listeElementParDefaut:
            elementGraphique.hide()
        if self.support is not None:
            print("verrouillage")
            self.supportPC2UI.boutonRinitialiserStatistiques.setEnabled(False)
            self.supportPC2UI.boutonSupprimerEquipement.setEnabled(False)
            self.supportPC2UI.boutonSupprimerBon.setEnabled(False)
            self.supportPC2UI.BoutonVerrou.setEnabled(True)


    def ajouterBonDeTravailEquipement(self):
        '''
            Affichage du widget permettant l'ajout d'un bon de travail par rapport a un equipement
            Masquage des autres elements graphiques de la partie principale
            :param: None
            :return:
        '''
        # On masque les autres elements
        self.BoutonFlecheNavigation.show()
        self.frameFleche.show()
        self.masquerElementGraphique()
        equipement = self.consultationEquipementUI.equipement
        if self.ajoutBonDeTravailEquipement is None:
            # Creation du widget s'il n'existe pas
            self.ajoutBonDeTravailEquipement = QtWidgets.QWidget()
            self.ajoutBonDeTravailEquipementUI = BonDeTravail(self.ajoutBonDeTravailEquipement, ajouterID=self.consultationEquipementUI.equipement["ID"])
            #TODO: garder seulement ce qui est utile, modifier la fenetreMDP en conséquent
            #TODO: Afficher le temps de chargement pour le changement de fenetreMDP
            self.ajoutBonDeTravailEquipementUI.boutonActualiser.clicked.connect(self.afficherChargement)
            self.ajoutBonDeTravailEquipementUI.lineEditID.returnPressed.connect(self.afficherChargement)
            self.ajoutBonDeTravailEquipementUI.chargement.finChargement.connect(self.finChargement)
            self.ajoutBonDeTravailEquipementUI.boutonSauvegarde.clicked.connect(self.sauvegardeEnCours)
            self.ajoutBonDeTravailEquipementUI.chargement.sauvegardeTermine.connect(self.sauvegardeTermine)

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
        #TODO passer les informations a la nouvelle fenetreMDP
        # On masque les autres elements
        self.BoutonFlecheNavigation.show()
        self.frameFleche.show()
        self.masquerElementGraphique()
        equipement = self.consultationEquipementUI.equipement
        if self.ajoutBonDeTravailEquipement is None:
            # Creation du widget s'il n'existe pas
            self.consultationBonDeTravail = QtWidgets.QWidget()
            # dictID = dict()
            # dictID["ID-EQ"] = self.consultationEquipementUI.equipement["ID"]
            # indice = self.consultationEquipementUI.comboBoxBons.currentText()
            # listeID = indice.split("-")
            # dictID["ID-BDT"] = listeID(len(listeID) - 1)
            print(self.consultationEquipementUI.listeBonDeTravail[self.consultationEquipementUI.comboBoxBons.currentIndex()])
            self.consultationBonDeTravailUI = BonDeTravail(self.consultationBonDeTravail, self.consultationEquipementUI.listeBonDeTravail[self.consultationEquipementUI.comboBoxBons.currentIndex()])
            #TODO: garder seulement ce qui est utile, modifier la fenetreMDP en conséquent
            #TODO: Afficher le temps de chargement pour le changement de fenetreMDP
            self.consultationBonDeTravailUI.boutonActualiser.clicked.connect(self.afficherChargement)
            self.consultationBonDeTravailUI.lineEditID.returnPressed.connect(self.afficherChargement)
            self.consultationBonDeTravailUI.chargement.finChargement.connect(self.finChargement)
            self.consultationBonDeTravailUI.boutonSauvegarde.clicked.connect(self.sauvegardeEnCours)
            self.consultationBonDeTravailUI.chargement.sauvegardeTermine.connect(self.sauvegardeTermine)

            self.listeElementParDefaut.append(self.consultationBonDeTravail)
            self.layoutAffichagePrincipal.addWidget(self.consultationBonDeTravail)
        else:
            # Affichage du widget s'il existe deja
            self.ajoutBonDeTravailEquipement.show()
            self.consultationBonDeTravailUI.equipementDictionnaire = equipement
            self.consultationBonDeTravailUI.consulterBonTravailSpecifique(self.consultationEquipementUI.listeBonDeTravail[self.consultationEquipementUI.comboBoxBons.currentIndex()])
        self.listeNavigation.append(self.consultationBonDeTravail)

    def imprimerInventaire(self):
        # pdf = PDF()
        # # pdf.creationPDF(pdf.fileName[0])
        # pdf.start()
        # # On attend la fin du thread, on annule le lancement en parallele pour l'instant car le logiciel repond mal
        # pdf.join()
        self.BoutonImprimerInventaire.setDisabled(True)

    def afficherSupport(self):
        '''
            Affichage du widget Support
            Masquage des autres elements graphiques de la partie principale
            :param: None
            :return:
        '''
        # On masque les autres elements
        self.masquerElementGraphique()
        self.selectionnerBouton(self.BoutonSupportTecnique)
        if self.support is None:
            # Creation du widget support s'il n'existe pas
            self.support = QtWidgets.QWidget()
            self.supportPC2UI = SupportPC2(self.support)
            self.supportPC2UI.boutonSupprimerEquipement.clicked.connect(self.supprimerEquipement)
            self.supportPC2UI.boutonSupprimerBon.clicked.connect(self.supprimerBonDeTravail)

            self.listeElementParDefaut.append(self.support)
            self.layoutAffichagePrincipal.addWidget(self.support)
            self.creation.supportCree.emit()
        else:
            # Affichage du widget support
            self.support.show()
        self.BoutonFlecheNavigation.hide()
        self.frameFleche.hide()
        self.listeNavigation.clear()
        self.listeNavigation.append(self.support)
        # self.attente.raise_()
        # self.attente.show()

    def supprimerEquipement(self):
        # On masque les autres elements
        self.masquerElementGraphique()
        self.frameFleche.show()
        self.BoutonFlecheNavigation.show()
        if self.supprimeEquipement is None:
            # Creation du widget s'il n'existe pas
            self.supprimeEquipement = QtWidgets.QWidget()
            self.supprimeEquipementUI = SuppressionEquipement(self.supprimeEquipement)
            self.supprimeEquipementUI.boutonAfficherEquipement.clicked.connect(self.afficherChargement)
            self.supprimeEquipementUI.lineEditId.returnPressed.connect(self.afficherChargement)
            self.supprimeEquipementUI.suppression.finChargement.connect(self.finChargement)
            self.supprimeEquipementUI.boutonSupprimerEquipement.clicked.connect(self.afficherSuppression)
            self.supprimeEquipementUI.suppression.suppressionTermine.connect(self.afficherSuppressionTermine)
            self.supprimeEquipementUI.suppression.aucunResultat.connect(self.afficherAucunResultat)
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

            self.supprimeBonDeTravailUI.boutonActualiser.clicked.connect(self.afficherChargement)
            self.supprimeBonDeTravailUI.lineEditID.returnPressed.connect(self.afficherChargement)
            self.supprimeBonDeTravailUI.chargement.finChargement.connect(self.finChargement)
            self.supprimeBonDeTravailUI.boutonSupprimerBon.clicked.connect(self.afficherSuppression)
            self.supprimeBonDeTravailUI.chargement.suppressionTermine.connect(self.afficherSuppressionTermine)

            self.listeElementParDefaut.append(self.supprimeBonDeTravail)
            self.layoutAffichagePrincipal.addWidget(self.supprimeBonDeTravail)
        else:
            # Affichage du widget s'il existe deja
            self.supprimeBonDeTravail.show()
        self.listeNavigation.append(self.supprimeBonDeTravail)

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



    def selectionnerBouton(self, bouton):
        if self.boutonSelectionne is not None:
            self.boutonSelectionne.setStyleSheet("QPushButton{ padding : 5px; border-radius: 8px; background-color: transparent ;color : white;}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #cccccc , stop: 1#f2f2f2);\n"
"}\n"
"\n"
"QPushButton:pressed{ background-color: #cccccc; }")
        self.boutonSelectionne = bouton
        if (self.boutonSelectionne != self.BoutonAccueil):
            self.boutonSelectionne.setStyleSheet("background: white;  border-radius: 0px ")

    def afficherChargement(self):
        self.attente.raise_()
        self.attente.show()

    def finChargement(self):
        print("fin chargement")
        self.attente.hide()

    def afficherAucunResultat(self):
        print("Aurcun resultat")
        self.aucunResultat.raise_()
        self.aucunResultat.show()

    def sauvegardeEnCours(self):
        print("Sauvegarde en cours")
        self.sauvegarde.raise_()
        self.sauvegarde.show()

    def sauvegardeTermine(self):
        print("Sauvegarde termine")
        self.sauvegarde.hide()
        self.sauvegardeReussi.raise_()
        self.sauvegardeReussi.show()

    def enregistrer(self):
        self.enregistrement.raise_()
        self.enregistrement.show()

    def enregistrementTermine(self):
        self.enregistrement.hide()
        print("EnregistrementTermine")
        self.enregistrementReussi.raise_()
        self.enregistrementReussi.show()

    def modificationTermine(self):
        self.naviguer()

    def afficherSuppression(self):
        self.suppression.raise_()
        self.suppression.show()

    def afficherSuppressionTermine(self):
        self.suppression.hide()
        self.suppressionTermine.raise_()
        self.suppressionTermine.show()

class SIMM():
    '''
        Fonction de lancement de la page d'accueil de SIMM
        :param: None
        :return:
    '''
    # On masque les autres elements
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        # MainFrame = QtWidgets.QMainWindow()
        # self.mapper = QSignalMapper(MainFrame)
        # self.mapper.mapped[QtWidgets.QWidget].connect(impressionPDF)
        # self.ui = Accueil(MainFrame)
        # ui.BoutonImprimerInventaire.clicked.connect(impressionPDF)
        # MainFrame.setWindowIcon(QIcon('Images/SIMM2.0.png'))
        # MainFrame.setWindowTitle("SIMM 2.0")
        # print(MainFrame.centralWidget())
        # self.attente = Overlay(MainFrame.centralWidget())
        # self.attente.hide()
        # self.ui.BoutonAccueil.clicked.connect(self.attente.show)
        # MainFrame.show()
        # print(MainFrame.size())
        # MainFrame.resize(self.resizeEvent())
        # self.attente.move(250,250)
        MainFrame = MainWindow()
        MainFrame.show()
        sys.exit(app.exec_())
        os.system("pause")


class MainWindow(QMainWindow, AbstractWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.mapper = QSignalMapper(self)
        self.mapper.mapped[QtWidgets.QWidget].connect(impressionPDF)
        self.attente = None
        self.aucunResultat = None
        self.sauvegarde = None
        self.enregistrement = None
        self.ui = Accueil(self)
        self.ui.BoutonImprimerInventaire.clicked.connect(self.mapper.map)
        self.mapper.setMapping(self.ui.BoutonImprimerInventaire, self.ui.BoutonImprimerInventaire)
        self.setWindowIcon(QIcon('Images/SIMM2.0.png'))
        self.setWindowTitle("SIMM 2.0")
        self.attente = Attente("Chargement...", self.centralWidget())
        self.aucunResultat = AffichageMessage("Aucun résultat !", self.centralWidget())
        self.sauvegarde = Attente("Sauvegarde en cours...", self.centralWidget())
        self.enregistrement = Attente("Enregistrement en cours...", self.centralWidget())
        self.attente.hide()
        self.aucunResultat.hide()
        self.sauvegarde.hide()
        self.enregistrement.hide()
        self.ui.attente = self.attente
        self.ui.aucunResultat = self.aucunResultat
        self.ui.sauvegarde = self.sauvegarde
        self.ui.enregistrement = self.enregistrement
        self.ui.creation.supportCree.connect(self.verrou)
        self.signal = Communicate()
        self.signal.motDePasseCorrect.connect(self.deverouillage)

    def resizeEvent(self, event):
        print(event)
        print("size", event.size())
        self.attente.resize(event.size())
        self.aucunResultat.resize(event.size())
        self.sauvegarde.resize(event.size())
        self.ui.suppression.resize(event.size())
        self.ui.enregistrementReussi.resize(event.size())
        self.ui.suppressionTermine.resize(event.size())
        self.enregistrement.resize(event.size())
        event.accept()

    def verrou(self):
        self.ui.supportPC2UI.BoutonVerrou.clicked.connect(self.demanderMotDePasse)

    def demanderMotDePasse(self):

        self.fenetreMDP = QInputDialog()
        self.fenetreMDP.setStyleSheet("QPushButton {\n"
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
        self.fenetreMDP.setCancelButtonText("Annuler")
        self.fenetreMDP.setTextEchoMode(QLineEdit.Password)
        self.fenetreMDP.setLabelText("Veuillez entrer le mot de passe :")
        self.fenetreMDP.setWindowTitle("SIMM 2.0")
        self.fenetreMDP.setWindowIcon(QIcon('Images/SIMM2.0.png'))
        retour = self.fenetreMDP.exec()
        if(retour == QInputDialog.Accepted):
            if(self.fenetreMDP.textValue() == "hopitalstmichel123" ):
                print(str(self.fenetreMDP.textValue()))
                self.signal.motDePasseCorrect.emit()
            else:
                print("erreur de mot de passe")



    def deverouillage(self):
        self.ui.supportPC2UI.BoutonVerrou.setEnabled(False)
        self.ui.supportPC2UI.boutonSupprimerEquipement.setEnabled(True)
        self.ui.supportPC2UI.boutonSupprimerBon.setEnabled(True)
        self.ui.supportPC2UI.boutonRinitialiserStatistiques.setEnabled(True)

def impressionPDF(bouton):
    print(bouton)

    # ui.BoutonImprimerInventaire.disabled(True)
    print("impression en cours")
    filter = "PDF (*.pdf)"
    fileName = QFileDialog.getSaveFileName(None, 'Save file', os.path.expanduser("~/Desktop/SIMM2.0.pdf"),
                                           filter)
    if(fileName[0] != ""):
        p = Process(target=imprimer, args=(fileName[0], bouton))
        p.start()
    else:
        bouton.setDisabled(False)


def imprimer(path, bouton):

    print("Impression en cours de chez cours")
    pdf = PDF(path, bouton)
    print("Impression en cours de chez cours")
    # pdf.creationPDF(path)
    print("Impression en cours de chez cours")

if __name__ == "__main__":
    SIMM()
