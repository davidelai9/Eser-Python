# Crea una variabile stringa e concatenala alla stringa "***"
# Usa la funzione print() per stampare nel terminale la stringa concatenata

a = "stringa"

print(a + "***")

# Crea due variabili, una di tipo stringa e l'altra di tipo intero, e utilizza l'operatore di ripetizione per valorizzare una terza variabile che conterrà la stringa ripetuta.Usa la funzione print() per stampare nel terminale la nuova stringa.

a = "stringa"

b = 2

c = a * b

print(c)

# Crea una lista di numeri primi da 2 a 29.
# A quale indice è presente il valore 29?

primi = [2,3,5,7,11,13,17,19,23,29]

print(len(primi)-1)

# Usando la lista dell'esercizio precedente, usa la corretta funzione built-in per
# valorizzare una variabile con il numero di elementi contenuti nella lista.
# Usa la funzione print() per stampare nel terminale:
# La lista è lunga X elementi


primi = [2,3,5,7,11,13,17,19,23,29]

lun =len(primi)

print("la lista è lunga",lun,"elementi")

# Usando la lista dell'esercizio precedente, usa la funzione print() per stampare nel terminale l'elemento all'indice -3

primi = [2,3,5,7,11,13,17,19,23,29]

print(primi[-3])

# Usando la lista dell'esercizio precedente, usa la funzione print() per stampare nel terminale l'elemento all'indice 15


# primi = [2,3,5,7,11,13,17,19,23,29]
# print(primi[15]) #ritorna errore

# Usando la lista dell'esercizio precedente, usa la corretta funzione built-in per
# sommare tutti gli elementi della lista e assegnare il valore ad una nuova variabile.Usa la funzione print() per stampare nel terminale:
# La somma degli elementi è pari a TOT. Il tipo restituito dalla funzione è X

primi = [2,3,5,7,11,13,17,19,23,29]
somma = sum(primi)

print("La somma degli elementi è pari a", somma, ". Il tipo restituito dalla funzione è " ,type(somma))


# Crea una lista di 10 numeri interi.
# Usa la funzione print() per stampare nel terminale la lista creata.
# Sostituisci l'elemento all'indice 4 con un altro numero e usa nuovamente print() per visualizzare il contenuto della lista.

primi = [1,45,5,3,51,2,5,15,6,10]

print("lista non modificata è",primi)

primi[4]= 17

print(primi)

# Crea una tupla di 10 numeri interi.
# Usa la funzione print() per stampare nel terminale la tupla creata.
# Sostituisci l'elemento all'indice 7 con un altro numero e usa nuovamente print() per visualizzare il contenuto della tupla. 

# primi = (1,45,5,3,51,2,5,15,6,10)

# print("lista non modificata è",primi)

# primi[4]= 17

# print(primi)  # le tuple sono immutabile

# Usa la tupla dell'esercizio precedente.
# Calcola la media aritmetica dei valori contenuti.
# Usa la funzione print() per stampare nel terminale:
# La media è MEDIA

primi = (1,45,5,3,51,2,5,15,6,10)

media = sum(primi) / len(primi)

print("La media è",media)

# Crea una variabile stringa.
# Crea una seconda variabile stringa che contenga la prima invertita
# Usa la funzione print() per stampare nel terminale:
# La stringa originale xxx 
# La stringa invertita yyy

stringa = "treno"
nuova =  stringa[4] + stringa[3] + stringa[2] + stringa[1] + stringa[0]
print(nuova)

# Crea una lista di 5 valori valutabili come veri (ad es. numeri interi > 0)
# Assegna ad una variabile il valore restituito dalla funzione all(lista). Modifica il primo elemento aggiungendo un valore valutabile come falso (ad es. 0)
# Assegna ad un'altra variabile il valore restituito dalla funzione all(lista). Usa la funzione print() per stampare nel terminale:
# Valore prima variabile: VALORE
# Valore seconda variabile: VALORE

valori = [9 > 7, 10 < 12, 3==3, 15-5 <= 10, True]

valori[1] = False

print(valori)

