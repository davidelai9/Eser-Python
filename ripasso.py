# #! Eser che poi elimino
# class Attivita():
#     def __init__(self , inizio , fine , descrizione , note):
#         self.inizio = inizio
#         self.fine = fine
#         self.descrizione = descrizione
#         self.note = note
    
#     def stampa():
#         pass

# ! While

# i = 0

# while i < 50:
#     i += 1
#     print(f"i è uguale a {i}")
#     if i % 2 ==0:
#         print("appostu")
#         continue
#     elif i == 30:
#         break    
#     else:
#         print("non appostu")    
# print("fuori blocco")    

# ! For

# for variabile in ["ciao",2,False,4,5,3,7,20,]:
#     print(f"Suga vale {variabile}")
#     print("Suga")

# for _ in range(1,150):
#     print(f"il ciclo viene fatto {_} volte")   

#     if _ == 30:
#         break 

# ? rompicapo ricorda che 2 e 4 vengono scambiati con 99 perchè? 
#! riguardatelo
# lista = [1,2,3,4,5]

# for elemento in lista:
#     # print(elemento)
#     if elemento < len(lista):
#         lista[elemento] = 99
# print(lista)
# # print(elemento) 

# ! Dizionari


# a = {}

#? Quasiasi tipo immutabile può essere una chiave

# a[250]= "Ciao"
# a[3.14]= "pi greco"
# a[True]= 1
# a["anno"]= 2023
# a [("Mario","Chimica")]= 27

# ? Accesso ad un valore usando []

# b = a["anno"]

# ?print(a[("Mario")]) # ? KeyError!

# print(a[("Mario","Chimica")]) # 27

# ? struttura da preferirsi : for Quando si itera un dizionario, per default vengono restituite le chiavi

# for chiave in a :
#     print(chiave)

# ? Per avere entrambi con il ciclo for entrambe chiave e valore
# ? bisogna usare il metodo items()

# for chiave, valore in a.items():
#     print(f"la chiave è {chiave} e il valore è {valore}")


# ! quando ti serve una chiave senza valore utilizza None che non ha valore!!

# ? del --> si utilizzare per eliminare una copia chiave valore

# ? La funzione len --> restituisce il numero di coppie chiave valore all' interno del dizionario  

# ! Gli open file 


#? da Docente DAITA05 a tutti:    11:47 AM

# att1 = {"inizio": "2023-07-06", "fine": None, "desc": "devo fare la spesa", "note": None}
# att2 = {"inizio": "2023-07-07", "fine": None, "desc": "devo fare gli addominali", "note": None}
# att3 = {"inizio": "2023-07-08", "fine": None, "desc": "chiamare nonna", "note": None}
# with open("prova.txt", "w") as f:
#     f.write(str(att1) + "\n" + str(att2) + "\n" + str(att3))
# with open("prova.txt", "r") as f:
#     contenuto = f.readlines()
# for cont in contenuto:
#     print(cont)

#! Con JSON

import json

class Persona:
    def __init__(self, n, c ,a):
        self.nome = n
        self.cognome = c
        self.anni = a

    def modifica_anni(self, a):
        self.anni = a
    
    def presentati(self):
        print(f"Ciao sono {self.nome} {self.cognome} e ho {self.anni} anni")

persona1 = Persona("Davide","Lai","29")

persona2 = Persona("Luca","Bisco", 28)

persona3 = Persona("Oronzo","Cana", 69)

persona1.presentati()
persona2.presentati()
persona3.presentati()

print(persona1.__dict__) #? __dict__ stampa gli attributi della classe in fomato dizionario!

# with open("persona.json","w")as f:  #! Salvare un unico oggetto
#     json.dump(persona1.__dict__,f)

persone = [persona1.__dict__, persona2.__dict__,persona3.__dict__ ]

with open("persona.json","w") as f:
    json.dump(persone, f)         #? scrivere dentro il file

