import random
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt

# V =  [(1,2), (1,5), (1,8), (1,3), (1,4), (1,6), (2,6), (2,9), (3,6), (3,8)]
# V = [(1,2),(1,4),(2,3),(4,5),(9,1)]

#|V|=125
V = [
    (5, 1),
    (6, 2),
    (8, 4),
    (9, 4),
    (9, 6),
    (11, 2),
    (13, 5),
    (14, 7),
    (14, 9),
    (14, 13),
    (15, 8),
    (16,10),
    (16,12),
    (17,2),
    (18,12),
    (19,5),
    (19,8),
    (19,11),
    (21,7),
    (21,8),
    (22,17),
    (23,13),
    (24,21),
    (25,3),
    (25,10),
    (27,2),
    (27,6),
    (28,9),
    (28,17),
    (28,19),
    (29,1),
    (29,24),
    (30,5),
    (30,15),
    (30,28),
    (31,10),
    (31,27),
    (32,2),
    (32,11),
    (34,12),
    (34,32),
    (35,3),
    (35,5),
    (35,12),
    (35,15),
    (36,20),
    (36,27),
    (36,35),
    (37,13),
    (37,22),
    (38,3),
    (38,4),
    (38,6),
    (38,17),
    (39,26),
    (40,2),
    (40,37),
    (41,3),
    (41,7),
    (41,16),
    (41,22),
    (41,35),
    (42,6),
    (42,7),
    (42,8),
    (42,12),
    (42,19),
    (42,25),
    (43,29),
    (43,33),
    (43,35),
    (44,1),
    (44,34),
    (45,16),
    (45,24),
    (46,2),
    (46,10),
    (46,25),
    (46,26),
    (46,36),
    (47,12),
    (47,20),
    (47,30),
    (47,36),
    (47,46),
    (48,19),
    (48,24),
    (49,9),
    (49,37),
    (49,43),
    (50,22),
    (50,23),
    (50,41),
    (50,47),
    (51,40),
    (51,41),
    (51,42),
    (51,44),
    (51,45),
    (51,47),
    (51,48),
    (51,50),
    (52,3),
    (52,4),
    (52,5),
    (52,9),
    (52,15),
    (55,28),
    (55,29),
    (55,30),
    (55,37),
    (55,38),
    (55,41),
    (55,46),
    (57,47),
    (58,54),
    (58,56),
    (59,3),
    (59,4),
    (59,5),
    (59,9),
    (59,11),
    (59,35),
    (59,37),
    (60,36)
    ]

