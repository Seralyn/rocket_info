# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QSplashScreen, QLabel, QCompleter, QGraphicsScene, 
QGraphicsView, QLineEdit, QLabel, QPushButton, QScrollArea, QVBoxLayout, QWidget,
QSpacerItem, QMainWindow, QSizePolicy, QHBoxLayout, QVBoxLayout, QDialog, QDialogButtonBox)
from PyQt5.QtCore import QTimer, Qt
from rocket_dictionary import rocketDictionary
from collections import OrderedDict
import sys
import ctypes  #this plus the two lines below (beginning with "myappid" and "ctypes.windll" respectively allows windwows to recognize the app's icon, as opposed to just giving the window it self the proper icon

# myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
# ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

#******* Sorting Functions (Helper) ***********

def filter_entered(attr_val):
    if isinstance(attr_val, int) or isinstance(attr_val, float):
        return attr_val
    return 0


ascending_alphabetical_rocket_choices = sorted(rocketDictionary.keys())
descending_alphabetical_rocket_choices = sorted(rocketDictionary.keys(), reverse=True)
ascending_country_rocket_choices = OrderedDict(sorted(rocketDictionary.items(), key=lambda i: i[1]['Country']))
descending_country_rocket_choices = OrderedDict(sorted(rocketDictionary.items(), key=lambda i: i[1]['Country'], reverse=True)) #reverse
ascending_agency_rocket_choices = OrderedDict(sorted(rocketDictionary.items(), key=lambda i: i[1]['Agency']))
descending_agency_rocket_choices = OrderedDict(sorted(rocketDictionary.items(), key=lambda i: i[1]['Agency'], reverse=True)) #reverse

ascending_height_rocket_choices = OrderedDict(sorted(rocketDictionary.items(), key=lambda i: filter_entered(i[1]['height_int'])))
descending_height_rocket_choices = OrderedDict(sorted(rocketDictionary.items(), key=lambda i: filter_entered(i[1]['height_int']), reverse=True)) #reverse
ascending_mass_rocket_choices = OrderedDict(sorted(rocketDictionary.items(), key=lambda i: filter_entered(i[1]['mass_int'])))
descending_mass_rocket_choices = OrderedDict(sorted(rocketDictionary.items(), key=lambda i: filter_entered(i[1]['mass_int']), reverse=True)) #reverse
ascending_diameter_rocket_choices = OrderedDict(sorted(rocketDictionary.items(), key=lambda i: filter_entered(i[1]['diameter_int'])))
descending_diameter_rocket_choices = OrderedDict(sorted(rocketDictionary.items(), key=lambda i: filter_entered(i[1]['diameter_int']), reverse=True)) #reverse
ascending_payload_rocket_choices = OrderedDict(sorted(rocketDictionary.items(), key=lambda i: filter_entered(i[1]['payload_int'])))
descending_payload_rocket_choices = OrderedDict(sorted(rocketDictionary.items(), key=lambda i: filter_entered(i[1]['payload_int']), reverse=True)) #reverse
ascending_cost_rocket_choices = OrderedDict(sorted(rocketDictionary.items(), key=lambda i: filter_entered(i[1]['cost_int'])))
descending_cost_rocket_choices = OrderedDict(sorted(rocketDictionary.items(), key=lambda i: filter_entered(i[1]['cost_int']), reverse=True)) #reverse
ascending_thrust_rocket_choices = OrderedDict(sorted(rocketDictionary.items(), key=lambda i: filter_entered(i[1]['initial_thrust_int'])))
descending_thrust_rocket_choices = OrderedDict(sorted(rocketDictionary.items(), key=lambda i: filter_entered(i[1]['initial_thrust_int']), reverse=True)) #reverse
ascending_asl_isp_rocket_choices = OrderedDict(sorted(rocketDictionary.items(), key=lambda i: filter_entered(i[1]['asl_isp_int'])))
descending_asl_isp_rocket_choices = OrderedDict(sorted(rocketDictionary.items(), key=lambda i: filter_entered(i[1]['asl_isp_int']), reverse=True)) #reverse
ascending_vac_isp_rocket_choices = OrderedDict(sorted(rocketDictionary.items(), key=lambda i: filter_entered(i[1]['vac_isp_int'])))
descending_vac_isp_rocket_choices = OrderedDict(sorted(rocketDictionary.items(), key=lambda i: filter_entered(i[1]['vac_isp_int']), reverse=True)) #reverse




# ascending_height_rocket_choices = OrderedDict(sorted(rocketDictionary.items(), key=lambda i: i[1]['height_int']))
# descending_height_rocket_choices = OrderedDict(sorted(rocketDictionary.items(), key=lambda i: i[1]['height_int'], reverse=True)) #reverse
#ascending_mass_rocket_choices = OrderedDict(sorted(rocketDictionary.items(), key=lambda i: i[1]['mass_int']))
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


class CustomDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(CustomDialog, self).__init__(*args, **kwargs)
        
        self.setWindowTitle("Placeholder")
        
        QBtn = QDialogButtonBox.Ok           #| QDialogButtonBox.Cancel
        
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        # self.buttonBox.rejected.connect(self.reject)
        self.label = QLabel("Placeholder text")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.buttonBox)
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)


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
        self.searchBox.setPlaceholderText(" Enter Name of Rocket...")
        self.searchBox.textChanged.connect(self.filter_rocket_list)
        self.searchBox.setMinimumSize(QtCore.QSize(0, 10))
        self.searchBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.searchBox.setStyleSheet("background-color: rgb(70, 70, 70);\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(66, 229, 243);")
        self.searchBox.setObjectName("searchBox")
        self.completer = QCompleter(rocketDictionary.keys())
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.searchBox.setCompleter(self.completer)
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
            
        for i in range(len(self.listWidget)):    
            flagIcon = QtGui.QIcon(rocketDictionary[self.listWidget.item(i).text()]["flag_icon"])
            self.listWidget.item(i).setIcon(flagIcon)
             
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
        self.infoLayout = QtWidgets.QVBoxLayout(self.infoPaneFrame)
        self.infoLayout.setContentsMargins(30, -1, 30, -1)
        self.infoLayout.setObjectName("infoLayout")
        self.informationHeaderLabel = QtWidgets.QLabel(self.infoPaneFrame)
        self.informationHeaderLabel.setMaximumSize(QtCore.QSize(16777215, 50))
        self.informationHeaderLabel.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.informationHeaderLabel.setObjectName("informationHeaderLabel")
        self.infoLayout.addWidget(self.informationHeaderLabel)
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
        self.infoLayout.addWidget(self.textBrowser)
        self.horizontalLayout.addWidget(self.infoPaneFrame)
        self.frame = QtWidgets.QFrame(self.columnViewFrame)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

