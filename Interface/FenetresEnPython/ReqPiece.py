# -*- coding: utf-8 -*-
import datetime
from threading import Thread

from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# from Interface.FenetresEnPython.ReqPieceUI import Ui_ReqPiece
from ReqPieceUI import Ui_ReqPiece

class ReqPiece(Ui_ReqPiece):

    def __init__(self, widget):
        self.setupUi(widget)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainFrame = QtWidgets.QWidget()
    ui = ReqPiece(MainFrame)
    MainFrame.show()
    sys.exit(app.exec_())