# |V|= 600
#V = [
#     (2,1),
#     (3,2),
#     (5,2),
#     (5,4),
#     (6,1),
#     (6,2),
#     (7,1),
#     (7,3),
#     (7,4),
#     (8,1),
#     (8,2),
#     (8,3),
#     (8,6),
#     (8,7),
#     (9,2),
#     (9,3),
#     (9,5),
#     (9,7),
#     (10,2),
#     (10,3),
#     (10,4),
#     (10,6),
#     (10,7),
#     (10,9),
#     (11,1),
#     (11,3),
#     (11,9),
#     (12,2),
#     (12,3),
#     (12,4),
#     (12,5),
#     (12,6),
#     (12,8),
#     (12,10),
#     (12,11),
#     (13,1),
#     (13,2),
#     (13,4),
#     (13,5),
#     (13,7),
#     (13,8),
#     (13,9),
#     (13,10),
#     (13,11),
#     (13,12),
#     (14,1),
#     (14,2),
#     (14,4),
#     (14,5),
#     (14,6),
#     (14,8),
#     (14,10),
#     (15,1),
#     (15,3),
#     (15,8),
#     (15,9),
#     (15,10),
#     (15,11),
#     (15,12),
#     (15,13),
#     (16,3),
#     (16,4),
#     (16,7),
#     (16,8),
#     (16,10),
#     (16,11),
#     (16,12),
#     (16,14),
#     (16,15),
#     (17,4),
#     (17,5),
#     (17,6),
#     (17,7),
#     (17,11),
#     (17,13),
#     (17,15),
#     (17,16),
#     (18,4),
#     (18,7),
#     (18,8),
#     (18,9),
#     (18,14),
#     (18,16),
#     (18,17),
#     (19,2),
#     (19,6),
#     (19,7),
#     (19,12),
#     (19,18),
#     (20,1),
#     (20,2),
#     (20,3),
#     (20,4),
#     (20,10),
#     (20,12),
#     (20,13),
#     (20,14),
#     (21,2),
#     (21,7),
#     (21,10),
#     (21,11),
#     (21,12),
#     (21,13),
#     (21,14),
#     (21,16),
#     (21,17),
#     (21,18),
#     (22,1),
#     (22,2),
#     (22,7),
#     (22,8),
#     (22,11),
#     (22,13),
#     (22,14),
#     (22,16),
#     (22,17),
#     (22,18),
#     (23,1),
#     (23,2),
#     (25,9),
#     (25,11),
#     (25,16),
#     (25,17),
#     (25,19),
#     (27,13),
#     (27,18),
#     (27,19),
#     (27,20),
#     (27,21),
#     (28,1),
#     (29,7),
#     (29,8),
#     (29,9),
#     (30,1),
#     (30,2),
#     (30,4),
#     (30,5),
#     (30,6),
#     (30,7),
#     (30,9),
#     (30,10),
#     (30,11),
#     (30,13),
#     (30,17),
#     (30,19),
#     (30,20),
#     (31,1),
#     (31,6),
#     (31,7),
#     (31,11),
#     (31,12),
#     (35,30),
#     (35,31),
#     (35,33),
#     (35,34),
#     (36,2),
#     (36,3),
#     (36,18),
#     (36,20),
#     (37,27),
#     (37,28),
#     (37,29),
#     (37,33),
#     (37,35),
#     (38,4),
#     (38,5),
#     (38,7),
#     (38,8),
#     (38,10),
#     (38,12),
#     (38,16),
#     (38,17),
#     (38,18),
#     (38,19),
#     (38,20),
#     (38,21),
#     (39,16),
#     (43,11),
#     (43,12),
#     (43,14),
#     (43,16),
#     (43,20),
#     (43,22),
#     (43,25),
#     (43,27),
#     (43,30),
#     (43,32),
#     (43,34),
#     (43,35),
#     (43,36),
#     (44,42),
#     (44,43),
#     (45,1),
#     (45,2),
#     (45,7),
#     (45,8),
#     (45,9),
#     (45,10),
#     (45,11),
#     (45,12),
#     (45,13),
#     (45,18),
#     (45,19),
#     (46,3),
#     (46,4),
#     (46,5),
#     (46,8),
#     (46,9),
#     (46,11),
#     (46,13),
#     (46,14),
#     (46,15),
#     (46,16),
#     (46,17),
#     (46,20),
#     (46,22),
#     (46,23),
#     (46,24),
#     (47,2),
#     (47,4),
#     (47,6),
#     (47,8),
#     (47,9),
#     (47,12),
#     (48,21),
#     (48,22),
#     (48,23),
#     (48,41),
#     (48,42),
#     (48,43),
#     (48,45),
#     (49,1),
#     (49,2),
#     (49,3),
#     (49,4),
#     (49,9),
#     (49,34),
#     (49,36),
#     (49,37),
#     (49,38),
#     (49,40),
#     (49,42),
#     (49,46),
#     (50,1),
#     (50,3),
#     (50,6),
#     (50,8),
#     (50,9),
#     (50,11),
#     (51,40),
#     (51,41),
#     (51,42),
#     (51,44),
#     (51,45),
#     (51,47),
#     (51,48),
#     (51,50),
#     (52,3),
#     (52,4),
#     (52,5),
#     (52,9),
#     (52,15),
#     (55,28),
#     (55,29),
#     (55,30),
#     (55,37),
#     (55,38),
#     (55,41),
#     (55,46),
#     (57,47),
#     (58,54),
#     (58,56),
#     (59,3),
#     (59,4),
#     (59,5),
#     (59,9),
#     (59,11),
#     (59,13),
#     (59,14),
#     (59,16),
#     (59,17),
#     (59,20),
#     (59,22),
#     (59,25),
#     (59,29),
#     (59,30),
#     (59,31),
#     (59,33),
#     (59,35),
#     (59,37),
#     (59,46),
#     (59,47),
#     (59,48),
#     (59,53),
#     (59,54),
#     (59,58),
#     (60,1),
#     (60,36),
#     (62,38),
#     (62,39),
#     (62,40),
#     (62,42),
#     (62,43),
#     (62,44),
#     (62,51),
#     (63,15),
#     (63,17),
#     (63,18),
#     (63,20),
#     (63,21),
#     (63,57),
#     (63,58),
#     (64, 43),
#     (64, 45),
#     (64, 46),
#     (64, 51),
#     (64, 52),
#     (65, 37),
#     (66, 15),
#     (66, 16),
#     (66, 18),
#     (66, 22),
#     (66, 28),
#     (66, 30),
#     (67, 3),
#     (67, 4),
#     (68, 11),
#     (68, 12),
#     (68, 13),
#     (68, 65),
#     (69, 1),
#     (69, 2),
#     (69, 3),
#     (69, 4),
#     (69, 5),
#     (69, 42),
#     (69, 43),
#     (69, 45),
#     (69, 47),
#     (69, 68),
#     (70, 1),
#     (70, 2),
#     (70, 3),
#     (70, 5),
#     (70, 6),
#     (70, 7),
#     (70, 8),
#     (70, 10),
#     (70, 11),
#     (70, 13),
#     (70, 14),
#     (70, 15),
#     (70, 18),
#     (70, 21),
#     (73, 31),
#     (73, 32),
#     (73, 33),
#     (73, 34),
#     (73, 35),
#     (73, 37),
#     (73, 38),
#     (73, 40),
#     (73, 55),
#     (73, 57),
#     (73, 60),
#     (73, 64),
#     (73, 65),
#     (73, 67),
#     (73, 68),
#     (73, 69),
#     (73, 70),
#     (73, 71),
#     (73, 72),
#     (74, 1),
#     (74, 3),
#     (74, 5),
#     (74, 7),
#     (74, 10),
#     (74, 11),
#     (74, 13),
#     (74, 14),
#     (74, 16),
#     (74, 26),
#     (74, 27),
#     (74, 29),
#     (74, 31),
#     (74, 32),
#     (75, 18),
#     (75, 22),
#     (75, 27),
#     (75, 28),
#     (75, 30),
#     (75, 34),
#     (75, 36),
#     (75, 38),
#     (75, 39),
#     (75, 71),
#     (75, 74),
#     (76, 1),
#     (76, 37),
#     (76, 40),
#     (77,61),
#     (77,62),
#     (77,63),
#     (77,68),
#     (77,69),
#     (77,70),
#     (77,73),
#     (78,1),
#     (78,3),
#     (78,5),
#     (78,8),
#     (78,10),
#     (78,11),
#     (78,12),
#     (78,14),
#     (78,15),
#     (78,16),
#     (78,17),
#     (78,18),
#     (80,54),
#     (80,57),
#     (80,63),
#     (80,67),
#     (80,68),
#     (80,70),
#     (80,71),
#     (80,72),
#     (80,73),
#     (82,18),
#     (82,21),
#     (82,22),
#     (82,23),
#     (82,24),
#     (82,26),
#     (82,30),
#     (82,80),
#     (83,1),
#     (83,2),
#     (83,5),
#     (83,9),
#     (83,10),
#     (83,13),
#     (83,78),
#     (83,79),
#     (84,3),
#     (84,5),
#     (84,7),
#     (84,8),
#     (84,10),
#     (84,12),
#     (84,14),
#     (84,15),
#     (84,18),
#     (84,19),
#     (84,62),
#     (84,63),
#     (84,67),
#     (84,68),
#     (84,72),
#     (84,74),
#     (84,75),
#     (84,76),
#     (84,77),
#     (84,80),
#     (86,53),
#     (86,55),
#     (86,56),
#     (86,57),
#     (86,59),
#     (86,62),
#     (86,64),
#     (86,65),
#     (86,67),
#     (86,68),
#     (86,71),
#     (86,72),
#     (86,73),
#     (86,74),
#     (87,34),
#     (87,37),
#     (87,38),
#     (87,39),
#     (87,41),
#     (87,86),
#     (88,3),
#     (88,4),
#     (88,5),
#     (88,6),
#     (88,8),
#     (88,9),
#     (88,10),
#     (88,81),
#     (88,82),
#     (89,2),
#     (89,38),
#     (89,39),
#     (89,40),
#     (89,41),
#     (89,42),
#     (90,41),
#     (90,43),
#     (90,47),
#     (91,22),
#     (91,23),
#     (91,89),
#     (91,90),
#     (92,1),
#     (92,2),
#     (92,5),
#     (92,7),
#     (92,61),
#     (92,63),
#     (92,65),
#     (94,4),
#     (94,8),
#     (94,9),
#     (94,10),
#     (94,12),
#     (94,13),
#     (94,17),
#     (94,20),
#     (94,24),
#     (94,26),
#     (94,92),
#     (94,93),
#     (95,1),
#     (96,9),
#     (96,10),
#     (96,14),
#     (96,15),
#     (96,21),
#     (96,22),
#     (96,24),
#     (96,28),
#     (96,29),
#     (96,30),
#     (96,31),
#     (96,33),
#     (97,18),
#     (97,20),
#     (97,21),
#     (97,23),
#     (97,25),
#     (97,27),
#     (97,28),
#     (97,30),
#     (98,74),
#     (98,75),
#     (98,77),
#     (98,78),
#     (98,79),
#     (98,93),
#     (98,94),
#     (99,57),
#     (99,58),
#     (99,60),
#     (99,62),
#     (100,74),
#     (100,75),
#     (100,96),
#     (101,1),
#     (101,62),
#     (101,63),
#     (101,64),
#     (101,66),
#     (101,67),
#     (113,7),
#     (113,9),
#     (113,12),
#     (113,18),
#     (114,6),
#     (114,7),
#     (114,11),
#     (114,16),
#     (114,17),
#     (114,26),
#     (114,28),
#     (115,28),
#     (115,65),
#     (128,6),
#     (128,7),
#     (128,9),
#     (128,10),
#     (128,14),
#     (128,15),
#     (128,16),
#     (129,1), 
#     (129,3), 
#     (129,5), 
#     (129,8), 
#     (129,9), 
#     (129,10), 
#     (129,46), 
#     (130,7), 
#     (130,8), 
#     (130,10), 
#     (130,16), 
#     (130,17), 
#     (130,21)
#     ]

