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

import os


try:
    # < Nuke 11
    import PySide.QtCore as QtCore
    import PySide.QtGui as QtGui
    import PySide.QtGui as QtWidgets
    import PySide.QtUiTools as QtUiTools
except ImportError:
    # >= Nuke 11
    import PySide2.QtCore as QtCore
    import PySide2.QtGui as QtGui
    import PySide2.QtWidgets as QtWidgets
    import PySide2.QtUiTools as QtUiTools

from Core.utils import cyc_utils as utils
from Apps.Brontes.Model import hydra_model as hm
from Apps.Brontes.View import brontes_main_ui as b_UI
from Apps.Brontes.View import type_widget_ui as type_widget
from Apps.Brontes.View import asset_widget_ui as asset_widget
from Apps.Brontes.View import MainStyleSheet


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


class Asset_widget(QtWidgets.QWidget, asset_widget.Ui_Asset_Widget):
    # creation of our custom widget based on asset_widget UI
    def __init__(self):
        super(Asset_widget, self).__init__()

        # Set up the user interface from Designer.
        self.setupUi(self)
        self.version_data.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)

    def set_icon(self, icon, width, height):
        self.icon.setPixmap(QtGui.QPixmap(icon).scaled(width, height, QtCore.Qt.KeepAspectRatio))

    def set_username(self, text):
        self.userName.setText(text)

    def set_date(self, text):
        self.date.setText(text)

    def set_task(self, text):
        self.task.setText(text)

    def set_name(self, text):
        self.name.setText(text)

    def set_frameRange(self, first, last):
        self.frame_range_data.setText("{}-{}".format(first, last))

    def set_version(self, text):
        self.version_data.setText("v{}".format(text))
        self.version_data.setStyleSheet("qproperty-alignment: AlignRight;")

    def set_UUID(self, text):
        self.UUID_label.setText(text)

    def set_path(self, text):
        self.path_label.setText(text)

    def mouseMoveEvent(self, event):
        if not self.UUID_label.text():
            return
        mimeData = QtCore.QMimeData()
        mimeData.setText(self.UUID_label.text())
        drag = QtGui.QDrag(self)
        drag.setMimeData(mimeData)
        drag.exec_()


