# Scrivi un programma che utilizzi map per raddoppiare ogni numero in una lista di 
# numeri interi

lista = [2,5,6,9,10]

raddopiati = list(map(lambda x : x**2,lista))

print(raddopiati)

# Scrivi un programma che utilizzi filter per filtrare solo i numeri pari da una lista di 
# numeri

lista = (3,6,89,24,20)

pari = tuple(filter(lambda x : x%2 == 0,lista))

print(pari)

# Scrivi un programma che utilizzi map per calcolare la lunghezza di ogni parola in 
# una lista di stringhe

# lista = ["ciao","ogni","Andiamo","AcMilan"]


stringhe = ["ciap","andiamo", "aio"]

lunghezza = list(map(len, stringhe)) 

print(lunghezza)

# Scrivi un programma che utilizzi filter per filtrare solo le parole in una lista di 
# stringhe che iniziano con una lettera specifica
        

lista = ["andiamo","forza","cavolo","fame","astro"]

parola = list(filter(lambda x : x.startswith("f"),lista))

print(parola)

# Scrivi un programma che utilizzi map per trasformare ogni stringa in una lista di 
# stringhe in maiuscolo

lista=["ciao","mamma","sorelle","addio"]

maiuscole = list(map(lambda x : x.upper(),lista))

print(maiuscole)

# Scrivi un programma che utilizzi filter per filtrare solo i numeri maggiori di un 
# valore specifico da una lista di numeri

numeri = [23,4,56,7,89,2,34]

maggiori = list(filter(lambda x : x >10,numeri))

print(maggiori)

# Scrivi un programma che utilizzi map per calcolare il cubo di ogni numero in una 
# lista di interi

numeri =[2,4,5,8,9,12]

cubo = tuple(map(lambda x : x**3 , numeri))

print(cubo)

# Scrivi un programma che utilizzi filter per filtrare solo le stringhe con una lunghezza 
# superiore a un valore specifico da una lista di stringhe


lista=["ciao","mamma","sorelle","addio"]

ciao = ["io","ruamamma"]

piu_lunghe= list(filter(lambda x : len(x)>4,lista + ciao))

print(piu_lunghe)

# Scrivi un programma che utilizzi map per calcolare la somma degli elementi 
# corrispondenti di due liste