def getEuclideanDistance(V):
    """ Implementazione per calcolare le distanze euclidee tra tutte le coppie di punti
    Parametri di input:
    - V: l'insieme delle coppie
    Ritorna:
    -  lista delle distanze """
    return  (cdist(V, V, metric='euclidean'))

def campione_sample(V,k):
    n = len(V)
    B = []

    for i in range(n):
        filtered_data = [x for x in V if x != V[i]]
        B.append(random.sample(filtered_data,k))
    
    print("V:\n", V)
    print("B campioni:\n", B)
    return B

def Bk_row(row_sample, soglia):
    """ Funzione per cercare gli elementi vicini. Il metodo consiste 
    nel cercare le distanze tra le  coppie di punti dell'insieme in input.
    Vengono considerati i punti che hanno una distanza entro un range (0, soglia).
    Parametri di input:
    - row_sample: set di coppie da considerare 
    - soglia: valore del limite superiore entro il quale la distanza euclidea deve trovarsi
    Ritorna:
    - Bk_row: Vettore contente l'insieme dei punti con una distanza compresa nel range richiesto """
    if not row_sample:
        return []  
    Bk_row = []
    euclidea_current =  getEuclideanDistance(row_sample)
    for row_euclidea_current in range(len(euclidea_current)):
        for colm_euclidea_current in range(len(euclidea_current[row_euclidea_current])):
            if 0 < euclidea_current[row_euclidea_current][colm_euclidea_current] < soglia: #controllo dell'elemento della distanza euclidea
                Bk_row.append(row_sample[row_euclidea_current]) #row_sample [row_euclidea_current] corrisponde all'elemento di posto row_euclidea_current nella riga di input              
    return Bk_row

