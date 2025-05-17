# prjbd
Mi sono occupata di implementare una soluzione al problema del KNearest Neighbor Descent per un progetto didattico, un algoritmo utilizzato per l’ottimizzazione
della ricerca dei vicini in grandi insiemi di dati. La realizzazione del progetto consiste nell’apprendimento ed implementazione in linguaggio
Python della versione dell’algoritmo dello pseudocodice “NNDescent” esposto nell’articolo scientifico Efficient K-Nearest Neighbor Graph
Construction for Generic Similarity Measures” di Wei Dong, Moses Charikar e Kai Li. 
#
La variante K-Nearest Neighbord Descent (KNN-Descent)
L’algoritmo K-Nearest Neighbor Descent è un’ottimizzazione
dell’algoritmo K-NN tradizionale, progettata per migliorare l’efficienza
nella ricerca dei vicini, i nearest neighbors, all’interno di grandi dataset.
A differenza del metodo classico che confronta ogni punto con tutti gli
altri, NN-Descent utilizza una strategia iterativa e approssimata per
costruire progressivamente una buona stima dei vicini più vicini di
ciascun punto. In pratica, si parte da una lista iniziale casuale di vicini,
che viene poi raffinata iterativamente riducendo il numero totale di
confronti. Questa tecnica sfrutta l’osservazione che i vicini di un punto
tendono ad avere vicini in comune. Questa ottimizzazione si è rivelata
fondamentale per affrontare scenari tipici del settore Big Data, in cui la
quantità di dati da gestire è particolarmente elevata.
----
