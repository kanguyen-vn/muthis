# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'schenky_update1.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import popplerqt5


class Ui_Schenky(object):
    def setupUi(self, Schenky):
        Schenky.setObjectName("Schenky")
        Schenky.resize(1088, 591)
        self.centralwidget = QtWidgets.QWidget(Schenky)
        self.centralwidget.setObjectName("centralwidget")
        self.keyLabel = QtWidgets.QLabel(self.centralwidget)
        self.keyLabel.setGeometry(QtCore.QRect(20, 10, 59, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.keyLabel.setFont(font)
        self.keyLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.keyLabel.setObjectName("keyLabel")
        self.keyCombo = QtWidgets.QComboBox(self.centralwidget)
        self.keyCombo.setGeometry(QtCore.QRect(90, 20, 191, 31))
        self.keyCombo.setObjectName("keyCombo")
        self.keyCombo.addItem("")
        self.keyCombo.addItem("")
        self.keyCombo.addItem("")
        self.keyCombo.addItem("")
        self.keyCombo.addItem("")
        self.keyCombo.addItem("")
        self.keyCombo.addItem("")
        self.keyCombo.addItem("")
        self.keyCombo.addItem("")
        self.keyCombo.addItem("")
        self.keyCombo.addItem("")
        self.keyCombo.addItem("")
        self.keyCombo.addItem("")
        self.keyCombo.addItem("")
        self.keyCombo.addItem("")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 60, 611, 121))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.noteInput = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.noteInput.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.noteInput.setContentsMargins(0, 0, 0, 0)
        self.noteInput.setVerticalSpacing(10)
        self.noteInput.setObjectName("noteInput")
        self.trebleLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.trebleLabel.setFont(font)
        self.trebleLabel.setObjectName("trebleLabel")
        self.noteInput.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.trebleLabel)
        self.trebleLayoutWidget = QtWidgets.QWidget(self.formLayoutWidget)
        self.trebleLayoutWidget.setMinimumSize(QtCore.QSize(0, 30))
        self.trebleLayoutWidget.setMaximumSize(QtCore.QSize(16777215, 30))
        self.trebleLayoutWidget.setMouseTracking(True)
        self.trebleLayoutWidget.setAutoFillBackground(False)
        self.trebleLayoutWidget.setStyleSheet("QWidget { background: white } \n QWidget:focus { background: #70D1D0 }")
        self.trebleLayoutWidget.setObjectName("trebleLayoutWidget")
        self.trebleLayoutWidget.setFocusPolicy(Qt.ClickFocus)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.trebleLayoutWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 551, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.trebleLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.trebleLayout.setContentsMargins(6, 0, 6, 0)
        self.trebleLayout.setObjectName("trebleLayout")