# ********** set up image frame/create containers for image and place them ************
        self.imageLayout = QtWidgets.QVBoxLayout(self.frame)
        self.imageLayout.setObjectName("imageLayout")
        self.imageHeaderLabel = QtWidgets.QLabel(self.frame)
        self.imageHeaderLabel.setMaximumSize(QtCore.QSize(580, 50))
        self.imageHeaderLabel.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.imageHeaderLabel.setObjectName("imageHeaderLabel")
        self.imageLayout.addWidget(self.imageHeaderLabel)
    
        self.imageLabel = QtWidgets.QLabel(self.frame)
        self.imageLabel.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap()
        self.imageLabel.setPixmap(pixmap)
        self.imageLabel.setMaximumSize(QtCore.QSize(580, 16777215))
        self.imageLabel.setMinimumWidth(480)
        self.imageLabel.show()
        
        self.imageLayout.addWidget(self.imageLabel)
        self.imageLabel.setStyleSheet("background-color: rgb(52, 52, 52)")
        self.imageLabel.setObjectName("imageLabel") 
        
        
        #self.graphicsView = QtWidgets.QGraphicsView(self.frame)
        #self.graphicsView.setMaximumSize(QtCore.QSize(580, 16777215))
        #self.graphicsView.setStyleSheet("background-color: rgb(52, 52, 52), background-image: url("")")
        #self.graphicsView.setObjectName("graphicsView")
        #self.imageLayout.addWidget(self.graphicsView)
        
        
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
        self.actionRocket_Families = QtWidgets.QAction(MainWindow)
        self.actionRocket_Families.setObjectName("actionRocket_Families")


        self.actionAscending = QtWidgets.QAction(MainWindow)
        self.actionAscending.setObjectName("actionAscending")
        self.actionDescending = QtWidgets.QAction(MainWindow)
        self.actionDescending.setObjectName("actionDescending")
        self.actionHeightLtH = QtWidgets.QAction(MainWindow)
        self.actionHeightLtH.setObjectName("actionHeightLtH")
        self.actionHeightHtL = QtWidgets.QAction(MainWindow)
        self.actionHeightHtL.setObjectName("actionHeightHtL")
        self.actionDiameterHtL = QtWidgets.QAction(MainWindow)
        self.actionDiameterHtL.setObjectName("actionDiameterHtL")
        self.actionDiameterLtH = QtWidgets.QAction(MainWindow)
        self.actionDiameterLtH.setObjectName("actionDiameterLtH")
        self.actionMassLtH = QtWidgets.QAction(MainWindow)
        self.actionMassLtH.setObjectName("actionMassLtH")
        self.actionMassHtL = QtWidgets.QAction(MainWindow)
        self.actionMassHtL.setObjectName("actionMassHtL")
        self.actionCostLtH = QtWidgets.QAction(MainWindow)
        self.actionCostLtH.setObjectName("actionCostLtH")
        self.actionCostHtL = QtWidgets.QAction(MainWindow)
        self.actionCostHtL.setObjectName("actionCostHtL")
        self.actionThrustLtH = QtWidgets.QAction(MainWindow)
        self.actionThrustLtH.setObjectName("actionThrustLtH")
        self.actionThrustHtL = QtWidgets.QAction(MainWindow)
        self.actionThrustHtL.setObjectName("actionThrustHtL")
        self.actionPayloadLtH = QtWidgets.QAction(MainWindow)
        self.actionPayloadLtH.setObjectName("actionPayloadLtH")
        self.actionPayloadHtL = QtWidgets.QAction(MainWindow)
        self.actionPayloadHtL.setObjectName("actionPayloadHtL")
        self.actionISP_ASL_LtH = QtWidgets.QAction(MainWindow)
        self.actionISP_ASL_LtH.setObjectName("actionISP_ASL_LtH")
        self.actionISP_ASL_HtL = QtWidgets.QAction(MainWindow)
        self.actionISP_ASL_HtL.setObjectName("actionISP_ASL_HtL")
        self.actionISP_VAC_LtH = QtWidgets.QAction(MainWindow)
        self.actionISP_VAC_LtH.setObjectName("actionISP_VAC_LtH")
        self.actionISP_VAC_HtL = QtWidgets.QAction(MainWindow)
        self.actionISP_VAC_HtL.setObjectName("actionISP_VAC_HtL")


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
        self.menuMass.addAction(self.actionMassLtH)
        self.menuMass.addAction(self.actionMassHtL)
        self.menuDiameter.addAction(self.actionDiameterLtH) #actionDiameterLtH
        self.menuDiameter.addAction(self.actionDiameterHtL) #actionDiameterHtL
        self.menuHeight.addAction(self.actionHeightLtH) #actionHeightLtH
        self.menuHeight.addAction(self.actionHeightHtL) #actionHeightHtL
        self.menuCost_Per_Launch.addAction(self.actionCostLtH) #actionCostLtH
        self.menuCost_Per_Launch.addAction(self.actionCostHtL) #actionCostHtL
        self.menuThrust.addAction(self.actionThrustLtH) #actionThrustLtH
        self.menuThrust.addAction(self.actionThrustHtL) #actionThrustHtL
        self.menuPayload_to_LEO.addAction(self.actionPayloadLtH) #actionPayloadLtH
        self.menuPayload_to_LEO.addAction(self.actionPayloadHtL) #actionPayloadHtL
        self.menuAlphabetical.addAction(self.actionAscending) 
        self.menuAlphabetical.addAction(self.actionDescending)

        self.menuISP.addAction(self.actionISP_ASL_LtH) 
        self.menuISP.addAction(self.actionISP_ASL_HtL) 
        self.menuISP.addAction(self.actionISP_VAC_LtH)
        self.menuISP.addAction(self.actionISP_VAC_HtL)


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
        self.imageLabel.setToolTip(_translate("MainWindow", "<html><head/><body><p style=\"color : black\">Image of selected rocket</p></body></html>"))
        self.imageLabel.setStatusTip(_translate("MainWindow", "Image of selected rocket"))
       
       
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
        self.actionMassLtH.setText(_translate("MainWindow", "Low to High"))
        self.actionMassLtH.setStatusTip(_translate("MainWindow", "Sort rockets by their mass on the launchpad from lightest to heaviest"))
        self.actionDiameterLtH.setText(_translate("MainWindow", "Low to High"))
        self.actionDiameterLtH.setStatusTip(_translate("MainWindow", "Sort rockets by their diameter from narrowest to widest"))
        self.actionHeightLtH.setText(_translate("MainWindow", "Low to High"))
        self.actionHeightLtH.setStatusTip(_translate("MainWindow", "Sort rockets by their height from shortest to tallest"))
        self.actionHeightHtL.setText(_translate("MainWindow", "High to Low"))
        self.actionHeightHtL.setStatusTip(_translate("MainWindow", "Sort rockets by their height from tallest to shortest"))
        self.actionCostLtH.setText(_translate("MainWindow", "Low to High"))
        self.actionCostLtH.setStatusTip(_translate("MainWindow", "Sort rockets by their cost to launch from least expensive to most expensive"))
        self.actionCostHtL.setText(_translate("MainWindow", "High to Low"))
        self.actionCostHtL.setStatusTip(_translate("MainWindow", "Sort rockets by their cost to launch from most expensive to least expensive"))
        self.actionThrustLtH.setText(_translate("MainWindow", "Low to High"))
        self.actionThrustLtH.setStatusTip(_translate("MainWindow", "Sort rockets by their thrust in kilonewtons from least to most"))
        self.actionThrustHtL.setText(_translate("MainWindow", "High to Low"))
        self.actionThrustHtL.setStatusTip(_translate("MainWindow", "Sort rockets by their thrust in kilonewtons from highest to lowest"))
        self.actionPayloadLtH.setText(_translate("MainWindow", "Low to High"))
        self.actionPayloadLtH.setStatusTip(_translate("MainWindow", "Sort rockets by their lifting capacity to Low Earth Orbit from lowest to highest"))
        self.actionAscending.setText(_translate("MainWindow", "Ascending"))
        self.actionAscending.setStatusTip(_translate("MainWindow", "Sort rockets in ascending order (A to Z)"))
        self.actionDescending.setText(_translate("MainWindow", "Descending"))
        self.actionDescending.setStatusTip(_translate("MainWindow", "Sort rockets in descending order(Z to A)"))
        self.actionMassHtL.setText(_translate("MainWindow", "High to Low"))
        self.actionMassHtL.setStatusTip(_translate("MainWindow", "Sort rockets by their mass on the launchpad from heaviest to lightest"))
        self.actionDiameterHtL.setText(_translate("MainWindow", "High to Low"))
        self.actionDiameterHtL.setStatusTip(_translate("MainWindow", "Sort rockets by their diameter from widest to narrowest"))
        self.actionPayloadHtL.setText(_translate("MainWindow", "High to Low"))
        self.actionPayloadHtL.setStatusTip(_translate("MainWindow", "Sort rockets by their lifting capacity to Low Earth Orbit from highest to lowest"))
        
        self.actionISP_ASL_LtH.setText(_translate("MainWindow", "ASL - Low to High"))
        self.actionISP_ASL_LtH.setStatusTip(_translate("MainWindow", "Sort rockets by their specific impulse at sea level from least to most"))
        self.actionISP_ASL_HtL.setText(_translate("MainWindow", "ASL - High to Low"))
        self.actionISP_ASL_HtL.setStatusTip(_translate("MainWindow", "Sort rockets by their specific impulse at sea level from most to least"))
        
        self.actionISP_VAC_LtH.setText(_translate("MainWindow", "Vac - Low to High"))
        self.actionISP_VAC_LtH.setStatusTip(_translate("MainWindow", "Sort rockets by their specific impulse in vacuum from least to most"))
        self.actionISP_VAC_HtL.setText(_translate("MainWindow", "Vac - High to Low"))
        self.actionISP_VAC_HtL.setStatusTip(_translate("MainWindow", "Sort rockets by their specific impulse in vacuum from most to least"))
        
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

         
         
         # ****************** Menu Bar Connections ***************************

