"""
Dans ce fichier vous pourrez voir :
-un exemple de creation d'une classe
-l'utilisation des getters et setters avec la fonction property
-l'utilisation des variables globales
"""
from datetime import datetime


class Equipement():
        """Classe Stockage va permettre de stocker les differentes informations du formulaire
        elle va contenir les attributs suivants :
        -un attribut global pour la liste des categories d'equipements
        -un attribut global pour la liste des salles
        -un attribut global pour la liste des centres de service
        -un attribut dictionnaire qui servira a stocker les differents informations des formulaires"""
        global listeCategorieEquipement
        listeCategorieEquipement= ["Categorie1", "Categorie2", "Categorie3"]
        global listeSalle
        listeSalle= ["Chambre patient", "Salle d'operation", "salle de reunion"]
        global listeUnite
        listeUnite= ["Unite 1", "Unite 2", "Unite 3"]
        global listeBonsDeTravail
        listeBonsDeTravail = ["Bon 1", "Bon 2", "Bon 3", "Bon 4", "Bon 5"]
        def __init__(self):  # Définition de la méthode de création d'un objet de la classe
            self._dictionnaire = dict()
            # self.remplissage()
            self.ajoutListeMethodes()

        def _getDictionnaire(self):  # accesseur sur la variable dictionnaire
            return self._dictionnaire

        def _setDictionnaire(self, dict):  # mutateur sur la variabe _dictionnaire
            self._dictionnaire = dict


        dictionnaire = property(_getDictionnaire, _setDictionnaire)




        def modifierCategorieEquipement(self, categorieEquipement):
            self.dictionnaire["CategorieEquipement"] = categorieEquipement

        def modifierMarque(self, marque):
            self.dictionnaire["Marque"] = marque

        def modifierModele(self, modele):
            self.dictionnaire["Modele"] = modele

        def modifierNumSerie(self, numSerie):
            self.dictionnaire["NumeroSerie"] = numSerie

        def modifierSalle(self, salle):
            self.dictionnaire["Salle"] = salle

        def modifierUnite(self, Unite):
            self.dictionnaire["Unite"] = Unite

        def modifierDateAcquisition(self, dateAcquisition):
            self.dictionnaire["DateAcquisition"] = dateAcquisition
            print(type(dateAcquisition))

        def modifierDateEntretien(self, dateEntretien):
            self.dictionnaire["DateDernierEntretien"] = dateEntretien
            print(type(dateEntretien))

        def modifierFreqEntretien(self, FreqEntretien):
            self.dictionnaire["FreqEntretien"] = FreqEntretien

        def modifierProvenance(self, provenance):
            self.dictionnaire["Provenance"] = provenance

        def modifierVoltage(self, Voltage):
            self.dictionnaire["Voltage"] = Voltage

        def modifierEtatService(self, etatService):
            self.dictionnaire["EtatService"] = etatService

        def modifierEtatConversation(self, etatConservation):
            self.dictionnaire["EtatConservation"] = etatConservation

        def modifierCommentaire(self, commentaire):
            self.dictionnaire["Commentaires"] = commentaire

        def modifierPDF(self, pdfPath):
            self.dictionnaire["PdfPath"] = pdfPath

        def ajoutListeMethodes(self):
            self.listeMethodes = list()
            self.listeMethodes.append(self.modifierCategorieEquipement)
            self.listeMethodes.append(self.modifierMarque)
            self.listeMethodes.append(self.modifierModele)
            self.listeMethodes.append(self.modifierNumSerie)
            self.listeMethodes.append(self.modifierSalle)
            self.listeMethodes.append(self.modifierUnite)
            self.listeMethodes.append(self.modifierDateAcquisition)
            self.listeMethodes.append(self.modifierDateEntretien)
            self.listeMethodes.append(self.modifierFreqEntretien)
            self.listeMethodes.append(self.modifierProvenance)
            self.listeMethodes.append(self.modifierVoltage)
            self.listeMethodes.append(self.modifierEtatService)
            self.listeMethodes.append(self.modifierEtatConversation)
            self.listeMethodes.append(self.modifierCommentaire)
            self.listeMethodes.append(self.modifierPDF)


