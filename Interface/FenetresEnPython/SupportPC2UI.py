# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SupportPC2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SupportPC2(object):
    def setupUi(self, SupportPC2):
        SupportPC2.setObjectName("SupportPC2")
        SupportPC2.resize(1350, 1273)
        self.verticalLayout = QtWidgets.QVBoxLayout(SupportPC2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.layoutTitre = QtWidgets.QHBoxLayout()
        self.layoutTitre.setObjectName("layoutTitre")
        self.label = QtWidgets.QLabel(SupportPC2)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/PC2_logo.png"))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.layoutTitre.addWidget(self.label)
        self.labelSupportPC2_2 = QtWidgets.QLabel(SupportPC2)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.labelSupportPC2_2.setFont(font)
        self.labelSupportPC2_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSupportPC2_2.setObjectName("labelSupportPC2_2")
        self.layoutTitre.addWidget(self.labelSupportPC2_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layoutTitre.addItem(spacerItem)
        self.verticalLayout.addLayout(self.layoutTitre)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.logoPC2 = QtWidgets.QLabel(SupportPC2)
        self.logoPC2.setMinimumSize(QtCore.QSize(300, 300))
        self.logoPC2.setSizeIncrement(QtCore.QSize(200, 0))
        self.logoPC2.setText("")
        self.logoPC2.setPixmap(QtGui.QPixmap("Images/PC2.png"))
        self.logoPC2.setAlignment(QtCore.Qt.AlignCenter)
        self.logoPC2.setObjectName("logoPC2")
        self.verticalLayout.addWidget(self.logoPC2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.labelDescription = QtWidgets.QLabel(SupportPC2)
        self.labelDescription.setTextFormat(QtCore.Qt.PlainText)
        self.labelDescription.setWordWrap(True)
        self.labelDescription.setObjectName("labelDescription")
        self.verticalLayout.addWidget(self.labelDescription)
        self.labelContact = QtWidgets.QLabel(SupportPC2)
        self.labelContact.setObjectName("labelContact")
        self.verticalLayout.addWidget(self.labelContact)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.boutonSupprimerEquipement = QtWidgets.QPushButton(SupportPC2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.boutonSupprimerEquipement.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/garbage (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonSupprimerEquipement.setIcon(icon)
        self.boutonSupprimerEquipement.setObjectName("boutonSupprimerEquipement")
        self.horizontalLayout_8.addWidget(self.boutonSupprimerEquipement)
        self.boutonSupprimerBon = QtWidgets.QPushButton(SupportPC2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/garbage.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonSupprimerBon.setIcon(icon1)
        self.boutonSupprimerBon.setIconSize(QtCore.QSize(32, 32))
        self.boutonSupprimerBon.setObjectName("boutonSupprimerBon")
        self.horizontalLayout_8.addWidget(self.boutonSupprimerBon)
        self.boutonRinitialiserStatistiques = QtWidgets.QPushButton(SupportPC2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Images/refresh-button-2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonRinitialiserStatistiques.setIcon(icon2)
        self.boutonRinitialiserStatistiques.setObjectName("boutonRinitialiserStatistiques")
        self.horizontalLayout_8.addWidget(self.boutonRinitialiserStatistiques)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.retranslateUi(SupportPC2)
        QtCore.QMetaObject.connectSlotsByName(SupportPC2)

    def retranslateUi(self, SupportPC2):
        _translate = QtCore.QCoreApplication.translate
        SupportPC2.setWindowTitle(_translate("SupportPC2", "Form"))
        self.labelSupportPC2_2.setText(_translate("SupportPC2", "Support PC2 - Projet S.I.M.M."))
        self.labelDescription.setText(_translate("SupportPC2", "Projet PC2 est un organisme à but non-lucratif fondé et dirigé par des étudiants de Polytechnique Montréal. Notre mission est de se rendre dans différents pays en développement pour outiller nos bénéficiaires afin qu’ils puissent eux-mêmes contribuer à l’amélioration de la santé, de l’éducation et de l’environnement dans leur pays. Nous tentons de donner une seconde vie au matériel informatique et médical en se rendant sur place pour offrir des formations sur l’utilisation et la maintenance de ces équipements. Notre stratégie est axée sur la maximisation des ressources déjà disponibles et le partage de connaissances. C’est en travaillant en collaboration avec nos bénéficiaires que nous pouvons y arriver.\n"
""))
        self.labelContact.setText(_translate("SupportPC2", "Contact : contact@xxx.com"))
        self.boutonSupprimerEquipement.setText(_translate("SupportPC2", "Supprimer un\n"
"Équipement"))
        self.boutonSupprimerBon.setText(_translate("SupportPC2", "Supprimer un\n"
"Bon de Travail"))
        self.boutonRinitialiserStatistiques.setText(_translate("SupportPC2", "Réinitialisier les\n"
"Statistiques"))