# **** Show Menu ****
        #self.actionShowIndividual.triggered.connect(self.showIndivid)  #placeholders for when these actions are written
        #self.actionShowFamilies.triggered.connect(self.showFams)   #placeholders for when these actions are written

# **** Sort Menu ****
    # *** High to Low Functions ***
        self.actionDescending.triggered.connect(self.actionDescendingClicked)
        self.actionAscending.triggered.connect(self.actionAscendingClicked)
        self.actionHeightLtH.triggered.connect(self.actionHeightAscendingClicked)
        self.actionHeightHtL.triggered.connect(self.actionHeightDescendingClicked)
        self.actionDiameterLtH.triggered.connect(self.actionDiameterAscendingClicked)
        self.actionDiameterHtL.triggered.connect(self.actionDiameterDescendingClicked)
        self.actionMassLtH.triggered.connect(self.actionMassAscendingClicked)
        self.actionMassHtL.triggered.connect(self.actionMassDescendingClicked)
        self.actionPayloadLtH.triggered.connect(self.actionPayloadAscendingClicked)
        self.actionPayloadHtL.triggered.connect(self.actionPayloadDescendingClicked)
        self.actionCostLtH.triggered.connect(self.actionCostAscendingClicked)
        self.actionCostHtL.triggered.connect(self.actionCostDescendingClicked)
        self.actionThrustLtH.triggered.connect(self.actionThrustAscendingClicked)
        self.actionThrustHtL.triggered.connect(self.actionThrustDescendingClicked)
        self.actionISP_ASL_LtH.triggered.connect(self.actionISP_ASL_AscendingClicked)
        self.actionISP_ASL_HtL.triggered.connect(self.actionISP_ASL_DescendingClicked)
        self.actionISP_VAC_LtH.triggered.connect(self.actionISP_Vac_AscendingClicked)
        self.actionISP_VAC_HtL.triggered.connect(self.actionISP_Vac_DescendingClicked)

    
    # *** One Sort-Only Functions ***
        self.actionCountry.triggered.connect(self.actionCountryAscendingClicked)
        self.actionAgency.triggered.connect(self.actionAgencyClicked)

