# Ci sono 3 cavalli.
# Vengono generate, in modo casuale, le quotazioni per i cavalli.
# Le quotazioni sono numeri interi da 2 a 20.
# Viene chiesto al giocatore di scegliere su quale cavallo puntare e quanto puntare.
# Ad ogni iterazione, in modo casuale, avanza un cavallo.
# La corsa finisce quando un cavallo raggiunge per primo il traguardo.
# Se a vincere è il cavallo sul quale il giocatore ha puntato, la vincita sarà pari al prodotto tra la somma puntata e la quota (es. punto 100 sul cavallo 1 che è quotato a 15 e se vince ottengo 1500)

# 1) 3 Cavalli -> Creare 3 variabili;
# 2) import random per generare le quoto dei cavalli, Quindi creare varibile quotazioni o funzione;
# 3) associa quotazione al cavallo
# 3) input per il giocatore con la scelta del cavallo;
# ! 4) variabile con input con scelta di quanto puntare;
# 5) modificare la velocità dei singoli cavalli ;
# 6) creare una condizione che riprenda come argomenti il cavallo vincente la sua quota assocciata  e la variabile puntata del giocatore
# La vincità sarà pari vincita = somma_puntata * quota.


import os, time, random


q_cavallo1 = random.randint(2,20)
q_cavallo2 = random.randint(2,20)
q_cavallo3 = random.randint(2,20)

print("Salve queste sono le seguenti quote per i cavalli in corsa oggi :")
print("Cavallo1 = ",q_cavallo1," a 1")
print("Cavallo2 =",q_cavallo2," a 1")
print("Cavallo3 =",q_cavallo3," a 1")

scelta_cavallo= int(input("Scegli tra i 3 cavalli digitando 1, 2, 3: "))

if scelta_cavallo == 1:
    cavallo1 = q_cavallo1
    print("Hai scelto il cavallo 1 quotato",q_cavallo1)
elif scelta_cavallo == 2:
    cavallo2 = q_cavallo2
    print("Hai scelto il cavallo 2 quotato",q_cavallo2)
elif scelta_cavallo == 3:
    cavallo3 = q_cavallo3
    print("Hai scelto il cavallo 3 quotato",q_cavallo3)
else:
    print("Questo cavallo non esiste")   

puntata = int(input("Quanto vuoi puntare : " "$")) 


cavallo1 = ["Cavallo n. 1"]
cavallo2 = ["Cavallo n. 2"]
cavallo3 = ["Cavallo n. 3"]

while True:    
    time.sleep(1)
    os.system('cls')
  
    numero_estratto = random.randint(1,3)
    if numero_estratto == 1:
        cavallo1.append("*")
    elif numero_estratto == 2:
        cavallo2.append("*")
        
    elif numero_estratto == 3:
        cavallo3.append("*")   
    
           

    print("Benvenuti all'ippodromo virtuale. Quale cavallo vincerà?")
    print("\n", cavallo1)
    print("\n", cavallo2)
    print("\n", cavallo3)

    if len(cavallo1) == 10 and scelta_cavallo == 1 and len(cavallo2) < 10 and len(cavallo3) < 10:
        print("Complimenti hai vinto $", puntata * q_cavallo1)
        break
    elif len(cavallo2) == 10 and scelta_cavallo == 2 and len(cavallo1) < 10 and len(cavallo3) < 10:
        print("Complimenti hai vinto $", puntata * q_cavallo2)
        break
    elif len(cavallo3) == 10 and scelta_cavallo == 3 and len(cavallo2) < 10 and len(cavallo1) < 10:
        print("Complimenti hai vinto $", puntata * q_cavallo3)   
        break
    else:
        if len(cavallo1) == 10 and (scelta_cavallo == 2 or scelta_cavallo == 3):
            print("Hai perso!")
            break
        elif len(cavallo2) == 10 and (scelta_cavallo == 1 or scelta_cavallo == 3):
            print("Hai perso!")
            break
        elif len(cavallo3) == 10 and (scelta_cavallo == 2 or scelta_cavallo == 1):
            print("Hai perso!")    

        
        
    
print("fine corsa")






    

        





