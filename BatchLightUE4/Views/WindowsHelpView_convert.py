# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WindowsHelpView.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Help(object):
    def setupUi(self, Help):
        Help.setObjectName("Help")
        Help.resize(387, 300)
        self.gridLayout = QtWidgets.QGridLayout(Help)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonClose = QtWidgets.QPushButton(Help)
        self.pushButtonClose.setObjectName("pushButtonClose")
        self.gridLayout.addWidget(self.pushButtonClose, 1, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(Help)
        self.tabWidget.setObjectName("tabWidget")
        self.version = QtWidgets.QWidget()
        self.version.setObjectName("version")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.version)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_url_website = QtWidgets.QLabel(self.version)
        self.label_url_website.setOpenExternalLinks(True)
        self.label_url_website.setObjectName("label_url_website")
        self.gridLayout_2.addWidget(self.label_url_website, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.version)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_url_octicons = QtWidgets.QLabel(self.version)
        self.label_url_octicons.setOpenExternalLinks(True)
        self.label_url_octicons.setObjectName("label_url_octicons")
        self.gridLayout_2.addWidget(self.label_url_octicons, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.version)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.version)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.version)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.version)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 1, 0, 1, 2)
        self.line = QtWidgets.QFrame(self.version)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 3, 0, 1, 2)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resources/Icons/issues-closed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.version, icon, "")
        self.shortcut = QtWidgets.QWidget()
        self.shortcut.setObjectName("shortcut")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.shortcut)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.shortcut)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Resources/Icons/pencil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.shortcut, icon1, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Help)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Help)

    def retranslateUi(self, Help):
        _translate = QtCore.QCoreApplication.translate
        Help.setWindowTitle(_translate("Help", "Help and Shorcut"))
        self.pushButtonClose.setText(_translate("Help", "Close"))
        self.label_url_website.setText(_translate("Help", "Github Depot"))
        self.label_4.setText(_translate("Help", "Website :"))
        self.label_url_octicons.setText(_translate("Help", "Github\'s Icons - Octicons"))
        self.label.setText(_translate("Help", "Ressources :"))
        self.label_3.setText(_translate("Help", "Release :"))
        self.lineEdit.setPlaceholderText(_translate("Help", "Number Version"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.version), _translate("Help", "Version"))
        self.label_2.setText(_translate("Help", "All shortcut."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.shortcut), _translate("Help", "Shortcut"))

