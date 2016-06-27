# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SuppressionÉquipement2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SuppressionEquipement(object):
    def setupUi(self, SuppressionEquipement):
        SuppressionEquipement.setObjectName("SuppressionEquipement")
        SuppressionEquipement.resize(1420, 1078)
        SuppressionEquipement.setStyleSheet("#MainFrame {\n"
"\n"
"background: white;\n"
"}\n"
"QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid gray;\n"
"border-radius: 8px;\n"
"min-width: 50px;\n"
"max-width: 150px;\n"
"}\n"
"\n"
"QDateEdit {\n"
"max-width: 105px\n"
"}\n"
"\n"
"QPushButton {\n"
"color: black;\n"
"background-color: rgb(240, 240, 240);\n"
"border-width: 2px;\n"
"border-color: grey;\n"
"border-style: solid;\n"
"border-radius: 4px;\n"
"padding: 3px;\n"
"font: bold 14px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 40px;\n"
"max-width:220px;\n"
"min-height: 40px;\n"
"max-height: 40px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #edf2f8, stop: 1 #c8d9ea);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(193, 213, 243);\n"
"}\n"
"\n"
"\n"
"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 8em;\n"
"    max-width: 200px;\n"
"    \n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgrey;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(SuppressionEquipement)
        self.gridLayout.setObjectName("gridLayout")
        self.titreLayout = QtWidgets.QHBoxLayout()
        self.titreLayout.setObjectName("titreLayout")
        self.iconConsultationEquipement = QtWidgets.QLabel(SuppressionEquipement)
        self.iconConsultationEquipement.setText("")
        self.iconConsultationEquipement.setPixmap(QtGui.QPixmap("../Images/garbage (2).png"))
        self.iconConsultationEquipement.setScaledContents(False)
        self.iconConsultationEquipement.setObjectName("iconConsultationEquipement")
        self.titreLayout.addWidget(self.iconConsultationEquipement)
        self.labelTitreConsultationEquipement = QtWidgets.QLabel(SuppressionEquipement)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.labelTitreConsultationEquipement.setFont(font)
        self.labelTitreConsultationEquipement.setObjectName("labelTitreConsultationEquipement")
        self.titreLayout.addWidget(self.labelTitreConsultationEquipement)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.titreLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.titreLayout, 0, 0, 1, 4)
        self.idLayout = QtWidgets.QHBoxLayout()
        self.idLayout.setObjectName("idLayout")
        self.labelId = QtWidgets.QLabel(SuppressionEquipement)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labelId.setFont(font)
        self.labelId.setAlignment(QtCore.Qt.AlignCenter)
        self.labelId.setObjectName("labelId")
        self.idLayout.addWidget(self.labelId)
        self.lineEditId = QtWidgets.QLineEdit(SuppressionEquipement)
        self.lineEditId.setObjectName("lineEditId")
        self.idLayout.addWidget(self.lineEditId)
        self.gridLayout.addLayout(self.idLayout, 1, 0, 1, 3)
        self.buttonsLayout = QtWidgets.QHBoxLayout()
        self.buttonsLayout.setObjectName("buttonsLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.boutonAfficherEquipement = QtWidgets.QPushButton(SuppressionEquipement)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.boutonAfficherEquipement.setFont(font)
        self.boutonAfficherEquipement.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/Refresh2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonAfficherEquipement.setIcon(icon)
        self.boutonAfficherEquipement.setIconSize(QtCore.QSize(36, 36))
        self.boutonAfficherEquipement.setObjectName("boutonAfficherEquipement")
        self.verticalLayout_3.addWidget(self.boutonAfficherEquipement)
        self.buttonsLayout.addLayout(self.verticalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonsLayout.addItem(spacerItem1)
        self.boutonSupprimerEquipement = QtWidgets.QPushButton(SuppressionEquipement)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.boutonSupprimerEquipement.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/garbage (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonSupprimerEquipement.setIcon(icon1)
        self.boutonSupprimerEquipement.setIconSize(QtCore.QSize(42, 42))
        self.boutonSupprimerEquipement.setObjectName("boutonSupprimerEquipement")
        self.buttonsLayout.addWidget(self.boutonSupprimerEquipement)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonsLayout.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonsLayout.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonsLayout.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonsLayout.addItem(spacerItem5)
        self.gridLayout.addLayout(self.buttonsLayout, 1, 3, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelTitreCategorie = QtWidgets.QLabel(SuppressionEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelTitreCategorie.setFont(font)
        self.labelTitreCategorie.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitreCategorie.setObjectName("labelTitreCategorie")
        self.verticalLayout.addWidget(self.labelTitreCategorie, 0, QtCore.Qt.AlignRight)
        self.labelTitreMarque = QtWidgets.QLabel(SuppressionEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelTitreMarque.setFont(font)
        self.labelTitreMarque.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitreMarque.setObjectName("labelTitreMarque")
        self.verticalLayout.addWidget(self.labelTitreMarque, 0, QtCore.Qt.AlignRight)
        self.labelTitreModele = QtWidgets.QLabel(SuppressionEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelTitreModele.setFont(font)
        self.labelTitreModele.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTitreModele.setObjectName("labelTitreModele")
        self.verticalLayout.addWidget(self.labelTitreModele)
        self.labelTitreNoDeSerie = QtWidgets.QLabel(SuppressionEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelTitreNoDeSerie.setFont(font)
        self.labelTitreNoDeSerie.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTitreNoDeSerie.setObjectName("labelTitreNoDeSerie")
        self.verticalLayout.addWidget(self.labelTitreNoDeSerie)
        self.labelTitreSalle = QtWidgets.QLabel(SuppressionEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelTitreSalle.setFont(font)
        self.labelTitreSalle.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTitreSalle.setObjectName("labelTitreSalle")
        self.verticalLayout.addWidget(self.labelTitreSalle)
        self.labelTitreCentreDeService = QtWidgets.QLabel(SuppressionEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelTitreCentreDeService.setFont(font)
        self.labelTitreCentreDeService.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTitreCentreDeService.setObjectName("labelTitreCentreDeService")
        self.verticalLayout.addWidget(self.labelTitreCentreDeService)
        self.labelTitreDateDaquisition = QtWidgets.QLabel(SuppressionEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelTitreDateDaquisition.setFont(font)
        self.labelTitreDateDaquisition.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTitreDateDaquisition.setObjectName("labelTitreDateDaquisition")
        self.verticalLayout.addWidget(self.labelTitreDateDaquisition)
        self.labelTitreDateDuDernierEntretien = QtWidgets.QLabel(SuppressionEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelTitreDateDuDernierEntretien.setFont(font)
        self.labelTitreDateDuDernierEntretien.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTitreDateDuDernierEntretien.setObjectName("labelTitreDateDuDernierEntretien")
        self.verticalLayout.addWidget(self.labelTitreDateDuDernierEntretien)
        self.labelTitreProvenance = QtWidgets.QLabel(SuppressionEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelTitreProvenance.setFont(font)
        self.labelTitreProvenance.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTitreProvenance.setObjectName("labelTitreProvenance")
        self.verticalLayout.addWidget(self.labelTitreProvenance)
        self.labelTitreEtatDeService = QtWidgets.QLabel(SuppressionEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelTitreEtatDeService.setFont(font)
        self.labelTitreEtatDeService.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTitreEtatDeService.setObjectName("labelTitreEtatDeService")
        self.verticalLayout.addWidget(self.labelTitreEtatDeService)
        self.labelTitreEtatDeConservation = QtWidgets.QLabel(SuppressionEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelTitreEtatDeConservation.setFont(font)
        self.labelTitreEtatDeConservation.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTitreEtatDeConservation.setObjectName("labelTitreEtatDeConservation")
        self.verticalLayout.addWidget(self.labelTitreEtatDeConservation)
        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelCategorie = QtWidgets.QLabel(SuppressionEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCategorie.setFont(font)
        self.labelCategorie.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelCategorie.setObjectName("labelCategorie")
        self.verticalLayout_2.addWidget(self.labelCategorie)
        self.labelMarque = QtWidgets.QLabel(SuppressionEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelMarque.setFont(font)
        self.labelMarque.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelMarque.setObjectName("labelMarque")
        self.verticalLayout_2.addWidget(self.labelMarque)
        self.labelModele = QtWidgets.QLabel(SuppressionEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelModele.setFont(font)
        self.labelModele.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelModele.setObjectName("labelModele")
        self.verticalLayout_2.addWidget(self.labelModele)
        self.labelNoDeSerie = QtWidgets.QLabel(SuppressionEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelNoDeSerie.setFont(font)
        self.labelNoDeSerie.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelNoDeSerie.setObjectName("labelNoDeSerie")
        self.verticalLayout_2.addWidget(self.labelNoDeSerie)
        self.labelSalle = QtWidgets.QLabel(SuppressionEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelSalle.setFont(font)
        self.labelSalle.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelSalle.setObjectName("labelSalle")
        self.verticalLayout_2.addWidget(self.labelSalle)
        self.labelCentreDeService = QtWidgets.QLabel(SuppressionEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCentreDeService.setFont(font)
        self.labelCentreDeService.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelCentreDeService.setObjectName("labelCentreDeService")
        self.verticalLayout_2.addWidget(self.labelCentreDeService)
        self.labelDateDaquisition = QtWidgets.QLabel(SuppressionEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelDateDaquisition.setFont(font)
        self.labelDateDaquisition.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelDateDaquisition.setObjectName("labelDateDaquisition")
        self.verticalLayout_2.addWidget(self.labelDateDaquisition)
        self.labelDateDuDernierEntretien = QtWidgets.QLabel(SuppressionEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelDateDuDernierEntretien.setFont(font)
        self.labelDateDuDernierEntretien.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelDateDuDernierEntretien.setObjectName("labelDateDuDernierEntretien")
        self.verticalLayout_2.addWidget(self.labelDateDuDernierEntretien)
        self.labelProvenance = QtWidgets.QLabel(SuppressionEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelProvenance.setFont(font)
        self.labelProvenance.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelProvenance.setObjectName("labelProvenance")
        self.verticalLayout_2.addWidget(self.labelProvenance)
        self.labelEtatDeService = QtWidgets.QLabel(SuppressionEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelEtatDeService.setFont(font)
        self.labelEtatDeService.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelEtatDeService.setObjectName("labelEtatDeService")
        self.verticalLayout_2.addWidget(self.labelEtatDeService)
        self.labelEtatDeConservation = QtWidgets.QLabel(SuppressionEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelEtatDeConservation.setFont(font)
        self.labelEtatDeConservation.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelEtatDeConservation.setObjectName("labelEtatDeConservation")
        self.verticalLayout_2.addWidget(self.labelEtatDeConservation)
        self.gridLayout.addLayout(self.verticalLayout_2, 2, 2, 1, 2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.labelTitreCommentaires = QtWidgets.QLabel(SuppressionEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelTitreCommentaires.setFont(font)
        self.labelTitreCommentaires.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitreCommentaires.setObjectName("labelTitreCommentaires")
        self.horizontalLayout_7.addWidget(self.labelTitreCommentaires, 0, QtCore.Qt.AlignRight)
        self.gridLayout.addLayout(self.horizontalLayout_7, 3, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.labelCommentaires = QtWidgets.QLabel(SuppressionEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCommentaires.setFont(font)
        self.labelCommentaires.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelCommentaires.setObjectName("labelCommentaires")
        self.horizontalLayout_5.addWidget(self.labelCommentaires)
        self.gridLayout.addLayout(self.horizontalLayout_5, 3, 1, 1, 3)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.labelTitreBons = QtWidgets.QLabel(SuppressionEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelTitreBons.setFont(font)
        self.labelTitreBons.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTitreBons.setObjectName("labelTitreBons")
        self.horizontalLayout_8.addWidget(self.labelTitreBons)
        self.gridLayout.addLayout(self.horizontalLayout_8, 4, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.comboBoxBons = QtWidgets.QComboBox(SuppressionEquipement)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.comboBoxBons.setFont(font)
        self.comboBoxBons.setMaxCount(2147483645)
        self.comboBoxBons.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBoxBons.setObjectName("comboBoxBons")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../SIMM-2.0/Apprentissage Python/exercices/Hatim/Accueil/view-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBoxBons.addItem(icon2, "")
        self.comboBoxBons.addItem(icon2, "")
        self.comboBoxBons.addItem(icon2, "")
        self.horizontalLayout_6.addWidget(self.comboBoxBons, 0, QtCore.Qt.AlignLeft)
        self.boutonConsulterBon = QtWidgets.QPushButton(SuppressionEquipement)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Images/navigation.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonConsulterBon.setIcon(icon3)
        self.boutonConsulterBon.setObjectName("boutonConsulterBon")
        self.horizontalLayout_6.addWidget(self.boutonConsulterBon)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.gridLayout.addLayout(self.horizontalLayout_6, 4, 1, 1, 3)

        self.retranslateUi(SuppressionEquipement)
        QtCore.QMetaObject.connectSlotsByName(SuppressionEquipement)

    def retranslateUi(self, SuppressionEquipement):
        _translate = QtCore.QCoreApplication.translate
        SuppressionEquipement.setWindowTitle(_translate("SuppressionEquipement", "Form"))
        self.labelTitreConsultationEquipement.setText(_translate("SuppressionEquipement", "Suppression d\'équipements"))
        self.labelId.setText(_translate("SuppressionEquipement", "  Entrez le numéro d\'ID :"))
        self.boutonSupprimerEquipement.setText(_translate("SuppressionEquipement", "Supprimer l\'équipement"))
        self.labelTitreCategorie.setText(_translate("SuppressionEquipement", "Catégorie : "))
        self.labelTitreMarque.setText(_translate("SuppressionEquipement", "Marque : "))
        self.labelTitreModele.setText(_translate("SuppressionEquipement", "Modèle : "))
        self.labelTitreNoDeSerie.setText(_translate("SuppressionEquipement", "No. de série : "))
        self.labelTitreSalle.setText(_translate("SuppressionEquipement", "Salle : "))
        self.labelTitreCentreDeService.setText(_translate("SuppressionEquipement", "Centre de service : "))
        self.labelTitreDateDaquisition.setText(_translate("SuppressionEquipement", "Date d\'aquisition : "))
        self.labelTitreDateDuDernierEntretien.setText(_translate("SuppressionEquipement", "Date du dernier entretien : "))
        self.labelTitreProvenance.setText(_translate("SuppressionEquipement", "Provenance : "))
        self.labelTitreEtatDeService.setText(_translate("SuppressionEquipement", "État de service : "))
        self.labelTitreEtatDeConservation.setText(_translate("SuppressionEquipement", "État de conservation : "))
        self.labelCategorie.setText(_translate("SuppressionEquipement", "Équipement de Néonatologie"))
        self.labelMarque.setText(_translate("SuppressionEquipement", "Bosch"))
        self.labelModele.setText(_translate("SuppressionEquipement", "XR310b"))
        self.labelNoDeSerie.setText(_translate("SuppressionEquipement", "A265XG680H"))
        self.labelSalle.setText(_translate("SuppressionEquipement", "C-7612"))
        self.labelCentreDeService.setText(_translate("SuppressionEquipement", "Unité des soins intensifs (Néonatologie)"))
        self.labelDateDaquisition.setText(_translate("SuppressionEquipement", "2015-10-05"))
        self.labelDateDuDernierEntretien.setText(_translate("SuppressionEquipement", "2016-01-22"))
        self.labelProvenance.setText(_translate("SuppressionEquipement", "Suisse"))
        self.labelEtatDeService.setText(_translate("SuppressionEquipement", "Excellent"))
        self.labelEtatDeConservation.setText(_translate("SuppressionEquipement", "Non-Périmable"))
        self.labelTitreCommentaires.setText(_translate("SuppressionEquipement", "Commentaires : "))
        self.labelCommentaires.setText(_translate("SuppressionEquipement", "Ici se trouveront des commentaires consernant\n"
"l\'équipement en question et pourront être de toute nature.\n"
"Le commentaire peut être assez long, comme vous pouvez le constater, mais\n"
"vous ne pouvez vous arrêter de le lire, car\n"
"nous sommes programmés ainsi."))
        self.labelTitreBons.setText(_translate("SuppressionEquipement", "Bons : "))
        self.comboBoxBons.setItemText(0, _translate("SuppressionEquipement", "Bon 2016-01-22"))
        self.comboBoxBons.setItemText(1, _translate("SuppressionEquipement", "Bon 2016-03-07"))
        self.comboBoxBons.setItemText(2, _translate("SuppressionEquipement", "Bon 2016-05-12"))
        self.boutonConsulterBon.setText(_translate("SuppressionEquipement", "Consulter le Bon"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainFrame = QtWidgets.QWidget()
    ui = Ui_SuppressionEquipement()
    ui.setupUi(MainFrame)
    MainFrame.show()
    sys.exit(app.exec_())