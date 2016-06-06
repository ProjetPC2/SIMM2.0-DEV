# coding=utf-8
import yaml
from tinydb import *
from yamlStorage import YAMLStorage
import re


list_categorie = ['ECG', 'IRM', 'oxymetre', 'dialyse']

class EquipementManager:
    def __init__(self, pathname):
        self._pathname = pathname                               # pathname de la base de données des équipements
        # self._nextID = 1   # pathname de la base de données de l'archive des équip.

        # nextID à mettre dans le fichier de configuration

    def AjouterEquipement(self, dictio):
        db1 = TinyDB(self._pathname, storage=YAMLStorage)       # data base des équipements
        id_eq = self._ObtenirProchainID()                       # id du nouvel équipement
        dictio['ID'] = id_eq
        # Verifier que tout ce qui est dans dictio est conforme à la forme d'un équipement et COMPLET
        db1.insert(dictio)                                      # ajout du nouvel équipement dans la base de données
        #self._nextID = 1   # pathname de la base de données de l'archive des équip.
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
            db = yaml.load(fichierConf)

        print(db)
        dernier_ID = db['ID']
        #print('dernierID', dernier_ID)
        prochain_ID = int(dernier_ID) + 1
        db['ID'] = prochain_ID
        #print('nextID', prochain_ID)

        with open('fichier_conf.yaml', 'w') as outfile:
            outfile.write( yaml.dump(db, default_flow_style=True) )

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
        return conforme

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
                
        


# TESTS
manager = EquipementManager('DataBase_Equipement.json')

data = {'CategorieEquipement': 'Equip',
        'Marque': 'Test',
        'Modele': 'blabla',
        'Nombre de bons de travail': 0}                     # À revoir après discussion Alex et Cath

#dic_request = {'CategorieEquipement': 'ECG',
#               'Marque': 'PierreSavard',
#               'Modele': 'blabla'}

dic_request = {'CategorieEquipement': 'ECG'}


manager.AjouterEquipement(data)
#manager.SupprimerEquipement(2)                     # id_supp en int
#print(manager.RechercherEquipement(dic_request))
#manager.ModifierEquipement(1, data)                 # id_modif en int






