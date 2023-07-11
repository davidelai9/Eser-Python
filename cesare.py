
# Scrivere ua funziona che prenda in input una stringa e un intero che rappresenta lo spostamento in avanti 
# Il cifrario di Cesare consiste nello spostare in avanti le lettere che contengono una parola per non far 
# capire il messagio a chi non è proprietario del programma 

# !ord() funzione bilt-in per avere l'ordine numerico delle singole lettere dell'alfabeto (differenti le minusc e le Maiusc)
# !chr
# dato un valore numerico restituisce la lettera corrispondente;    

parola = input("Dammi una parola da decifrare: ").lower()



def cifrario(stringa,numero):
    lettere = []
    for lettera in stringa:
        shift = ord(lettera) + numero
        lettere.append(shift)
        
    return lettere
        
    
print(cifrario(parola,3))    

def parola_nascosta(stringa):
    lettere2 = []
    for lettera in stringa:
        shift = chr(lettera)
        lettere2.append(shift)
    return lettere2   

parola_segreta = "".join(parola_nascosta(cifrario(parola,3)))

print(f"La parola cifrata è {parola_segreta}")


def decifrario(stringa,numero):
    lettere = []
    for lettera in stringa:
        shift = chr(ord(lettera) + numero)
        lettere.append(shift)
    return  "".join(lettere)

print(f"Questa è la parola originale: {decifrario(parola_segreta, -3)}")