# **** Edit Menu ****
        self.actionCopy.triggered.connect(self.textBrowser.copy)   #figure out how to make copy and paste work. The documentation lies about it.
        #self.actionPaste.triggered.connect(self.paste)


# **** Help Menu ****
        self.actionVersion.triggered.connect(self.showVersionClicked)
        self.actionAbout.triggered.connect(self.showAboutClicked)
        self.actionLicensing.triggered.connect(self.showLicensingClicked)
        self.actionAcronyms.triggered.connect(self.showAcroynmClicked)
        


        # *************** Tool Bar Connections ******************
        self.actionPrint.triggered.connect(self.printButtonClicked)
        self.actionCompare.triggered.connect(self.compareButtonClicked)


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
        


#******* Printer Dialogue Window ************
    # def print_widget(self):
    #     # Create printer
    #     printer = QtPrintSupport.QPrinter()
    #     # Create painter
    #     painter = QtGui.QPainter()
    #     # Start painter
    #     painter.begin(printer)
    #     # Grab a widget you want to print
    #     screen = self.textBrowser.grab()
    #     # Draw grabbed pixmap
    #     painter.drawPixmap(10, 10, screen)
    #     # End painting
    #     painter.end()   


    # ********** Toolbar Button Click Methods **********

    def compareButtonClicked(self):
        #repopulate current sorted list with checkable versions of those items
        _translate = QtCore.QCoreApplication.translate
        item_count = len(self.listWidget)
        for i in range(item_count):
            item = self.listWidget.item(i)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
        self.imageLabel.hide()
        self.imageHeaderLabel.hide()
        #self.informationHeaderLabel.setText("Compare Rockets")
        self.informationHeaderLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">Compare Rockets</span></p></body></html>"))


    def printButtonClicked(self):
        selectedItem = self.listWidget.currentItem()
        if selectedItem == None:
            selectedItem = self.listWidget.item(0).text()
        else:
             selectedItem = selectedItem.text()
        
        printWindow.setWindowTitle(f"Printer-Friendly Layout for:  {selectedItem}")
        printWindow.setGeometry(400, 200, 600, 800)

        def sendToPrinter():
            #Create printer
            printer = QtPrintSupport.QPrinter()
            # Create painter
            painter = QtGui.QPainter()
            # Start painter
            painter.begin(printer)
            # Grab a widget you want to print
            screen = printWindow.grab()
            # Draw grabbed pixmap
            painter.drawPixmap(10, 10, screen)
            # End painting
            painter.end()


        printerWindowRocketNameFont = QtGui.QFont()
        printerWindowRocketNameFont.setFamily("Arial")
        printerWindowRocketNameFont.setPointSize(30)
        printerWindowRocketNameFont.setWeight(100)

        verticalPrintLayout = QVBoxLayout()
        nameAndFlagsPrintLayout = QHBoxLayout()
        imageAndSpecsPrintLayout = QHBoxLayout()

        printRocketName = self.listWidget.currentItem().text()

        printRocketNameLabel = QLabel(printRocketName)
        printRocketNameLabel.setAlignment(Qt.AlignHCenter)
        printRocketNameLabel.setFont(printerWindowRocketNameFont)
        printFlagLeftLabel = QLabel()
        printFlagRightLabel = QLabel()
        printFlagLeftLabel.setAlignment(Qt.AlignRight)
        printFlagRightLabel.setAlignment(Qt.AlignLeft)
        printFlagPixmap = QPixmap(rocketDictionary[printRocketName]['flag_icon'])
        printFlagPixmapScaled = printFlagPixmap.scaledToHeight(40)
        printFlagLeftLabel.setPixmap(printFlagPixmapScaled)
        printFlagRightLabel.setPixmap(printFlagPixmapScaled)

        printRocketImageLabel = QLabel()
        printRocketPixmap = QPixmap("images/" + rocketDictionary[printRocketName]['Image'])
        printRocketPixmapScaled = printRocketPixmap.scaledToHeight(300)
        printRocketImageLabel.setPixmap(printRocketPixmapScaled)
        printRocketImageLabel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        printRocketSpecsLabel = QLabel(
            f'''
Agency: {rocketDictionary[printRocketName]['Agency']}
Manufacturer: {rocketDictionary[printRocketName]['Manufacturer']}
Payload Capacity to LEO: {rocketDictionary[printRocketName]['Payload Capacity to LEO']}
Height: {rocketDictionary[printRocketName]['Height']}
Mass: {rocketDictionary[printRocketName]['Mass']}
Years in Operation: {rocketDictionary[printRocketName]['Years in Operation']}
Country: {rocketDictionary[printRocketName]['Country']}
Operational Status: {rocketDictionary[printRocketName]['Operational Status']}
Number of Stages: {rocketDictionary[printRocketName]['Number of Stages']}
Burn Time: {rocketDictionary[printRocketName]['Burn Time']}
Thrust: {rocketDictionary[printRocketName]['Thrust']}
ISP: {rocketDictionary[printRocketName]['ISP']}
Cost Per Launch: {rocketDictionary[printRocketName]['Cost Per Launch']}
Fuel Type: {rocketDictionary[printRocketName]['Fuel Type']}
Total Launches: {rocketDictionary[printRocketName]['Total Launches']}
Launch Successes: {rocketDictionary[printRocketName]['Successful Launches']}
Launch Failures: {rocketDictionary[printRocketName]['Launch Failures']}
            ''')
        printRocketSpecsLabel.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        #printRocketSpecsLabel.setAlignment(QtCore.Qt.AlignRight)
        
        # printRocketInfoLabel = QLabel(rocketDictionary[printRocketName]['Additional Information'])
        # printRocketInfoLabel.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        
        printInsidePrintButton = QPushButton("Send to Printer")
        printInsidePrintButton.clicked.connect(sendToPrinter)


        verticalPrintLayout.addWidget(printInsidePrintButton)
        verticalPrintLayout.addLayout(nameAndFlagsPrintLayout)
        nameAndFlagsPrintLayout.addWidget(printFlagLeftLabel)
        nameAndFlagsPrintLayout.addWidget(printRocketNameLabel)
        nameAndFlagsPrintLayout.addWidget(printFlagRightLabel)
        verticalPrintLayout.addLayout(imageAndSpecsPrintLayout)
        imageAndSpecsPrintLayout.addWidget(printRocketImageLabel)
        imageAndSpecsPrintLayout.addWidget(printRocketSpecsLabel)
        #verticalPrintLayout.addWidget(printRocketInfoLabel)

        printCentralwidget = QtWidgets.QWidget()
        printCentralwidget.setObjectName("printCentralwidget")
        printCentralwidget.setLayout(verticalPrintLayout)
        
        # scrollArea = QtWidgets.QScrollArea(printCentralwidget)
        # verticalPrintLayout.addWidget(scrollArea)
        # scrollAreaWidgetContents = QtWidgets.QWidget()
        # scrollArea.setWidget(scrollAreaWidgetContents)
        #vericalPrintLayout = QtWidgets.QVBoxLayout(scrollAreaWidgetContents)

        printWindowTextBrowser = QtWidgets.QTextBrowser(printCentralwidget)
        printWindowTextBrowser.setMaximumSize(QtCore.QSize(650, 400))
        printWindowTextBrowser.setMouseTracking(True)
