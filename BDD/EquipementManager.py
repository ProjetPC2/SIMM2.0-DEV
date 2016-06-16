# coding=utf-8
############################################################################################################
# NOM : Projet PC2
# DATE DE LA DERNIÈRE  MODIFICATION : 15 juin 2016
#
# DESCRIPTION : CLASSE EQUIPEMENT_MANAGER
# Permet la gestion d'une base de données d'Équipements à partir de dictionnaires.
# Les fonctions possibles sont : AjouterEquipement, SupprimerEquipement, ModificerEquipement,
# RechercherEquipement.
# Un fichier de configuration est nécessaire au bon fonctionnement de cette classe (fichier_conf.yaml). *À compléter
############################################################################################################

# Ajouter fonction ActualiserConfiguration qui ecrit dans le fichier de configuration la configuration actualisee
# Cette fonction devra etre appelee apres chaque fonction suivante :
# AjouterEquipement
# SupprimerEquipement
# ModifierEquipement
# pour etre surs que la configuration est toujours maintenu a jour

# Pour les fonctions qui dialoguent avec l'interface, renvoyer un dictionnaire
# avec le champ Reussite a True ou False selon la reussite de la fonction
# - Ajouter équipement
# - Supprimer équipement
# - Modifier équipement


import yaml
from tinydb import *
from yamlStorage import YAMLStorage
import os
import datetime


