# Cornejo Morales Paola
# Henández Martínez Ernesto Ulises

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

# Usar los parámetros:
p = 0.2 #   -p = 0.2
q = 1 #   -q = 1
a = 1.5 #   -a = 1.5
b = 0.8 #   -b = 0.8
max_caminatas = 50 # Realizar 50 iteraciones(caminatas)

def print_matrix(M):
    for i in range(len(M)):
        print(f"{M[i][0]:.3f}\t", f"{M[i][1]:.3f}\t", f"{M[i][2]:.3f}\t", f"{M[i][3]:.3f}\t", f"{M[i][4]:.3f}\t", f"{M[i][5]:.3f}\t")
    print("\n")

def m_visibilidad(MA):
    # Visibilidad de las aristas
    return [[(1/MA[i][j]) if MA[i][j] != 0 else 0 for j in range(len(MA))] for i in range(len(MA))]

def m_feromonas(MA, t_ini = 0.1):
    # La inicialización de las feronomas:
    #   Diferente de 0
    #   Valores positivos y pequeños
    #   Recomendable valores entre 0 y 1
    #   Recomendable todas las aritas con el mismo valor
    # Feromonas de las aristas
    return [[t_ini if MA[i][j] != 0 else 0 for j in range(len(MA))] for i in range(len(MA))]

def ruleta(probabilidades):
    # se genera un número random entre 0 y 1
    r = random.random()

    # las probabilidades ahora pasan a ser probabilidades acumuladas
    acumuladas = []
    suma = 0
    for proba in probabilidades:
        suma += proba # agarramos el valor acumulado
        acumuladas.append(suma)
    # ahora probabilidades tiene las probabilidades acumuladas

    for i, valor in enumerate(acumuladas):
        if r <= valor:
            return i # retornamos el valor del nodo al que debemos de ir

def colonia_hormigas():# colonia_hormigas() devuelve una lista de los caminos encontrados por cada hormiga
    # Recorrido de cada hormiga
    nodos = list(range(6))
    #print(nodos) # DEBUGGING
    c_hormigas = []

    # ciclo por hormiga
    for i in range(len(nodos)):
        nodo_actual = i # es el nodo actual
        l_tabu = [nodo_actual] # guarda los nodos visitados
        hormiga = [nodo_actual] # va a guardar el camino

        while True:
            # se calcula
            probabilidades = []
            nodos_disponibles = [n for n in nodos if n not in l_tabu]

            for nodo_siguiente in nodos_disponibles:
                # Aqui se usa la fórumla de T(i,j)**a * N(i,j)**b
                feromona = MT[nodo_actual][nodo_siguiente] ** a
                visibilidad = MN[nodo_actual][nodo_siguiente] ** b
                probabilidades.append(feromona * visibilidad)

            # Una vez que se tiene a todas las probabilidades, se suman para luego dividir a las probabilidades entre la suma
            suma_probabilidades = sum(probabilidades)
            if suma_probabilidades > 0:
                probabilidades = [proba / suma_probabilidades for proba in probabilidades]
            else:
                probabilidades = [1 / len(nodos_disponibles)] * len(nodos_disponibles)

            # se tiene que elegir el nuevo nodo al que se moverá
            # la elección se hará usando ruleta
            indice = ruleta(probabilidades)
            nodo_siguiente = nodos_disponibles[indice]

            nodo_actual = nodo_siguiente # aqui se asigna el nodo elegido

            l_tabu.append(nodo_actual) # se agrega el nodo a la lista tabú
            hormiga.append(nodo_actual) # guarda el camino
            if len(l_tabu) >= 6: # se sale una vez que todos los nodos han sido visitados
                break
        # Se tiene que regresar al nodo inicial
        hormiga.append(hormiga[0])
        c_hormigas.append(hormiga)

    return c_hormigas

def calcular_distancia(camino, MA):
    distancia = 0
    for i in range(len(camino) - 1):
        distancia += MA[camino[i]][camino[i+1]] # checamos en la matriz de distancias de un punto A -> B
    return distancia

def actualizar_feromonas(caminos, distancias, MT):
    # Evaporación de feromonas
    for i in range(len(MT)):
        for j in range(len(MT[i])):
            MT[i][j] *= (1 - p)
            MT[j][i] *= (1 - p)

    # Añadir feromonas por cada camino
    for camino, distancia in zip(caminos, distancias):
        deposito = q / distancia
        for i in range(len(camino) - 1):
            MT[camino[i]][camino[i+1]] += deposito

def print_caminos(caminos, distancias):
    for i in range(len(caminos)):
        print(caminos[i], " - ", distancias[i])
    print("\n")

def print_HoF(HoF, MA):
    for i in range(len(HoF)):
        print("Gen ", i, " - ", HoF[i], " - ", calcular_distancia(HoF[i], MA))

# Ejecutar algoritmo
mejor_distancia = float('inf') # se inicializa un número muy grande, puesto que queremos minimizar
mejor_camino = None

HoF = [] # Hall of Fame

# Definimos la matriz de distancias
MA = [[0, 6, 9, 17, 13, 21],
      [6, 0, 19, 21, 12, 18],
      [9, 19, 0, 20, 23, 11],
      [17, 21, 20, 0, 15, 10],
      [13, 12, 23, 15, 0, 21],
      [21, 18, 11, 10, 21, 0]
]
print("Matriz de distancias \n")
print_matrix(MA) # DEBUGGING

MN = m_visibilidad(MA)
print("Matriz de visibilidad \n")
print_matrix(MN) # DEBBUGING

MT = m_feromonas(MA, t_ini=0.1)
print("Matriz de feromonas \n")
print_matrix(MT) # DEBUGGING

for i in range(max_caminatas): # se detiene al alcanzar las maximas caminatas dadas
    print("Caminos encontrados en caminata", i,"\n")
    caminos = colonia_hormigas()
    distancias = [calcular_distancia(camino, MA) for camino in caminos]
    print_caminos(caminos, distancias)

    actualizar_feromonas(caminos, distancias, MT)
    print("Matriz de feromonas \n")
    print_matrix(MT) # DEBUGGING

    # Guardar mejor solución
    min_dist = min(distancias)
    mejor_camino = caminos[distancias.index(min_dist)]
    HoF.append(mejor_camino)
    if min_dist <= mejor_distancia:
        mejor_distancia = min_dist
        gbest_camino = caminos[distancias.index(min_dist)]

print("Mejor camino encontrado: ", gbest_camino, " - ", mejor_distancia)
print("\nHall of Fame")
print_HoF(HoF, MA)