def Bk(sample, soglia):
    Bk_neighbors = []
    for i in range(len(sample)):
        Bk_neighbors.append(Bk_row(sample[i],soglia))
    return Bk_neighbors

def reverse(V, B):
    """ R = { u Є V | v Є BK(u) } 
    Parametri di input:
    - V: insieme di tutti i punti
    - B: insieme dei punti vicini 
    Ritorna:
    - R: l'insieme dei vicini inversi """
    n = len(V)
    R = []
    for i in range(n):
        Ri =[]
        for j in range(n):
            if V[i] in B[j]:
               Ri.append(V[j])
        R.append(Ri)
    # R = [[V[j] if V[i] in B[j] else None for j in range(n)] for i in range(n)]
    return R

def unione(Bk, Reverse):
    """ Metodo per unire Bk e Reverse.
    Parametri di input:
    - Bk: insieme contenente gli elementi dei vicinati 
    - Reverse: l'insieme dei vicini inversi    
    Ritorna:
    - insieme dei punti dei due set presi come parametri di input"""

    return Bk + Reverse

def UpdateNN(Bsegnato, soglia):
    """ Metodo per aggiornare il vicinato.
    Parametri di input:
    - Bsegnato: unione del Bk e Reverse
    - soglia: valore del limite superiore entro il quale la distanza euclidea deve trovarsi
    Ritorna:
    - 1 se è ancora necessario aggiornare, o 0 se si è raggiunta la soglia e l'insieme aggiornato"""
    Bk_neighbors = Bk(Bsegnato,soglia)

    if(  1.5 ==  soglia):
        return 0, Bk_neighbors
    
    return 1, Bk_neighbors

