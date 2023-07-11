# # ? lancia 2 dadi per 10 volte , nel caso in cui per un certo lancio escono 2 faccie uguali hai vinto e anche nel caso la somma delle 2 faccie sia 7

import random

giocatore1= input("Ciao come ti chiami? ")

print("Benvenuto,",giocatore1)

i = 0

while i < 1:
    ciao=input("Vuoi Giocare ? ")
    if ciao == "No":
        break
    elif ciao == "Si":
        crupier= int(input("Quante volte vuoi lanciare il dado? "))
        for _ in range(crupier):
            dado1 = random.randint(1,6)
            dado2= random.randint(1,6)
            if dado1 == dado2 or dado1 + dado2 == 7:
                print("Il primo dado è",dado1,"il secondo dado è",dado2,"Hai vinto")
            else:
                print("Il primo dado  è",dado1,"il secondo dado  è",dado2,"Hai perso")
    i+=1




    
                
        


  


# crupier= int(input("Quante volte vuoi lanciare il dado? "))

# for _ in range(crupier):
#     dado1 = random.randint(1,6)
#     dado2= random.randint(1,6)
#     if dado1 == dado2 or dado1 + dado2 == 7:
#         print("Il primo dado è",dado1,"il secondo dado è",dado2,"Hai vinto")
#     else:
#        print("Il primo dado  è",dado1,"il secondo dado  è",dado2,"Hai perso")    



