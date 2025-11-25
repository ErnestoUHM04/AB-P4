# Cornejo Morales Paola
# Henández Martínez Ernesto Ulises

import numpy as np
import random

# Hormigas

# 6 nodos
# 6 ciudades
# Se tiene que encontrar la ruta más corta para recorrer 6 ciudades y regresar a la ciudad de partida - Algoritmo de colonia de hormigas (ACO)
# Con base a la siguiente matriz que representa al grafo
#       1   2   3   4   5   6
#    --------------------------
# 1 |   0   6   9   17  13  21
# 2 |   6   0   19  21  12  18
# 3 |   9   19  0   20  23  11
# 4 |   17  21  20  0   15  10
# 5 |   13  12  23  15  0   21
# 6 |   21  18  11  10  21  0

def print_matrix(M):
    for i in range(len(MA)):
        print(f"{M[i][0]:.3f}\t", f"{M[i][1]:.3f}\t", f"{M[i][2]:.3f}\t", f"{M[i][3]:.3f}\t", f"{M[i][4]:.3f}\t", f"{M[i][5]:.3f}\t")
    print("\n")

MA = [[0, 6, 9, 17, 13, 21],
      [6, 0, 19, 21, 12, 18],
      [9, 19, 0, 20, 23, 11],
      [17, 21, 20, 0, 15, 10],
      [13, 12, 23, 15, 0, 21],
      [21, 18, 11, 10, 21, 0]
]
print_matrix(MA)

# Visibilidad de las aristas
MN = [[(1/MA[i][j]) if MA[i][j] != 0 else 0 for j in range(len(MA))] for i in range(len(MA))]
print_matrix(MN)

"""
# Same but with NumPy
MA_np = np.array(MA, dtype=float)
with np.errstate(divide='ignore', invalid='ignore'):
    MN_np = np.where(MA_np != 0, 1.0 / MA_np, 0.0)
MN = MN_np.tolist()
print(MN, "\n")
"""
# La inicialización de las feronomas:
#   Diferente de 0
#   Valores positivos y pequeños
#   Recomendable valores entre 0 y 1
#   Recomendable todas las aritas con el mismo valor
t_ini = 0.1
# Feromonas de las aristas
MT = [[t_ini if MA[i][j] != 0 else 0 for j in range(len(MA))] for i in range(len(MA))]
print_matrix(MT)

# Usar los parámetros:
#   -p = 0.2
p = 0.2
#   -q = 1
q = 1
#   -a = 1.5
a = 1.5
#   -b = 0.8
b = 0.8

# Realizar 50 iteraciones(caminatas)
max_caminatas = 50

def ruleta():

    return

def colonia_hormigas(n_nodes):
    # hormigas será la lista de hormigas, donde cada hormiga lleva consigo un camino
    hormigas = []
    for i in range(n_nodes):
        # Usar 1 hormiga por cada nodo, todas las ciudades deben de ser visitadas por las hormigas y cada hormiga debe regresar al nodo de donde salió
        nodo_actual = str(i+1)
        hormiga = nodo_actual + "->"
        l_tabu = [nodo_actual]
        print(l_tabu) # THIS IS FOR DEBBUGING

        while True:
            # Usar ruleta para la selección de a que nodo se mueve la hormiga.
            ruleta()
            break

        hormiga = hormiga + str(i+1)

        hormigas.append(hormiga)
    return hormigas

hormigas = colonia_hormigas(len(MA))
print(hormigas)