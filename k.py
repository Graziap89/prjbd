# import random
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt
V = [(1,2),(1,4),(2,3),(4,5),(9,1)]

def getEuclideanDistance(V):
    """ Implementazione per calcolare le distanze euclidee tra tutte le coppie di punti
    Parametri di input:
    - V: l'insieme delle coppie
    Ritorna:
    -  lista delle distanze """
    return  (cdist(V, V, metric='euclidean'))

#conservo le distanze euclidee:
def distanze(V):
    arr = []
    for i in range(len(V)):
        arr.append(getEuclideanDistance(V[i])[0][1])
    # Conversione in lista di float standard
    distanza_euclidea = [float(x) for x in arr]
    return distanza_euclidea

def Bk_row(row_sample, soglia):
    """ Funzione per cercare gli elementi più prossimi. Il metodo consiste nel cercare le distanze tra le 
    coppie di punti dell'insieme in input in cui è presente il nodo corrente e devono essere considerati i nodi che 
    hanno una distanza entro un range (0, soglia).
    Parametri di input:
    - row_sample: set di coppie da considerare 
    - soglia: valore del limite superiore entro il quale la distanza euclidea deve trovarsi
    Ritorna:
    - Bk_row: Vettore contente l'insieme dei punti trovati che hanno una distanza compresa nel range richiesto """
    if not row_sample:
        return []  
    Bk_row = []
    euclidea_current =  getEuclideanDistance(row_sample)
    for row_euclidea_current in range(len(euclidea_current)):
        for colm_euclidea_current in range(len(euclidea_current[row_euclidea_current])):
            if 0 < euclidea_current[row_euclidea_current][colm_euclidea_current] < soglia: #controllo dell'elemento della distanza euclidea
                Bk_row.append(row_sample[row_euclidea_current]) #sample [row_euclidea_current] corrisponde all'elemento di posto row_euclidea_current nella riga di input              
    return (Bk_row)

def Bk(sample, soglia):
    Bk_neighbors = []
    for i in range(len(sample)):
        Bk_neighbors.append(Bk_row(sample[i],soglia))

    return Bk_neighbors

def reverse(V, B):
    """ Implementazione per calcolare l'insieme reverse. Permette di trovare tutti gli elementi appartenenti all'insieme
    dei punti che hanno nel proprio insieme dei k neigbors più prossimi, il nodo corrente. {u € V t.c v € Bk(u)}
    Parametri di input:
    - V: insieme di tutti i punti
    - B: insieme dei nodi più vicini
    Ritorna:
    - reverse: vettore contenente tutti i punti che all'interno del proprio insieme di neigbords più prossimi 
    contengono il nodo corrente """

    n = len(V)
    R = []
   
    for v in range(n):
        Ri =[]
        for u in range(n):
            if V[v] in B[u]:
               Ri.append(V[u])
        R.append(Ri)
    # R = [[V[j] if V[i] in B[j] else None for j in range(n)] for i in range(n)]
    return R

# def unione(Bk, Reverse):
    """ Metodo per unire i set Bk_neighbors e reverse.
    Parametri di input:
    - Bk: insieme contenente gli elementi più aprrosimativamente vicini di un nodo corrente v.
    - Reverse: l'insieme degli elementi u in cui il nodo corrente si trova rispettivamente negli insiemi Bk(u) dei nodi più prossimi di u
    Ritorna:
    - insieme dei punti dei due set presi come parametri di input """

    return Bk + Reverse


def unione(Bk, Reverse):
    """ Metodo per unire i set Bk_neighbors e reverse, evitando duplicati.
    Parametri di input:
    - Bk_corrente: insieme contenente gli elementi più aprrosimativamente vicini di un nodo corrente v.
    - reverse_corrente: l'insieme degli elementi u in cui il nodo corrente si trova rispettivamente negli insiemi Bk(u) dei nodi più prossimi di u
    Ritorna:
    - insieme dei punti dei due set presi come parametri di input senza i duplicati """

    return Bk + Reverse

def UpdateNN(Bsegnato, soglia):
    """ Aggiorna i nearest neighbors, l'insieme preso in considerazione in quell'iterazione.
    Parametri di input:
    - Bk_corrente: insieme contenente gli elementi più aprrosimativamente vicini di un nodo corrente v.
    - Bsegnato : unione del bk e reverse di un'iterazione 
    - u2: punto corrente
    - soglia: valore del limite superiore entro il quale la distanza euclidea deve trovarsi
       """
    Bk_neighbors = Bk(Bsegnato,soglia)

    if(  2 ==  soglia):
        return 0, Bk_neighbors
    
    return 1, Bk_neighbors


def NNDescent(Vicinato_start, soglia, k):

    #sample = campione_sample(V,k) #lista
    sample = Vicinato_start
    if not sample:  # Se il sample è vuoto, interrompe l'algoritmo
        print("Errore: Sample restituisce una lista vuota")
        return []
    V = [(1,2),(1,4),(2,3),(4,5),(9,1)]

    Bk_neighbors = sample

    c = -1 #Valore iniziale scelto in modo convenzionale per poter entrare nel ciclo while
    # soglia_minima = 0.5 # Valore minimo per la soglia
    soglia_minima = 2
    soglia_riduzione = 0.9  # Riduce più lentamente la soglia

    while(c != 0):
        # if not Bk_neighbors:  # Controlla che non sia vuoto 
        #     print("Errore: Bk_neighbors è vuoto")
        #     return []
        
        Reverse = reverse(V,Bk_neighbors)
        Bsegnato = unione(Bk_neighbors, Reverse)

        c = 0    
        for v in range(len(V)): #da 0 a 5(escluso)
            for u1 in range(len(Bsegnato[v])):
                for u2 in range(len(Bsegnato[u1])):

                    soglia = max(soglia * soglia_riduzione, soglia_minima)  # Riduzione più lenta
                    tmp, Bk_neighbors = UpdateNN(Bsegnato, soglia)        
                    c += tmp
          
    return Bk_neighbors

if __name__ == "__main__":
    k = 2  # Numero dei nearest neighbors
    soglia = 5
    #lista di liste, in cui ogni lista contiene k tuple.
    Vicinato_start =    [
                        [(1,2),(1,4)], #Vicinato_start[0] del punto 0
                        [(2,3),(4,5)], #Vicinato_start[1] del punto 1
                        [(9,1),(1,2)], #Vicinato_start[2] del punto 2
                        [(4,5),(1,4)], #Vicinato_start[3] del punto 3
                        [(1,2),(9,1)]  #Vicinato_start[4] del punto 4
                        ]

    distanze = distanze(Vicinato_start)
    B = Bk(Vicinato_start,soglia)

    R = reverse(V,B)
    #U = unione(B,R)
    U2 = unione(B,R)

    BNuovo = NNDescent(Vicinato_start,soglia,k)
    print("\nB1:\n", BNuovo)