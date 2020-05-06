# GuiEx3.py

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import gpanel
import random

# --------------- Class MyDialog ---------------------- 
class MyDialog(QDialog):

    def __init__(self):
        super(MyDialog, self).__init__()

        # Create widgets
        self.p = gpanel.GPane(-0.1, 1.1, -0.1, 1.1)
        lbl1 = QLabel("Number of drops:")
        lbl2 = QLabel("Pi =")
        self.le1 = QLineEdit("10000")
        self.le2 = QLineEdit()
        goBtn = QPushButton("Go")

        # Layout of whole dialog
        dlgLayout = QVBoxLayout()  

        # Layout of buttons
        btnLayout = QHBoxLayout() 
        
        # Add buttons to button layout
        btnLayout.addWidget(lbl1) 
        btnLayout.addWidget(self.le1) 
        btnLayout.addWidget(goBtn) 
        btnLayout.addWidget(lbl2) 
        btnLayout.addWidget(self.le2) 
        
        # Add button layout to dialog layout
        dlgLayout.addLayout(btnLayout)
       
        # Add gpane to dialog layout
        dlgLayout.addWidget(self.p)
        
        # Set main layout 
        self.setLayout(dlgLayout)

        # Register callbacks
        self.connect(goBtn, SIGNAL("clicked()"), self.onGo)
        self.setWindowTitle("Raindrop Simulation")

    def init(self):
        self.le2.setText("")
        self.p.clear()
        self.p.setPenColor("black")
        self.p.pos(0.5, 0.5)
        self.p.rectangle(1, 1)
        self.p.pos(0, 0)
        self.p.arc(1, 0, 90)

    def onGo(self):
        global hits
        try:
            n = int(self.le1.text())
            if n < 10 or n > 100000:
                self.le2.setText("n not in 10...100000")
                return
        except:
            self.le2.setText("n not in 10...100000")
            return
        self.init()
        hits = 0
        for i in range(n):
            self.le1.setText(str(i + 1))
            zx = random.random()
            zy = random.random()
            if zx * zx + zy * zy < 1:
                hits += 1
                self.p.setPenColor("red")
            else:
                self.p.setPenColor("green")
            self.p.point(zx, zy)
        pi =  4.0 * hits / n
        self.le2.setText(str(pi))

# --------------- Main ---------------------- 
app = QApplication(sys.argv)
dlg = MyDialog()
dlg.show()
app.exec_()

