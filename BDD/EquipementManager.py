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
from BDD.yamlStorage import YAMLStorage ## RAJOUT BDD.
import os
import datetime
import copy

class EquipementManager:
    def __init__(self, pathname):
        self._pathname = pathname                               # pathname de la base de données des équipements
        self.conf_file = 'fichier_conf.yaml'                    # pathname du fichier de configuration
        self.stats_file = 'fichier_stats.yaml'


    def AjouterEquipement(self, dictio):
        conf = self._getConf()
        stats = self._getStats()

        # ouverture de la base des données contenant les équipements
        db = self._getDB()

        dict_renvoi = {'Reussite': False}
        if self._verifierChamps(dictio, conf) and self._verifierDict(dictio, conf, stats):   # ARRANGER FONCTION AVANT
            id_eq = self._ObtenirProchainID()               # id du nouvel équipement
            dictio['ID'] = str(id_eq)                       # ajout de l'ID au dictionnaire
            dictio['NbBonTravail'] = 0                      # ajout du nombre de bon de travail qui est toujours 0 pour un nouvel équipement
            if db.insert(dictio) != list([]):
                dict_renvoi['Reussite'] = True              # ajout du nouvel équipement dans la base de données
                conf['dernierID-Equipement'] = id_eq      # mise à jour du champ dernierID-equipement dans le fichier de conf
                # mise à jour des données dans le fichier de stats pour l'ajout d'un nouvel équipement
                self._miseAJourStats(ancien_dict=None, nouveau_dict=dictio, stats_dict=stats)
            self._ActualiserConfiguration(conf)
        else:
            print('An error occured')
        
        return dict_renvoi
        
        # Renvoyer ID de l'equipement ajoute en plus dans le dictionnaire renvoye a l'interface


    def SupprimerEquipement(self, id_supp):                 # id_supp en int
        stats = self._getStats()

        Equipement = Query()
        dict_renvoi = {'Reussite': False}
        # ouverture de la base des données contenant les équipements
        db = self._getDB()
        
        ancien_dict = db.get(Equipement['ID'] == id_supp)
        if db.remove(Equipement['ID'] == id_supp) != list():
            dict_renvoi['Reussite'] = True                  # suppression de l'équipement, renvoie True seulement si l'équipement a été trouvé
            # modification du fichier de stats lors de la suppression d'un équipement
            self._miseAJourStats(ancien_dict=ancien_dict, nouveau_dict=None, stats_dict=stats)

        return dict_renvoi


    def RechercherEquipement(self, regex_dict):
        db = self._getDB()
        
        recherche = Query()
        firstEntry = True
        for key, value in regex_dict.items():
            if (key == "ID"):
                # Dans le cas de la recherche par ID
                queryUser = recherche.ID == value
            else:
                if firstEntry:
                    queryUser = (recherche[key].matches(value))
                    firstEntry = False
                else:
                    queryUser = (queryUser) & (recherche[key].matches(value))
        result = db.search(queryUser)

        return result


    def ModifierEquipement(self, id_modif, dict_modif):
        conf = self._getConf()
        stats = self._getStats()
        Equipement = Query()
        dict_renvoi = {'Reussite': False}
        db = self._getDB()
        
        ancien_dict = db.get(Equipement['ID'] == id_modif)
        # Verifier que tout ce qui est dans dict_modif est conforme à la forme d'un équipement et COMPLET
        if self._verifierChamps(dict_modif, conf) and self._verifierDict(dict_modif, conf, stats):
            if db.update(dict_modif, Equipement['ID'] == id_modif) != []:
                dict_renvoi['Reussite'] = True              # modif du dict associé à l'équipement
                self._miseAJourStats(ancien_dict=ancien_dict, nouveau_dict=dict_modif, stats_dict=stats)
        self._ActualiserConfiguration(conf)
        return dict_renvoi


    def _ObtenirProchainID(self):
        conf = self._getConf()
        dernier_ID = conf['dernierID-Equipement']
        prochain_ID = int(dernier_ID) + 1
        return prochain_ID


    def _verifierChamps(self, dictio, conf):
        conforme = True
        list_accepted_key_temp = list(conf['champsAcceptes-Equipement'])  # récupère la liste des 'accepted keys' dans le fichier de configuration
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
    def _verifierDict(self, dictio, conf, stats):
        #stats = self._getStats()

        conforme = True
        # récupère la liste des champs auxquels on peut ajouter des valeurs
        list_champ_ajout = list(conf['Equipement_ChampAjoutPermis'])
        # récupère la liste des champs auxquels on ne peut pas ajouter des valeurs
        list_champ_pas_ajout = list(conf['Equipement_ChampAjoutNonPermis'])
        # récupère la liste des champs qui doivent avoir un format précis
        list_champ_format_precis = list(conf['Equipement_ChampFormatPrecis'])
        # récupère la liste des champs qui doivent être ajoutés au fichier de stats
        list_champ_fichier_stat = list(conf['StatsAjoutFichier'])
        for key, value in dictio.items():              # parcourir le dictionnaire
            #print(key,value)
            if key in list_champ_ajout:                # à la recherche d'un champ que l'on peut ajouter des valeurs
                list_temp = list(conf[key])      # si la valeur recue n'est pas dans la le fichier de conf
                if value not in list_temp:             # on l'ajoute
                    conf[key].append(value)
            elif key in list_champ_pas_ajout:          # on regarde si la key fait partie des champs dont l'ajout de valeur n'est pas permis
                list_temp = list(conf[key])
                if value not in list_temp:             # si la valeur du dictio ne fait pas partie de la liste non modifiable, on renvoie false
                    conforme = False
            elif key in list_champ_format_precis:
                if not isinstance(value, datetime.date):    # PB: spécifique aux instances datetime.date...
                    conforme = False
            if key in list_champ_fichier_stat:      # vérifie si clée fait partie des champs qui modifient le fichier de stats
                if (key == 'Provenance') and (value not in stats['nbEquipementProvenance']):         # ajoute la provenance au fichier de stats
                    stats['nbEquipementProvenance'][value] = 0
                if key == 'CategorieEquipement':
                    if dictio['CentreService'] not in stats['nbEquipementCentreService']:  # vérifie si le centre de service associé à l'éq. est dans le fichier de stats
                        stats['nbEquipementCentreService'][dictio['CentreService']] = dict()   # si non, ajout du centre de service
                    if value not in stats['nbEquipementCentreService'][dictio['CentreService']]: # vérifie si l'équipement est dans le centre de service associé
                        stats['nbEquipementCentreService'][dictio['CentreService']][value] = 0    # si non, ajout de l'éq. dans le centre de service associé
        self._ActualiserConfiguration(conf)       # actualise le fichier de configuration et de stats pour qu'il contienne la nouvelle entrée
        self._ActualiserStats(stats)
        return conforme                       # retourne un booléen qui indique si le dictionnaire est conforme ou non


    def _ActualiserConfiguration(self, conf):
        try:
            if not os.path.exists(self.conf_file):                                      # vérifie si le fichier de configuration existe
                raise OSError
            else:
                with open(self.conf_file, 'w') as fichierConf:                               # ouvre le fichier et l'actualise
                    fichierConf.write(yaml.dump(conf, default_flow_style=False))
        except OSError:
            print("Could not update: ", self.conf_file)


    # Cette méthode renvoie le nombre d'équipements contenus dans la base de données
    def _statsNbTotalEquipement(self):
        stats = self._getStats()
        return stats['nbEquipement']


    # Cette méthode renvoie un dictionnaire avec comme clées les trois états de service possibles et comme valeur le
    # nombre d'équipements par état de service
    # key: {'En service', 'En maintenance', 'Au rebut'}
    def _statsNbEquipementEtatService(self):
        stats = self._getStats()
        return stats['nbEquipementEtatService']


    # Cette méthode renvoie un dictionnaire avec comme clées les quatre états de conservation possibles et comme valeur le
    # nombre d'équipements par état de conservation
    # key: {'Quasi neuf', 'Acceptable', 'En fin de vie', 'Desuet'}
    def _statsNbEquipementEtatConservation(self):
        stats = self._getStats()
        return stats['nbEquipementEtatConservation']


    # Cette méthode renvoie un dictionnaire avec comme clées les provenance possibles et comme valeur le
    # nombre d'équipements par provenance
    def _statsNbEquipementProvenance(self):
        stats = self._getStats()
        return stats['nbEquipementProvenance']


    # Cette méthode renvoie un dictionnaire à deux niveaux. Le premier niveau a comme clée les différents centres de
    # de service ('CentreService') qui se trouvent dans le fichier de configuration. Dans le champs des données pour ces clées,
    # on retrouve un dictionnaire (2e niveau) qui lui a comme clée les catégories d'équipements ('CategorieEquipement') que l'on
    # retrouve dans le fichier de configuration. Il est à noter que lorsqu'un centre de service ne possède pas d'équipements
    # d'un type X (ex. IRM), le champ contenant la clée X et la valeur 0 au deuxième niveau est retiré du dictionnaire.
    def _statsNbEquipementCentreServiceCategorie(self):
        stats = self._getStats()

        dict_renvoi = copy.deepcopy(stats['nbEquipementCentreService'])

        for key1, value1 in stats['nbEquipementCentreService'].items():
            for key2, value2 in value1.items():
                if value2 == 0:
                    del dict_renvoi[key1][key2]
        return dict_renvoi


    # Cette méthode permet de mettre à jour self._stats pour refléter les changements à la base de données lors
    # de l'ajout, de la suppression ou de la modification d'un équipement. Il met les champs à jour dans la variable globale
    # de la classe EquipementManager:_stats. L'utilisateur doit tout de même faire appel à la fonction _ActualiserStats pour mettre à
    # jour le fichier contenant les statistiques (fichier_stats.yaml)
    def _miseAJourStats(self, ancien_dict, nouveau_dict, stats_dict):
        if ancien_dict is None and nouveau_dict is not None:             # cas où on ajoute un equipement
            print('cas de ajout')
            stats_dict['nbEquipement'] += 1
            stats_dict['nbEquipementEtatConservation'][nouveau_dict['EtatConservation']] += 1
            stats_dict['nbEquipementEtatService'][nouveau_dict['EtatService']] += 1
            stats_dict['nbEquipementCentreService'][nouveau_dict['CentreService']][nouveau_dict['CategorieEquipement']] += 1
            stats_dict['nbEquipementProvenance'][nouveau_dict['Provenance']] += 1
        elif nouveau_dict is None and ancien_dict is not None:          # cas où on supprime un équipement
            print('cas de la suppression')
            stats_dict['nbEquipement'] -= 1
            stats_dict['nbEquipementEtatConservation'][ancien_dict['EtatConservation']] -= 1
            stats_dict['nbEquipementEtatService'][ancien_dict['EtatService']] -= 1
            stats_dict['nbEquipementCentreService'][ancien_dict['CentreService']][ancien_dict['CategorieEquipement']] -= 1
            stats_dict['nbEquipementProvenance'][ancien_dict['Provenance']] -= 1
        elif nouveau_dict is not None and ancien_dict is not None:      # cas où on modifie un équipement
            print('cas de la modification')
            if ancien_dict['EtatConservation'] != nouveau_dict['EtatConservation']:
                stats_dict['nbEquipementEtatConservation'][ancien_dict['EtatConservation']] -= 1
                stats_dict['nbEquipementEtatConservation'][nouveau_dict['EtatConservation']] += 1
            if ancien_dict['EtatService'] != nouveau_dict['EtatService']:
                stats_dict['nbEquipementEtatService'][ancien_dict['EtatService']] -= 1
                stats_dict['nbEquipementEtatService'][nouveau_dict['EtatService']] += 1
            if ancien_dict['Provenance'] != nouveau_dict['Provenance']:
                stats_dict['nbEquipementProvenance'][ancien_dict['Provenance']] -= 1
                stats_dict['nbEquipementProvenance'][nouveau_dict['Provenance']] += 1
            if ancien_dict['CentreService'] != nouveau_dict['CentreService'] or ancien_dict['CategorieEquipement'] != nouveau_dict['CategorieEquipement']:
                stats_dict['nbEquipementCentreService'][ancien_dict['CentreService']][ancien_dict['CategorieEquipement']] -= 1
                stats_dict['nbEquipementCentreService'][nouveau_dict['CentreService']][nouveau_dict['CategorieEquipement']] += 1
        self._ActualiserStats(stats_dict)


    def _ActualiserStats(self, stats):
        try:
            if not os.path.exists(self.stats_file):   # vérifie si le fichier de configuration existe
                raise OSError
            else:
                with open(self.stats_file, 'w') as fichierStat:      # ouvre le fichier et l'actualise
                    fichierStat.write(yaml.dump(stats, default_flow_style=False))
        except OSError:
            print("Could not update: ", self.stats_file)
    

    def _getConf(self):
        try:
            with open(self.conf_file, 'r') as fichierConf:            # try: ouvrir le fichier et le lire
                conf = yaml.load(fichierConf)
        except IOError:                                                             # attrape l'erreur IOError si elle se présente et renvoie
            print("Could not read file: ", self.conf_file)                          # définir ce qu'il faut faire pour corriger

        return conf


    def _getStats(self):
        try:
            with open(self.stats_file, 'r') as statFile:
                stats  = yaml.load(statFile)
        except IOError:
            print("Could not read file: ", self.stats_file)
        
        return stats


    def _getDB(self):
        try:
            if not os.path.exists(self._pathname):
                raise OSError("Oups nous ne trouvons plus la bdd équipements!")    # erreur si le path n'existe pas
            else:
                db = TinyDB(self._pathname, storage=YAMLStorage)  # data base des équipements
        except OSError as e:
            print(e)
        
        return db

if __name__ == "__main__":#Execution lorsque le fichier est lance
    if True:
        #  TESTS
        manager = EquipementManager('DataBase_Equipement.json')

        data = {'CategorieEquipement': 'Lit',
                'Marque': 'Bed-Ultra',
                'Modele': 'E432',
                'NumeroSerie': '1134',
                'Salle': 'A867',
                'CentreService': 'Natalité',
                'DateAcquisition': datetime.date(2008, 7, 12),
                'DateDernierEntretien': datetime.date(2011, 2, 27),
                'Provenance': 'Poly',
                'EtatService': 'En service',
                'EtatConservation': 'Quasi neuf',
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
        #print(manager.SupprimerEquipement('1'))                     # id_supp en int
        #print(manager.RechercherEquipement(dic_request))
        #print(manager.ModifierEquipement('3', data))               # id_modif en int

        # Stats
        #print(manager._statsNbTotalEquipement())
        #print(manager._statsNbEquipementEtatService())
        #print(manager._statsNbEquipementEtatConservation())
        #print(manager._statsNbEquipementProvenance())
        #print(manager._statsNbEquipementCentreServiceCategorie())



