# The MIT License (MIT)
#
# Copyright (c) 2017 Geoffroy Givry
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
import os
from PySide2 import QtGui, QtCore, QtWidgets
from Apps.Brontes.View import brontes_main_ui as b_UI
from Apps.Brontes.View import type_widget_ui as type_widget


class Type_widget(QtWidgets.QWidget, type_widget.Ui_type_widget):
    # creation of our custom widget based on type_widget UI
    def __init__(self):
        super(Type_widget, self).__init__()

        # Set up the user interface from Designer.
        self.setupUi(self)

    def set_text(self, text):
        self.type_label.setText(text)

    def set_icon(self, icon):
        self.type_icon.setPixmap(QtGui.QPixmap(icon))


class Brontes(QtWidgets.QWidget, b_UI.Ui_brontes_main):
    # main window UI
    def __init__(self):
        super(Brontes, self).__init__()

        # Set up the user interface from Designer.
        self.setupUi(self)
        type_list = ['All', 'Cam', "Layout", "CG", "3D", "Libs"]
        icon_all = os.path.join(os.getenv("CYC_CORE_PATH"), "icons", "all_icon.png")

        # populating The left widget list part with different types of assets.
        for n in type_list:
            type_wid = Type_widget()
            type_wid.set_text(n)
            type_wid.set_icon(icon_all)
            wid2 = QtWidgets.QListWidgetItem()
            wid2.setSizeHint(QtCore.QSize(100, 40))
            self.types_listWidget.addItem(wid2)
            self.types_listWidget.setItemWidget(wid2, type_wid)


def run_in_nuke():
    run_in_nuke.panel = Brontes()
    run_in_nuke.panel.show()


def runStandalone():

    app = QtWidgets.QApplication(sys.argv)
    panel = Brontes()
    panel.show()
    app.exec_()


if __name__ == "__main__":
    runStandalone()