class EquipementManager:
    def __init__(self, pathname):
        self._pathname = pathname                           # pathname de la base de données des équipements
        conf_file = 'fichier_conf.yaml'                     # pathname du fichier de configuration
        try:
            fichierConf = open(conf_file, 'r')              # try: ouvrir le fichier et le lire
            with fichierConf:
                self._conf = yaml.load(fichierConf)
        except IOError:                                     # attrape l'erreur IOError si elle se présente et renvoie
            print("Could not read file: ", conf_file)       # définir ce qu'il faut faire pour corriger

    def AjouterEquipement(self, dictio):
        # ouverture de la base des données contenant les équipements
        try:
            if not os.path.exists(self._pathname):
                raise OSError("Oups nous ne trouvons plus la bdd équipements!")    # erreur si le path n'existe pas
            else:
                db = TinyDB(self._pathname, storage=YAMLStorage)  # data base des équipements
        except OSError as e:
            print(e)

        dict_renvoi = {'Reussite': False}
        if self._verifierChamps(dictio) and self._verifierDict(dictio):   # ARRANGER FONCTION AVANT
            id_eq = self._ObtenirProchainID()               # id du nouvel équipement
            dictio['ID'] = str(id_eq)                       # ajout de l'ID au dictionnaire
            dictio['NbBonTravail'] = 0                      # ajout du nombre de bon de travail qui est toujours 0 pour un nouvel équipement
            if db.insert(dictio) != list([]):
                dict_renvoi['Reussite'] = True              # ajout du nouvel équipement dans la base de données
            self._conf['dernierID-Equipement'] = id_eq      # mise à jour du champ dernierID-equipement dans le fichier de conf
            self._ActualiserConfiguration()
            return dict_renvoi
        else:
            print('An error occured')
            return dict_renvoi
        
        # Renvoyer ID de l'equipement ajoute en plus dans le dictionnaire renvoye a l'interface

    def SupprimerEquipement(self, id_supp):                 # id_supp en int
        Equipement = Query()
        dict_renvoi = {'Reussite': False}
        # ouverture de la base des données contenant les équipements
        try:
            if not os.path.exists(self._pathname):
                raise OSError("Oups nous ne trouvons plus la bdd équipements!")  # erreur si le path n'existe pas
            else:
                db = TinyDB(self._pathname, storage=YAMLStorage)  # data base des équipements
        except OSError as e:
            print(e)
        if db.remove(Equipement['ID'] == id_supp) != list():
            dict_renvoi['Reussite'] = True                  # suppression de l'équipement, renvoie True seulement si l'équipement a été trouvé
        self._ActualiserConfiguration()
        return dict_renvoi

    def RechercherEquipement(self, regex_dict):
        try:
            if not os.path.exists(self._pathname):
                raise OSError("Oups nous ne trouvons plus la bdd équipements!")  # erreur si le path n'existe pas
            else:
                db = TinyDB(self._pathname, storage=YAMLStorage)  # data base des équipements
        except OSError as e:
            print(e)
        recherche = Query()
        firstEntry = True
        for key, value in regex_dict.items():
            if firstEntry:
                queryUser = (recherche[key].matches(value))
                firstEntry = False
            else:
                queryUser = (queryUser) & (recherche[key].matches(value))
        result = db.search(queryUser)
        return result

    def ModifierEquipement(self, id_modif, dict_modif):
        Equipement = Query()
        dict_renvoi = {'Reussite': False}
        try:
            if not os.path.exists(self._pathname):
                raise OSError("Oups nous ne trouvons plus la bdd équipements!")    # erreur si le path n'existe pas
            else:
                db = TinyDB(self._pathname, storage=YAMLStorage)  # data base des équipements
        except OSError as e:
            print(e)
        # Verifier que tout ce qui est dans dict_modif est conforme à la forme d'un équipement et COMPLET
        if self._verifierChamps(dict_modif) and self._verifierDict(dict_modif):
            if db.update(dict_modif, Equipement['ID'] == id_modif) != []:
                dict_renvoi['Reussite'] = True              # modif du dict associé à l'équipement
        self._ActualiserConfiguration()
        return dict_renvoi

    def _ObtenirProchainID(self):
        dernier_ID = self._conf['dernierID-Equipement']
        prochain_ID = int(dernier_ID) + 1
        return prochain_ID

    def configParser(configFile):
        config = yaml.load(configFile)
        for k in ['swsets']:
            if k in config:
                tup = ()
                for v in config[k]:
                    tup += (v,)
                config[k] = tup
        return config

    def _verifierChamps(self, dictio):
        conforme = True
        list_accepted_key_temp = list(self._conf['champsAcceptes-Equipement'])  # récupère la liste des 'accepted keys' dans le fichier de configuration
        for key, value in dictio.items():
            if key in list_accepted_key_temp:
                list_accepted_key_temp.remove(key)          # retire la clée du dictionnaire si elle est présente
            else:
                conforme = False                            # si on rencontre une clée non-attendue, le dictionnaire n'est pas conforme
        if (not conforme) or (len(list_accepted_key_temp) != 0):   # on renvoit Faux si la liste n'est pas vide (tous les champs attendus ne
            return False                                    # sont pas présents) ou si on a un champ en trop
        else:
            return True

    # Deux étapes :
    # Étape 1: Vérifier que tous les champs attendus sont là
    # Étape 2: Vérifier qu'il n'y a pas un champ non attendu qui est là

    # Verifier si les valeurs des champs sont dans la configuration, si non ajouter la nouvelle valeur au dictionnaire
    def _verifierDict(self, dictio):
        conforme = True
        # récupère la liste des champs auxquels on peut ajouter des valeurs
        list_champ_ajout = list(self._conf['Equipement_ChampAjoutPermis'])
        # récupère la liste des champs auxquels on ne peut pas ajouter des valeurs
        list_champ_pas_ajout = list(self._conf['Equipement_ChampAjoutNonPermis'])
        # récupère la liste des champs qui doivent avoir un forma précis
        list_champ_format_precis = list(self._conf['Equipement_ChampFormatPrecis'])
        for key, value in dictio.items():              # parcourir le dictionnaire
            if key in list_champ_ajout:                # à la recherche d'un champ que l'on peut ajouter des valeurs
                list_temp = list(self._conf[key])      # si la valeur recue n'est pas dans la le fichier de conf
                if value not in list_temp:             # on l'ajoute
                    self._conf[key].append(value)
            elif key in list_champ_pas_ajout:          # on regarde si la key fait partie des champs dont l'ajout de valeur n'est pas permis
                list_temp = list(self._conf[key])
                if value not in list_temp:             # si la valeur du dictio ne fait pas partie de la liste non modifiable, on renvoie false
                    conforme = False
            elif key in list_champ_format_precis:
                if not isinstance(value, datetime.date):    # PB: spécifique aux instances datetime.date...
                    conforme = False
        self._ActualiserConfiguration()       # actualise le fichier de configuration pour qu'il contienne la nouvelle entrée
        return conforme                       # retourne un booléen qui indique si le dictionnaire est conforme ou non

    def _ActualiserConfiguration(self):
        conf_file = 'fichier_conf.yaml'         # pathname du fichier de configuration
        try:
            if not os.path.exists(conf_file):   # vérifie si le fichier de configuration existe
                raise OSError
            else:
                fichierConf = open(conf_file, 'w')      # ouvre le fichier et l'actualise
                fichierConf.write(yaml.dump(self._conf, default_flow_style=False))
        except OSError:
            print("Could not update: ", conf_file)

    def _statsNbTotalEquipement(self):
        try:
            if not os.path.exists(self._pathname):
                raise OSError("Oups nous ne trouvons plus la bdd équipements!")    # erreur si le path n'existe pas
            else:
                db = TinyDB(self._pathname, storage=YAMLStorage)  # data base des équipements
        except OSError as e:
            print(e)
        return len(db)

    # Cette méthode renvoie un dictionnaire avec comme clées les trois états de service possibles et comme valeur le
    # nombre d'équipements par état de service
    # key: {'En service', 'En maintenance', 'Au rebut'}

    def _statsNbEquipementEtatService(self):
        try:
            if not os.path.exists(self._pathname):
                raise OSError("Oups nous ne trouvons plus la bdd équipements!")    # erreur si le path n'existe pas
            else:
                db = TinyDB(self._pathname, storage=YAMLStorage)  # data base des équipements
        except OSError as e:
            print(e)
        list_etat_service = list(self._conf['EtatService'])         # récupère les états de services possibles
        Equipement = Query()
        dictRenvoiEtatService = {}
        for element in list_etat_service:                   # parcoure la liste des états de service et recherche dans bdd
            dictRenvoiEtatService[element] = db.count(Equipement['EtatService'] == element)   # combien d'équipements ont le champ
        return dictRenvoiEtatService                                                          # 'EtatService' à la valeur de element

    # Cette méthode renvoie un dictionnaire avec comme clées les quatre états de conservation possibles et comme valeur le
    # nombre d'équipements par état de conservation
    # key: {'Quasi neuf', 'Acceptable', 'En fin de vie', 'Desuet'}

    def _statsNbEquipementEtatConservation(self):
        try:
            if not os.path.exists(self._pathname):
                raise OSError("Oups nous ne trouvons plus la bdd équipements!")    # erreur si le path n'existe pas
            else:
                db = TinyDB(self._pathname, storage=YAMLStorage)  # data base des équipements
        except OSError as e:
            print(e)
        list_etat_conservation = list(self._conf['EtatConservation'])  # récupère les états de conservation possibles
        Equipement = Query()
        dictRenvoiEtatConservation = {}
        for element in list_etat_conservation:                           # parcoure la liste des provenance et recherche dans bdd
            dictRenvoiEtatConservation[element] = db.count(Equipement['EtatConservation'] == element)  # combien d'équipements ont le champ
        return dictRenvoiEtatConservation                                                              # 'EtatConservation' à la valeur de element

    # Cette méthode renvoie un dictionnaire avec comme clées les provenance possibles et comme valeur le
    # nombre d'équipements par provenance
    def _statsNbEquipementProvenance(self):
        try:
            if not os.path.exists(self._pathname):
                raise OSError("Oups nous ne trouvons plus la bdd équipements!")    # erreur si le path n'existe pas
            else:
                db = TinyDB(self._pathname, storage=YAMLStorage)  # data base des équipements
        except OSError as e:
            print(e)
        list_provenance = list(self._conf['Provenance'])    # récupère la liste des provenances possibles
        Equipement = Query()
        dictRenvoiProvenance = {}
        for element in list_provenance:                         # parcoure la liste des provenance et recherche dans bdd
            dictRenvoiProvenance[element] = db.count(Equipement['Provenance'] == element)  # combien d'équipements ont le champ
        return dictRenvoiProvenance                                                        # 'Provenance' à la valeur de element

    # Cette méthode renvoie un dictionnaire à deux niveaux. Le premier niveau a comme clée les différents centres de
    # de service ('CentreService') qui se trouvent dans le fichier de configuration. Dans le champs des données pour ces clées,
    # on retrouve un dictionnaire (2e niveau) qui lui a comme clée les catégories d'équipements ('CategorieEquipement') que l'on
    # retrouve dans le fichier de configuration. Il est à noter que lorsqu'un centre de service ne possède pas d'équipements
    # d'un type X (ex. IRM), le champ contenant la clée X et la valeur 0 au deuxième niveau est retiré du dictionnaire.

    def _statsNbEquipementCentreServiceCategorie(self):
        try:
            if not os.path.exists(self._pathname):
                raise OSError("Oups nous ne trouvons plus la bdd équipements!")    # erreur si le path n'existe pas
            else:
                db = TinyDB(self._pathname, storage=YAMLStorage)  # data base des équipements
        except OSError as e:
            print(e)
        list_centre_service = list(self._conf['CentreService'])             # récupère les listes pour 'CentreService'
        list_categorie_equipement = list(self._conf['CategorieEquipement']) # et 'CategorieEquipement' dans le fichier de conf
        Equipement = Query()
        dictRenvoiCentreServiceCategorie = {}
        for centre in list_centre_service:                                  # on parcoure d'abord les centres de service
            dictRenvoiCentreServiceCategorie[centre] = {}
            for categorie in list_categorie_equipement:
                recherche_temp = db.count((Equipement['CategorieEquipement'] == categorie) &  # On compte le nombre de fois qu'il y un equipement
                                          (Equipement['CentreService'] == centre))            # qui est dans le même centre de service ET qui est de même catégorie
                if recherche_temp != 0:                                                       # On s'assure que la recherche ne retourne par 0, car ce n'est pas pertinent
                    dictRenvoiCentreServiceCategorie[centre][categorie] = recherche_temp      # pour nos statistiques
        return dictRenvoiCentreServiceCategorie


