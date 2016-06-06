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
        db1 = TinyDB(self._pathname, storage=YAMLStorage)        # data base des équipements
        # Verifier que tout ce qui est dans dictio est conforme à la forme d'un équipement et COMPLET
        id_eq = self._ObtenirProchainID()
        dictio['ID'] = id_eq
        db1.insert(dictio)

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


    # À COMPLÉTER
    def _verifierChamps(self, dictio):
        length_normal_dictio = 5
        conforme = True
        if len(dictio) is not length_normal_dictio:
            conforme = False
        else:
            if 'CategorieEquipement' not in dictio:
                conforme = False
            elif 'Marque' not in dictio:
                conforme = False
            elif 'Modele' not in dictio:
                conforme = False
        return conforme

    def _VerifierDict(self, dictio):
        conforme = self._verifierChamps(dictio)
        # Vérifier que le contenu de chaque champ est conforme à ce qui est attendu
        for key, value in dictio.items():
            if key == 'CategorieEquipement':
                if (value not in list_categorie):
                    conforme = False
            elif key == 'Marque':
                if(isinstance(value, str) is False):
                    print('Hello')
                    conforme = False
        return conforme
                
        

"""
# TESTS
manager = EquipementManager('DataBase_Equipement.json')

data = {'CategorieEquipement': 'Equip-modif',
        'Marque': 'Test-modif',
        'Modele': 'Modifie',
        'Nombre de bons de travail': 0}

#dic_request = {'CategorieEquipement': 'ECG',
#               'Marque': 'PierreSavard',
#               'Modele': 'blabla'}

dic_request = {'CategorieEquipement': 'ECG'}


manager.AjouterEquipement(data)
#manager.SupprimerEquipement(6)                     # id_supp en int
#print(manager.RechercherEquipement(dic_request))
#manager.ModifierEquipement(4, data)                 # id_modif en int

"""




