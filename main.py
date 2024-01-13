#
# Created on: 21 mar 2019
# Author: Mariusz
#
import sys
from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from prettytable import PrettyTable
from NSGA import NSGA
global NSGA_values

class NSGA_Variable:
    def __init__(self):
        self.Fun1 = '(x_1-2)^2'
        self.Fun2 = 'x_1^2'
        self.tab_lim = [[-10.0,10.0],[-10.0,10.0],[-10.0,10.0],[-10.0,10.0],[-10.0,10.0]]
        self.lam = 0.9
        self.lamshare = 0.01
        self.T = 20
        self.P0 = 1000
        self.tab_response = []
        self.tab_xi = []
        self.x = []
        self.y = []
        self.p_n = 0.5 # promien niszy
        self.alpha = 2

    def change_val(self, text, values):
        if text == "F1":
            self.Fun1 = values
        elif text == "F2":
            self.Fun2 = values
        elif text == "Promien":
            self.p_n = values[0]
            self.alpha = int(values[1])
        elif text == "x1":
            self.tab_lim[0] = [values[0], values[1]]
        elif text == "x2":
            self.tab_lim[1] = [values[0], values[1]]
        elif text == "x3":
            self.tab_lim[2] = [values[0], values[1]]
        elif text == "x4":
            self.tab_lim[3] = [values[0], values[1]]
        elif text == "x5":
            self.tab_lim[4] = [values[0], values[1]]
        elif text == "lam":
            self.lam = values[0]
            self.lamshare = values[1]
        elif text == "T":
            self.T = int(values[0])
            self.P0 = int(values[1])


    def get_values(self):
        string = ''
        string = string + 'Badane Funkcje: \n'
        string = string + "Funkcja1: " + str(self.Fun1)+ '\n'
        string = string + 'Funkcja2: ' + str(self.Fun2) + '\n'
        string = string + 'Zakresy poszczegolnych zmiennych: \n'
        string = string + 'x1: (' + str(self.tab_lim[0][0]) + ';' + str(self.tab_lim[0][1]) + ')\n'
        string = string + 'x2: (' + str(self.tab_lim[1][0]) + ';' + str(self.tab_lim[1][1]) + ')\n'
        string = string + 'x3: (' + str(self.tab_lim[2][0]) + ';' + str(self.tab_lim[2][1]) + ')\n'
        string = string + 'x4: (' + str(self.tab_lim[3][0]) + ';' + str(self.tab_lim[3][1]) + ')\n'
        string = string + 'x5: (' + str(self.tab_lim[4][0]) + ';' + str(self.tab_lim[4][1]) + ')\n'
        string = string + 'Parametry algorytmu NSGA: \n'
        string = string + 'Prawdopodobienstwo krzyzowania = ' + str(self.lam) + '\n'
        string = string + 'Prawdopodobienstwo mutacji = ' + str(self.lamshare) + '\n'
        string = string + 'Promien niszy = ' + str(self.p_n) + '\n'
        string = string + 'Alpha = ' + str(self.alpha) + '\n'
        string = string + 'T = ' + str(self.T) + '\n'
        string = string + 'P0 = ' + str(self.P0) + '\n'
        return string


class PlainText(QLabel):
    def __init__(self, text, name):
        self.p = QLabel(str(text))
        self.name = name


class Buttons:

    def __init__(self, text, values, results1 = "None", results2 = "None"):
        if results1 == "None":
            if text == "NSGA":
                self.b = QPushButton("Rozpoczecie pracy algorytmu")
            elif text == "Wykres":
                self.b = QPushButton("Przedstaw wynik")
        else:
            self.b = QPushButton("Zatwierdz")
        self.text = text
        self.results1 = results1
        self.results2 = results2
        self.values = values
        self.b.clicked.connect(lambda: self.handleInput(self.text))

    def handleInput(self, v):
        global tablica_wynik_algorytmu
        if self.results1 == "None":
            if self.text == "Wykres":
                draw_chart()
            elif self.text == "NSGA":
                NSGA_values.tab_response, NSGA_values.tab_xi = NSGA(NSGA_values.P0, NSGA_values.T, NSGA_values.lam,
                                            NSGA_values.lamshare, 2, 0.5, NSGA_values.tab_lim,
                                            NSGA_values.Fun1, NSGA_values.Fun2)
                result_presentation(NSGA_values.tab_response[NSGA_values.T-1], NSGA_values.tab_xi)
        elif self.results2 == "None":
            NSGA_values.change_val(v,str(self.results1.text()))
            self.results1.setText("")
        else:
            NSGA_values.change_val(v,[float(self.results1.text()),float(self.results2.text())])
            self.results1.setText("")
            self.results2.setText("")
        self.values.setText(NSGA_values.get_values())


