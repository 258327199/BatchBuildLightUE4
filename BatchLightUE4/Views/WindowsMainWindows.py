# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WindowsMainWindows.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(465, 385)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushToolsBuils = QtWidgets.QPushButton(self.groupBox_2)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("BatchLightUE4/Ressources/gear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushToolsBuils.setIcon(icon)
        self.pushToolsBuils.setIconSize(QtCore.QSize(16, 16))
        self.pushToolsBuils.setObjectName("pushToolsBuils")
        self.horizontalLayout.addWidget(self.pushToolsBuils)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addWidget(self.groupBox_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_3)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("BatchLightUE4/Ressources/book.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.pushToolsCache = QtWidgets.QPushButton(self.groupBox_3)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("BatchLightUE4/Ressources/trashcan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushToolsCache.setIcon(icon2)
        self.pushToolsCache.setObjectName("pushToolsCache")
        self.horizontalLayout_4.addWidget(self.pushToolsCache)
        self.horizontalLayout_3.addWidget(self.groupBox_3)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushLevelsSelect = QtWidgets.QPushButton(self.groupBox)
        self.pushLevelsSelect.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushLevelsSelect.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("BatchLightUE4/Ressources/checklist.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushLevelsSelect.setIcon(icon3)
        self.pushLevelsSelect.setCheckable(False)
        self.pushLevelsSelect.setChecked(False)
        self.pushLevelsSelect.setFlat(False)
        self.pushLevelsSelect.setObjectName("pushLevelsSelect")
        self.horizontalLayout_5.addWidget(self.pushLevelsSelect)
        self.pushLevelsDeselect = QtWidgets.QPushButton(self.groupBox)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("BatchLightUE4/Ressources/circle-slash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushLevelsDeselect.setIcon(icon4)
        self.pushLevelsDeselect.setObjectName("pushLevelsDeselect")
        self.horizontalLayout_5.addWidget(self.pushLevelsDeselect)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.toolLevelsEdit = QtWidgets.QToolButton(self.groupBox)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("BatchLightUE4/Ressources/beaker.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolLevelsEdit.setIcon(icon5)
        self.toolLevelsEdit.setObjectName("toolLevelsEdit")
        self.horizontalLayout_5.addWidget(self.toolLevelsEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.frame_level = QtWidgets.QFrame(self.groupBox)
        self.frame_level.setStyleSheet("background: red")
        self.frame_level.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_level.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_level.setObjectName("frame_level")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_level)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout.addWidget(self.frame_level)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 465, 21))
        self.menubar.setObjectName("menubar")
        self.menu_Fichier = QtWidgets.QMenu(self.menubar)
        self.menu_Fichier.setToolTip("")
        self.menu_Fichier.setObjectName("menu_Fichier")
        self.menuLoad = QtWidgets.QMenu(self.menu_Fichier)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("BatchLightUE4/Ressources/link-external.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuLoad.setIcon(icon6)
        self.menuLoad.setObjectName("menuLoad")
        self.menuSetup = QtWidgets.QMenu(self.menubar)
        self.menuSetup.setObjectName("menuSetup")
        self.menuLog = QtWidgets.QMenu(self.menubar)
        self.menuLog.setObjectName("menuLog")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setAutoFillBackground(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNouveau_Setup = QtWidgets.QAction(MainWindow)
        self.actionNouveau_Setup.setChecked(False)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("BatchLightUE4/Ressources/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNouveau_Setup.setIcon(icon7)
        self.actionNouveau_Setup.setObjectName("actionNouveau_Setup")
        self.actionUpdate = QtWidgets.QAction(MainWindow)
        self.actionUpdate.setObjectName("actionUpdate")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("BatchLightUE4/Ressources/sign-out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon8)
        self.actionExit.setObjectName("actionExit")
        self.actionPaths = QtWidgets.QAction(MainWindow)
        self.actionPaths.setObjectName("actionPaths")
        self.actionNetworks = QtWidgets.QAction(MainWindow)
        self.actionNetworks.setObjectName("actionNetworks")
        self.actionCSV = QtWidgets.QAction(MainWindow)
        self.actionCSV.setObjectName("actionCSV")
        self.actionShow_log_folder = QtWidgets.QAction(MainWindow)
        self.actionShow_log_folder.setObjectName("actionShow_log_folder")
        self.actionClean_Log = QtWidgets.QAction(MainWindow)
        self.actionClean_Log.setObjectName("actionClean_Log")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("BatchLightUE4/Ressources/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon9)
        self.actionAbout.setObjectName("actionAbout")
        self.actionUpdates = QtWidgets.QAction(MainWindow)
        self.actionUpdates.setObjectName("actionUpdates")
        self.actionShortcut = QtWidgets.QAction(MainWindow)
        self.actionShortcut.setObjectName("actionShortcut")
        self.actionOuvrir = QtWidgets.QAction(MainWindow)
        self.actionOuvrir.setObjectName("actionOuvrir")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("BatchLightUE4/Ressources/pencil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_as.setIcon(icon10)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionLast_project = QtWidgets.QAction(MainWindow)
        self.actionLast_project.setObjectName("actionLast_project")
        self.actionProj_blabla = QtWidgets.QAction(MainWindow)
        self.actionProj_blabla.setObjectName("actionProj_blabla")
        self.actionOptions = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("BatchLightUE4/Ressources/tools.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOptions.setIcon(icon11)
        self.actionOptions.setObjectName("actionOptions")
        self.menuLoad.addAction(self.actionLast_project)
        self.menuLoad.addSeparator()
        self.menuLoad.addAction(self.actionProj_blabla)
        self.menu_Fichier.addAction(self.actionNouveau_Setup)
        self.menu_Fichier.addAction(self.actionSave_as)
        self.menu_Fichier.addAction(self.menuLoad.menuAction())
        self.menu_Fichier.addSeparator()
        self.menu_Fichier.addAction(self.actionExit)
        self.menuSetup.addAction(self.actionOptions)
        self.menuSetup.addSeparator()
        self.menuSetup.addAction(self.actionPaths)
        self.menuSetup.addAction(self.actionNetworks)
        self.menuSetup.addAction(self.actionCSV)
        self.menuLog.addAction(self.actionShow_log_folder)
        self.menuLog.addAction(self.actionClean_Log)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionUpdates)
        self.menuHelp.addAction(self.actionShortcut)
        self.menubar.addAction(self.menu_Fichier.menuAction())
        self.menubar.addAction(self.menuSetup.menuAction())
        self.menubar.addAction(self.menuLog.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Build Setup"))
        self.pushToolsBuils.setStatusTip(_translate("MainWindow", "Build all level(s) selected"))
        self.pushToolsBuils.setText(_translate("MainWindow", "Builds Levels"))
        self.checkBox.setText(_translate("MainWindow", "Use all machines"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Another options"))
        self.pushButton.setToolTip(_translate("MainWindow", "Open a folder"))
        self.pushButton.setStatusTip(_translate("MainWindow", "Open log folder, give more info about the build succees or error"))
        self.pushButton.setText(_translate("MainWindow", "Show log folder"))
        self.pushToolsCache.setStatusTip(_translate("MainWindow", "Clean the cache folder (not functionnal)"))
        self.pushToolsCache.setText(_translate("MainWindow", "Clean Cache"))
        self.groupBox.setTitle(_translate("MainWindow", "Levels"))
        self.pushLevelsSelect.setStatusTip(_translate("MainWindow", "Select all levels"))
        self.pushLevelsSelect.setText(_translate("MainWindow", "Select all Levels"))
        self.pushLevelsDeselect.setStatusTip(_translate("MainWindow", "Deselect all levels"))
        self.pushLevelsDeselect.setText(_translate("MainWindow", "Deselect all Levels"))
        self.toolLevelsEdit.setStatusTip(_translate("MainWindow", "Edit your levels choice"))
        self.toolLevelsEdit.setText(_translate("MainWindow", "..."))
        self.menu_Fichier.setTitle(_translate("MainWindow", "&Fichier"))
        self.menuLoad.setTitle(_translate("MainWindow", "Load"))
        self.menuSetup.setTitle(_translate("MainWindow", "Setup"))
        self.menuLog.setTitle(_translate("MainWindow", "Log"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNouveau_Setup.setText(_translate("MainWindow", "New Setup"))
        self.actionNouveau_Setup.setIconText(_translate("MainWindow", "New Setup"))
        self.actionNouveau_Setup.setToolTip(_translate("MainWindow", "New Setup"))
        self.actionNouveau_Setup.setStatusTip(_translate("MainWindow", "Create a news projects"))
        self.actionNouveau_Setup.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionUpdate.setText(_translate("MainWindow", "Update"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("MainWindow", "Close this program"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionPaths.setText(_translate("MainWindow", "Paths"))
        self.actionPaths.setStatusTip(_translate("MainWindow", "Choose all path needed for this software"))
        self.actionNetworks.setText(_translate("MainWindow", "Networks"))
        self.actionNetworks.setStatusTip(_translate("MainWindow", "Find all setup to configure your network"))
        self.actionCSV.setText(_translate("MainWindow", "CSV"))
        self.actionCSV.setStatusTip(_translate("MainWindow", "Choose all setup for your CSV software"))
        self.actionShow_log_folder.setText(_translate("MainWindow", "Show log folder"))
        self.actionShow_log_folder.setStatusTip(_translate("MainWindow", "Open the log folder"))
        self.actionClean_Log.setText(_translate("MainWindow", "Clean Log"))
        self.actionClean_Log.setStatusTip(_translate("MainWindow", "Clean the cache folder, can be resolve build light error"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionAbout.setStatusTip(_translate("MainWindow", "Information and Licence about this software"))
        self.actionUpdates.setText(_translate("MainWindow", "Updates"))
        self.actionUpdates.setStatusTip(_translate("MainWindow", "Check if a news update are avaible"))
        self.actionShortcut.setText(_translate("MainWindow", "Shortcut"))
        self.actionShortcut.setStatusTip(_translate("MainWindow", "Show all shortcut for this software"))
        self.actionOuvrir.setText(_translate("MainWindow", "Open Setup"))
        self.actionOuvrir.setStatusTip(_translate("MainWindow", "Choose the project you want open"))
        self.actionOuvrir.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        self.actionSave_as.setStatusTip(_translate("MainWindow", "Save your project"))
        self.actionLast_project.setText(_translate("MainWindow", "Last project"))
        self.actionLast_project.setStatusTip(_translate("MainWindow", "Load the last project create"))
        self.actionLast_project.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionProj_blabla.setText(_translate("MainWindow", "Proj blabla"))
        self.actionOptions.setText(_translate("MainWindow", "Options"))

