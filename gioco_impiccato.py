# Regole
# Il programma sceglie casualmente una parola (almeno 5 caratteri) da un file # ! V
# Il giocatore deve indovinare questa parola
# La parola viene rappresentata da una serie di trattini o underscore, uno per ogni lettera della parola. Ad esempio, "casa" diventa 
# "_ _ _ _"
# Il giocatore cerca di indovinare la parola inserendo una lettera alla volta
# Se la lettera proposta è presente nella parola da indovinare, viene rivelata in tutte le sue posizioni corrette. Ad esempio, se la 
# parola segreta è "casa" e il giocatore inserisce la lettera "a", la parola visualizzata diventa "_ a _ a"
# Se la lettera proposta non è presente nella parola segreta, viene conteggiato un errore
# Il gioco finisce se il giocatore indovina la parola oppure commette 7 errori
# Due modalità di input per il giocatore: singola lettera oppure parola, quando vuole dare la soluzione


import random

# io = input("Ciao vuoi giocare al gioco dell' impiccato? ")

# if io == "no":
#     print("coddadi")
# elif io == "si":
#     print("bene iniziamo")

# print(contenuto[indice].strip())

with open("parole.txt") as f:
    
    contenuto = f.readlines()
    
indice = random.randrange(1,len(contenuto))

while True:

    if len(contenuto[indice].strip()) >= 5:
        print("la parola va bene") #contenuto[indice].strip())
        break
    else:
        print("la parola non è valida")
        break
        
        
parola = contenuto[indice].strip()
 
lettere_indovinate = []

for p in parola:
    lettere_indovinate.append("_")

print(lettere_indovinate)

print("Benvenuto al gioco dell'impiccato\nDovrai indovinare una parola di",len(parola),"lettere\nAvrai un massimo di 7 tentativi")

tentativi = 7
         
lista = []

while tentativi > 0:
    parola_giusta = input("Vuoi provare ad indovinare la parola?\nrispondi no per provare a indovinare una lettera ")

    if parola_giusta == "no":
        print("Okay prova a dirmi una lettera")
        
    else:
        if parola_giusta == parola:
            print("Bravo hai indovinato la parola",parola)
            break
        else:
            tentativi -= 1
            print("La parola è sbagliata riprova ti rimangono",tentativi,"tentativi")
            
    lettera = input("Indovina una lettera ")

    if lettera in parola:
        print("Hai indovinato la lettera",lettera)
    elif tentativi == 1:
        print("Hai finito i tentativi hai perso, la parola da indovinare era",parola)
        break
    else:    
        tentativi -= 1    
        print("Questa lettera non è presente",lettera,"Ti rimangono", tentativi,"tentativi")

    lista.append(lettera)
    i = 0
    for l in parola:
        if l not in lista:
            lettere_indovinate[i]="_"
            i += 1
        else: 
            lettere_indovinate[i]=l
            i += 1  
    print(lettere_indovinate)
        

    
    # lettera = input("Indovina una lettera ")


        
        






        