class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NSGA")
        self.CreateApp()

    def CreateApp(self):
        # Create out grid
        grid = QGridLayout()
        # okna do wpisywania wartoĹ›ci
        Values = QLabel()
        Fun1 = QLineEdit()
        Fun2 = QLineEdit()
        Radius = QLineEdit()
        Alpha = QLineEdit()
        x1_min = QLineEdit()
        x1_max = QLineEdit()
        x2_min = QLineEdit()
        x2_max = QLineEdit()
        x3_min = QLineEdit()
        x3_max = QLineEdit()
        x4_min = QLineEdit()
        x4_max = QLineEdit()
        x5_min = QLineEdit()
        x5_max = QLineEdit()
        lam = QLineEdit()
        lamshare = QLineEdit()
        T = QLineEdit()
        P0 = QLineEdit()
        # string z wartoĹ›ciami do plain textu
        str = ['Funkcja1: ', 'Funkcja2: ', 'x1_min: ', 'x1_max: ', 'x2_min: ', 'x2_max: ', 'x3_min: ', 'x3_max: ',
               'x4_min: ', 'x4_max: ', 'x5_min: ', 'x5_max: ', 'Krzyzowanie', 'Mutacja', 'T', 'Populacja', 'Promien niszy', 'Alpha']
        F1 = PlainText(str[0], 'F1')
        bF1 = Buttons('F1',Values,Fun1)
        # definiowanie pierwszej linii
        grid.addWidget(F1.p, 0, 0, 1, 1)
        grid.addWidget(Fun1, 0, 1, 1, 3)
        grid.addWidget(bF1.b, 0, 4, 1, 1)
        # definiowanie drugiej linii
        F1 = PlainText(str[1], 'F2')
        bF2 = Buttons('F2',Values, Fun2)
        grid.addWidget(F1.p, 1, 0, 1, 1)
        grid.addWidget(Fun2, 1, 1, 1, 3)
        grid.addWidget(bF2.b, 1, 4, 1, 1)
        row = 2
        i = 0
        # dodawanie plain textu do pozostalej czesci
        for text in str[2:]:
            F1 = PlainText(text, text)
            if i%2 == 0:
                grid.addWidget(F1.p, row, 0, 1, 1)
                i+= 1
            else:
                grid.addWidget(F1.p, row, 2, 1, 1)
                row += 1
                i+= 1
        # definiowanie przyciskow do poszczegolnych zmiennych.
        bx1 = Buttons('x1',Values, x1_min, x1_max)
        bx2 = Buttons('x2',Values, x2_min, x2_max)
        bx3 = Buttons('x3',Values, x3_min, x3_max)
        bx4 = Buttons('x4',Values, x4_min, x4_max)
        bx5 = Buttons('x5',Values, x5_min, x5_max)
        blam = Buttons('lam',Values, lam, lamshare)
        bT = Buttons('T',Values, T, P0)
        bRadius = Buttons('Promien', Values, Radius, Alpha)
        # dodawanie okien do wpisywanie tekstu oraz przyciskow do nich przeznaczonych
        grid.addWidget(x1_min, 2, 1, 1, 1)
        grid.addWidget(x1_max, 2, 3, 1, 1)
        grid.addWidget(bx1.b,2,4,1,1)
        grid.addWidget(x2_min, 3, 1, 1, 1)
        grid.addWidget(x2_max, 3, 3, 1, 1)
        grid.addWidget(bx2.b,3,4,1,1)
        grid.addWidget(x3_min, 4, 1, 1, 1)
        grid.addWidget(x3_max, 4, 3, 1, 1)
        grid.addWidget(bx3.b,4,4,1,1)
        grid.addWidget(x4_min, 5, 1, 1, 1)
        grid.addWidget(x4_max, 5, 3, 1, 1)
        grid.addWidget(bx4.b,5,4,1,1)
        grid.addWidget(x5_min, 6, 1, 1, 1)
        grid.addWidget(x5_max, 6, 3, 1, 1)
        grid.addWidget(bx5.b,6,4,1,1)
        grid.addWidget(lam, 7, 1, 1, 1)
        grid.addWidget(lamshare, 7, 3, 1, 1)
        grid.addWidget(blam.b,7,4,1,1)
        grid.addWidget(T, 8, 1, 1, 1)
        grid.addWidget(P0, 8, 3, 1, 1)
        grid.addWidget(bT.b,8,4,1,1)
        grid.addWidget(Radius, 9, 1, 1, 1)
        grid.addWidget(Alpha, 9, 3, 1, 1)
        grid.addWidget(bRadius.b,9,4,1,1)
        # koniec pierwszej kolumny w aplikacji
        #-------------------------------------------------------------------------------------------
        # tekst z poszczegolnymi wartosciami do algorytmu

        grid.addWidget(Values, 0, 5, 5, 4)
        Values.setText(NSGA_values.get_values())
        Rozpocznij = Buttons('NSGA',Values)
        Rysuj = Buttons('Wykres',Values)
        grid.addWidget(Rozpocznij.b, 5,5,1,4)
        grid.addWidget(Rysuj.b, 6, 5, 1, 4)

        #----------------------------------------------------------------------
        # setlayout i jestesmy w domu apka zbudowana
        self.setLayout(grid)

        self.show()


