# #?Crea una sequenza di 20 parole. Il programma sceglie, in modo casuale, una di queste parole e la mostra al giocatore 
#?con le lettere mischiate.
#?Al giocatore viene chiesto di digitare quella che crede possa essere la parola esatta e ha X tentativi per riuscire ad 
#?indovinare.
#?Se il giocatore indovina, il programma scrive nel terminale:
#?Bene! Hai indovinato. La parola era PAROLA e hai impiegato TOT tentativi.
#?Se finiscono i tentativi senza che la parola sia stata indovinata, il programma scrive nel terminale:
#?Hai perso! La parola era PAROLA
 
#!Vincoli:
#!devi implementare una funzione mischia_lettere() che accetti una stringa in input e restituisca una stringa 
#!contenente gli stessi caratteri di quella di input ma "mischiati" in modo casuale

import random

def mischia_lettere(stringa):
    a=random.sample(stringa,len(stringa))# oppure lista=list(stringa) while lista: indice= random.randint(0,len(lista)-1) stringa_1 += lista.pop(indice)
    nuova_stringa=""
    for e in a:
        nuova_stringa+=e
    return nuova_stringa

lista_parole =["ciao", "hello", "cocomero", "divano","castello","palazzo","montagna","programma","anagramma","lista","funzione","estate","programmazione","trovare","cappello"]
x=random.randint(0,14)
parola=lista_parole[x]
mischia_lettere(parola)


nome = input("Ciao, come ti chiami? ")
print("Benvenuto", nome)
while True:
    g=input("ti va di giocare? ").lower()
    if g == "no":
        break
    elif g!="no" and g!="si":
        print("Devi rispondere si oppure no")
    elif g=="si":
        print("Bene, cominciamo")
        print("Guarda queste lettere e trova la parola nascosta :  ", mischia_lettere(parola))

        for n in range(1,11):
            tentativo = input("Digita una parola:  ")
            if n == 1 and tentativo == parola:
                print("Complimenti, hai trovato", parola,"al primo colpo!")
                break
            if tentativo == parola:
                print("Complimenti, hai trovato", parola,"dopo",n,"tentativi!")
                break
            else:
                print("Sbagliato, riprova")
                if n==10:
                    print("Hai perso, la parola era",parola)
    break
        



# soluzione 2

import random

def mischia_lettere(stringa):
    a=random.sample(stringa,len(stringa)) # oppure lista=list(stringa) while lista: indice= random.randint(0,len(lista)-1) stringa_1 += lista.pop(indice)
    nuova_stringa=""
    for e in a:
        nuova_stringa+=e
    return nuova_stringa

lista_parole =["ciao", "hello", "cocomero", "divano","castello","palazzo","montagna","programma","anagramma","lista","funzione","estate","programmazione","trovare","cappello"]
x=random.randint(0,len(lista_parole))
parola=lista_parole[x]
mischia_lettere(parola)


nome = input("Ciao, come ti chiami? ")
print("Benvenuto", nome)
while True:
    g=input("ti va di giocare? ").lower()
    if g == "no":
        break
    elif g!="no" and g!="si":
        print("Devi rispondere si oppure no")
    elif g=="si":
        print("Bene, cominciamo")
        print("Guarda queste lettere e trova la parola nascosta :  ", mischia_lettere(parola))

        for n in range(1,11):
            tentativo=input("Digita una parola:  ")
            if n == 1 and tentativo==parola:
                print("Complimenti, hai trovato", parola,"al primo colpo!")
                break
            if tentativo==parola:
                print("Complimenti, hai trovato", parola,"dopo",n,"tentativi!")
                break
            else:
                print("Sbagliato, riprova")
                if n==10:
                    print("Hai perso, la parola era",parola)
    break