#         self.c4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
#         self.c4.setMinimumSize(QtCore.QSize(50, 0))
#         self.c4.setMaximumSize(QtCore.QSize(50, 16777215))
#         self.c4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
#         self.c4.setStyleSheet("QPushButton {\n"
# "border-width: 1px;\n"
# "border-style: solid;\n"
# "border-color: black;\n"
# "}")
#         self.c4.setCheckable(False)
#         self.c4.setChecked(False)
#         self.c4.setAutoDefault(False)
#         self.c4.setDefault(False)
#         self.c4.setFlat(True)
#         self.c4.setObjectName("c4")
#         self.trebleLayout.addWidget(self.c4)
#         self.d4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
#         self.d4.setMinimumSize(QtCore.QSize(50, 0))
#         self.d4.setMaximumSize(QtCore.QSize(50, 16777215))
#         self.d4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
#         self.d4.setStyleSheet("QPushButton {\n"
# "border-width: 1px;\n"
# "border-style: solid;\n"
# "border-color: black;\n"
# "}")
#         self.d4.setFlat(True)
#         self.d4.setObjectName("d4")
#         self.trebleLayout.addWidget(self.d4)
#         spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
#         self.trebleLayout.addItem(spacerItem)
        self.noteInput.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.trebleLayoutWidget)
        self.bassLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.bassLabel.setFont(font)
        self.bassLabel.setObjectName("bassLabel")
        self.noteInput.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.bassLabel)
        self.bassLayoutWidget = QtWidgets.QWidget(self.formLayoutWidget)
        self.bassLayoutWidget.setMinimumSize(QtCore.QSize(0, 30))
        self.bassLayoutWidget.setMaximumSize(QtCore.QSize(16777215, 30))
        self.bassLayoutWidget.setStyleSheet("QWidget { background: white } \n QWidget:focus { background: #70D1D0 }")
        self.bassLayoutWidget.setObjectName("bassLayoutWidget")
        self.bassLayoutWidget.setFocusPolicy(Qt.ClickFocus)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.bassLayoutWidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 551, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.bassLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.bassLayout.setContentsMargins(6, 0, 6, 0)
        self.bassLayout.setObjectName("bassLayout")
        self.noteInput.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.bassLayoutWidget)
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.formLayoutWidget)
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.noteInput.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.horizontalScrollBar)
        
        self.imageLabel = QtWidgets.QLabel()
        self.imageLabel.setGeometry(QtCore.QRect(0, 0, 581, 281))
        self.imageLabel.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        self.imageLabel.setScaledContents(True)
        self.imageLabel.setObjectName("imageLabel")

        self.previewScrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.previewScrollArea.setGeometry(QtCore.QRect(30, 250, 581, 281))
        self.previewScrollArea.setWidgetResizable(False)
        self.previewScrollArea.setObjectName("previewScrollArea")
        self.previewScrollArea.setBackgroundRole(QtGui.QPalette.Dark)
        self.previewScrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.previewScrollArea.setBackgroundRole(QtGui.QPalette.Dark)
        self.previewScrollArea.setWidget(self.imageLabel)

        self.previewLabel = QtWidgets.QLabel(self.centralwidget)
        self.previewLabel.setGeometry(QtCore.QRect(30, 220, 81, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.previewLabel.setFont(font)
        self.previewLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.previewLabel.setObjectName("previewLabel")
        self.elementTabs = QtWidgets.QTabWidget(self.centralwidget)
        self.elementTabs.setGeometry(QtCore.QRect(670, 220, 391, 311))
        self.elementTabs.setObjectName("elementTabs")
        self.slursTab = QtWidgets.QWidget()
        self.slursTab.setObjectName("slursTab")
        self.elementTabs.addTab(self.slursTab, "")
        self.unfoldingsTab = QtWidgets.QWidget()
        self.unfoldingsTab.setObjectName("unfoldingsTab")
        self.elementTabs.addTab(self.unfoldingsTab, "")
        self.linesTab = QtWidgets.QWidget()
        self.linesTab.setObjectName("linesTab")
        self.elementTabs.addTab(self.linesTab, "")
        self.propertiesLabel = QtWidgets.QLabel(self.centralwidget)
        self.propertiesLabel.setGeometry(QtCore.QRect(670, 10, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.propertiesLabel.setFont(font)
        self.propertiesLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.propertiesLabel.setObjectName("propertiesLabel")
        self.propertiesTable = QtWidgets.QTableWidget(self.centralwidget)
        self.propertiesTable.setGeometry(QtCore.QRect(670, 50, 391, 151))
        self.propertiesTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.propertiesTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.propertiesTable.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.propertiesTable.setAlternatingRowColors(True)
        self.propertiesTable.setTextElideMode(QtCore.Qt.ElideRight)
        self.propertiesTable.setWordWrap(True)
        self.propertiesTable.setCornerButtonEnabled(True)
        self.propertiesTable.setRowCount(7)
        self.propertiesTable.setColumnCount(2)
        self.propertiesTable.setObjectName("propertiesTable")
        item = QtWidgets.QTableWidgetItem()
        self.propertiesTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.propertiesTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
        self.propertiesTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable)
        self.propertiesTable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
        self.propertiesTable.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
        self.propertiesTable.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
        self.propertiesTable.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
        self.propertiesTable.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.propertiesTable.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.propertiesTable.setItem(6, 0, item)
        self.propertiesTable.horizontalHeader().setDefaultSectionSize(125)
        self.propertiesTable.horizontalHeader().setStretchLastSection(True)
        self.propertiesTable.verticalHeader().setVisible(False)
        self.propertiesTable.verticalHeader().setDefaultSectionSize(25)
        self.refreshButton = QtWidgets.QPushButton(self.centralwidget)
        self.refreshButton.setGeometry(QtCore.QRect(528, 220, 113, 25))
        self.refreshButton.setObjectName("refreshButton")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(180, 220, 341, 23))
        self.checkBox.setObjectName("checkBox")
        self.zoomInButton = QtWidgets.QPushButton(self.centralwidget)
        self.zoomInButton.setGeometry(QtCore.QRect(616, 250, 25, 25))
        self.zoomInButton.setObjectName("zoomInButton")
        self.zoomOutButton = QtWidgets.QPushButton(self.centralwidget)
        self.zoomOutButton.setGeometry(QtCore.QRect(616, 280, 25, 25))
        self.zoomOutButton.setObjectName("zoomOutButton")
        Schenky.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Schenky)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1088, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        Schenky.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Schenky)
        self.statusbar.setObjectName("statusbar")
        Schenky.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(Schenky)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(Schenky)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(Schenky)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(Schenky)
        self.actionExit.setObjectName("actionExit")
        self.actionCopy = QtWidgets.QAction(Schenky)
        self.actionCopy.setObjectName("actionCopy")
        self.actionCut = QtWidgets.QAction(Schenky)
        self.actionCut.setObjectName("actionCut")
        self.actionPaste = QtWidgets.QAction(Schenky)
        self.actionPaste.setObjectName("actionPaste")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionPaste)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(Schenky)
        self.elementTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Schenky)

        self.globalVarsSetup()
        QtWidgets.qApp.focusChanged.connect(self.onFocusChanged)
        self.zoomInButton.clicked.connect(self.zoomIn)
        self.zoomOutButton.clicked.connect(self.zoomOut)
        self.refreshButton.clicked.connect(self.displayPdf)
    
    def globalVarsSetup(self):
        self.currentStaff = None
        self.currentNote = None
        self.scaleFactor = 1.0
    
    def onFocusChanged(self, old, now):
        if old == self.trebleLayoutWidget or old == self.bassLayoutWidget:
            old.clearFocus()
        if now == self.trebleLayoutWidget:
            self.currentStaff = self.trebleLayout
        elif now == self.bassLayoutWidget:
            self.currentStaff = self.bassLayout
        else:
            self.currentStaff = None
    
    def loadPdf(self):
        pdf = popplerqt5.Poppler.Document.load("output.pdf")
        if not pdf:
            print("Cannot load output.pdf")
            return
        print("Import successful")
        self.pdf = pdf

    def displayPdf(self):
        pdfPage = self.pdf.page(0)
        if not pdfPage:
            print("Cannot load page")
            return
        print("Page successful")
        image = pdfPage.renderToImage(300, 300, -1, -1, -1, -1)
        if image.isNull():
            print("QImage is null")
            return
        print("QImage successful")
        pixmap01 = QtGui.QPixmap.fromImage(image)
        pixmapImage = QtGui.QPixmap(pixmap01)
        self.imageLabel.setPixmap(pixmapImage)
        self.scaleFactor = 1.0
        # self.previewScrollArea.setVisible(True)
        self.imageLabel.adjustSize()

    def scaleImage(self, factor):
        self.scaleFactor *= factor
        self.imageLabel.resize(self.scaleFactor * self.imageLabel.pixmap().size())
        self.adjustScrollBar(self.previewScrollArea.horizontalScrollBar(), factor)
        self.adjustScrollBar(self.previewScrollArea.verticalScrollBar(), factor)
        self.zoomInButton.setEnabled(self.scaleFactor < 3.0)
        self.zoomOutButton.setEnabled(self.scaleFactor > 0.333)

    def adjustScrollBar(self, scrollbar, factor):
        scrollbar.setValue(int(factor * scrollbar.value() + (factor - 1) * scrollbar.pageStep() / 2))

    def zoomIn(self):
        self.scaleImage(1.25)

    def zoomOut(self):
        self.scaleImage(0.8)
    
    def retranslateUi(self, Schenky):
        _translate = QtCore.QCoreApplication.translate
        Schenky.setWindowTitle(_translate("Schenky", "Schenky"))
        self.keyLabel.setText(_translate("Schenky", "Key:"))
        self.keyCombo.setStatusTip(_translate("Schenky", "Choose a key"))
        self.keyCombo.setItemText(0, _translate("Schenky", "C major/A minor"))
        self.keyCombo.setItemText(1, _translate("Schenky", "C# major/A# minor"))
        self.keyCombo.setItemText(2, _translate("Schenky", "Db major/Bb minor"))
        self.keyCombo.setItemText(3, _translate("Schenky", "D major/B minor"))
        self.keyCombo.setItemText(4, _translate("Schenky", "Eb major/C minor"))
        self.keyCombo.setItemText(5, _translate("Schenky", "E major/C# minor"))
        self.keyCombo.setItemText(6, _translate("Schenky", "F major/D minor"))
        self.keyCombo.setItemText(7, _translate("Schenky", "F# major/D# minor"))
        self.keyCombo.setItemText(8, _translate("Schenky", "Gb major/Eb minor"))
        self.keyCombo.setItemText(9, _translate("Schenky", "G major/E minor"))
        self.keyCombo.setItemText(10, _translate("Schenky", "Ab major/F minor"))
        self.keyCombo.setItemText(11, _translate("Schenky", "A major/F# minor"))
        self.keyCombo.setItemText(12, _translate("Schenky", "Bb major/G minor"))
        self.keyCombo.setItemText(13, _translate("Schenky", "B major/G# minor"))
        self.keyCombo.setItemText(14, _translate("Schenky", "Cb major/Ab minor"))
        self.trebleLabel.setText(_translate("Schenky", "Treble:"))
        # self.c4.setText(_translate("Schenky", "C4"))
        # self.d4.setText(_translate("Schenky", "D4"))
        self.bassLabel.setText(_translate("Schenky", "Bass:"))
        self.previewScrollArea.setStatusTip(_translate("Schenky", "Schenkerian graph preview"))
        self.previewLabel.setText(_translate("Schenky", "Preview:"))
        self.elementTabs.setStatusTip(_translate("Schenky", "Add or remove Schenkerian elements"))
        self.elementTabs.setTabText(self.elementTabs.indexOf(self.slursTab), _translate("Schenky", "Slurs"))
        self.elementTabs.setTabText(self.elementTabs.indexOf(self.unfoldingsTab), _translate("Schenky", "Unfoldings"))
        self.elementTabs.setTabText(self.elementTabs.indexOf(self.linesTab), _translate("Schenky", "Lines"))
        self.propertiesLabel.setText(_translate("Schenky", "Note properties:"))
        self.propertiesTable.setStatusTip(_translate("Schenky", "Edit note properties"))
        item = self.propertiesTable.horizontalHeaderItem(0)
        item.setText(_translate("Schenky", "Property"))
        item = self.propertiesTable.horizontalHeaderItem(1)
        item.setText(_translate("Schenky", "Value"))
        __sortingEnabled = self.propertiesTable.isSortingEnabled()
        self.propertiesTable.setSortingEnabled(False)
        item = self.propertiesTable.item(0, 0)
        item.setText(_translate("Schenky", "ID"))
        item = self.propertiesTable.item(1, 0)
        item.setText(_translate("Schenky", "Note"))
        item = self.propertiesTable.item(2, 0)
        item.setText(_translate("Schenky", "Accidental"))
        item = self.propertiesTable.item(3, 0)
        item.setText(_translate("Schenky", "Register"))
        item = self.propertiesTable.item(4, 0)
        item.setText(_translate("Schenky", "Slurs to..."))
        item = self.propertiesTable.item(5, 0)
        item.setText(_translate("Schenky", "Unfolds with..."))
        item = self.propertiesTable.item(6, 0)
        item.setText(_translate("Schenky", "Part of lines..."))
        self.propertiesTable.setSortingEnabled(__sortingEnabled)
        self.refreshButton.setStatusTip(_translate("Schenky", "Refresh Schenkerian graph"))
        self.refreshButton.setText(_translate("Schenky", "Refresh"))
        self.checkBox.setText(_translate("Schenky", "Auto-refresh (uncheck for better performance)"))
        self.zoomInButton.setStatusTip(_translate("Schenky", "Zoom In"))
        self.zoomInButton.setText(_translate("Schenky", "+"))
        self.zoomOutButton.setStatusTip(_translate("Schenky", "Zoom Out"))
        self.zoomOutButton.setText(_translate("Schenky", "-"))
        self.menuFile.setTitle(_translate("Schenky", "File"))
        self.menuEdit.setTitle(_translate("Schenky", "Edit"))
        self.actionNew.setText(_translate("Schenky", "New"))
        self.actionNew.setStatusTip(_translate("Schenky", "Create a new file"))
        self.actionNew.setShortcut(_translate("Schenky", "Ctrl+N"))
        self.actionOpen.setText(_translate("Schenky", "Open"))
        self.actionOpen.setStatusTip(_translate("Schenky", "Open a file"))
        self.actionOpen.setShortcut(_translate("Schenky", "Ctrl+O"))
        self.actionSave.setText(_translate("Schenky", "Save"))
        self.actionSave.setStatusTip(_translate("Schenky", "Save file"))
        self.actionExit.setText(_translate("Schenky", "Exit"))
        self.actionCopy.setText(_translate("Schenky", "Copy"))
        self.actionCopy.setShortcut(_translate("Schenky", "Ctrl+C"))
        self.actionCut.setText(_translate("Schenky", "Cut"))
        self.actionCut.setShortcut(_translate("Schenky", "Ctrl+X"))
        self.actionPaste.setText(_translate("Schenky", "Paste"))
        self.actionPaste.setShortcut(_translate("Schenky", "Ctrl+V"))


