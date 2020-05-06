#GuiEx1.py

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import gpanel

# -------------- Class MyDialog -----------------------
class MyDialog(QDialog):

    def __init__(self):
        super(MyDialog, self).__init__()

        # Create widgets
        self.p = gpanel.GPane()
        redBtn = QPushButton("Red")
        greenBtn = QPushButton("Green")
        blackBtn = QPushButton("Black")
        goBtn = QPushButton("Go")

        # Layout of whole dialog
        dlgLayout = QVBoxLayout()

        # Layout of buttons
        btnLayout = QHBoxLayout()

        # Add buttons to button layout
        btnLayout.addWidget(redBtn)
        btnLayout.addWidget(greenBtn)
        btnLayout.addWidget(blackBtn)
        btnLayout.addWidget(goBtn)

        # Add button layout to dialog layout
        dlgLayout.addLayout(btnLayout)

        # Add gpane to dialog layout
        dlgLayout.addWidget(self.p)       

        # Set main layout
        self.setLayout(dlgLayout)

        # Register callbacks
        self.connect(redBtn, SIGNAL("clicked()"), self.onRed)
        self.connect(greenBtn, SIGNAL("clicked()"), self.onGreen)
        self.connect(blackBtn, SIGNAL("clicked()"), self.onBlack)
        self.connect(goBtn, SIGNAL("clicked()"), self.onGo)  

    def onRed(self):
        self.statusBar.showMessage("Pen color set to red")
        self.p.setPenColor([255, 0, 0])

    def onGreen(self):
        self.statusBar.showMessage("Pen color set to green")
        self.p.setPenColor([0, 255, 0])

    def onBlack(self):
        self.statusBar.showMessage("Pen color set to black")
        self.p.setPenColor([0, 0, 0])

    def onGo(self):
        self.statusBar.showMessage("Drawing Moire with n = " + str(n))
        self.p.clear()
        self.moire()
        self.statusBar.showMessage("Done")

    def moire(self):
        for i in range(n + 1):
            for k in range(n + 1):
                self.p.line(1.0*i / n, 0, 1.0*k / n, 1)
        for i in range(n + 1):
            for k in range(n + 1):
                self.p.line(0, 1.0*i / n, 1, 1.0*k / n)

    def setStatusBar(self, statusBar):
        self.statusBar = statusBar


class MyWindow(QMainWindow):

    def __init__(self, dialog):
        super(MyWindow, self).__init__()
        self.initUI(dialog)

    def initUI(self, dialog):
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar().showMessage('Ready')
        self.setCentralWidget(dialog)
        dialog.setStatusBar(self.statusBar())
        self.setWindowTitle('Moire Generator')
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(exitAction)
        self.show()

n = 10
app = QApplication(sys.argv)
dlg = MyDialog()
ex = MyWindow(dlg)
dlg.onGo()
sys.exit(app.exec_())

