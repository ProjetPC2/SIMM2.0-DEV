# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SupportPC2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from Interface.FenetresEnPython.SupportPC2UI import Ui_SupportPC2


class SupportPC2(Ui_SupportPC2):
    def __init__(self, widget):
        self.setupUi(widget)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainFrame = QtWidgets.QWidget()
    ui = SupportPC2(MainFrame)
    MainFrame.show()
    sys.exit(app.exec_())
