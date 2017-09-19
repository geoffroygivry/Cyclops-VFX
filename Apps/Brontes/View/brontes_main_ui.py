# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Brontes_main.ui'
#
# Created: Mon Sep 18 21:50:14 2017
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_brontes_main(object):
    def setupUi(self, brontes_main):
        brontes_main.setObjectName("brontes_main")
        brontes_main.resize(993, 548)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(brontes_main)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.top_vertical_layout = QtWidgets.QVBoxLayout()
        self.top_vertical_layout.setObjectName("top_vertical_layout")
        self.top_horizontal_layout = QtWidgets.QHBoxLayout()
        self.top_horizontal_layout.setObjectName("top_horizontal_layout")
        self.cyc_icon = QtWidgets.QLabel(brontes_main)
        self.cyc_icon.setMaximumSize(QtCore.QSize(150, 16777215))
        self.cyc_icon.setText("")
        self.cyc_icon.setPixmap(QtGui.QPixmap("../../../Core/config/icons/cyc_small.png"))
        self.cyc_icon.setObjectName("cyc_icon")
        self.top_horizontal_layout.addWidget(self.cyc_icon)
        self.show_shot_layout = QtWidgets.QFormLayout()
        self.show_shot_layout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.show_shot_layout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.show_shot_layout.setHorizontalSpacing(10)
        self.show_shot_layout.setObjectName("show_shot_layout")
        self.show_label = QtWidgets.QLabel(brontes_main)
        self.show_label.setObjectName("show_label")
        self.show_shot_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.show_label)
        self.show_comboBox = QtWidgets.QComboBox(brontes_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(60)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.show_comboBox.sizePolicy().hasHeightForWidth())
        self.show_comboBox.setSizePolicy(sizePolicy)
        self.show_comboBox.setMinimumSize(QtCore.QSize(200, 0))
        self.show_comboBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.show_comboBox.setObjectName("show_comboBox")
        self.show_shot_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.show_comboBox)
        self.shot_label = QtWidgets.QLabel(brontes_main)
        self.shot_label.setObjectName("shot_label")
        self.show_shot_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.shot_label)
        self.shot_comboBox = QtWidgets.QComboBox(brontes_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shot_comboBox.sizePolicy().hasHeightForWidth())
        self.shot_comboBox.setSizePolicy(sizePolicy)
        self.shot_comboBox.setMinimumSize(QtCore.QSize(200, 0))
        self.shot_comboBox.setObjectName("shot_comboBox")
        self.show_shot_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.shot_comboBox)
        self.top_horizontal_layout.addLayout(self.show_shot_layout)
        self.vertical_divider = QtWidgets.QFrame(brontes_main)
        self.vertical_divider.setFrameShape(QtWidgets.QFrame.VLine)
        self.vertical_divider.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vertical_divider.setObjectName("vertical_divider")
        self.top_horizontal_layout.addWidget(self.vertical_divider)
        spacerItem = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.top_horizontal_layout.addItem(spacerItem)
        self.search_lineEdit = QtWidgets.QLineEdit(brontes_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_lineEdit.sizePolicy().hasHeightForWidth())
        self.search_lineEdit.setSizePolicy(sizePolicy)
        self.search_lineEdit.setMinimumSize(QtCore.QSize(200, 0))
        self.search_lineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.search_lineEdit.setObjectName("search_lineEdit")
        self.top_horizontal_layout.addWidget(self.search_lineEdit)
        self.search_pushButton = QtWidgets.QPushButton(brontes_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_pushButton.sizePolicy().hasHeightForWidth())
        self.search_pushButton.setSizePolicy(sizePolicy)
        self.search_pushButton.setObjectName("search_pushButton")
        self.top_horizontal_layout.addWidget(self.search_pushButton)
        self.top_vertical_layout.addLayout(self.top_horizontal_layout)
        self.verticalLayout_2.addLayout(self.top_vertical_layout)
        self.divider_top = QtWidgets.QFrame(brontes_main)
        self.divider_top.setFrameShape(QtWidgets.QFrame.HLine)
        self.divider_top.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.divider_top.setObjectName("divider_top")
        self.verticalLayout_2.addWidget(self.divider_top)
        self.mid_horizontal_layout = QtWidgets.QHBoxLayout()
        self.mid_horizontal_layout.setObjectName("mid_horizontal_layout")
        self.poly_label = QtWidgets.QLabel(brontes_main)
        self.poly_label.setObjectName("poly_label")
        self.mid_horizontal_layout.addWidget(self.poly_label)
        self.poly_lineEdit = QtWidgets.QLineEdit(brontes_main)
        self.poly_lineEdit.setMaximumSize(QtCore.QSize(16777215, 20))
        self.poly_lineEdit.setSizeIncrement(QtCore.QSize(0, 35))
        self.poly_lineEdit.setBaseSize(QtCore.QSize(0, 12))
        self.poly_lineEdit.setObjectName("poly_lineEdit")
        self.mid_horizontal_layout.addWidget(self.poly_lineEdit)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.mid_horizontal_layout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.mid_horizontal_layout)
        self.divider = QtWidgets.QFrame(brontes_main)
        self.divider.setFrameShape(QtWidgets.QFrame.HLine)
        self.divider.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.divider.setObjectName("divider")
        self.verticalLayout_2.addWidget(self.divider)
        self.bottom_verticalLayout = QtWidgets.QVBoxLayout()
        self.bottom_verticalLayout.setObjectName("bottom_verticalLayout")
        self.bottom_horizontalLayout = QtWidgets.QHBoxLayout()
        self.bottom_horizontalLayout.setObjectName("bottom_horizontalLayout")
        self.types_listView = QtWidgets.QListView(brontes_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.types_listView.sizePolicy().hasHeightForWidth())
        self.types_listView.setSizePolicy(sizePolicy)
        self.types_listView.setMaximumSize(QtCore.QSize(120, 16777215))
        self.types_listView.setSizeIncrement(QtCore.QSize(10, 0))
        self.types_listView.setBaseSize(QtCore.QSize(10, 0))
        self.types_listView.setObjectName("types_listView")
        self.bottom_horizontalLayout.addWidget(self.types_listView)
        self.central_asset_tableView = QtWidgets.QTableView(brontes_main)
        self.central_asset_tableView.setSizeIncrement(QtCore.QSize(0, 0))
        self.central_asset_tableView.setBaseSize(QtCore.QSize(100, 0))
        self.central_asset_tableView.setObjectName("central_asset_tableView")
        self.bottom_horizontalLayout.addWidget(self.central_asset_tableView)
        self.comments_listView = QtWidgets.QListView(brontes_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comments_listView.sizePolicy().hasHeightForWidth())
        self.comments_listView.setSizePolicy(sizePolicy)
        self.comments_listView.setMinimumSize(QtCore.QSize(10, 0))
        self.comments_listView.setMaximumSize(QtCore.QSize(200, 16777215))
        self.comments_listView.setObjectName("comments_listView")
        self.bottom_horizontalLayout.addWidget(self.comments_listView)
        self.bottom_verticalLayout.addLayout(self.bottom_horizontalLayout)
        self.verticalLayout_2.addLayout(self.bottom_verticalLayout)

        self.retranslateUi(brontes_main)
        QtCore.QMetaObject.connectSlotsByName(brontes_main)

    def retranslateUi(self, brontes_main):
        brontes_main.setWindowTitle(QtWidgets.QApplication.translate("brontes_main", "Form", None, -1))
        self.show_label.setText(QtWidgets.QApplication.translate("brontes_main", "Show", None, -1))
        self.shot_label.setText(QtWidgets.QApplication.translate("brontes_main", "Shot", None, -1))
        self.search_pushButton.setText(QtWidgets.QApplication.translate("brontes_main", "search", None, -1))
        self.poly_label.setText(QtWidgets.QApplication.translate("brontes_main", "Polyphemus ", None, -1))

