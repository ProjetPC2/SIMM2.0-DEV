# coding=utf-8
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
# Cette fonction devra etre appelee apres chaque fonction suivante :
# AjouterEquipement
# SupprimerEquipement
# ModifierEquipement
# pour etre surs que la configuration est toujours maintenu a jour

# Pour les fonctions qui dialoguent avec l'interface, renvoyer un dictionnaire
# avec le champ Reussite a True ou False selon la reussite de la fonction
# - Ajouter équipement
# - Modifier équipement



import yaml
from tinydb import *
from yamlStorage import YAMLStorage
import re


class EquipementManager:
    def __init__(self, pathname):
        self._pathname = pathname                               # pathname de la base de données des équipements
        with open('fichier_conf.yaml', 'r') as fichierConf:
            self._conf = yaml.load(fichierConf)

    def AjouterEquipement(self, dictio):
        db1 = TinyDB(self._pathname, storage=YAMLStorage)       # data base des équipements

        if (self._VerifierDict(dictio)):   # ARRANGER FONCTION AVANT
            id_eq = self._ObtenirProchainID()                       # id du nouvel équipement
            dictio['ID'] = str(id_eq)
            db1.insert(dictio)           # ajout du nouvel équipement dans la base de données
            self._ActualiserConfiguration()
            # Return dictio avec true ['Réussite' : True]
        else:
            print('An error occured')
            # Return dictio avec False
        
        # Renvoyer ID de l'equipement ajoute en plus dans le dictionnaire renvoye a l'interface

    def SupprimerEquipement(self, id_supp):                     # id_supp en int
        Equipement = Query()
        db = TinyDB(self._pathname, storage=YAMLStorage)        # data base des équipements
        result = db.remove(Equipement['ID'] == id_supp)         # suppression de l'équipement
        self._ActualiserConfiguration()
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
        self._ActualiserConfiguration()

    def _ObtenirProchainID(self):
        dernier_ID = self._conf['dernierID-Equipement']
        prochain_ID = int(dernier_ID) + 1
        ##### QUESTION ???? ##### ------------------------------- \/
        self._conf['dernierID-Equipement'] = prochain_ID        # À mettre directement dans AjouterEquipement??
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
        list_accepted_key_temp = list(self._conf['champsAcceptes-Equipement'])
        for key, value in dictio.items():
            if key in list_accepted_key_temp:
                list_accepted_key_temp.remove(key)
            else:
                conforme = False
        if (not conforme) or (len(list_accepted_key_temp) is not 0):
            return False
        else:
            return True

    # Deux étapes :
    # Étape 1: Vérifier que tous les champs attendus sont là
    # Étape 2: Vérifier qu'il n'y a pas un champ non attendu qui est là

    # Verifier si les valeurs des champs sont dans la configuration, si non ajouter la nouvelle valeur au dictionnaire
    def _VerifierDict(self, dictio):
        conforme = self._verifierChamps(dictio)
        list_categorie = list(self._conf['listeValeurs-categorieEquipement'])
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

    def _ActualiserConfiguration(self):
        with open('fichier_conf.yaml', 'w') as fichierConf:
            fichierConf.write(yaml.dump(self._conf, default_flow_style=False))

#if __name__ == "__main__":#Execution lorsque le fichier est lance
if True:
    #  TESTS
    manager = EquipementManager('DataBase_Equipement.json')

    data = {'CategorieEquipement': 'IRM',
            'Marque': 'blabla',
            'Modele': '23434',
            'NumeroSerie': None,
            'Salle': None,
            'CentreService': None,
            'DateAcquisition': None,
            'DateDernierEntretien': None,
            'Provenance': None,
            'EtatService': None,
            'EtatConservation': None,
            'Commentaires': None,
            'NbBonTravail': 0}

    #manager._ObtenirProchainID()
    #print(manager._VerifierDict(data))

    #dic_request = {'CategorieEquipement': 'ECG',
    #               'Marque': 'Peter',
    #               'Modele': 'blabla'}
    #dic_request = {'CategorieEquipement': 'ECG'}
    manager.AjouterEquipement(data)
    #manager.SupprimerEquipement('3')                     # id_supp en int
    #print(manager.RechercherEquipement(dic_request))
    #manager.ModifierEquipement('1', data)                 # id_modif en int