def NNDescent(V, soglia, k):
    Bk_neighbors = campione_sample(V,k)

    if not Bk_neighbors:  # Se il sample è vuoto, interrompe l'algoritmo
        print("Errore: Sample restituisce una lista vuota")
        return []

    c = -1 #Valore iniziale scelto in modo convenzionale per poter entrare nel ciclo while
    soglia_minima = 1.5 # Valore minimo per la soglia
    soglia_riduzione = 0.9  # Riduce più lentamente la soglia

    while(c != 0):
        if not Bk_neighbors:  # Controlla che non sia vuoto
            print("Errore: Bk_neighbors è vuoto")
            return []

        
        Reverse = reverse(V,Bk_neighbors)
        Bsegnato = unione(Bk_neighbors, Reverse)

        c = 0 
        for v in range(len(V)):
            for u1 in range(len(Bsegnato[v])):
                for u2 in range(len(Bsegnato[u1])):

                    soglia = max(soglia * soglia_riduzione, soglia_minima)
                    tmp, Bk_neighbors = UpdateNN(Bsegnato, soglia)        
                    c += tmp
          
    return Bk_neighbors

def plot(dati):
    # Estrarre i punti, vengono ignorate le liste vuote
    punti = []
    for sotto_lista in dati:
        punti.extend(sotto_lista)

    # Eliminazione dei duplicati 
    punti_unici = list(set(punti))

    # Separazione coordinate X e Y
    x = [p[0] for p in punti_unici]
    y = [p[1] for p in punti_unici]

  
    plt.figure(figsize=(6, 6))
    plt.scatter(x, y, color='blue', marker='o')

    for (xi, yi) in punti_unici:
        plt.text(xi + 0.1, yi + 0.1, f"({xi},{yi})", fontsize=9)

    plt.title("Punti del vicinato")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis("equal")
    plt.show()
          
if __name__ == "__main__":
    k = 5  # Numero dei nearest neighbors
    soglia = 5
    
    # Bc = campione_sample(V,k) #struttura che contiene i vicini in modo random
    # B = Bk(Bc,soglia)
    # R = reverse(V,B)
    # U = unione(B,R)
    
    # print("\nBc:\n", Bc)
    # print("\nU:\n", U)
    print(f"size(V) = {len(V)}")
    BNuovo =  NNDescent(V,soglia,k)
    print(f"\nVicinato:\n {BNuovo}")
    plot(BNuovo)