from sympy import symbols, lambdify
import copy
import numpy as np
from sympy.parsing.sympy_parser import (parse_expr,
standard_transformations, implicit_multiplication_application)
x_1, x_2, x_3, x_4, x_5 = symbols('x_1, x_2, x_3, x_4, x_5')    #inicjalizuje wykorzystywane symbole
x_6, x_7, x_8, x_9, x_10 = symbols('x_6, x_7, x_8, x_9, x_10')    #inicjalizuje wykorzystywane symbole
x_11, x_12, x_13, x_14, x_15 = symbols('x_11, x_12, x_13, x_14, x_15')    #inicjalizuje wykorzystywane symbole
x_16, x_17, x_18, x_19, x_20 = symbols('x_16, x_17, x_18, x_19, x_20')    #inicjalizuje wykorzystywane symbole
x_21, x_22, x_23, x_24, x_25 = symbols('x_21, x_22, x_23, x_24, x_25')    #inicjalizuje wykorzystywane symbole
x_26, x_27, x_28, x_29, x_30 = symbols('x_26, x_27, x_28, x_29, x_30')    #inicjalizuje wykorzystywane symbole

                                          # oddanie wyniku w formacie float  """


def enter_function(string):

   #  print("sprawdzamy ile x w funckji")
    n = 0
    if (string.count("x_30")):
        n = 30
    elif(string.count("x_5")):
        n = 5
        print("n===5")
    elif (string.count("x_4")):
        n = 4
    elif (string.count("x_3")):
        n = 3
    elif (string.count("x_2")):
        n = 2
    elif (string.count("x_1")):
        n = 1

    string = string.lstrip()
    string = string.replace('^','**')
    print("wprowadzona funkcja: {}".format(string))
    readed_function = parse_expr(string,transformations=(standard_transformations +
                                       (implicit_multiplication_application,)))  #parsowanie
    print("odczytana funkcja: {}".format(readed_function))
    return readed_function, n


def function_value(funkcja1, funkcja2,N, Lp, tab_population, tab_function_value):
    if N == 1:
        fun_1 = lambdify([x_1], funkcja1, 'numpy')
        fun_2 = lambdify([x_1], funkcja2, 'numpy')

        tab_function_value[:, 0] = fun_1(tab_population[:, 0])
        tab_function_value[:, 1] = fun_2(tab_population[:, 0])

    elif N == 2:
        fun_1 = lambdify([x_1, x_2], funkcja1, 'numpy')
        fun_2 = lambdify([x_1, x_2], funkcja2, 'numpy')
        tab_function_value[:, 0] = fun_1(tab_population[:, 0], tab_population[:, 1])
        tab_function_value[:, 1] = fun_2(tab_population[:, 0], tab_population[:, 1])

    elif N == 3:
        fun_1 = lambdify([x_1, x_2, x_3], funkcja1, 'numpy')
        fun_2 = lambdify([x_1, x_2, x_3], funkcja2, 'numpy')
        tab_function_value[:, 0] = fun_1(tab_population[:, 0], tab_population[:, 1], tab_population[:, 2])
        tab_function_value[:, 1] = fun_2(tab_population[:, 0], tab_population[:, 1], tab_population[:, 2])

    elif N == 4:
        fun_1 = lambdify([x_1, x_2, x_3, x_4], funkcja1, 'numpy')
        fun_2 = lambdify([x_1, x_2, x_3, x_4], funkcja2, 'numpy')
        tab_function_value[:, 0] = fun_1(tab_population[:, 0], tab_population[:, 1], tab_population[:, 2],
                                           tab_population[:, 3])
        tab_function_value[:, 1] = fun_2(tab_population[:, 0], tab_population[:, 1], tab_population[:, 2],
                                           tab_population[:, 3])
    elif N == 5:
        fun_1 = lambdify([x_1, x_2, x_3, x_4, x_5], funkcja1, 'numpy')
        fun_2 = lambdify([x_1, x_2, x_3, x_4, x_5], funkcja2, 'numpy')
        tab_function_value[:, 0] = fun_1(tab_population[:, 0], tab_population[:, 1], tab_population[:, 2],
                                           tab_population[:, 3], tab_population[:, 4])
        tab_function_value[:, 1] = fun_2(tab_population[:, 0], tab_population[:, 1], tab_population[:, 2],
                                           tab_population[:, 3], tab_population[:, 4])


    elif N == 30:
        fun_1 = lambdify([x_1, x_2, x_3, x_4, x_5, x_6, x_7, x_8, x_9, x_10,
                          x_11, x_12, x_13, x_14, x_15, x_16, x_17, x_18, x_19, x_20,
                          x_21, x_22, x_23, x_24, x_25, x_26, x_27, x_28, x_29, x_30], funkcja1, 'numpy')

        fun_2 = lambdify([x_1, x_2, x_3, x_4, x_5, x_6, x_7, x_8, x_9, x_10,
                          x_11, x_12, x_13, x_14, x_15, x_16, x_17, x_18, x_19, x_20,
                          x_21, x_22, x_23, x_24, x_25, x_26, x_27, x_28, x_29, x_30], funkcja2, 'numpy')

        tab_function_value[:, 0] = fun_1(tab_population[:, 0], tab_population[:, 1], tab_population[:, 2],
                                           tab_population[:, 3], tab_population[:, 4], tab_population[:, 5],
                                           tab_population[:, 6], tab_population[:, 7], tab_population[:, 8],
                                           tab_population[:, 9], tab_population[:, 10], tab_population[:, 11],
                                           tab_population[:, 12], tab_population[:, 13], tab_population[:, 14],
                                           tab_population[:, 15], tab_population[:, 16], tab_population[:, 17],
                                           tab_population[:, 18], tab_population[:, 19], tab_population[:, 20],
                                           tab_population[:, 21], tab_population[:, 22], tab_population[:, 23],
                                           tab_population[:, 24], tab_population[:, 25], tab_population[:, 26],
                                           tab_population[:, 27], tab_population[:, 28], tab_population[:, 29])

        tab_function_value[:, 1] = fun_2(tab_population[:, 0], tab_population[:, 1], tab_population[:, 2],
                                           tab_population[:, 3], tab_population[:, 4], tab_population[:, 5],
                                           tab_population[:, 6], tab_population[:, 7], tab_population[:, 8],
                                           tab_population[:, 9], tab_population[:, 10], tab_population[:, 11],
                                           tab_population[:, 12], tab_population[:, 13], tab_population[:, 14],
                                           tab_population[:, 15], tab_population[:, 16], tab_population[:, 17],
                                           tab_population[:, 18], tab_population[:, 19], tab_population[:, 20],
                                           tab_population[:, 21], tab_population[:, 22], tab_population[:, 23],
                                           tab_population[:, 24], tab_population[:, 25], tab_population[:, 26],
                                           tab_population[:, 27], tab_population[:, 28], tab_population[:, 29])

# funkcja_1 = enter_function()
# wynik_1 = function_value(funkcja_1,1,2,3,4,5)

#print(wynik_1)