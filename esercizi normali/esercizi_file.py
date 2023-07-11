# Viene generata una sequenza di 1000 numeri interi positivi da 1 a 100 in maniera 
# casuale
# Il programma chiede all'utente di inserire il nome di un file. Se il file esiste, il 
# programma chiede se l'utente vuole sovrascriverlo altrimenti chiede di inserire un 
# altro nome di file
# Gli elementi della sequenza vengono salvati nel file, uno alla volta

import random


def genera_numeri():
    numeri_casuali = []
    for _ in range(1,1001):
        numeri_casuali.append(random.randint(1,100))
        continue
    return numeri_casuali 
        

print(genera_numeri())

nome_file = input("Ciao inserisci il nome di un file: ")

with open(nome_file,"w") as f:
    for _ in nome_file:
        contenuto =  f.write(str(genera_numeri())+"\n")

if contenuto == nome_file :
    print("questo file già esiste")

elif contenuto != nome_file:
    with open("nome_file","w") as f:

         f.write(str(genera_numeri())+"\n")








    
        
    





