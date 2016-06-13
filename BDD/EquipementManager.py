############################################################################################################
# NOM : Projet PC2
# DATE DE LA DERNIÈRE  MODIFICATION : 9 juin 2016
#
# DESCRIPTION : CLASSE EQUIPEMENT_MANAGER
# Permet la gestion d'une base de données d'Équipements à partir de dictionnaires.
# Les fonctions possibles sont : AjouterEquipement, SupprimerEquipement, ModificerEquipement,
# RechercherEquipement.
# Un fichier de configuration est nécessaire au bon fonctionnement de cette classe (fichier_conf.yaml). *À compléter
############################################################################################################

# Ajouter fonction ActualiserConfiguration qui ecrit dans le fichier de configuration la configuration actualisee
# Cette fonction devra etre appelee apres chaque fonction pour etre surs que la configuration est toujours maintenu a jour

# coding=utf-8
import yaml
from tinydb import *
from yamlStorage import YAMLStorage
import re

#################################### A METTRE DANS FICHIER CONF ############################################
list_accepted_key = ['CategorieEquipement', 'Marque', 'Modele', 'NbBonTravail']
"""list_accepted_key = ['CategorieEquipement',      # voir list_catergorie
                     'Marque',
                     'Modele',
                     'NumeroSerie',
                     'Salle',                       # voir list_salle + autres entrees
                     'CentreService',               # voir list_centre_service + autres entrees
                     'DateAcquisition',
                     'DateDernierEntretien',
                     'Provenance',
                     'EtatService',                 # voir list_etat_service
                     'EtatConservation',            # voir list_etat_conservation
                     'Commentaires',
                     'NbBonTravail']"""
list_categorie = ['ECG', 'IRM', 'oxymetre', 'dialyse']
# list_salle = []
# list_centre_service = []
# list_etat_service = ['En service', 'En maintenance', 'Au rebut']
# list_etat_conservation = ['Quasi neuf', 'Acceptable', 'En fin de vie', 'Desuet']
############################################################################################################


class EquipementManager:
    def __init__(self, pathname):
        self._pathname = pathname                               # pathname de la base de données des équipements
        # self._nextID = 1   # pathname de la base de données de l'archive des équip.

        # nextID à mettre dans le fichier de configuration

    def AjouterEquipement(self, dictio):
        db1 = TinyDB(self._pathname, storage=YAMLStorage)       # data base des équipements

        # if (self._VerifierDict(dictio)):   # ARRANGER FONCTION AVANT
        id_eq = self._ObtenirProchainID()                       # id du nouvel équipement
        dictio['ID'] = id_eq
        db1.insert(dictio)           # ajout du nouvel équipement dans la base de données
        #else:
        #    print('An error occured')

    def SupprimerEquipement(self, id_supp):                     # id_supp en int
        Equipement = Query()
        db = TinyDB(self._pathname, storage=YAMLStorage)        # data base des équipements
        result = db.remove(Equipement['ID'] == id_supp)         # suppression de l'équipement
        return result

    def RechercherEquipement(self, regex_dict):
        db = TinyDB(self._pathname, storage=YAMLStorage)
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
        db = TinyDB(self._pathname, storage=YAMLStorage)        # data base des équipements
        # Verifier que tout ce qui est dans dict_modif est conforme à la forme d'un équipement et COMPLET
        db.update(dict_modif, Equipement['ID'] == id_modif)     # modif du dict associé à l'équipement

    def _ObtenirProchainID(self):
        with open('fichier_conf.yaml', 'r') as fichierConf:
            conf = yaml.load(fichierConf)
        dernier_ID = conf['ID']
        prochain_ID = int(dernier_ID) + 1
        conf['ID'] = prochain_ID

        with open('fichier_conf.yaml', 'w') as fichierConf:
            fichierConf.write(yaml.dump(conf, default_flow_style=False))
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

    # À COMPLÉTER
    def _verifierChamps(self, dictio):
        conforme = True
        list_accepted_key_temp = list(list_accepted_key)
        for key, value in dictio.items():
            if key in list_accepted_key_temp:
                list_accepted_key_temp.remove(key)
            else:
                conforme = False
        if (not conforme) or (len(list_accepted_key_temp) is not 0):
            return False
        else:
            return True

    """def _verifierChamps(self, dictio):
        length_normal_dictio = 6            # À REVOIR
        conforme = True
        if len(dictio) is not length_normal_dictio:  # Il faudrait toujours vérifier tous les champs, pas seulement la
                                                     # longueur du dictionnaire
            conforme = False
        else:
            if 'CategorieEquipement' not in dictio:
                conforme = False
            elif 'Marque' not in dictio:
                conforme = False
            elif 'Modele' not in dictio:
                conforme = False
            elif 'Nombre de bons de travail' not in dictio:                  # À revoir après discussion Alex et Cath
                conforme = False
        return conforme"""

    # Deux étapes :
    # Étape 1: Vérifier que tous les champs attendus sont là
    # Étape 2: Vérifier qu'il n'y a pas un champ non attendu qui est là

    def _VerifierDict(self, dictio):
        conforme = self._verifierChamps(dictio)
        # Vérifier que le contenu de chaque champ est conforme à ce qui est attendu
        for key, value in dictio.items():
            if key == 'CategorieEquipement':
                if (value not in list_categorie):
                    conforme = False
            if key == 'Marque':
                if not isinstance(value, str):
                    print('Hello')
                    conforme = False
        return conforme



if __name__ == "__main__":#Execution lorsque le fichier est lance
    #  TESTS
    manager = EquipementManager('DataBase_Equipement.json')

    data = {'CategorieEquipement': 'ECG',
            'Marque': 'Test',
            'Modele': 'blabla',
            'NbBonTravail': 0}                     # À revoir après discussion Alex et Cath


    print(manager._VerifierDict(data))

    #dic_request = {'CategorieEquipement': 'ECG',
    #               'Marque': 'Peter',
    #               'Modele': 'blabla'}
    dic_request = {'CategorieEquipement': 'ECG'}
    manager.AjouterEquipement(data)
    #manager.SupprimerEquipement(2)                     # id_supp en int
    #print(manager.RechercherEquipement(dic_request))
    #manager.ModifierEquipement(1, data)                 # id_modif en int






