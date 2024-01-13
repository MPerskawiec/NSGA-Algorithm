from population import *
from parsing import *
import numpy
import copy

def NSGA(L_p, L_g, p_c, p_m, alpha_, p_n, tab_lim, string_f1, string_f2):
    #****************************** Parametry do ustawiania w aplikacji *************
    Lp = L_p # liczba populacji
    Lg = L_g # liczba iteracji

    pc = p_c
    pm = p_m

    alpha = alpha_
    pn = p_n


    function_1, n_1 = enter_function(string_f1)
    function_2, n_2 = enter_function(string_f2)
    n = max(n_1, n_2)  # SPRAWDZAMY JAKI MAMY WYMIAR ZADANIA TZN ILE ROZNYCH X JEST DLA X_1+X_2+X_3  n = 3

    P_1 = Population(Lp, n, pc, pm)

    P_1.population_initialization(tab_lim)   # tutaj inicjalizujemy liste odpowiedniej wielkosci

    function_tab_value = np.zeros((Lp, 2), dtype=float)
    tab_xi = []
    generation_tab_value = []

    print("START!!!!!!!!")

    for i in range(0, Lg):
        P_1.adaptation_function_2(n, function_1, function_2, pn, alpha)

        P_1.selection_and_recombination_function2(tab_lim)
        print("petla:  {}".format(i+1))


        tab_pop = P_1.return_population_tab()

        # tutaj jest kod na szukanie ostatecznej populacji niezdominowanej
        function_value(function_1, function_2, n, Lp, tab_pop, function_tab_value)

        C_pom = np.zeros((Lp), dtype=bool)
        hel_var_non_dominated = np.zeros((Lp), dtype=bool)

        for i in range(0, Lp):
            A_pom = function_tab_value[i][0] > function_tab_value[:, 0]
            B_pom = function_tab_value[i][1] > function_tab_value[:, 1]
            C_pom = A_pom*B_pom
            if not (C_pom).any():  # tutaj mamy niezdominowane
                hel_var_non_dominated[i] = True
        generation_tab_value.append(copy.copy(function_tab_value[hel_var_non_dominated]))
    tab_xi = list(tab_pop[hel_var_non_dominated])

    #np.savetxt('test.out', function_tab_value[hel_var_non_dominated], delimiter=';')

    #print("Koniec")
    return generation_tab_value, tab_xi
