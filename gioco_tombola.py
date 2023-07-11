# # ? Il programma chiede di inserire il numero di giocatori.
#? Ogni giocatore ha una sola scheda (o cartella), contenente 15 numeri unici, da 1 a 90.
#? In ogni partita, viene estratto casualmente un numero da 1 a 90, estremi inclusi. Il numero estratto non è più utilizzabile nella 
#? stessa partita. Quando c'è corrispondenza tra un numero estratto ed un numero presente in una scheda, il giocatore tiene traccia
#? di questa corrispondenza ad es. usando un pennarello per cerchiare o barrare il numero nella propria scheda.

# ! Lista di liste nel caso di ambo terno quaterna e cinquina

import random

def numeri():
     return random.randint(1,90)
     


def cartella():
    lista = []
    
    while len(lista) < 15:
        n = numeri()
        if n <= 90:
            lista.append(n)
        else:
            break
    return lista 
  
def chiamata():
    for call in range(1,91):
        n= numeri()
        call =[]
        call.append(n)
        return call

print(chiamata())         


giocatori =int(input("Quanti giocatori siete? "))

cartelle = []

for _ in range(giocatori):
    cartelle.append(cartella())
    
print(cartelle)    
     
vincente = []   
while True :
    numero_estratto = chiamata()
    print("questo è il numero estratto", numero_estratto)
    if numero_estratto in cartelle :
        vincente = cartelle.remove(numero_estratto)
        continue
    else:
        break
    



        
           
    


        
    



    
     







  

   