# if __name__ == "__main__":#Execution lorsque le fichier est lance
if True:
    #  TESTS
    manager = EquipementManager('DataBase_Equipement.json')

    data = {'CategorieEquipement': 'IRM',
            'Marque': 'HARRISON',
            'Modele': 'IS',
            'NumeroSerie': 'NICE',
            'Salle': 'A867',
            'CentreService': 'Urgence',
            'DateAcquisition': datetime.date(2010, 7, 12),
            'DateDernierEntretien': datetime.date(2011, 2, 27),
            'Provenance': 'CHU Ste-Justine',
            'EtatService': 'En maintenance',
            'EtatConservation': 'En fin de vie',
            'Commentaires': 'NONE'}

    #manager._ObtenirProchainID()
    #print(manager._VerifierDict(data))
    #dic_request = {'CategorieEquipement': 'ECG',
    #               'Marque': 'Peter',
    #               'Modele': 'blabla'}
    #dic_request = {'CategorieEquipement': '',
    #               'Salle': 'B',
    #               'CentreService': '',
    #               'NumeroSerie': '',
    #               'Provenance': '',
    #               'EtatService': '',
    #               'EtatConservation': ''}

    #print(manager.AjouterEquipement(data))
    #print(manager.SupprimerEquipement('9'))                     # id_supp en int
    #print(manager.RechercherEquipement(dic_request))
    #print(manager.ModifierEquipement('20', data))               # id_modif en int

    # Stats
    #print(manager._statsNbTotalEquipement())
    #print(manager._statsNbEquipementEtatService()
    #print(manager._statsNbEquipementEtatConservation())
    #print(manager._statsNbEquipementProvenance())
    #print(manager._statsNbEquipementCentreServiceCategorie())
