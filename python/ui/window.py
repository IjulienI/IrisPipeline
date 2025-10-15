import sys
import os

from Qt.QtCompat import loadUi
from qtpy import QtWidgets
from iris import conf
from iris.core.finder import find

ui_path = os.path.join(os.path.dirname(__file__), "qt/browser.ui")

class Browser(QtWidgets.QMainWindow):

    cb = QtWidgets.QApplication.clipboard()

    def __init__(self):
        super(Browser, self).__init__()
        loadUi(ui_path, self)
        self.setWindowTitle(conf.browser_title)
        self.lw_asset_type.itemClicked.connect(self.fill_asset_name)

    def fill_asset_types(self, fill_object, search_type):
        types = find(search_type)
        fill_object.clear()
        for item in types:
            fill_object.addItem(item.data.get(search_type))

    def fill_asset_name(self, item = None):
        item_type = item.text()
        self.lw_asset_name.clear()
        types = find("asset_name", { "asset_type": item_type })
        for item in types:
            self.lw_asset_name.addItem(item.data.get("asset_name"))

app = QtWidgets.QApplication(sys.argv)
browser = Browser()
browser.fill_asset_types(browser.lw_asset_type, "asset_type")
browser.show()

app.exec()