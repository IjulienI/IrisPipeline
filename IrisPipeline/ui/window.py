import webbrowser

import qtpy
import sys
import os

from PySide6.QtCore import QUrl, Slot, Qt
from PySide6.QtWebEngineWidgets import QWebEngineView
from qtpy import QtCore, QtWidgets, QtGui

ui_path = os.path.join(os.path.dirname(__file__), "qt/browser.ui")

class Browser(QtWidgets.QMainWindow):

    cb = QtWidgets.QApplication.clipboard()

    def __init__(self):
        super(Browser, self).__init__()
        from qtpy.uic import loadUi
        loadUi(ui_path, self)
        self.setWindowTitle("Browser")

app = QtWidgets.QApplication(sys.argv)
b = Browser()
b.show()

app.exec()