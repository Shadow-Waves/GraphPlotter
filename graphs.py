from pyqtgraph import PlotWidget,mkPen
from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel,QLineEdit
from PyQt5.QtGui import QMovie,QIcon
from PyQt5.QtCore import QSize
from sys import argv
from math import *
from re import match

class Graphs(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,50,600,600)
        self.setFixedSize(600,600)
        self.setWindowTitle("Function's Plotter")
        self.setWindowIcon(QIcon("C:\\Users\\Hafedh\\Desktop\\Plotter\\integral.jpg"))
        self.setWindowOpacity(.9)
        
        self.g = PlotWidget(self)
        self.g.setLabel("left","Y-Axis")
        self.g.setLabel("bottom","X-Axis")
        self.g.setTitle("Function Plotter",color="g")
        self.g.showGrid(x = True , y = True)
        
        self.setCentralWidget(self.g)

        self.inputs = QMainWindow(self)
        self.inputs.setGeometry(self.x() + self.width(),self.y() + self.height() // 2,400,200)
        self.inputs.setWindowOpacity(.9)
        self.inputs.setWindowTitle("Inputs")
        self.inputs.setStyleSheet("background-color:black;")
        self.inputs.setWindowIcon(QIcon("C:\\Users\\Hafedh\\Desktop\\Plotter\\neon.png"))

        self.function = QLabel("Fill The Inputs",self.inputs)
        self.function.setGeometry(120,0,200,50)
        self.function.setStyleSheet("background-color:transparent;color:orange;font-size:20px;")

        self.f = QLabel("f(x) = ",self.inputs)
        self.f.setGeometry(10,60,60,30)
        self.f.setStyleSheet("background-color:transparent;color:violet;font-size:20px;")
        
        self.inputt = QLineEdit(self.inputs)
        self.inputt.setGeometry(70,64,300,30)
        self.inputt.setStyleSheet("background-color:transparent;color:cyan;font-size:14px;border:2px groove green;border-radius:5px;padding:4px;")
        self.inputt.setPlaceholderText("Example : cos(x) * sin(x) or tan²(x) ...")

        self.xrange = QLabel("X-Range : ",self.inputs)
        self.xrange.setGeometry(10,100,80,30)
        self.xrange.setStyleSheet("background-color:transparent;color:red;font-size:16px;")

        self.xrange_in = QLineEdit(self.inputs)
        self.xrange_in.setGeometry(90,100,150,30)
        self.xrange_in.setStyleSheet("background-color:transparent;color:gold;font-size:14px;border:2px groove green;border-radius:5px;padding:4px;")
        self.xrange_in.setPlaceholderText("Example { 0 : 100 }")

        self.plotter = QLabel(self.inputs)
        self.plotter.setGeometry(300,120,50,50)

        self.movie = QMovie("C:\\Users\\Hafedh\\Desktop\\Plotter\\plotme.gif")
        self.movie.setScaledSize(QSize(50,50))
        self.plotter.setMovie(self.movie)
        self.movie.start()

        self.key = QLabel("PLOT",self.inputs)
        self.key.setGeometry(308,124,100,100)
        self.key.setStyleSheet("background-color:transparent;color:orange;font-size:14px;")
        self.key.mousePressEvent = self.do

        self.inputs.show()

        self.show()

    def compute(self,a = -10,b = 11):
        i = a
        while i <= b:
            if i != 0:
                yield i
            i += .01

    def do(self,e):
        try:
           if match(r'-?\d+\s*:\s*-?\d+',self.xrange_in.text()) and match(r'[\w\.\*\+\/\(\)-]+',self.inputt.text()):
                del(self.g)
                self.g = PlotWidget(self)
                self.g.setLabel("left","Y-Axis")
                self.g.setLabel("bottom","X-Axis")
                self.g.setTitle("Function Plotter",color="g")
                self.g.showGrid(x = True , y = True)
                self.setCentralWidget(self.g)
                
                xrange = self.xrange_in.text().replace(" ","").replace("{","").replace('}',"").split(":")
                l = list(self.compute(a = float(xrange[0]) , b = float(xrange[1])))
                text = self.inputt.text().replace("^","**")
                exec(f'self.g.plot({l},list(map(lambda x : {text},{l})),pen = mkPen(color = "m",width = 3,cosmetic = True))')
        except Exception as e: print(str(e))

if __name__ == "__main__":
    application = QApplication(argv)
    graph = Graphs()
    application.exec()