import os
import sys
import time
from multiprocessing.pool import Pool

import yaml
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QFileDialog, QApplication, QPushButton
from multiprocessing import Process
from reportlab.lib import colors
from reportlab.lib.pagesizes import inch, A4, landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Table, Spacer
from reportlab.rl_config import defaultPageSize
from PyQt5.QtCore import *

import random
import sys
from threading import Thread
import time

from BDD.EquipementManagerSQLite import EquipementManager
from Interface.FenetresEnPython.Fichiers import pathEquipementDatabase
from BDD.BonTravailManagerSQLite import BonTravailManager
from Interface.FenetresEnPython.PDF2 import Signal


class Rapport():
    def __init__(self, path):
        # Thread.__init__(self)
        self.PAGE_WIDTH = defaultPageSize[1];
        self.PAGE_HEIGHT = defaultPageSize[0]

        #TODO : a completer avec le nom de l'hopital
        self.nomHopital = "Hopital Universitaire Justinien"

        self.Title = "Rapport - S.I.M.M 2.1"
        self.pageinfo = "S.I.M.M 2.1"
        #On autorise que les pdf
        # self.filter = "PDF (*.pdf)"
        # fileName = QFileDialog.getSaveFileName(None, 'Save file', "/home/SIMM2.0.pdf", filter)
        #On ouvre une fenetre de dialogue pour demander ou placer le fichier
        #On place le fichier par defaut dans le bureau avec le nom SIMM2.0.pdf
        # self.fileName = QFileDialog.getSaveFileName(None, 'Save file', os.path.expanduser("~/Desktop/SIMM2.0.pdf"), self.filter)
        # print("bouton", bouton.text())

        self.finImpression = Signal()
        self.listeCle = ["Date", "NomTechnicien", "IdEquipement", "NumeroBonTravail", "CategorieEquipement", "Marque", "Unite",
                         "Modele", "Salle", "DescriptionSituation", "DescriptionIntervention"]
        print(path)
        self.creationPDF(path.split(".csv")[0])

    def myFirstPage(self, canvas, doc):
        """Methode s'occupant de la mise en page du debut de document
        On va ici mettre les differentes informations utiles comme le titre, et les differentes informations d'impressions
        Cette methode fait la mise en page du debut du document"""
        canvas.saveState()
        canvas.setFont('Times-Bold',16)
        canvas.drawCentredString(self.PAGE_WIDTH/2.0, self.PAGE_HEIGHT-108, self.Title)
        canvas.setFont('Times-Roman',9)
        canvas.drawString(inch, 0.75 * inch, "Page %d / %s" % (doc.page, self.pageinfo))
        espace_soulignement = 10
        facteurDivision = 10
        espacement = 130
        technicien = "Techniciens de l'Hôpital Universitaire Justinien"
        canvas.drawString(self.PAGE_WIDTH / facteurDivision, 3 * self.PAGE_HEIGHT / 4, 'Hôpital Universitaire Justinien')
        canvas.line(self.PAGE_WIDTH / facteurDivision, 3 * self.PAGE_HEIGHT / 4 - espace_soulignement,
                    self.PAGE_WIDTH / facteurDivision + 230, 3 * self.PAGE_HEIGHT / 4 - espace_soulignement)
        # canvas.setLineWidth(1.2)
        canvas.drawString(self.PAGE_WIDTH / facteurDivision, 3 * self.PAGE_HEIGHT / 4 - 3 * espace_soulignement,
                          "Inventaire du parc d'équipements médicaux")
        canvas.drawString(500, 750, "12/12/2010")
        canvas.line(480, 747, 580, 747)
        canvas.drawString(6 * self.PAGE_WIDTH / facteurDivision, 3 * self.PAGE_HEIGHT / 4,
                          "Délivré par l'atelier de génie biomédical de l'HUJ")
        canvas.line(6 * self.PAGE_WIDTH / facteurDivision, 3 * self.PAGE_HEIGHT / 4 - espace_soulignement,
                    6 * self.PAGE_WIDTH / facteurDivision + 295, 3 * self.PAGE_HEIGHT / 4 - espace_soulignement)
        date = time.strftime("%d/%m/%Y")
        # datetime.datetime.now()#datetime.time.strftime("%d/%m/%Y")
        canvas.drawString(6 * self.PAGE_WIDTH / facteurDivision, 3 * self.PAGE_HEIGHT / 4 - 3 * espace_soulignement,
                          "Date : %s" % date)
        canvas.drawString(6 * self.PAGE_WIDTH / facteurDivision + espacement, 3 * self.PAGE_HEIGHT / 4 - 3 * espace_soulignement,
                          "Technicien : %s" % technicien)
        # canvas.drawImage(ImageReader(os.path.join("Images","SIMM2.0.png")), 100, 100)#, width=None, height=None, mask=None)

        # canvas.save()
        canvas.restoreState()

    def myLaterPages(self, canvas, doc):
        """Methode permettant d'avoir la numerotation de la page en bas a gauche
        Affichage du numero de la page et du nom du logiciel"""
        canvas.saveState()
        canvas.setFont('Times-Roman',9)
        canvas.drawString(inch, 0.75 * inch, "Page %d %s" % (doc.page, self.pageinfo))
        canvas.restoreState()

    def creationPDF(self, path):
        doc = SimpleDocTemplate(path, pagesize = landscape(A4))
        # Conteneur elements pour les objets qui vont etre dessines sur le pdf
        # Ajout d'un espacement
        elements = [Spacer(0, 2 * inch)]
        # Ajout du logo de SIMM
        elements.append(self.get_image(os.path.join("Images","Logo_SIMM.png"), width=5 * cm))
        elements.append(Spacer(0, 1 * inch))
        #Creation du style par defaut
        styleSheet = getSampleStyleSheet()
        style = styleSheet["Normal"]

        #Recuperation des donnees utiles dans les fichiers de la BDD
        bonTravailManager = BonTravailManager("Equipement.db")
        conf_file = 'fichier_conf.yaml'  # pathname du fichier de configuration
        try:
            fichierConf = open(conf_file, 'r')  # try: ouvrir le fichier et le lire
            with fichierConf:
                conf = yaml.load(fichierConf)
        except IOError:  # attrape l'erreur IOError si elle se présente et renvoie
            print("Could not read file: ", conf_file)  # définir ce qu'il faut faire pour corriger

        # récupère la liste des centres de services dans le fichier de configuration
        #listeUnite = list(conf['Unite'])
        l = [1]
        #Creation du tableau avec les informations concernant le centre de service

        currentDate = (QDate.currentDate().toPyDate())
        listeUnite = list(conf['Unite'])

        for Unite in l:

            print("DATE AUJOURHDUI ", currentDate)
            listBon = bonTravailManager.RechercherBonTravailRapport({"AvantLe" : currentDate})
            listeTotal = list()
            listeColonne1 = [Paragraph("<b>IdEq</b>", style),
                             Paragraph("<b>Categorie</b>", style),
                             Paragraph("<b>Marque // Modele</b>", style),
                             Paragraph("<b>DescriptionSituation</b>", style),
                             Paragraph("<b>Date</b>", style),
                             Paragraph("<b>NomTechnicien</b>", style),
                             Paragraph("<b>DescriptionIntervention</b>", style),
                             Paragraph("<b>Repare</b>", style),
                             Paragraph("<b>Assistance</b>", style)]
            listeTotal.append(listeColonne1)

            if (any(listBon)):
                # Cas ou l'equipement existe

                for i, dictionnaire in enumerate(listBon):
                    # Recuperation des donnees sous forme de string

                    print(dictionnaire)
                    idbdt = "{0}-{1}".format(str(dictionnaire["IdEquipement"]), str(dictionnaire["NumeroBonTravail"]))

                    equipementManager = EquipementManager(pathEquipementDatabase)
                    listeEquipement = equipementManager.RechercherEquipement({"ID": dictionnaire["IdEquipement"]})
                    if (any(listeEquipement)):
                        # Cas ou l'equipement existe
                        for i, dictionnaire2 in enumerate(listeEquipement):

                            MM = "{0} // {1}".format(str(dictionnaire2["Marque"]),str(dictionnaire["Modele"]))
                            #PARTIE RAPPORT EN FORMAT PDF
                            listTemp = list()
                            # for element in dictionnaire.values():
                            #     listTemp.append(element)
                            listTemp.append(Paragraph(idbdt, styleSheet['Normal']))
                            listTemp.append(Paragraph(dictionnaire2["CategorieEquipement"],styleSheet['Normal']))
                            listTemp.append(Paragraph(MM, styleSheet['Normal']))
                            listTemp.append(Paragraph(dictionnaire["DescriptionSituation"], styleSheet['Normal']))
                            listTemp.append(Paragraph(dictionnaire["Date"], styleSheet['Normal']))
                            listTemp.append(Paragraph(dictionnaire["NomTechnicien"], styleSheet['Normal']))
                            listTemp.append(Paragraph(dictionnaire["DescriptionIntervention"], styleSheet['Normal']))

                            #FIN

                            assistanceString = ""

                            if(dictionnaire["EtatBDT"] != "Ferme"):
                                listTemp.append(Paragraph("Non", styleSheet['Normal']))

                                listeAssistance = list()
                                #Ecriture des donnees d'assistance
                                if dictionnaire["Outils"] == 1:
                                    listeAssistance.append("Outils")
                                if dictionnaire["Pieces"] == 1:
                                    listeAssistance.append("Pieces")
                                if dictionnaire["Formation"] == 1:
                                    listeAssistance.append("Aide exterieur")
                                if dictionnaire["Manuel"] == 1:
                                    listeAssistance.append("Manuel")
                                #Creation de la chaine de caractere pour l'assistance
                                for i, assistance in enumerate(listeAssistance):
                                    assistanceString += assistance
                                    i += 1
                                    if(i < len(listeAssistance)):
                                        assistanceString += ", "

                            else:
                                listTemp.append(Paragraph("Oui", styleSheet['Normal']))

                            listTemp.append(Paragraph(assistanceString, styleSheet['Normal']))
                            listeTotal.append(listTemp)
            else:
                # Cas ou l'equipement n'existe pas
                pass

            tableauUnite = Table(listeTotal, style=[('BACKGROUND', (0, 0), (-1, 0), colors.gray),
                                         ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
                                         ('BOX', (0, 0), (-1, 0), 2, colors.black),
                                         ('BOX', (0, 0), (-1, -1), 2, colors.black),
                                         ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                                         ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                                         ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                                         ('FONTSIZE', (0, 0), (-1, -1), 12),
                                         ('FONTSIZE', (0, 0), (-1, 0), 14)

                                         ],)

            # t._argW[3] = 0.5 * inch

            #On ajoute les differents elements a la liste contenant les differents elements graphique du pdf
            Service = ("<b><u> Rapport des bons de travail </u></b>")
            titreTableau = Paragraph(Service, style)
            elements.append(titreTableau)
            #elements.append(Spacer(0,10))
            elements.append(tableauUnite)
            elements.append(Spacer(0, 50))


        # Ecriture du document pdf
        doc.build(elements, onFirstPage=self.myFirstPage, onLaterPages= self.myLaterPages)

        print("termine")
        self.finImpression.finImpression.emit()


    def get_image(self, path, width=1*cm):
        """Methode permettant la creation de l'image"""
        img = ImageReader(path)
        iw, ih = img.getSize()
        aspect = ih / float(iw)
        return Image(path, width=width, height=(width * aspect))

    def run(self):
        if(self.fileName[0] != None and self.fileName[0] !=""):
            # p = Process(target=self.creationPDF, args=(self.fileName[0],))
            # self.creationPDF(self.fileName[0])
            # p.start()
            pool = Pool(processes=4)  # start 4 worker processes
            result = pool.apply_async(self.creationPDF, [self.fileName[0]])
        else:
            print("Sauvegarde annule")

    def writeNewFileCsv(self, donnees):
        currentDate = str(QDate.currentDate().toPyDate())
        mon_fichier = open("Rapport_SIMM_" + currentDate + ".csv", "w")



class Signal(QObject):
    finImpression = pyqtSignal()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    pdf = Rapport(os.path.expanduser("~/Desktop/SIMM_Rapport.pdf"))

    # print(pdf.fileName[0])
    # # pdf.creationPDF(pdf.fileName[0])
    # pdf.run()
    sys.exit(app.exec_())