#         printWindowTextBrowser.setStyleSheet("selection-background-color: rgb(33, 237, 255);\n"
# "color: rgb(255, 255, 255);\n"
# "border-color: rgb(255, 255, 255);\n"
# "selection-color: rgb(0, 0, 0);\n"
# "background-color: rgb(52, 52, 52);")
        printWindowTextBrowser.setFrameShadow(QtWidgets.QFrame.Raised)
        printWindowTextBrowser.setLineWrapColumnOrWidth(1)
        printWindowTextBrowser.setLineWrapMode(True)
        printWindowTextBrowser.setOpenExternalLinks(False)
        printWindowTextBrowser.setObjectName("PrintWindowTextBrowser")
        printWindowTextBrowser.setPlainText(rocketDictionary[printRocketName]['Additional Information'])
#         printWindowTextBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
# "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
# "p, li { white-space: pre-wrap; }\n"
# f"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial, sans-serif\'; font-size:12pt; color:#ffffff; background-color:transparent;\"><b>Additional Information:</b><br><br> {rocketDictionary[printRocketName]['Additional Information']}</span></p></body></html>")

        verticalPrintLayout.addWidget(printWindowTextBrowser)


        printWindow.setCentralWidget(printCentralwidget)
        
        # printRocketNameLabel.show()
        # printCentralwidget.show()
        
        printWindow.show()

         


    # ****** Sorting Menu - Rocket ListWidget Sorting Methods **********
    def addFlags(self):    
        for i in range(len(self.listWidget)):
            flagIcon = QtGui.QIcon(rocketDictionary[self.listWidget.item(i).text()]["flag_icon"])
            self.listWidget.item(i).setIcon(flagIcon)

  # ********** filter list by user input  **********
    def filter_rocket_list(self, text):
        for i in range(len(self.listWidget)):
            if text.lower() not in self.listWidget.item(i).text().lower():
                self.listWidget.item(i).setHidden(True)
            else: 
                self.listWidget.item(i).setHidden(False)


    def actionShowIndivid(self):
        self.listWidget.clear()
        for rocket in ascending_alphabetical_rocket_choices:   
            self.listWidget.addItem(rocket)
        self.addFlags()
            

    def actionAscendingClicked(self):
        self.listWidget.clear()
        for rocket in ascending_alphabetical_rocket_choices:   
            self.listWidget.addItem(rocket)
        self.addFlags()

    def actionDescendingClicked(self):
        self.listWidget.clear() 
        for rocket in descending_alphabetical_rocket_choices:
            self.listWidget.addItem(rocket)
        self.addFlags()

    def actionCountryAscendingClicked(self):
        self.listWidget.clear()
        for rocket in ascending_country_rocket_choices:
            self.listWidget.addItem(rocket)
        self.addFlags()
    
    # def actionCountryDescendingClicked(self):
    #     for i in range(len(self.listWidget)):
    #         self.listWidget.clear()
    #         for rocket in descending_country_rocket_choices:
    #             self.listWidget.addItem(rocket)
       
    def actionAgencyClicked(self):
        self.listWidget.clear()
        for rocket in ascending_agency_rocket_choices:
            self.listWidget.addItem(rocket)
        self.addFlags()

    def actionHeightAscendingClicked(self):
        self.listWidget.clear()
        for rocket in ascending_height_rocket_choices:
            self.listWidget.addItem(rocket)
        self.addFlags()

    def actionHeightDescendingClicked(self):
        self.listWidget.clear()
        for rocket in descending_height_rocket_choices:
            self.listWidget.addItem(rocket)
        self.addFlags()

    def actionDiameterAscendingClicked(self):
        self.listWidget.clear()
        for rocket in ascending_diameter_rocket_choices:
            self.listWidget.addItem(rocket)
        self.addFlags()

    def actionDiameterDescendingClicked(self):
        self.listWidget.clear()
        for rocket in descending_diameter_rocket_choices:
            self.listWidget.addItem(rocket)
        self.addFlags()
    
    def actionMassAscendingClicked(self):
        self.listWidget.clear()
        for rocket in ascending_mass_rocket_choices:
            self.listWidget.addItem(rocket)
        self.addFlags()

    def actionMassDescendingClicked(self):
        self.listWidget.clear()
        for rocket in descending_mass_rocket_choices:
            self.listWidget.addItem(rocket)
        self.addFlags()

    def actionPayloadAscendingClicked(self):
        self.listWidget.clear()
        for rocket in ascending_payload_rocket_choices:
            self.listWidget.addItem(rocket)
        self.addFlags()

    def actionPayloadDescendingClicked(self):
        self.listWidget.clear()
        for rocket in descending_payload_rocket_choices:
            self.listWidget.addItem(rocket)
        self.addFlags()

    def actionCostAscendingClicked(self):
        self.listWidget.clear()
        for rocket in ascending_cost_rocket_choices:
            self.listWidget.addItem(rocket)
        self.addFlags()

    def actionCostDescendingClicked(self):
        self.listWidget.clear()
        for rocket in descending_cost_rocket_choices:
            self.listWidget.addItem(rocket)
        self.addFlags()

    def actionThrustAscendingClicked(self):
        self.listWidget.clear()
        for rocket in ascending_thrust_rocket_choices:
            self.listWidget.addItem(rocket)
        self.addFlags()
    
    def actionThrustDescendingClicked(self):
        self.listWidget.clear()
        for rocket in descending_thrust_rocket_choices:
            self.listWidget.addItem(rocket)
        self.addFlags()

    def actionISP_ASL_AscendingClicked(self):
        self.listWidget.clear()
        for rocket in ascending_asl_isp_rocket_choices:
            self.listWidget.addItem(rocket)
        self.addFlags()

    def actionISP_ASL_DescendingClicked(self):
        self.listWidget.clear()
        for rocket in descending_asl_isp_rocket_choices:
            self.listWidget.addItem(rocket)
        self.addFlags()

    def actionISP_Vac_AscendingClicked(self):
        self.listWidget.clear()
        for rocket in ascending_vac_isp_rocket_choices:
            self.listWidget.addItem(rocket)
        self.addFlags()

    def actionISP_Vac_DescendingClicked(self):
        self.listWidget.clear()
        for rocket in descending_vac_isp_rocket_choices:
            self.listWidget.addItem(rocket)
        self.addFlags()