with open("persona.json") as f:
    dati_file_json= json.load(f) #? estrarre fuori

persone_salvate= []

#? Qui ristampo nel terminale

for dati_persona in dati_file_json:
    oggetto_persona = Persona(dati_persona["nome"],dati_persona["cognome"],dati_persona["anni"])
    persone_salvate.append(oggetto_persona)

print("********* DOPO LA LETTURA DEL FILE JSON **********")

for persona in persone_salvate:
    persona.presentati()

# ? Modifiche alle persone

persona2.nome = "Francesco"
persona_nuova1 = persone_salvate[2]

persona_nuova1.nome = "Gualtiero"

persona2.presentati()
persona_nuova1.presentati()

# ! I Set (Ricordati di copiare dai sorgenti dell'accademia)

# mio_set = {"a",0.5,"Ciao",True, -3}

# # ! Espressioni Lambda (funzioni anonime )

addizzione = lambda x,y : x + y  # ? prima dei : punti ci vanno gli argomenti dopo l'espressione della funzione

# print(addizzione(2,5))

# ! map() and filter()


# def quadrato(x):
#     return x **2

# numeri = [90,105,12,4,1,1024,16]
# numeri2 = [2,106,127,8,9,124,6]
# numeri3 = [9,10,128,47,16,102,156]

# print(list(map(lambda x,y,z : x*y+z, numeri,numeri2,numeri3))) #? list per convertire, map che richiama la funzione, quadrato(funzione di su), poi argomento su cui usare la funzione


# numeri = [90,105,12,4,1,1024,16]
# numeri2 = [2,106,127,8,9,124,6]
# numeri3 = [9,10,128,47,16,102,156]

# # ? la stessa cosa con un for 

# num4= []

# for x in range(len(numeri)):
#     num4.append(numeri[x]* numeri2[x] + numeri3[x])

# print(num4)

# ! filter

# numeri = (1,2,4,5,67,89,8,76,5,4)

# pari = tuple(filter(lambda x: x%2 ==0, numeri))

# print(pari)

# soglia = 50

# minori = tuple(filter(lambda x: x < soglia, numeri))

# print(minori)

# minuscole =["ciao","noi","Andiamo","FORSE","aIo"]

# maiuscole = list(filter(lambda x : x.isupper(), minuscole))

# print(maiuscole)

# ! Gestione eccezzioni 

# ? Si usano per giocare di anticipo e non far crashare il programma o comunque non perdere i dati nel caso di crash

# ?esempio 1
# a = 10 

# b = 0

# print("il risultato è",a/b)

# print("Questa istruzione non viene eseguita")

# ? esempio2 
# try:
#     with open("mio.txt","r") as f:
#         pass

# except:
#     print("c'è stato un errore")
    
# print("il programma continua")    

# # ? esempio 3 del perchè serve al posto di una consizione
# while True:
#     try:
#         a = int(input("Digita un numero")) #? se non digiti un numero il programma comunque continua
#         b = int(input("Digita altro numero")) #? se non digiti un numero il programma comunque continua
#         c = a + b
#         break
#     except:
#         print("Digita i dati correttamente") # ? se l'utente sbaglia questo fa tornare su

# ? esempio 5 intercetta anche l'errore        
    
while True:
    try:
        with open("ciccio.txt") as f:
            pass
        a = int(input("Digita un numero")) #? se non digiti un numero il programma comunque continua
        b = int(input("Digita altro numero")) #? se non digiti un numero il programma comunque continua
        c = a + b
        break
    except ValueError:
        print("Digita i dati correttamente") 
    except FileNotFoundError:
        print("Non ho trovato questo file")
    except ZeroDivisionError:
        print("Non puoi dividere per 0")
    except:                        # ? Quando non specifici e puè essere solo uno come nel caso dell'else nel if
        print("Errore generico")            
    finally:                      # ? permette di eseguire cmq l'istruzione anche se ci sono gli errori
        print("mi eseguo sempre")
        