class BonDeTravail():
    """Classe Stockage va permettre de stocker les differentes informations du formulaire
    elle va contenir les attributs suivants :
    -un attribut global pour la liste des categories d'equipements
    -un attribut global pour la liste des salles
    -un attribut global pour la liste des centres de service
    -un attribut dictionnaire qui servira a stocker les differents informations des formulaires"""

    def __init__(self):  # Définition de la méthode de création d'un objet de la classe
        self._dictionnaire = dict()
        self.remplissage()
        self.ajoutListeMethodes()

    def __init__(self):  # Définition de la méthode de création d'un objet de la classe
        self._dictionnaire = dict()
        self.ajoutListeMethodes()

    def _getDictionnaire(self):  # accesseur sur la variable _age
        return self._dictionnaire

    def _setDictionnaire(self, dict):  # mutateur sur la variabe _age
        self._dictionnaire = dict

    dictionnaire = property(_getDictionnaire, _setDictionnaire)

    def remplissage(self, equipement):
        self.dictionnaire["categorieEquipement"] = equipement.dictionnaire["categorieEqipement"]
        self.dictionnaire["marque"] = equipement.dictionnaire["marque"]
        self.dictionnaire["modele"] = equipement.dictionnaire["modele"]
        self.dictionnaire["salle"] = equipement.dictionnaire["salle"]
        self.dictionnaire["unite"] = equipement.dictionnaire["Unite"]
        self.dictionnaire["numeroBonDeTravail"] = ""
        self.dictionnaire["DescriptionSituation"] = ""
        self.dictionnaire["date"] = ""
        self.dictionnaire["tempsEstime"] = ""
        self.dictionnaire["descriptionIntervention"] = ""
        self.dictionnaire["etat"] = ""

    def modifierCategorieEquipement(self, categorieEquipement):
        self.dictionnaire["categorieEquipement"] = categorieEquipement

    def modifierMarque(self, marque):
        self.dictionnaire["marque"] = marque

    def modifierModele(self, modele):
        self.dictionnaire["modele"] = modele

    def modifierSalle(self, salle):
        self.dictionnaire["salle"] = salle

    def modifierUnite(self, unite):
        self.dictionnaire["unite"] = unite

    def modifierNumeroBonDeTravail(self, numeroBonDeTravail):
        self.dictionnaire["numeroBonDeTravail"] = numeroBonDeTravail

    def modifierDescriptionSituation(self, descriptionSituation):
        self.dictionnaire["DescriptionSituation"] = descriptionSituation

    def modifierDate(self, date):
        self.dictionnaire["date"] = date

    def modifierTempsEstime(self, tempsEstime):
        self.dictionnaire["tempsEstime"] = tempsEstime

    def modifierDescriptionIntervention(self, descriptionIntervention):
        self.dictionnaire["descriptionIntervention"] = descriptionIntervention

    def modifierEtat(self, etat):
        self.dictionnaire["etat"] = etat

    def modifierAssistance(self, assistance):
        self.dictionnaire["assistance"] = assistance

    def ajoutListeMethodes(self):
        self.listeMethodes = list()
        # self.listeMethodes.append(self.modifierIdEquipement)
        # self.listeMethodes.append(self.modifierCategorieEquipement)
        # self.listeMethodes.append(self.modifierMarque)
        # self.listeMethodes.append(self.modifierModele)
        # self.listeMethodes.append(self.modifierSalle)
        # self.listeMethodes.append(self.modifierCentreService)
        self.listeMethodes.append(self.modifierNumeroBonDeTravail)
        self.listeMethodes.append(self.modifierDescriptionSituation)
        self.listeMethodes.append(self.modifierDate)
        self.listeMethodes.append(self.modifierTempsEstime)
        self.listeMethodes.append(self.modifierDescriptionIntervention)
        self.listeMethodes.append(self.modifierEtat)
        self.listeMethodes.append(self.modifierAssistance)

def listeCle(dictionnaire) :
    cles = list()
    for key in dictionnaire:
        cles.append(key)
    return cles