# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rocket_GUI_PyQt-final.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QSplashScreen, QLabel
from PyQt5.QtCore import QTimer, Qt
from rocket_dictionary import rocketDictionary
from collections import OrderedDict

ascending_alphabetical_rocket_choices = sorted(rocketDictionary.keys())
descending_alphabetical_rocket_choices = sorted(rocketDictionary.keys(), reverse=True)
# ascending_country_rocket_choices = OrderedDict(sorted(rocketDictionary.items(), key=lambda i: i[1]['Country']))
# descending_country_rocket_choices = OrderedDict(sorted(rocketDictionary.items(), key=lambda i: i[1]['Country'], reverse=True)) #reverse
# ascending_height_rocket_choices = OrderedDict(sorted(rocketDictionary.items(), key=lambda i: i[1]['height_int']))
# descending_height_rocket_choices = OrderedDict(sorted(rocketDictionary.items(), key=lambda i: i[1]['height_int'], reverse=True)) #reverse
# ascending_mass_rocket_choices = OrderedDict(sorted(rocketDictionary.items(), key=lambda i: i[1]['mass_int']))
# descending_mass_rocket_choices = OrderedDict(sorted(rocketDictionary.items(), key=lambda i: i[1]['mass_int'], reverse=True)) #reverse
# ascending_diameter_rocket_choices = OrderedDict(sorted(rocketDictionary.items(), key=lambda i: i[1]['diameter_int']))
# descending_diameter_rocket_choices = OrderedDict(sorted(rocketDictionary.items(), key=lambda i: i[1]['diameter_int'], reverse=True)) #reverse
# ascending_payload_rocket_choices = OrderedDict(sorted(rocketDictionary.items(), key=lambda i: i[1]['payload_int']))
# descending_payload_rocket_choices = OrderedDict(sorted(rocketDictionary.items(), key=lambda i: i[1]['payload_int'], reverse=True)) #reverse
# ascending_cost_rocket_choices = OrderedDict(sorted(rocketDictionary.items(), key=lambda i: i[1]['cost_int']))
# descending_cost_rocket_choices = OrderedDict(sorted(rocketDictionary.items(), key=lambda i: i[1]['cost_int'], reverse=True)) #reverse
# ascending_thrust_rocket_choices = OrderedDict(sorted(rocketDictionary.items(), key=lambda i: i[1]['initial_thrust_int']))
# descending_thrust_rocket_choices = OrderedDict(sorted(rocketDictionary.items(), key=lambda i: i[1]['initial_thrust_int'], reverse=True)) #reverse
# ascending_asl_isp_rocket_choices = OrderedDict(sorted(rocketDictionary.items(), key=lambda i: i[1]['asl_isp_int']))
# descending_asl_isp_rocket_choices = OrderedDict(sorted(rocketDictionary.items(), key=lambda i: i[1]['asl_isp_int'], reverse=True)) #reverse
# ascending_vac_isp_rocket_choices = OrderedDict(sorted(rocketDictionary.items(), key=lambda i: i[1]['vac_isp_int']))
# descending_vac_isp_rocket_choices = OrderedDict(sorted(rocketDictionary.items(), key=lambda i: i[1]['vac_isp_int'], reverse=True)) #reverse

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setStyleSheet("QToolTip {background-color: black; color: white; border: black solid 1px}")
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon('rocket_icon_512.ico')) 
        MainWindow.resize(1600, 900)
        MainWindow.setStyleSheet("background-color: rgb(52, 52, 52);\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.522, y1:1, x2:0.528, y2:0, stop:0 rgba(34, 34, 34, 255), stop:1 rgba(54, 54, 54, 255));\n"
"\n"
"")
        #MainWindow.setStyleSheet("QToolTip{background-color : blue ; color: k ; font: 12pt}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.columnViewFrame = QtWidgets.QFrame(self.centralwidget)
        self.columnViewFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.columnViewFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.columnViewFrame.setObjectName("columnViewFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.columnViewFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rocketClusterFrame = QtWidgets.QFrame(self.columnViewFrame)
        self.rocketClusterFrame.setMaximumSize(QtCore.QSize(280, 16777215))
        self.rocketClusterFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rocketClusterFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rocketClusterFrame.setObjectName("rocketClusterFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.rocketClusterFrame)
        self.verticalLayout.setContentsMargins(20, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rocketHeaderLabel = QtWidgets.QLabel(self.rocketClusterFrame)
        self.rocketHeaderLabel.setMaximumSize(QtCore.QSize(260, 50))
        self.rocketHeaderLabel.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.rocketHeaderLabel.setObjectName("rocketHeaderLabel")
        self.verticalLayout.addWidget(self.rocketHeaderLabel)
        self.searchBarFrame = QtWidgets.QFrame(self.rocketClusterFrame)
        self.searchBarFrame.setMaximumSize(QtCore.QSize(260, 16777215))
        self.searchBarFrame.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.searchBarFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.searchBarFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.searchBarFrame.setObjectName("searchBarFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.searchBarFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.searchHeaderLabel = QtWidgets.QLabel(self.searchBarFrame)
        self.searchHeaderLabel.setMaximumSize(QtCore.QSize(80, 60))
        self.searchHeaderLabel.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.searchHeaderLabel.setObjectName("searchHeaderLabel")
        self.horizontalLayout_2.addWidget(self.searchHeaderLabel)
        self.searchBox = QtWidgets.QLineEdit(self.searchBarFrame)
        self.searchBox.setMinimumSize(QtCore.QSize(0, 10))
        self.searchBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.searchBox.setStyleSheet("background-color: rgb(70, 70, 70);\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(66, 229, 243);")
        self.searchBox.setObjectName("searchBox")
        self.horizontalLayout_2.addWidget(self.searchBox)
        self.verticalLayout.addWidget(self.searchBarFrame)
        self.listWidget = QtWidgets.QListWidget(self.rocketClusterFrame)
        self.listWidget.setMaximumSize(QtCore.QSize(260, 16777215))
        self.listWidget.setMouseTracking(True)
        self.listWidget.setUpdatesEnabled(True)
        self.listWidget.setStyleSheet("color: rgb(255, 255, 255);\n"
"selection-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(6, 236, 248);\n"
"background-color: rgb(52, 52, 52);")
        self.listWidget.setObjectName("listWidget")
        
        for rocket in ascending_alphabetical_rocket_choices:
            #item = QtWidgets.QListWidgetItem()
            self.listWidget.addItem(rocket)

        self.listWidget.itemSelectionChanged.connect(self.selectionChanged)
        
        # item = QtWidgets.QListWidgetItem()
        # self.listWidget.addItem(item)
        # item = QtWidgets.QListWidgetItem()
        # self.listWidget.addItem(item)
        
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout.addWidget(self.rocketClusterFrame)
        self.infoPaneFrame = QtWidgets.QFrame(self.columnViewFrame)
        self.infoPaneFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.infoPaneFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.infoPaneFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.infoPaneFrame.setObjectName("infoPaneFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.infoPaneFrame)
        self.verticalLayout_2.setContentsMargins(30, -1, 30, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.informationHeaderLabel = QtWidgets.QLabel(self.infoPaneFrame)
        self.informationHeaderLabel.setMaximumSize(QtCore.QSize(16777215, 50))
        self.informationHeaderLabel.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.informationHeaderLabel.setObjectName("informationHeaderLabel")
        self.verticalLayout_2.addWidget(self.informationHeaderLabel)
        self.textBrowser = QtWidgets.QTextBrowser(self.infoPaneFrame)
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textBrowser.setMouseTracking(True)
        self.textBrowser.setStyleSheet("selection-background-color: rgb(33, 237, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"selection-color: rgb(0, 0, 0);\n"
"background-color: rgb(52, 52, 52);")
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textBrowser.setLineWrapColumnOrWidth(0)
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.horizontalLayout.addWidget(self.infoPaneFrame)
        self.frame = QtWidgets.QFrame(self.columnViewFrame)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.imageHeaderLabel = QtWidgets.QLabel(self.frame)
        self.imageHeaderLabel.setMaximumSize(QtCore.QSize(580, 50))
        self.imageHeaderLabel.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.imageHeaderLabel.setObjectName("imageHeaderLabel")
        self.verticalLayout_3.addWidget(self.imageHeaderLabel)
        self.graphicsView = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView.setMaximumSize(QtCore.QSize(580, 16777215))
        self.graphicsView.setStyleSheet("background-color: rgb(52, 52, 52), background-image: url("")")
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_3.addWidget(self.graphicsView)
        self.horizontalLayout.addWidget(self.frame)
        self.gridLayout.addWidget(self.columnViewFrame, 2, 0, 4, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        
        
  # ***** Menu Bar Item Creation and Naming ******      
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1593, 21))
        self.menubar.setObjectName("menubar")
        self.menuShow = QtWidgets.QMenu(self.menubar)
        self.menuShow.setObjectName("menuShow")
        self.menuSort = QtWidgets.QMenu(self.menubar)
        self.menuSort.setObjectName("menuSort")
        self.menuMass = QtWidgets.QMenu(self.menuSort)
        self.menuMass.setObjectName("menuMass")
        self.menuDiameter = QtWidgets.QMenu(self.menuSort)
        self.menuDiameter.setObjectName("menuDiameter")
        self.menuHeight = QtWidgets.QMenu(self.menuSort)
        self.menuHeight.setObjectName("menuHeight")
        self.menuCost_Per_Launch = QtWidgets.QMenu(self.menuSort)
        self.menuCost_Per_Launch.setObjectName("menuCost_Per_Launch")
        self.menuThrust = QtWidgets.QMenu(self.menuSort)
        self.menuThrust.setObjectName("menuThrust")
        self.menuPayload_to_LEO = QtWidgets.QMenu(self.menuSort)
        self.menuPayload_to_LEO.setObjectName("menuPayload_to_LEO")
        self.menuAlphabetical = QtWidgets.QMenu(self.menuSort)
        self.menuAlphabetical.setObjectName("menuAlphabetical")
        self.menuISP = QtWidgets.QMenu(self.menuSort)
        self.menuISP.setObjectName("menuISP")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setToolTip("Toolbar")
        self.toolBar.setStyleSheet("background-color: rgb(60, 60, 60);")
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QtCore.QSize(32,32))
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionIndividual_Rockets = QtWidgets.QAction(MainWindow)
        self.actionIndividual_Rockets.setObjectName("actionIndividual_Rockets")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionVersion = QtWidgets.QAction(MainWindow)
        self.actionVersion.setObjectName("actionVersion")
        self.actionAcronyms = QtWidgets.QAction(MainWindow)
        self.actionAcronyms.setObjectName("actionAcronyms")
        self.actionLicensing = QtWidgets.QAction(MainWindow)
        self.actionLicensing.setObjectName("actionLicensing")
        self.actionLow_to_High = QtWidgets.QAction(MainWindow)
        self.actionLow_to_High.setObjectName("actionLow_to_High")
        self.actionLow_to_High_2 = QtWidgets.QAction(MainWindow)
        self.actionLow_to_High_2.setObjectName("actionLow_to_High_2")
        self.actionLow_to_High_3 = QtWidgets.QAction(MainWindow)
        self.actionLow_to_High_3.setObjectName("actionLow_to_High_3")
        self.actionHigh_to_Low = QtWidgets.QAction(MainWindow)
        self.actionHigh_to_Low.setObjectName("actionHigh_to_Low")
        self.actionLow_to_High_4 = QtWidgets.QAction(MainWindow)
        self.actionLow_to_High_4.setObjectName("actionLow_to_High_4")
        self.actionHigh_to_Low_2 = QtWidgets.QAction(MainWindow)
        self.actionHigh_to_Low_2.setObjectName("actionHigh_to_Low_2")
        self.actionLow_to_High_5 = QtWidgets.QAction(MainWindow)
        self.actionLow_to_High_5.setObjectName("actionLow_to_High_5")
        self.actionHigh_to_Low_3 = QtWidgets.QAction(MainWindow)
        self.actionHigh_to_Low_3.setObjectName("actionHigh_to_Low_3")
        self.actionLow_to_High_6 = QtWidgets.QAction(MainWindow)
        self.actionLow_to_High_6.setObjectName("actionLow_to_High_6")
        self.actionAscending = QtWidgets.QAction(MainWindow)
        self.actionAscending.setObjectName("actionAscending")
        self.actionDescending = QtWidgets.QAction(MainWindow)
        self.actionDescending.setObjectName("actionDescending")
        self.actionHigh_to_Low_4 = QtWidgets.QAction(MainWindow)
        self.actionHigh_to_Low_4.setObjectName("actionHigh_to_Low_4")
        self.actionHigh_to_Low_5 = QtWidgets.QAction(MainWindow)
        self.actionHigh_to_Low_5.setObjectName("actionHigh_to_Low_5")
        self.actionHigh_to_Low_6 = QtWidgets.QAction(MainWindow)
        self.actionHigh_to_Low_6.setObjectName("actionHigh_to_Low_6")
        self.actionLow_to_High_7 = QtWidgets.QAction(MainWindow)
        self.actionLow_to_High_7.setObjectName("actionLow_to_High_7")
        self.actionHigh_to_Low_7 = QtWidgets.QAction(MainWindow)
        self.actionHigh_to_Low_7.setObjectName("actionHigh_to_Low_7")
        self.actionRocket_Families = QtWidgets.QAction(MainWindow)
        self.actionRocket_Families.setObjectName("actionRocket_Families")
        self.actionticke = QtWidgets.QAction(MainWindow)
        self.actionticke.setObjectName("actionticke")
        self.actiontouch = QtWidgets.QAction(MainWindow)
        self.actiontouch.setObjectName("actiontouch")
        self.actionstrongly = QtWidgets.QAction(MainWindow)
        self.actionstrongly.setObjectName("actionstrongly")
        self.actionmildly = QtWidgets.QAction(MainWindow)
        self.actionmildly.setObjectName("actionmildly")
        
        
        
 # ****** Tool Bar Item Creation and Naming ******        
        self.actionCompare = QtWidgets.QAction(MainWindow)  #add QIcon("printer.png") into this part after insantiating it
        self.actionCompare.setObjectName("actionCompare")   # to set window icon = self.setWindowIcon(QtGui.QIcon("rocket_icon_512.ico"))
        self.actionPrint = QtWidgets.QAction(MainWindow)  
        self.actionPrint.setObjectName("actionPrint")
        
        
 # ***** Menu Bar Action Linking *****        
        self.actionCountry = QtWidgets.QAction(MainWindow)
        self.actionCountry.setObjectName("actionCountry")
        self.actionAgency = QtWidgets.QAction(MainWindow)
        self.actionAgency.setObjectName("actionAgency")
        self.menuShow.addAction(self.actionIndividual_Rockets)
        self.menuShow.addAction(self.actionRocket_Families)
        self.menuMass.addAction(self.actionLow_to_High)
        self.menuMass.addAction(self.actionHigh_to_Low_4)
        self.menuDiameter.addAction(self.actionLow_to_High_2)
        self.menuDiameter.addAction(self.actionHigh_to_Low_5)
        self.menuHeight.addAction(self.actionLow_to_High_3)
        self.menuHeight.addAction(self.actionHigh_to_Low)
        self.menuCost_Per_Launch.addAction(self.actionLow_to_High_4)
        self.menuCost_Per_Launch.addAction(self.actionHigh_to_Low_2)
        self.menuThrust.addAction(self.actionLow_to_High_5)
        self.menuThrust.addAction(self.actionHigh_to_Low_3)
        self.menuPayload_to_LEO.addAction(self.actionLow_to_High_6)
        self.menuPayload_to_LEO.addAction(self.actionHigh_to_Low_6)
        self.menuAlphabetical.addAction(self.actionAscending)
        self.menuAlphabetical.addAction(self.actionDescending)
        self.menuISP.addAction(self.actionLow_to_High_7)
        self.menuISP.addAction(self.actionHigh_to_Low_7)
        self.menuSort.addAction(self.menuAlphabetical.menuAction())
        self.menuSort.addAction(self.menuPayload_to_LEO.menuAction())
        self.menuSort.addAction(self.menuMass.menuAction())
        self.menuSort.addAction(self.menuDiameter.menuAction())
        self.menuSort.addAction(self.menuHeight.menuAction())
        self.menuSort.addAction(self.menuCost_Per_Launch.menuAction())
        self.menuSort.addAction(self.menuThrust.menuAction())
        self.menuSort.addAction(self.menuISP.menuAction())
        self.menuSort.addAction(self.actionCountry)
        self.menuSort.addAction(self.actionAgency)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionVersion)
        self.menuHelp.addAction(self.actionAcronyms)
        self.menuHelp.addAction(self.actionLicensing)
        self.menubar.addAction(self.menuShow.menuAction())
        self.menubar.addAction(self.menuSort.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionCompare)
        self.toolBar.addAction(self.actionPrint)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Working Title: SRP 0.3"))
        MainWindow.setToolTip(_translate("MainWindow", "<html><head/><body><p style=\"color : black\">SRP 0.3</p></body></html>"))
        self.rocketHeaderLabel.setToolTip(_translate("MainWindow", "<html><head/><body><p style=\"color : black\">Rockets!!!!</p></body></html>"))
        self.rocketHeaderLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">Rockets</span></p></body></html>"))
        self.searchHeaderLabel.setToolTip(_translate("MainWindow", "<html><head/><body><p style=\"color : black\">Enter text in the bar to the right to search for a specific rocket</p></body></html>"))
        self.searchHeaderLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Search</span></p></body></html>"))
        self.searchBox.setStatusTip(_translate("MainWindow", "Enter text to search for rocket by name"))
        self.listWidget.setToolTip(_translate("MainWindow", "<html><head/><body><p style=\"color : black\">List of rockets</p></body></html>"))
        self.listWidget.setStatusTip(_translate("MainWindow", "Rocket List"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        j = 0

        for rocket in ascending_alphabetical_rocket_choices:
            item = self.listWidget.item(j)
            item.setText(_translate("MainWindow", rocket))
            j = j + 1

        # item = self.listWidget.item(0)
        # item.setText(_translate("MainWindow", "poop"))
        # item = self.listWidget.item(1)
        # item.setText(_translate("MainWindow", "poop1"))
        
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.searchBox.setToolTip(_translate("searchBarFrame", "<html><head/><body><p style=\"color : black\">Enter search term here</p></body></html>"))
        self.informationHeaderLabel.setToolTip(_translate("MainWindow", "<html><head/><body><p style=\"color : black\">Information</p></body></html>"))
        self.informationHeaderLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">Information</span></p></body></html>"))
        self.textBrowser.setToolTip(_translate("MainWindow", "<html><head/><body><p style=\"color : black\">Various information about selected rocket</p></body></html>"))
        self.textBrowser.setStatusTip(_translate("MainWindow", "Information on selected rocket"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.imageHeaderLabel.setToolTip(_translate("MainWindow", "<html><head/><body><p style=\"color : black\">Image</p></body></html>"))
        self.imageHeaderLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">Image</span></p></body></html>"))
        self.graphicsView.setToolTip(_translate("MainWindow", "<html><head/><body><p style=\"color : black\">Image of selected rocket</p></body></html>"))
        self.graphicsView.setStatusTip(_translate("MainWindow", "Image of selected rocket"))
       
       
   # ***** Placing and naming Menu Bar Items ******    
        self.menuShow.setTitle(_translate("MainWindow", "Show"))
        self.menuSort.setTitle(_translate("MainWindow", "Sort"))
        self.menuMass.setStatusTip(_translate("MainWindow", "Sort Rockets by their mass on the launchpad"))
        self.menuMass.setTitle(_translate("MainWindow", "Mass"))
        self.menuDiameter.setStatusTip(_translate("MainWindow", "Sort rockets by their diameter"))
        self.menuDiameter.setTitle(_translate("MainWindow", "Diameter"))
        self.menuHeight.setStatusTip(_translate("MainWindow", "Sort rockets by their height"))
        self.menuHeight.setTitle(_translate("MainWindow", "Height"))
        self.menuCost_Per_Launch.setStatusTip(_translate("MainWindow", "Sort rockets by how much it costs to launch them in USD"))
        self.menuCost_Per_Launch.setTitle(_translate("MainWindow", "Cost Per Launch"))
        self.menuThrust.setStatusTip(_translate("MainWindow", "Sort rockets by how much thrust they output"))
        self.menuThrust.setTitle(_translate("MainWindow", "Thrust"))
        self.menuPayload_to_LEO.setStatusTip(_translate("MainWindow", "Sort rockets by payload capacity to Low Earth Orbit"))
        self.menuPayload_to_LEO.setTitle(_translate("MainWindow", "Payload to LEO"))
        self.menuAlphabetical.setStatusTip(_translate("MainWindow", "Sort rockets alphabetically"))
        self.menuAlphabetical.setTitle(_translate("MainWindow", "Alphabetical"))
        self.menuISP.setStatusTip(_translate("MainWindow", "Sort rockets by their Specific Impulse"))
        self.menuISP.setTitle(_translate("MainWindow", "ISP"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionIndividual_Rockets.setText(_translate("MainWindow", "Individual Rockets"))
        self.actionIndividual_Rockets.setStatusTip(_translate("MainWindow", "Show all rockets"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setStatusTip(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setStatusTip(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionAbout.setStatusTip(_translate("MainWindow", "View information about this program"))
        self.actionVersion.setText(_translate("MainWindow", "Version"))
        self.actionVersion.setStatusTip(_translate("MainWindow", "Display version information"))
        self.actionAcronyms.setText(_translate("MainWindow", "Acronyms"))
        self.actionAcronyms.setStatusTip(_translate("MainWindow", "A list of acronyms used in this program and what they stand for"))
        self.actionLicensing.setText(_translate("MainWindow", "Licensing"))
        self.actionLicensing.setStatusTip(_translate("MainWindow", "Information about the license and attributing"))
        self.actionLow_to_High.setText(_translate("MainWindow", "Low to High"))
        self.actionLow_to_High.setStatusTip(_translate("MainWindow", "Sort rockets by their mass on the launchpad from lightest to heaviest"))
        self.actionLow_to_High_2.setText(_translate("MainWindow", "Low to High"))
        self.actionLow_to_High_2.setStatusTip(_translate("MainWindow", "Sort rockets by their diameter from narrowest to widest"))
        self.actionLow_to_High_3.setText(_translate("MainWindow", "Low to High"))
        self.actionLow_to_High_3.setStatusTip(_translate("MainWindow", "Sort rockets by their height from shortest to tallest"))
        self.actionHigh_to_Low.setText(_translate("MainWindow", "High to Low"))
        self.actionHigh_to_Low.setStatusTip(_translate("MainWindow", "Sort rockets by their height from tallest to shortest"))
        self.actionLow_to_High_4.setText(_translate("MainWindow", "Low to High"))
        self.actionLow_to_High_4.setStatusTip(_translate("MainWindow", "Sort rockets by their cost to launch from least expensive to most expensive"))
        self.actionHigh_to_Low_2.setText(_translate("MainWindow", "High to Low"))
        self.actionHigh_to_Low_2.setStatusTip(_translate("MainWindow", "Sort rockets by their cost to launch from most expensive to least expensive"))
        self.actionLow_to_High_5.setText(_translate("MainWindow", "Low to High"))
        self.actionLow_to_High_5.setStatusTip(_translate("MainWindow", "Sort rockets by their thrust in kilonewtons from least to most"))
        self.actionHigh_to_Low_3.setText(_translate("MainWindow", "High to Low"))
        self.actionHigh_to_Low_3.setStatusTip(_translate("MainWindow", "Sort rockets by their thrust in kilonewtons from highest to lowest"))
        self.actionLow_to_High_6.setText(_translate("MainWindow", "Low to High"))
        self.actionLow_to_High_6.setStatusTip(_translate("MainWindow", "Sort rockets by their lifting capacity to Low Earth Orbit from lowest to highest"))
        self.actionAscending.setText(_translate("MainWindow", "Ascending"))
        self.actionAscending.setStatusTip(_translate("MainWindow", "Sort rockets in ascending order (A to Z)"))
        self.actionDescending.setText(_translate("MainWindow", "Descending"))
        self.actionDescending.setStatusTip(_translate("MainWindow", "Sort rockets in descending order(Z to A)"))
        self.actionHigh_to_Low_4.setText(_translate("MainWindow", "High to Low"))
        self.actionHigh_to_Low_4.setStatusTip(_translate("MainWindow", "Sort rockets by their mass on the launchpad from heaviest to lightest"))
        self.actionHigh_to_Low_5.setText(_translate("MainWindow", "High to Low"))
        self.actionHigh_to_Low_5.setStatusTip(_translate("MainWindow", "Sort rockets by their diameter from widest to narrowest"))
        self.actionHigh_to_Low_6.setText(_translate("MainWindow", "High to Low"))
        self.actionHigh_to_Low_6.setStatusTip(_translate("MainWindow", "Sort rockets by their lifting capacity to Low Earth Orbit from highest to lowest"))
        self.actionLow_to_High_7.setText(_translate("MainWindow", "Low to High"))
        self.actionLow_to_High_7.setStatusTip(_translate("MainWindow", "Sort rockets by their specific impulse from least to most"))
        self.actionHigh_to_Low_7.setText(_translate("MainWindow", "High to Low"))
        self.actionHigh_to_Low_7.setStatusTip(_translate("MainWindow", "Sort rockets by their specific impulse from most to least"))
        self.actionRocket_Families.setText(_translate("MainWindow", "Rocket Families"))
        self.actionRocket_Families.setStatusTip(_translate("MainWindow", "Show rocket families"))
        self.actionCountry.setText(_translate("MainWindow", "Country"))
        self.actionCountry.setStatusTip(_translate("MainWindow", "Sort rockets by the countries that produced them, alphabetically"))
        self.actionAgency.setText(_translate("MainWindow", "Agency"))
        self.actionAgency.setStatusTip(_translate("MainWindow", "Sort rockets by the agencies that utilize them, alphabetically"))
        self.actionticke.setText(_translate("MainWindow", "ticke"))
        self.actiontouch.setText(_translate("MainWindow", "touch"))
        self.actionstrongly.setText(_translate("MainWindow", "strongly"))
        self.actionmildly.setText(_translate("MainWindow", "mildly"))


     # ***** Placing, Naming, Setting Tool and Status tips for Toolbar Items ******   
        self.actionCompare.setText(_translate("MainWindow", "Compare"))
        self.actionCompare.setToolTip(_translate("MainWindow", "<html><head/><body><p style=\"color : black\">Compare two rockets</p></body></html>"))
        self.actionCompare.setStatusTip(_translate("MainWindow", "Compare two rockets"))
        self.actionCompare.setShortcut(_translate("MainWindow", "Alt+C"))
        self.actionPrint.setText(_translate("MainWindow", "Print"))
        self.actionCompare.setIcon(QtGui.QIcon("compare.png"))
        self.actionPrint.setToolTip(_translate("MainWindow", "<html><head/><body><p style=\"color : black\">Generates a layout for printing</p></body></html>"))
        self.actionPrint.setStatusTip(_translate("MainWindow", "Generates a layout for printing"))
        self.actionPrint.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionPrint.setIcon(QtGui.QIcon("printer.png"))

        
#     def flashSplash(self):
#         self.splash = QSplashScreen(QPixmap('splash.jpg'))

#         # By default, SplashScreen will be in the center of the screen.
#         # You can move it to a specific location if you want:
#         # self.splash.move(10,10)

#         self.splash.show()

#         # Close SplashScreen after 2 seconds (2000 ms)
#         QTimer.singleShot(2500, self.splash.close)

# ***** Define what happens when a rocket is selected from listWidget ******
    def selectionChanged(self):
        _translate = QtCore.QCoreApplication.translate
        rocketName = self.listWidget.currentItem().text()
        rocketImage = "/Users/seralyncampbell/DevOps/rocket_info/images/" + rocketDictionary[rocketName]['Image']
        self.graphicsView.setStyleSheet(f"background-color: rgb(52, 52, 52); background-image: url({rocketImage}); background-repeat: no-repeat;")
        manufacturer = rocketDictionary[rocketName]['Manufacturer'].replace('\n', '<br />').replace('\n\n', '<br /><br />')
        height = rocketDictionary[rocketName]['Height'].replace('\n', '<br />')
        #height_string = rocketDictionary[rocketName]['HeightString'].replace('\n', '<br />')    #add this and also add {height_string} in html line below, but also make height above this a str(rocketDic....)
        diameter = rocketDictionary[rocketName]['Diameter'].replace('\n', '<br />')
        mass = rocketDictionary[rocketName]['Mass'].replace('\n', '<br />')
        operationalStatus = rocketDictionary[rocketName]['Operational Status'].replace('\n', '<br />').replace('\n\n', '<br /><br />').replace('        ', '')
        burnTime = rocketDictionary[rocketName]['Burn Time'].replace('\n', '<br />')
        thrust = rocketDictionary[rocketName]['Thrust'].replace('\n', '<br />')
        isp = rocketDictionary[rocketName]['Years in Operation'].replace('\n', '<br />')
        fuelType = rocketDictionary[rocketName]['Fuel Type'].replace('\n', '<br />').replace('H2','H<sub>2</sub>').replace('N2','N<sub>2</sub>').replace('O4','O<sub>4</sub>')
        costPerLaunch = rocketDictionary[rocketName]['Cost Per Launch'].replace('\n', '<br />')
        yearsInOperation = rocketDictionary[rocketName]['Years in Operation'].replace('\n', '<br />').replace('        ', '')
        additionalInformation = rocketDictionary[rocketName]['Additional Information'].replace('\n\n', '<br /><br />').replace('            ', '')
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
f"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">{rocketName}</span></p>\n"
f"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial, sans-serif\'; font-size:12pt; color:#ffffff; background-color:transparent;\"><b>Agency:</b> {rocketDictionary[rocketName]['Agency']}</span></p>\n"
f"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial, sans-serif\'; font-size:12pt; color:#ffffff; background-color:transparent;\"><b>Manufacturer:</b> {manufacturer}</span></p>\n"
f"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial, sans-serif\'; font-size:12pt; color:#ffffff; background-color:transparent;\"><b>Payload Capacity to LEO:</b> {rocketDictionary[rocketName]['Payload Capacity to LEO']}</span></p>\n"
f"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial, sans-serif\'; font-size:12pt; color:#ffffff; background-color:transparent;\"><b>Height:</b> {height}</span></p>\n"
f"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial, sans-serif\'; font-size:12pt; color:#ffffff; background-color:transparent;\"><b>Diameter:</b> {diameter}</span></p>\n"
f"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial, sans-serif\'; font-size:12pt; color:#ffffff; background-color:transparent;\"><b>Mass:</b> {mass}</span></p>\n"
f"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial, sans-serif\'; font-size:12pt; color:#ffffff; background-color:transparent;\"><b>Years in Operation:</b> {yearsInOperation}</span></p>\n"
f"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial, sans-serif\'; font-size:12pt; color:#ffffff; background-color:transparent;\"><b>Country:</b> {rocketDictionary[rocketName]['Country']}</span></p>\n"
f"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial, sans-serif\'; font-size:12pt; color:#ffffff; background-color:transparent;\"><b>Operational Status:</b> {operationalStatus}</span></p>\n"
f"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial, sans-serif\'; font-size:12pt; color:#ffffff; background-color:transparent;\"><b>Number of Stages:</b> {rocketDictionary[rocketName]['Number of Stages']}</span></p>\n"
f"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial, sans-serif\'; font-size:12pt; color:#ffffff; background-color:transparent;\"><b>Burn Time:</b> {burnTime}</span></p>\n"
f"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial, sans-serif\'; font-size:12pt; color:#ffffff; background-color:transparent;\"><b>Thrust:</b> {thrust}</span></p>\n"
f"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial, sans-serif\'; font-size:12pt; color:#ffffff; background-color:transparent;\"><b>ISP:</b> {isp}</span></p>\n"
f"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial, sans-serif\'; font-size:12pt; color:#ffffff; background-color:transparent;\"><b>Cost Per Launch:</b> {costPerLaunch}</span></p>\n"
f"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial, sans-serif\'; font-size:12pt; color:#ffffff; background-color:transparent;\"><b>Fuel Type:</b> {fuelType}</span></p>\n"
f"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial, sans-serif\'; font-size:12pt; color:#ffffff; background-color:transparent;\"><b>-------------------------------------------------------------------------------------------------</b></span></p>\n"
f"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial, sans-serif\'; font-size:12pt; color:#ffffff; background-color:transparent;\"><b>Additional Information:</b><br><br> {additionalInformation}</span></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    splash_label = QLabel()
    pixmap = QPixmap('splash2.png')
    splash_label.setPixmap(pixmap)
    splash_label.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
    splash_label.move(750,200)
    splash_label.setMask(pixmap.mask())
    splash_label.show()
    QTimer.singleShot(1600, splash_label.close)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