# **********  Menu-->[Help] Button Click Methods **************

    def showVersionClicked(self):
        versionDlg = CustomDialog()  #removing self from CustomDiaglog(self) made this work.
        versionDlg.setWindowTitle("Version Info")
        versionDlg.label.setText(
            '''Version: 0.4.5 Alpha''')
        versionDlg.exec_()

    def showAcroynmClicked(self):
        acronymDlg = CustomDialog()  #removing self from CustomDiaglog(self) made this work.
        acronymDlg.setWindowTitle("Acronyms")
        acronymDlg.label.setText(
            '''
            -Agencies-
NASA: National Aeronautics and Space Administration
ESA: European Space Agency
CNES: Centre national d'études spatiales
JAXA: Japan Aerospace and Exploration Agency
ASI: Italian Space Agency
USAF: United States Air Force
USSF: United States Space Force
DARPA: Defense Advanced Research Projects Agency
ELDO: European Launcher Development Organisation
ABMA: Army Ballistic Missile Agency
INTA: Instituto Nacional de Técnica Aeroespacial
SSIA: Space Services Inc. of America
EER: 

             -Orbits-
LEO: Low Earth Orbit
MEO: Mid Earth Orbit
HEO: High Earth Orbit
GEO: Geostationary Orbit
GTO: Geostationary Transfer Orbit
SSO: Sun-Synchronous Orbit (Polar Orbit)
TLI: Trans Lunar Injection

             -Fuel Types-
SRB: Solid Rocket Booster
ISP: Specific Impulse
HTPB: Hydroxyl-Terminated Polybutadiene
CTPB: Carboxy-Terminated Polybutadiene
PBAN: Polybutadiene Acrylonitrile
LOX: Liquid Oxygen
LH2: Liquid Hydrogen
(I)RFNA: Red Fuming Nitric Acid
UDMH: Unsymmetrical Dimethylhydrazine
MMH: Monomethyl Hydrazine
APCP: Ammonium Perchlorate Composite Propellant
NEPE: Nitrate Ester Plasticized Polyether
JP-4: Jet Propellant 4

ICBM: Intercontinental Ballistic Missile
IRBM: Intermediate Range Ballistic Missile

            ''')
        acronymDlg.exec_()

    def showLicensingClicked(self):
        licensingDlg = CustomDialog()  #removing self from CustomDiaglog(self) made this work.
        licensingDlg.setWindowTitle("Licensing")
        licensingDlg.label.setText(
            '''
License: MIT (https://opensource.org/licenses/MIT)

Printer Icon: (https://p.yusukekamiyamane.com/)
Compare Icon: (Freepik from "https://www.flaticon.com/")
Flag Icons: (Freepik from www.flaticon.com)
''')
        licensingDlg.exec_()

    
    def showAboutClicked(self):
        aboutDlg = CustomDialog()  #removing self from CustomDiaglog(self) made this work.
        aboutDlg.setWindowTitle("About")
        aboutDlg.label.setText(
            '''
Developer: Seralyn Campbell
with a huge thanks to Gabrielė Žarskutė for advising

Email: seralyn.dev@gmail.com

Written in: Python 3.8.5

Open Source Software: 
https://github.com/Seralyn/rocket_info''')
        aboutDlg.exec_()
        


        