class Index(object):
    global chart
    ind = 20
    value = True
    def next(self, event):
        self.data_preparation()
        self.ind +=1
        i = self.ind % NSGA_values.T
        x,y = data_preparation_for_drawing(NSGA_values.tab_response[i])
        chart.set_xdata(x)
        chart.set_ydata(y)
        plt.suptitle('Przedstawiam pokolenie: ' + str(i+1))
        plt.draw()

    def prev(self, event):
        self.data_preparation()
        self.ind -=1
        i = self.ind % NSGA_values.T
        x,y = data_preparation_for_drawing(NSGA_values.tab_response[i])
        chart.set_xdata(x)
        chart.set_ydata(y)
        plt.suptitle('Przedstawiam pokolenie: ' + str(i+1))
        plt.draw()

    def data_preparation(self):
        if self.value == True:
            self.ind = NSGA_values.T
            self.value = False


def draw_chart():
    global chart
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.2)
    x, y = data_preparation_for_drawing(NSGA_values.tab_response[NSGA_values.T-1])
    chart, = plt.plot(x, y, 'ro')
    plt.suptitle('Przedstawiam pokolenie: ' + str(NSGA_values.T))
    callback = Index()
    axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
    axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
    bnext = Button(axnext, 'Next')
    bnext.on_clicked(callback.next)
    bprev = Button(axprev, 'Previous')
    bprev.on_clicked(callback.prev)
    plt.show()


def data_preparation_for_drawing(tab):
    x = []
    y = []
    for i in tab:
        x.append(i[0])
        y.append(i[1])
    return x,y


def data_preparation_for_presentation(tab):
    x = []
    for i in range(len(tab[0])):
        li = []
        for j in tab:
            li.append(j[i])
        x.append(li)
    return x


def result_presentation(tab1, tab):
    x = PrettyTable()
    Lp = []
    for i in range(len(tab)):
        Lp.append(i+1)
    x.add_column("Lp.", Lp)
    xi = data_preparation_for_presentation(tab)
    fi = data_preparation_for_presentation(tab1)
    for i in range(len(xi)):
        x.add_column("x_"+str(i+1),xi[i])
    for i in range(len(fi)):
        x.add_column("f_"+str(i+1), fi[i])
    plik = open('./wyniki.txt','w+')
    plik.write(str(x))
    plik.close()


if __name__ == "__main__":
    NSGA_values = NSGA_Variable()
    app = QApplication(sys.argv)
    window = Application()
    sys.exit(app.exec_())