class MainWindow(QtWidgets.QMainWindow, Ui_Schenky):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
    
    def newNote(self, name, staff, widget):
        newNote = QtWidgets.QPushButton(widget)
        newNote.setMinimumSize(QtCore.QSize(50, 0))
        newNote.setMaximumSize(QtCore.QSize(50, 16777215))
        newNote.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        newNote.setStyleSheet("QPushButton {\n"
            "border-width: 1px;\n"
            "border-style: solid;\n"
            "border-color: black;\n"
            "}")
        newNote.setCheckable(False)
        newNote.setChecked(False)
        newNote.setAutoDefault(False)
        newNote.setDefault(False)
        newNote.setFlat(True)
        newNote.setObjectName("someNote")
        newNote.setText(QtCore.QCoreApplication.translate("Schenky", name))
        count = staff.count()
        if count > 1:
            staff.removeItem(staff.itemAt(count - 1))
        staff.addWidget(newNote)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        staff.addItem(spacerItem)

    def keyPressEvent(self, e):
        if self.currentStaff == None:
            return
        if e.key() == Qt.Key_C:
            note = "C"
        elif e.key() == Qt.Key_D:
            note = "D"
        elif e.key() == Qt.Key_E:
            note = "E"
        elif e.key() == Qt.Key_F:
            note = "F"
        elif e.key() == Qt.Key_G:
            note = "G"
        elif e.key() == Qt.Key_A:
            note = "A"
        elif e.key() == Qt.Key_B:
            note = "B"
        else:
            return
        note += "4"

        if self.currentStaff == self.trebleLayout:
            self.newNote(note, self.trebleLayout, self.horizontalLayoutWidget)
            self.newNote("S", self.bassLayout, self.horizontalLayoutWidget_2)
        else:
            self.newNote(note, self.bassLayout, self.horizontalLayoutWidget_2)
            self.newNote("S", self.trebleLayout, self.horizontalLayoutWidget)

        # if self.currentStaff == self.trebleLayout:
        #     newNote = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        #     otherStaff = self.bassLayout
        # else:
        #     newNote = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        #     otherStaff = self.trebleLayout

        # newNote.setMinimumSize(QtCore.QSize(50, 0))
        # newNote.setMaximumSize(QtCore.QSize(50, 16777215))
        # newNote.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # newNote.setStyleSheet("QPushButton {\n"
        #     "border-width: 1px;\n"
        #     "border-style: solid;\n"
        #     "border-color: black;\n"
        #     "}")
        # newNote.setCheckable(False)
        # newNote.setChecked(False)
        # newNote.setAutoDefault(False)
        # newNote.setDefault(False)
        # newNote.setFlat(True)
        # newNote.setObjectName("someNote")
        # newNote.setText(QtCore.QCoreApplication.translate("Schenky", note))
        # count = self.currentStaff.count()
        # if count > 1:
        #     self.currentStaff.removeItem(self.currentStaff.itemAt(count - 1))
        # self.currentStaff.addWidget(newNote)
        # spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.currentStaff.addItem(spacerItem)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # Schenky = QtWidgets.QMainWindow()
    # ui = Ui_Schenky()
    # ui.setupUi(Schenky)
    # Schenky.show()
    ui = MainWindow()
    ui.show()
    ui.loadPdf()
    ui.displayPdf()
    sys.exit(app.exec_())
