# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ReqPiece.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ReqPiece(object):
    def setupUi(self, ReqPiece):
        ReqPiece.setObjectName("ReqPiece")
        ReqPiece.resize(1016, 913)
        self.valider_pushButton = QtWidgets.QPushButton(ReqPiece)
        self.valider_pushButton.setGeometry(QtCore.QRect(470, 830, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.valider_pushButton.setFont(font)
        self.valider_pushButton.setObjectName("valider_pushButton")
        self.annuler_pushButton = QtWidgets.QPushButton(ReqPiece)
        self.annuler_pushButton.setGeometry(QtCore.QRect(680, 830, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.annuler_pushButton.setFont(font)
        self.annuler_pushButton.setObjectName("annuler_pushButton")
        self.verticalLayoutWidget = QtWidgets.QWidget(ReqPiece)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 120, 179, 341))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.verticalLayoutWidget.setFont(font)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.equipement_titles_verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.equipement_titles_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.equipement_titles_verticalLayout.setObjectName("equipement_titles_verticalLayout")
        self.ID_title_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ID_title_label.setFont(font)
        self.ID_title_label.setObjectName("ID_title_label")
        self.equipement_titles_verticalLayout.addWidget(self.ID_title_label)
        self.cat_equip_title_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cat_equip_title_label.setFont(font)
        self.cat_equip_title_label.setObjectName("cat_equip_title_label")
        self.equipement_titles_verticalLayout.addWidget(self.cat_equip_title_label)
        self.marque_title_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.marque_title_label.setFont(font)
        self.marque_title_label.setObjectName("marque_title_label")
        self.equipement_titles_verticalLayout.addWidget(self.marque_title_label)
        self.modele_title_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.modele_title_label.setFont(font)
        self.modele_title_label.setObjectName("modele_title_label")
        self.equipement_titles_verticalLayout.addWidget(self.modele_title_label)
        self.unite_title_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.unite_title_label.setFont(font)
        self.unite_title_label.setObjectName("unite_title_label")
        self.equipement_titles_verticalLayout.addWidget(self.unite_title_label)
        self.salle_title_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.salle_title_label.setFont(font)
        self.salle_title_label.setObjectName("salle_title_label")
        self.equipement_titles_verticalLayout.addWidget(self.salle_title_label)
        self.nom_tech_title_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.nom_tech_title_label.setFont(font)
        self.nom_tech_title_label.setObjectName("nom_tech_title_label")
        self.equipement_titles_verticalLayout.addWidget(self.nom_tech_title_label)
        self.date_title_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.date_title_label.setFont(font)
        self.date_title_label.setObjectName("date_title_label")
        self.equipement_titles_verticalLayout.addWidget(self.date_title_label)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(ReqPiece)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(210, 120, 251, 341))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.verticalLayoutWidget_2.setFont(font)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.equipement_values_verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.equipement_values_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.equipement_values_verticalLayout.setObjectName("equipement_values_verticalLayout")
        self.ID_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.ID_label.setFont(font)
        self.ID_label.setText("")
        self.ID_label.setObjectName("ID_label")
        self.equipement_values_verticalLayout.addWidget(self.ID_label)
        self.cat_equip_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.cat_equip_label.setFont(font)
        self.cat_equip_label.setText("")
        self.cat_equip_label.setObjectName("cat_equip_label")
        self.equipement_values_verticalLayout.addWidget(self.cat_equip_label)
        self.marque_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.marque_label.setFont(font)
        self.marque_label.setText("")
        self.marque_label.setObjectName("marque_label")
        self.equipement_values_verticalLayout.addWidget(self.marque_label)
        self.modele_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.modele_label.setFont(font)
        self.modele_label.setText("")
        self.modele_label.setObjectName("modele_label")
        self.equipement_values_verticalLayout.addWidget(self.modele_label)
        self.unite_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.unite_label.setFont(font)
        self.unite_label.setText("")
        self.unite_label.setObjectName("unite_label")
        self.equipement_values_verticalLayout.addWidget(self.unite_label)
        self.salle_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.salle_label.setFont(font)
        self.salle_label.setText("")
        self.salle_label.setObjectName("salle_label")
        self.equipement_values_verticalLayout.addWidget(self.salle_label)
        self.nom_tech_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.nom_tech_label.setFont(font)
        self.nom_tech_label.setText("")
        self.nom_tech_label.setObjectName("nom_tech_label")
        self.equipement_values_verticalLayout.addWidget(self.nom_tech_label)
        self.date_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.date_label.setFont(font)
        self.date_label.setText("")
        self.date_label.setObjectName("date_label")
        self.equipement_values_verticalLayout.addWidget(self.date_label)
        self.function_title_label = QtWidgets.QLabel(ReqPiece)
        self.function_title_label.setGeometry(QtCore.QRect(30, 30, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.function_title_label.setFont(font)
        self.function_title_label.setObjectName("function_title_label")
        self.enregistrer_pdf_checkBox = QtWidgets.QCheckBox(ReqPiece)
        self.enregistrer_pdf_checkBox.setGeometry(QtCore.QRect(470, 770, 171, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.enregistrer_pdf_checkBox.setFont(font)
        self.enregistrer_pdf_checkBox.setObjectName("enregistrer_pdf_checkBox")
        self.envoyer_courriel_checkbox = QtWidgets.QCheckBox(ReqPiece)
        self.envoyer_courriel_checkbox.setGeometry(QtCore.QRect(680, 770, 181, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.envoyer_courriel_checkbox.setFont(font)
        self.envoyer_courriel_checkbox.setObjectName("envoyer_courriel_checkbox")
        self.envoyer_courriel_checkbox.setEnabled(False)
        self.equipement_title_label = QtWidgets.QLabel(ReqPiece)
        self.equipement_title_label.setGeometry(QtCore.QRect(30, 80, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setUnderline(True)
        self.equipement_title_label.setFont(font)
        self.equipement_title_label.setObjectName("equipement_title_label")
        self.piece_associee_title_label = QtWidgets.QLabel(ReqPiece)
        self.piece_associee_title_label.setGeometry(QtCore.QRect(470, 80, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setUnderline(True)
        self.piece_associee_title_label.setFont(font)
        self.piece_associee_title_label.setObjectName("piece_associee_title_label")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(ReqPiece)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(470, 120, 160, 141))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.verticalLayoutWidget_3.setFont(font)
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.piece_titles_verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.piece_titles_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.piece_titles_verticalLayout.setObjectName("piece_titles_verticalLayout")
        self.cat_piece_title_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cat_piece_title_label.setFont(font)
        self.cat_piece_title_label.setObjectName("cat_piece_title_label")
        self.piece_titles_verticalLayout.addWidget(self.cat_piece_title_label)
        self.nom_piece_title_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.nom_piece_title_label.setFont(font)
        self.nom_piece_title_label.setObjectName("nom_piece_title_label")
        self.piece_titles_verticalLayout.addWidget(self.nom_piece_title_label)
        self.nbr_unites_title_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.nbr_unites_title_label.setFont(font)
        self.nbr_unites_title_label.setObjectName("nbr_unites_title_label")
        self.piece_titles_verticalLayout.addWidget(self.nbr_unites_title_label)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(ReqPiece)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(630, 120, 251, 141))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.verticalLayoutWidget_4.setFont(font)
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.piece_values_verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.piece_values_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.piece_values_verticalLayout.setObjectName("piece_values_verticalLayout")
        self.cat_piece_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.cat_piece_label.setFont(font)
        self.cat_piece_label.setText("")
        self.cat_piece_label.setObjectName("cat_piece_label")
        self.piece_values_verticalLayout.addWidget(self.cat_piece_label)
        self.nom_piece_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.nom_piece_label.setFont(font)
        self.nom_piece_label.setText("")
        self.nom_piece_label.setObjectName("nom_piece_label")
        self.piece_values_verticalLayout.addWidget(self.nom_piece_label)
        self.nbr_unites_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.nbr_unites_label.setFont(font)
        self.nbr_unites_label.setText("")
        self.nbr_unites_label.setObjectName("nbr_unites_label")
        self.piece_values_verticalLayout.addWidget(self.nbr_unites_label)
        self.desc_situation_title_label = QtWidgets.QLabel(ReqPiece)
        self.desc_situation_title_label.setGeometry(QtCore.QRect(471, 300, 221, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.desc_situation_title_label.setFont(font)
        self.desc_situation_title_label.setObjectName("desc_situation_title_label")
        self.desc_intervention_title_label = QtWidgets.QLabel(ReqPiece)
        self.desc_intervention_title_label.setGeometry(QtCore.QRect(471, 460, 231, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.desc_intervention_title_label.setFont(font)
        self.desc_intervention_title_label.setObjectName("desc_intervention_title_label")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(ReqPiece)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(470, 320, 411, 131))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.verticalLayoutWidget_5.setFont(font)
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.desc_situation_verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.desc_situation_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.desc_situation_verticalLayout.setObjectName("desc_situation_verticalLayout")
        self.desc_situation_label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.desc_situation_label.sizePolicy().hasHeightForWidth())
        self.desc_situation_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.desc_situation_label.setFont(font)
        self.desc_situation_label.setText("")
        self.desc_situation_label.setObjectName("desc_situation_label")
        self.desc_situation_verticalLayout.addWidget(self.desc_situation_label, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(ReqPiece)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(470, 480, 411, 131))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.verticalLayoutWidget_6.setFont(font)
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.desc_intervention_verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.desc_intervention_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.desc_intervention_verticalLayout.setObjectName("desc_intervention_verticalLayout")
        self.desc_intervention_label = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.desc_intervention_label.sizePolicy().hasHeightForWidth())
        self.desc_intervention_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.desc_intervention_label.setFont(font)
        self.desc_intervention_label.setText("")
        self.desc_intervention_label.setObjectName("desc_intervention_label")
        self.desc_intervention_verticalLayout.addWidget(self.desc_intervention_label, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.photo_label = QtWidgets.QLabel(ReqPiece)
        self.photo_label.setGeometry(QtCore.QRect(30, 510, 421, 371))
        self.photo_label.setText("")
        self.photo_label.setObjectName("photo_label")
        self.photo_piece_title_label = QtWidgets.QLabel(ReqPiece)
        self.photo_piece_title_label.setGeometry(QtCore.QRect(30, 470, 131, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.photo_piece_title_label.setFont(font)
        self.photo_piece_title_label.setObjectName("photo_piece_title_label")
        self.parcourir_pushButton = QtWidgets.QPushButton(ReqPiece)
        self.parcourir_pushButton.setGeometry(QtCore.QRect(170, 470, 151, 25))
        self.parcourir_pushButton.setObjectName("parcourir_pushButton")

        self.retranslateUi(ReqPiece)
        QtCore.QMetaObject.connectSlotsByName(ReqPiece)

    def retranslateUi(self, ReqPiece):
        _translate = QtCore.QCoreApplication.translate
        ReqPiece.setWindowTitle(_translate("ReqPiece", "Réquisition de Pièce"))
        self.valider_pushButton.setText(_translate("ReqPiece", "Valider"))
        self.annuler_pushButton.setText(_translate("ReqPiece", "Annuler"))
        self.ID_title_label.setText(_translate("ReqPiece", "ID:"))
        self.cat_equip_title_label.setText(_translate("ReqPiece", "Catégorie d\'équipement:"))
        self.marque_title_label.setText(_translate("ReqPiece", "Marque:"))
        self.modele_title_label.setText(_translate("ReqPiece", "Modèle:"))
        self.unite_title_label.setText(_translate("ReqPiece", "Unité:"))
        self.salle_title_label.setText(_translate("ReqPiece", "Salle:"))
        self.nom_tech_title_label.setText(_translate("ReqPiece", "Nom du technicien:"))
        self.date_title_label.setText(_translate("ReqPiece", "Date:"))
        self.function_title_label.setText(_translate("ReqPiece", "Réquisition de pièce"))
        self.enregistrer_pdf_checkBox.setText(_translate("ReqPiece", "Enregistrer en PDF"))
        self.envoyer_courriel_checkbox.setText(_translate("ReqPiece", "Envoyer par courriel"))
        self.equipement_title_label.setText(_translate("ReqPiece", "Équipement"))
        self.piece_associee_title_label.setText(_translate("ReqPiece", "Pièce associée"))
        self.cat_piece_title_label.setText(_translate("ReqPiece", "Catégorie de la pièce:"))
        self.nom_piece_title_label.setText(_translate("ReqPiece", "Nom de la pièce:"))
        self.nbr_unites_title_label.setText(_translate("ReqPiece", "Nombre d\'unités:"))
        self.desc_situation_title_label.setText(_translate("ReqPiece", "Description de la situation:"))
        self.desc_intervention_title_label.setText(_translate("ReqPiece", "Description de l\'intervention:"))
        self.photo_piece_title_label.setText(_translate("ReqPiece", "Photo de la pièce:"))
        self.parcourir_pushButton.setText(_translate("ReqPiece", "Parcourir"))

