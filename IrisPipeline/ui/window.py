import webbrowser

import qtpy
import sys
import os

from PySide6.QtCore import QUrl, Slot, Qt
from PySide6.QtWebEngineWidgets import QWebEngineView
from qtpy import QtCore, QtWidgets, QtGui

ui_path = os.path.join(os.path.dirname(__file__), "qt/browser.ui")

class WebWindow(QtWidgets.QMainWindow):
    def __init__(self, url: str, title: str = "Web", size=(1024, 750), parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose, True)
        self.setWindowTitle(title)
        self.resize(*size)

        self.view = QWebEngineView(self)
        self.setCentralWidget(self.view)
        self.view.load(QUrl.fromUserInput(url))

    def load_url(self, url: str):
        self.view.load(QUrl.fromUserInput(url))

class Browser(QtWidgets.QMainWindow):

    cb = QtWidgets.QApplication.clipboard()

    def __init__(self):
        super(Browser, self).__init__()
        from qtpy.uic import loadUi
        loadUi(ui_path, self)
        self.setWindowTitle("Browser")

        self._windows  = []
        self.PB_help.clicked.connect(self.on_help_clicked)

    @Slot()
    def on_help_clicked(self):
        self.open_url("https://www.youtube.com/watch?v=xvFZjo5PgG0", title="Help")

    def open_url(self, url: str, title: str = "Web"):
        win = WebWindow(url=url, title=title, parent=None)
        win.show()

        self._windows.append(win)

        win.destroyed.connect(lambda *_: self._windows.remove(win) if win in self._windows else None)

app = QtWidgets.QApplication(sys.argv)
b = Browser()
b.show()

app.exec()