class Brontes(QtWidgets.QWidget, b_UI.Ui_brontes_main):
    # main window UI
    def __init__(self):
        super(Brontes, self).__init__()
        # Set up the user interface from Designer.
        self.setupUi(self)

        self.spacer01 = self.central_icon_verticalLayout.itemAt(0)
        self.cyc_icon_label = self.central_icon_label
        self.spacer02 = self.central_icon_verticalLayout.itemAt(2)
        self.toggle_central_icon()
        self.Model = hm.Model()
        self.types_tabWidget.setCurrentIndex(1)
        self.populate_type_shot_Widget()
        self.populate_type_asset_Widget()
        self.populate_entities()
        self.get_type_shot()

        self.populate_shows()  # populates list of actives shows in the show combobox
        self.populate_seqs()  # populates list of sequences in the seq combobox
        self.populate_shots()  # populates list of shots in the shot combobox

        self.asset_listWidget.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.cyc_icon.setPixmap(QtGui.QPixmap(
                                os.path.join(os.getenv("CYC_CORE_PATH"),
                                             "icons", "cyc_small.png")))
        self.search_button.setIcon(QtGui.QPixmap(
            os.path.join(os.getenv("CYC_CORE_PATH"),
                         "icons", "search.png")))

        MainStyleSheet.setStyleSheet(self)

        # Signals
        self.shot_type_listWidget.currentItemChanged.connect(self.populate_entities)
        self.shot_type_listWidget.currentItemChanged.connect(self.clear_search_lineEdit)
        self.assets_type_listWidget.currentItemChanged.connect(self.populate_entities)
        self.assets_type_listWidget.currentItemChanged.connect(self.clear_search_lineEdit)
        self.asset_listWidget.currentItemChanged.connect(self.populate_details)
        self.show_comboBox.currentIndexChanged.connect(self.populate_seqs)
        self.shot_comboBox.currentIndexChanged.connect(self.tab_changed)
        self.seq_comboBox.currentIndexChanged.connect(self.populate_shots)
        self.latest_checkBox.stateChanged.connect(self.populate_entities)
        self.latest_checkBox.stateChanged.connect(self.populate_entities_by_search_toggle)
        self.poly_lineEdit.returnPressed.connect(self.populate_entities_by_polyphemus)
        self.search_lineEdit.returnPressed.connect(self.populate_entities_by_search)
        self.search_button.clicked.connect(self.populate_entities_by_search)
        self.types_tabWidget.currentChanged.connect(self.tab_changed)

    def populate_type_shot_Widget(self):
        type_shot_dict = {"ALL": "all_icon.png", "CAM": "cam_icon.png",
                          "LGT": "lgt_icon.png", "ANM": "animation_icon.png",
                          "DMP": "matte_painting_icon.png", "PNT": "pnt_icon.png",
                          "RTO": "Roto_icon.png", "CMP": "cmp_icon.png",
                          "SFX": "sfx_icon.png"
                          }

        # populating The left widget list part with different types of assets.
        for n, v in sorted(type_shot_dict.iteritems()):
            icon_all = os.path.join(os.getenv("CYC_CORE_PATH"), "icons", v)
            type_wid = Type_widget()
            type_wid.set_text(n)
            type_wid.set_icon(icon_all)
            wid2 = QtWidgets.QListWidgetItem()
            wid2.setSizeHint(type_wid.sizeHint())
            self.shot_type_listWidget.addItem(wid2)
            self.shot_type_listWidget.setContentsMargins(100, 100, 100, 100)
            self.shot_type_listWidget.setItemWidget(wid2, type_wid)

    def populate_type_asset_Widget(self):
        type_asset_dict = {"ALL": "all_icon.png",
                           "CPA": "Concept_art_icon.png",
                           "MOD": "modeling_icon.png",
                           "TXT": "texture_icon.png",
                           "RIG": "rigging_icon.png",
                           "LYT": "layout_icon.png",
                           "CRE": "Creature_icon.png",
                           "SHD": "SHD_icon.png"
                           }

        # populating The left widget list part with different types of assets.
        for n, v in sorted(type_asset_dict.iteritems()):
            icon_all = os.path.join(os.getenv("CYC_CORE_PATH"), "icons", v)
            type_wid = Type_widget()
            type_wid.set_text(n)
            type_wid.set_icon(icon_all)
            wid2 = QtWidgets.QListWidgetItem()
            wid2.setSizeHint(type_wid.sizeHint())
            self.assets_type_listWidget.addItem(wid2)
            self.assets_type_listWidget.setContentsMargins(100, 100, 100, 100)
            self.assets_type_listWidget.setItemWidget(wid2, type_wid)

    def get_shot_entities_by_type(self):
        type_asset = self.get_type_shot()
        assets = []
        if type_asset == "ALL":
            if self.latest_checkBox.isChecked():
                assets = self.Model.get_all_latest_publish_shot(self.show_comboBox.currentText(), self.shot_comboBox.currentText())
            else:
                assets = self.Model.get_all_publish_shot(self.show_comboBox.currentText(), self.shot_comboBox.currentText())
        shot_tasks = ['ANM', 'CAM', 'CMP', 'DMP', 'LGT', 'PNT', 'RTO', 'SFX']
        for task in shot_tasks:
            if type_asset == task:
                if self.latest_checkBox.isChecked():
                    assets = self.Model.get_latest_publish_by_task(self.show_comboBox.currentText(), self.shot_comboBox.currentText(), task)
                else:
                    assets = self.Model.get_all_publish_by_task(self.show_comboBox.currentText(), self.shot_comboBox.currentText(), task)
        return assets

    def get_asset_entities_by_type(self):
        type_asset = self.get_type_assets()
        assets = []
        if type_asset == "ALL":
            if self.latest_checkBox.isChecked():
                assets = self.Model.get_all_latest_publish_asset(self.show_comboBox.currentText())
            else:
                assets = self.Model.get_all_publish_asset(self.show_comboBox.currentText())
        asset_tasks = ['CPA', 'MOD', 'TXT', 'RIG', 'LYT', 'CRE', 'SHD']
        for task in asset_tasks:
            if type_asset == task:
                if self.latest_checkBox.isChecked():
                    assets = self.Model.get_latest_asset_publish_by_task(self.show_comboBox.currentText(), task)
                else:
                    assets = self.Model.get_all_publish_assets_by_task(self.show_comboBox.currentText(), task)
        return assets

    def get_entities_by_polyphemus(self):
        return self.Model.get_unity_response(self.poly_lineEdit.text())

    def get_entities_by_search(self):
        search_query = self.search_lineEdit.text()
        if self.latest_checkBox.isChecked():
            if self.types_tabWidget.currentIndex() == 0:
                return self.Model.get_latest_asset_publish_by_search(self.show_comboBox.currentText(), search_query)
            if self.types_tabWidget.currentIndex() == 1:
                return self.Model.get_latest_publish_by_search(self.show_comboBox.currentText(), self.shot_comboBox.currentText(), search_query)
        else:
            if self.types_tabWidget.currentIndex() == 0:
                return self.Model.get_all_asset_publish_by_search(self.show_comboBox.currentText(), search_query)
            if self.types_tabWidget.currentIndex() == 1:
                return self.Model.get_all_publish_by_search(self.show_comboBox.currentText(), self.shot_comboBox.currentText(), search_query)

    def populate_widget_entities(self, assets):
        self.asset_listWidget.clear()
        for asset in assets:
            asset_widget = Asset_widget()
            asset_UUID = asset.get("UUID")
            if self.types_tabWidget.currentIndex() == 0:
                uuid_obj = utils.UUID(asset_UUID, "asset")
                if not uuid_obj.task() == 'TXT':
                    asset_widget.frame_range_data.hide()
                    asset_widget.frame_range_label.hide()
                else:
                    asset_widget.frame_range_label.setText("UDIM")
            if self.types_tabWidget.currentIndex() == 1:
                uuid_obj = utils.UUID(asset_UUID, "shot")
            asset_widget.set_username(asset.get('publisher'))
            pretty_date = utils.pretty_date(asset.get('pub_date'))
            asset_widget.set_date(pretty_date)
            asset_widget.set_task(uuid_obj.task())
            asset_widget.set_name(uuid_obj.name())
            if asset.get('type') == "2D":
                UUID_thumbnail = os.path.join(os.getenv("SHOW_PATH"), os.getenv("SHOW"), "tmp", "thumbnails", "{}.jpg".format(asset_UUID))
                if os.path.isfile(UUID_thumbnail):
                    asset_widget.set_icon(UUID_thumbnail, 75, (75 / 1.775))
                else:
                    asset_widget.set_icon(os.path.join(os.getenv("CYC_ICON"), "cyc_small.png"), 75, 75)

                first_frame = int(asset.get('first_frame'))
                last_frame = int(asset.get('last_frame'))
                asset_widget.set_frameRange(first_frame, last_frame)
            if asset.get('type') == "script":
                asset_widget.set_icon(os.path.join(os.getenv("CYC_ICON"), "script_small.png"), 75, 75)
                asset_widget.frame_range_label.hide()
                asset_widget.frame_range_data.hide()
            if uuid_obj.task() == "MOD":
                asset_widget.set_icon(os.path.join(os.getenv("CYC_ICON"), "mod_256.png"), 75, 75)
            if uuid_obj.task() == "TXT":
                asset_widget.set_icon(os.path.join(os.getenv("CYC_ICON"), "txt_256.png"), 75, 75)
            if uuid_obj.task() == "SHD":
                asset_widget.set_icon(os.path.join(os.getenv("CYC_ICON"), "shd_256.png"), 75, 75)
            if uuid_obj.task() == "CRE":
                asset_widget.set_icon(os.path.join(os.getenv("CYC_ICON"), "cre_256.png"), 75, 75)
            if uuid_obj.task() == "RIG":
                asset_widget.set_icon(os.path.join(os.getenv("CYC_ICON"), "rig_256.png"), 75, 75)
            if uuid_obj.task() == "LYT":
                asset_widget.set_icon(os.path.join(os.getenv("CYC_ICON"), "lyt_256.png"), 75, 75)
            asset_widget.set_version(uuid_obj.version())
            asset_widget.set_UUID(asset.get('UUID'))
            asset_widget.set_path(asset.get('path'))
            asset_widget.UUID_label.hide()
            asset_widget.path_label.hide()
            wid2 = QtWidgets.QListWidgetItem()
            asset_widget.setProperty("asset", True)
            wid2.setSizeHint(asset_widget.sizeHint())
            self.asset_listWidget.addItem(wid2)
            self.asset_listWidget.setItemWidget(wid2, asset_widget)
            self.asset_listWidget.setStyleSheet("QListWidget::item {margin-bottom: 4px; background-color: rgb(45,45,45);}")
            wid2.setBackground(QtGui.QColor(45, 45, 45))

    def populate_entities(self):
        try:
            self.poly_lineEdit.clear()
            self.latest_checkBox.setEnabled(True)
            if self.types_tabWidget.currentIndex() == 0:
                self.populate_widget_entities(self.get_asset_entities_by_type())
            if self.types_tabWidget.currentIndex() == 1:
                self.populate_widget_entities(self.get_shot_entities_by_type())
        except AttributeError:
            self.asset_listWidget.clear()
        self.toggle_central_icon()

    def populate_entities_by_polyphemus(self):
        self.assets_type_listWidget.clearSelection()
        self.shot_type_listWidget.clearSelection()
        self.search_lineEdit.clear()
        self.latest_checkBox.setEnabled(False)
        self.populate_widget_entities(self.get_entities_by_polyphemus())
        self.toggle_central_icon()

    def populate_entities_by_search(self):
        self.poly_lineEdit.clear()
        self.tab_changed()
        self.populate_widget_entities(self.get_entities_by_search())
        self.toggle_central_icon()

    def populate_entities_by_search_toggle(self):
        # This method has been made to separate on the same button "latest" the method by search and the method by the type list widget. th if statement does not work on th signals themself. That's why I had to create this callback.
        if not self.search_lineEdit.text() == "":
            self.populate_entities_by_search()

    def clear_search_lineEdit(self):
        if self.assets_type_listWidget.currentRow() != -1 or self.shot_type_listWidget.currentRow() != -1:
            self.search_lineEdit.clear()

    def populate_details(self):
        selected_asset_widget = self.get_selected_asset_widget()
        if selected_asset_widget is not None:
            publish_obj = self.Model.get_publish(selected_asset_widget.UUID_label.text())
            hmtl_detail = "<font size=3 color=orange><strong>Path:</strong></font><br/><font color=cyan>|-></font> {}<br/><font size=3 color=orange><strong>Script:</strong></font><br/><font color=cyan>|-></font> {}".format(publish_obj.get("path"), publish_obj.get("script"))
            self.bottom_textBrowser.setHtml(hmtl_detail)

    def get_type_shot(self):
        selected_type_widget = self.shot_type_listWidget.itemWidget(self.shot_type_listWidget.currentItem())
        if selected_type_widget is not None:
            return selected_type_widget.type_label.text()

    def get_type_assets(self):
        selected_type_widget = self.assets_type_listWidget.itemWidget(self.assets_type_listWidget.currentItem())
        if selected_type_widget is not None:
            return selected_type_widget.type_label.text()

    def get_selected_asset_widget(self):
        selected_asset_widget = self.asset_listWidget.itemWidget(self.asset_listWidget.currentItem())
        if selected_asset_widget is not None:
            return selected_asset_widget

    def populate_shows(self):
        self.show_comboBox.clear()
        shows = self.Model.get_active_shows()
        self.show_comboBox.addItems(shows)
        self.show_comboBox.setCurrentIndex(shows.index(os.getenv('SHOW')))

    def populate_seqs(self):
        self.seq_comboBox.clear()
        seqs = self.Model.get_seqs(self.show_comboBox.currentText())
        self.seq_comboBox.addItems(seqs)
        self.seq_comboBox.setCurrentIndex(seqs.index(os.getenv('SEQ')))

    def populate_shots(self):
        self.shot_comboBox.clear()
        shots = self.Model.get_shots(self.show_comboBox.currentText(), self.seq_comboBox.currentText())
        self.shot_comboBox.addItems(shots)
        if os.getenv('SHOT') in shots:
            self.shot_comboBox.setCurrentIndex(shots.index(os.getenv('SHOT')))

    def tab_changed(self):
        self.asset_listWidget.clear()
        self.assets_type_listWidget.clearSelection()
        self.assets_type_listWidget.setCurrentRow(-1)
        self.shot_type_listWidget.clearSelection()
        self.shot_type_listWidget.setCurrentRow(-1)
        self.bottom_textBrowser.clear()

    def hide_central_icon(self):
        self.cyc_icon_label.hide()
        self.spacer01.changeSize(0, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Ignored)
        self.spacer02.changeSize(0, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Ignored)
        self.asset_listWidget.show()

    def show_central_icon(self):
        self.spacer01.changeSize(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.spacer02.changeSize(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.cyc_icon_label.show()
        self.asset_listWidget.hide()

    def toggle_central_icon(self):
        if self.asset_listWidget.count() == 0:
            self.show_central_icon()
        else:
            self.hide_central_icon()

    def clear_secondary_widgets(self):
        self.Version_detail_listWidget.clear()
        self.search_lineEdit.clear()
        self.poly_lineEdit.clear()