# ***** Define what happens when a rocket is selected from listWidget ******
    def selectionChanged(self):
        _translate = QtCore.QCoreApplication.translate
        rocketName = self.listWidget.currentItem().text()
        rocketImage = "images/" + rocketDictionary[rocketName]['Image']
        
        pixmap2 = QPixmap(rocketImage)
        self.imageLabel.setPixmap(pixmap2)
        #self.graphicsView.setStyleSheet(f"background-color: rgb(52, 52, 52); background-image: url({rocketImage}); background-repeat: no-repeat; position: absolute; top: 50%; left: 50%")
        manufacturer = rocketDictionary[rocketName]['Manufacturer'].replace('\n', '<br />').replace('\n\n', '<br /><br />')
        height = rocketDictionary[rocketName]['Height'].replace('\n', '<br />')
        #height_string = rocketDictionary[rocketName]['HeightString'].replace('\n', '<br />')    #add this and also add {height_string} in html line below, but also make height above this a str(rocketDic....)
        diameter = rocketDictionary[rocketName]['Diameter'].replace('\n', '<br />')
        mass = rocketDictionary[rocketName]['Mass'].replace('\n', '<br />')
        operationalStatus = rocketDictionary[rocketName]['Operational Status']
        burnTime = rocketDictionary[rocketName]['Burn Time'].replace('\n', '<br />')
        thrust = rocketDictionary[rocketName]['Thrust'].replace('\n', '<br />')
        isp = rocketDictionary[rocketName]['ISP'].replace('\n', '<br />')
        fuelType = rocketDictionary[rocketName]['Fuel Type']
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
    app.setWindowIcon(QtGui.QIcon("rocket_icon_512.ico"))
    
    splash_label = QLabel()
    splashPixmap = QPixmap('splash2.png')
    splash_label.setPixmap(splashPixmap)
    splash_label.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
    splash_label.move(750,200)
    splash_label.setMask(splashPixmap.mask())
    splash_label.show()
    QTimer.singleShot(1600, splash_label.close)

   #initialize print window...maybe?
    printWindow = QtWidgets.QMainWindow()
    MainWindow = QtWidgets.QMainWindow()
    
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    MainWindow.show()
    sys.exit(app.exec_())


