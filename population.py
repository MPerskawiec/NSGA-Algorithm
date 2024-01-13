import random
from parsing import *
import math
import copy
import numpy as np

NUMBER_RANGE = 12  # liczba z przedzialu od 2^-30 do 2^30


class Population:

    def __init__(self, lp, n, pc, pm):

        self.Lp = lp
        self.N = n
        self.pc = pc
        self.pm = pm

        self.tab_population = np.zeros((self.Lp, self.N), dtype=float)
        self.tab_function_value = np.zeros((self.Lp, 2), dtype=float)
        self.tab_adaptation_value = np.zeros((self.Lp), dtype=float)

        self.tab_help_population = np.zeros((self.Lp, self.N), dtype=float)

    def return_population_tab(self):
        return self.tab_population

    def population_initialization(self, tab_lim):
        if self.N == 1:
            for i in range(0, self.Lp):
                for j in range(0, self.N):
                    self.tab_population[i][j] = random.uniform(tab_lim[j][0], tab_lim[j][1])

        elif self.N == 2:
            for i in range(0, self.Lp):
                for j in range(0, self.N):
                    self.tab_population[i][j] = random.uniform(tab_lim[j][0], tab_lim[j][1])

        elif self.N == 3:
            for i in range(0, self.Lp):
                for j in range(0, self.N):
                    self.tab_population[i][j] = random.uniform(tab_lim[j][0], tab_lim[j][1])

        elif self.N == 4:
            for i in range(0, self.Lp):
                for j in range(0, self.N):
                    self.tab_population[i][j] = random.uniform(tab_lim[j][0], tab_lim[j][1])

        elif self.N == 5:
            for i in range(0, self.Lp):
                for j in range(0, self.N):
                    self.tab_population[i][j] = random.uniform(tab_lim[j][0], tab_lim[j][1])

        elif self.N == 30:
            for i in range(0, self.Lp):
                for j in range(0, self.N):
                    self.tab_population[i][j] = random.uniform(tab_lim[j][0], tab_lim[j][1])

    def count_function_value(self, n, funkcja_1, funkcja_2):
        if self.N == 1:
            for i in range(0, self.Lp):
                self.tab_function_value[i][0] = function_value(funkcja_1, self.tab_population[i][0])
                self.tab_function_value[i][1] = function_value(funkcja_2, self.tab_population[i][0])
        elif self.N == 2:
            for i in range(0, self.Lp):
                self.tab_function_value[i][0] = function_value(funkcja_1, self.tab_population[i][0],
                                                               self.tab_population[i][1])
                self.tab_function_value[i][1] = function_value(funkcja_2, self.tab_population[i][0],
                                                               self.tab_population[i][1])
        elif self.N == 3:
            for i in range(0, self.Lp):
                self.tab_function_value[i][0] = function_value(funkcja_1, self.tab_population[i][0],
                                                               self.tab_population[i][1],
                                                               self.tab_population[i][2])
                self.tab_function_value[i][1] = function_value(funkcja_2, self.tab_population[i][0],
                                                               self.tab_population[i][1],
                                                               self.tab_population[i][2])
        elif self.N == 4:
            for i in range(0, self.Lp):
                self.tab_function_value[i][0] = function_value(funkcja_1, self.tab_population[i][0],
                                                               self.tab_population[i][1],
                                                               self.tab_population[i][2],
                                                               self.tab_population[i][3])
                self.tab_function_value[i][1] = function_value(funkcja_2, self.tab_population[i][0],
                                                               self.tab_population[i][1],
                                                               self.tab_population[i][2],
                                                               self.tab_population[i][3])
        elif self.N == 5:
            for i in range(0, self.Lp):
                self.tab_function_value[i][0] = function_value(funkcja_1, self.tab_population[i][0],
                                                               self.tab_population[i][1],
                                                               self.tab_population[i][2],
                                                               self.tab_population[i][3],
                                                               self.tab_population[i][4])
                self.tab_function_value[i][1] = function_value(funkcja_2, self.tab_population[i][0],
                                                               self.tab_population[i][1],
                                                               self.tab_population[i][2],
                                                               self.tab_population[i][3],
                                                               self.tab_population[i][4])

    def test_population_initialization(self):

        self.tab_population[0][0] = -1.0
        self.tab_population[1][0] = -0.8
        self.tab_population[2][0] = -0.6
        self.tab_population[3][0] = -0.4
        self.tab_population[4][0] = -0.2
        self.tab_population[5][0] = 0.0
        self.tab_population[6][0] = 0.2
        self.tab_population[7][0] = 0.4
        self.tab_population[8][0] = 0.6
        self.tab_population[9][0] = 0.8
        self.tab_population[10][0] = 1.0
        self.tab_population[11][0] = 1.2
        self.tab_population[12][0] = 1.4
        self.tab_population[13][0] = 1.6
        self.tab_population[14][0] = 1.8
        self.tab_population[15][0] = 2.0
        self.tab_population[16][0] = 2.2
        self.tab_population[17][0] = 2.4
        self.tab_population[18][0] = 2.6
        self.tab_population[19][0] = 2.8

    def print_population(self):
        print(self.tab_population)
        # print(self.tab_function_value)

    # Funkcji przekazujemy chromosm, ktora nastepnie w zaleznosci od miejsca podzialu zwroci wartosc ktora
    # w operacji krzyzowania zostanie podmieniona na inna z drugiego chromosomu
    def get_result(self, value_, division_place):
        result = value_  # ZWRACA wartosc za podzialem np101|001 zwraca 001 tylko w zapisie dziesietnym

        if value_ >= 0:  # jezeli chromosom jest dodatni lub zerowy
            for i in range(-NUMBER_RANGE, NUMBER_RANGE + 1 - division_place):
                j = -i
                if pow(2, j) <= result:
                    result = result - pow(2, j)
        else:
            for i in range(-NUMBER_RANGE, NUMBER_RANGE + 1 - division_place):
                j = -i
                if -pow(2, j) > result:
                    result = result + pow(2, j)

        return result

    def cross_function(self, chromosom_a, chromosom_b):

        # losujemy miejsce podzialu - 0 oznacza maksymalnie z prawej strony, wartosc maksymalna maksymalnie z lewej
        # czyli w tym przypadku liczby zostana calkowicie zamienione
        division_place = random.randrange(0, 2 * NUMBER_RANGE)
        # print("mijesce podzialu: {}".format(miejesce_podzialu))

        part_a = self.get_result(chromosom_a, division_place)
        part_b = self.get_result(chromosom_b, division_place)

        # Jezeli chromosomy maja dwa ruzne znaki potrzeba innego wzoru dlatego te warunki if/else
        if (chromosom_a >= 0 and chromosom_b >= 0) or (
                chromosom_a < 0 and chromosom_b < 0):  # dla dwoch dodatnich dziala perfect
            nowy_chromosm_a = chromosom_a - part_a + part_b  # dla dwoch ujemnych rowniez
            nowy_chromosm_b = chromosom_b - part_b + part_a

        else:  # jezeli dwa chromosomy o roznych znakach
            # potrzebny gdy krzyzujemy liczbe dodatnia z liczba ujemna
            wspolczynnik = pow(2, division_place - NUMBER_RANGE)
            # print("Wspolczynnik: {}".format(wspolczynnik))

            if chromosom_a < 0:  # jest roznica we wzorze nizej dla chromosomu ujemnego i dodatniego
                znak = 1
            else:
                znak = -1

            nowy_chromosm_a = chromosom_a - part_a - znak * wspolczynnik + part_b  # ujemny
            nowy_chromosm_b = chromosom_b - part_b + znak * wspolczynnik + part_a  # dodatni

        return nowy_chromosm_a, nowy_chromosm_b

    def mutation(self, chromosom):

        nowy_chromosom = chromosom

        if random.uniform(0,
                          1) <= self.pm:
            # print("zachodzi mutation - zmiana znaku!!!")
            if chromosom >= 0:
                nowy_chromosom = chromosom - pow(2, NUMBER_RANGE)
            else:
                nowy_chromosom = chromosom + pow(2, NUMBER_RANGE)

        pom = nowy_chromosom
        if nowy_chromosom >= 0:
            # print("dodatni chromosom")

            for i in range(-NUMBER_RANGE + 1, NUMBER_RANGE + 1):
                j = -i
                if pow(2, j) <= pom:
                    pom = pom - pow(2, j)
                    if random.uniform(0, 1) <= self.pm:
                        # print("tutaj sie dzieje1 {}".format(j))
                        nowy_chromosom = nowy_chromosom - pow(2, j)
                else:
                    if random.uniform(0, 1) <= self.pm:
                        # print("tutaj sie dzieje2 {}".format(j))
                        nowy_chromosom = nowy_chromosom + pow(2, j)

        else:
            # print("ujemny chromosom")

            for i in range(-NUMBER_RANGE + 1, NUMBER_RANGE + 1):
                j = -i
                if -pow(2, j) > pom:
                    pom = pom + pow(2, j)
                    if random.uniform(0, 1) <= self.pm:
                        # print("tutaj sie dzieje ujemne 1 {}".format(j))
                        nowy_chromosom = nowy_chromosom + pow(2, j)
                else:
                    if random.uniform(0, 1) <= self.pm:
                        # print("tutaj sie dzieje ujemne 2 {}".format(j))
                        nowy_chromosom = nowy_chromosom - pow(2, j)

        return nowy_chromosom

    def adaptation_function_2(self, n, fun_1, fun_2, pn_, alpha):
        Fd = self.Lp
        Fd_pom = 9999999;

        function_value(fun_1, fun_2, self.N, self.Lp, self.tab_population, self.tab_function_value)

        pom = np.ones((self.Lp), dtype=bool)
        hel_var_non_dominated = np.zeros((self.Lp), dtype=bool)

        # print(self.tab_population)
        while (len(self.tab_population[pom])):
            id = np.where(pom)
            id = np.transpose(id)
            # print(id)
            for i in id:
                i = int(i)  # musi to byĂ„â€ˇ bo inaczej nizej zamiast podstawic 1 element podstawia caly wektor
                A_pom = self.tab_function_value[i][0] > self.tab_function_value[pom, 0]
                B_pom = self.tab_function_value[i][1] > self.tab_function_value[pom, 1]
                C_pom = A_pom * B_pom
                if not (C_pom).any():  # tutaj mamy niezdominowane
                    hel_var_non_dominated[i] = True

            pom[hel_var_non_dominated] = False  # Od calej populacji odejmujemy osobniki niezdominowane

            nb = np.where(hel_var_non_dominated)
            nb = np.transpose(nb)

            # print(self.tab_function_value[hel_var_non_dominated])

            for i in nb:
                i = int(i)
                a = self.tab_function_value[i][0] - self.tab_function_value[hel_var_non_dominated, 0]
                b = self.tab_function_value[i][1] - self.tab_function_value[hel_var_non_dominated, 1]
                a = a * a
                b = b * b
                c = (a + b) ** 0.5
                # print(c)
                d = c < pn_
                # print(d)
                e = 1 - (c[d] / pn_) ** alpha
                # print(e)
                sd = sum(e)
                f = float(Fd / (sd + 1))
                self.tab_adaptation_value[i] = f
                Fd_pom = min(Fd_pom, f)  # szukamy najmniejszej wartosci przystosowania z danego zbioru

            Fd = 0.90 * Fd_pom
            # print(self.tab_adaptation_value)

            hel_var_non_dominated[hel_var_non_dominated] = False

    def selection_and_recombination_function2(self, tab_lim):
        # ************* tutaj metoda kola ruletki
        denominator = sum(self.tab_adaptation_value)
        sum_ = 0.0
        for i in range(0, len(self.tab_adaptation_value)):
            sum_ += self.tab_adaptation_value[i]
            self.tab_adaptation_value[i] = sum_ / denominator

        number_a = 0
        number_b = 0
        counter = 0
        pom = [0 for col in range(self.N)]

        for i in range(0, int((self.Lp) / 2)):
            draw_1 = random.random()
            draw_2 = random.random()
            for j in range(0, len(self.tab_adaptation_value)):  # szukamy pierwszej liczny
                if draw_1 <= self.tab_adaptation_value[j]:
                    number_a = copy.deepcopy(self.tab_population[j])
                    break
            for j in range(0, len(self.tab_adaptation_value)):  # szukamy pierwszej liczny
                if draw_2 <= self.tab_adaptation_value[j]:
                    number_b = copy.deepcopy(self.tab_population[j])
                    break
            # print("Liczba a : {}".format(number_a))
            # print("Liczba b : {}".format(number_b))

            if (random.random() <= self.pc):  # prawdopodobienstwo mniejsze od krzyzowania wiec dzialamy
                # print("cross_function")
                r = random.randrange(0, self.N)  # r jesy to miejsce krzyzowania np mamy w funkcji x1 x2 x3
                # r == 1   to  x1 zostaje stare x2 krzyzujemy x3 przepisujemy od 2 liczby
                # print("miejsce krzyzowania liczby to: {}".format(r))
                number_a[r], number_b[r] = self.cross_function(number_a[r], number_b[r])

                for i in range(r + 1, self.N):  # tutaj zamieniamy reszte  rownania jak miejsce krzyzowania bedzie x1

                    pom[i] = number_a[i];
                    number_a[i] = number_b[i]
                    number_b[i] = pom[i]

            for p in range(0, self.N):
                number_a[p] = self.mutation(number_a[p])
                number_b[p] = self.mutation(number_b[p])
                if number_a[p] < tab_lim[p][0]:
                    number_a[p] = tab_lim[p][0]
                if number_a[p] > tab_lim[p][1]:
                    number_a[p] = tab_lim[p][1]

                if number_b[p] < tab_lim[p][0]:
                    number_b[p] = tab_lim[p][0]
                if number_b[p] > tab_lim[p][1]:
                    number_b[p] = tab_lim[p][1]

            # print("nowa Liczba a po mutacji: {}".format(number_a))
            # print("nowa Liczba b po mutacji: {}".format(number_b))

            self.tab_help_population[counter] = number_a
            counter += 1
            self.tab_help_population[counter] = number_b
            counter += 1

        # print(self.tab_population)
        self.tab_population = self.tab_help_population
        # print(self.tab_population)


