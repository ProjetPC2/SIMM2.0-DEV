# coding=utf-8
from tinydb import *
from tinydb.operations import increment
from yamlStorage import YAMLStorage
import datetime


class BonTravailManager:
    _listOfLegalKeys_BDT = ['Date', 'Temps estime', 'Description de la situation']  # Champs possibles pour BDT

    def __init__(self, bdt_pathname, equip_pathname):
        self._pathname = bdt_pathname                           # pathname de la base de données des bons de travail
        self._equip_pathname = equip_pathname

    def AjouterBonTravail(self, id_equipement, dictio):
        # Ajout du bon de travail dans la base de données
        db = TinyDB(self._pathname, storage=YAMLStorage)        # data base des bons de travail
        id_bdt = self._ObtenirProchainIDdeBDT(id_equipement)    # id du nouveau bon de travail

        if self._verifierDict(dictio):
            dictio['ID-EQ'] = id_equipement
            dictio['ID-BDT'] = id_bdt
            db.insert(dictio)                                       # ajout du nouveau bdt dans la db

            # Mise à jour du nombre de bons de travail pour cet équipement dans la base de données des équipements
            db_equip = TinyDB(self._equip_pathname, storage=YAMLStorage)
            Equipement = Query()
            db_equip.update(increment('Nombre de bons de travail'), Equipement['ID'] == id_equipement)
        else:
            print('Erreur dans le dictionnaire')

    def SupprimerBonTravail(self, id_eq_supp, id_bdt_supp):
        BonTravail = Query()
        db = TinyDB(self._pathname, storage=YAMLStorage)        # data base des bons de travail
        result = db.remove((BonTravail['ID-EQ'] == id_eq_supp) & (BonTravail['ID-BDT'] == id_bdt_supp))  # suppression du bdt
        return result

    def RechercherBonTravail(self, regex_dict):
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

    def ModifierBonTravail(self, id_eq_modif, id_bdt_modif, dict_modif):
        BonTravail = Query()
        db = TinyDB(self._pathname, storage=YAMLStorage)        # data base des bons de travail
        # modif du dict associé au bdt
        db.update(dict_modif, (BonTravail['ID-EQ'] == id_eq_modif) & (BonTravail['ID-BDT'] == id_bdt_modif))

    def _ObtenirProchainIDdeBDT(self, id_equip):
        Equipement = Query()
        db = TinyDB(self._equip_pathname, storage=YAMLStorage)
        equipement_ = db.get((Equipement['ID'] == id_equip))
        nb_bdt_pour_eq = equipement_['Nombre de bons de travail']
        # faire étape de vérification si l'équipement existe
        if nb_bdt_pour_eq is None:                                  # vérifier si des bons ont déjà été enregistrés
            new_id_bdt = 1
        else:
            new_id_bdt = nb_bdt_pour_eq + 1                         # nouvel id de bdt
        return new_id_bdt

    def _verifierChamps(self, dictio):
        conforme = True
        listeOfLegalKeys_temp = list(self._listOfLegalKeys_BDT)      # Enregistrer les champs possibles
        for key, value in dictio.items():                           # Vérifier pour chaque champ sa présence dans dictio
            if key in listeOfLegalKeys_temp:                        # Si champ présent dans champs possibles
                listeOfLegalKeys_temp.remove(key)                   # Le retirer de la liste temporaire
            else:                                                   # Sinon afficher erreur pour ce champ
                conforme = False                                    # Le dictionnaire n'est pas conforme
        if (not conforme) or (len(listeOfLegalKeys_temp) is not 0):
            return False
        else:
            return True

    def _verifierDict(self, dictio):
        conforme = self._verifierChamps(dictio)
        #print('Verification champs', conforme)
        for key, value in dictio.items():
            if key == 'Date':
                if not isinstance(value, datetime.date):
                    conforme = False
            if (key == 'Temps estime') or \
               (key == 'Description de la situation'):
                if not isinstance(value, str):
                    conforme = False
        #print('Verification Dict', conforme)
        return conforme



# TESTS
manager = BonTravailManager('DataBase_BDT.json', 'DataBase_Equipement.json')

data1 = {'Date': datetime.date(2016, 02, 22),                              # format de la date à vérifier
        'Temps estime': '1 semaine',
        'Description de la situation': 'tesst'}

"""data2 = {'Date': datetime.date.today(),                              # format de la date à vérifier
        'Temps estime': '2',
        'Description de la situation': 'test2'}"""

dic_request = {'Description de la situation': 'test',               # VÉRIFIER LA RECHERCHE POUR LES DATES...
               'Temps estime': '2'}


manager.AjouterBonTravail(1, data1)                                 # Ajout de 2 équipements de suite (pour tester...
#manager.AjouterBonTravail(1, data2)                                 # ... la vérification des champs)
#manager.SupprimerBonTravail(1, 2)                  # id_supp en int
#print(manager.RechercherBonTravail(dic_request))
#manager.ModifierBonTravail(1, 2, data)                # id_modif en int























