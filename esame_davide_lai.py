# Cosa fa la seguente linea di codice Python? print("Hello, World!")
# A. Stampa "Hello, World!" sulla console. 
# B. Crea una variabile chiamata "Hello, World!". 
# C. Genera un errore. 
# D. Nessuna delle precedenti.

#? La risposta corretta è la A. Stampa "Hello, World!" sulla console.

# Cosa significa IDE in termini di programmazione? 
# A. Integrated Development Environment 
# B. Internal Development Environment 
# C. Integral DerivaƟve EquaƟon
# D. Integrated Deployment Environment 

#? La risposta corretta è la A. Integrated Development Environment 

# Cosa fa la seguente linea di codice? x = 5 
# A. Stampa "5" sulla console. 
# B. Crea una variabile chiamata "5" e le assegna il valore "x". 
# C. Crea una variabile chiamata "x" e le assegna il valore 5. 
# D. Genera un errore.

# ? La risposta corretta è la C. Crea una variabile chiamata "x" e le assegna il valore 5.

# Come si chiamano le funzioni che fanno parte di un oggeƩo in Python?
# A. Methods 
# B. Variables 
# C. Loops 
# D. Conditions

# ? La risposta è la A. Methods

# Cosa restituisce l'operatore % in Python?
# A. Il quoziente di una divisione. 
# B. Il resto di una divisione. 
# C. Il prodotto di una moltiplicazione.
# D. Il risultato di un'esponenziazione. 

# ? La risposta corretta è la B. Il resto di una divisione. 

# Python è un linguaggio di programmazione compilato. Vero o falso?

# ? La risposta è falso poichè Python è un linguaggio di programmazione interpretato, dove il codice viene eseguito tramite un sorgente riga per riga

# In Python, possiamo concatenare solo stringhe con altre stringhe. Vero o falso?

# ? in questo caso la risposta è vera poichè in python non possiamo concatenare le stringhe con tipi di dato differenti, fanno eccezioni gli integer con i float che tra loro possono essere sommati. 

# Una lista Python può contenere elementi di tipi di dati diversi. Vero o falso?

# ? Si la risposta è vera poichè una lista può contenere contemporaneamente al suo interno tutti i tipi di dati presenti in Python 

# In Python, una funzione può restituire più di un valore. Vero o falso?

# ? la risposta è vera poichè in Python con la funzione return e separando i valori tramite una virgola si possono restituire più valori, Es: return x,y

# I dizionari in Python possono avere solo stringhe come chiavi. Vero o falso?

# ? Falso, l'importante e che siano coppie chiavi valore con in mezzo a loro i ":" e a separare le coppie chiave valore ci sia la virgola, Es : a = {"ciao": 5 , True : 67 , 5 : "ciao"}

#! Scrivi un programma che stampa i numeri da 1 a 10 utilizzando un ciclo for

# for numero in range(1,11):
#    print(numero)

#! Crea una funzione che accetta due numeri come input e restituisce il loro prodotto.

# def moltiplico(num1,num2):
#      prodotto = num1 * num2
#      return prodotto

# print(moltiplico(3,5))

#! Crea una lista di numeri da 1 a 5. Quindi, scrivi un programma che itera attraverso la lista e stampa ogni 
#! numero.

# numeri = [1,2,3,4,5]

# for numero in numeri:
#     print(numero)

#! Scrivi un programma che utilizza un ciclo while per stampare i numeri dispari da 1 a 10. 

# a = 1
# while a <= 10:
#     if a % 2 != 0:
#         print(a)
#     a += 1

#! Crea un dizionario con le seguente coppie chiave-valore: "nome" e "Mario", "età" e 25, "città" e "Roma". 
#! Quindi, scrivi un programma che stampa il valore della chiave "città".

# dizionario = {"nome":"Mario", "età": 25, "città":"Roma"}

# print(dizionario["città"])

#! Cosa si intende per "tipizzazione dinamica" in Python?

# ? Python è un linguaggio a tipizzazione dinamica perchè è possibile assegnare e riassegnare valori di qualsiasi tipo ad una variabile, Es:

# a = 5
# a = 100

#? dove nella riga 101 a vale 5 mentre nella riga 102 gli viene riassegnato il valore 100;


# Spiega la differenza tra una lista e un tuple. 

# ? Sono entrambi sequenze di Python dove le sostanziali differenze sono: in primis i valori all'interno della lista vengono delimitati dalle [] parentesi quadre mentre le tuple dalle () parentesi tonde; la seconda differenza è che le liste sono sequenze mutabili quindi possono essere modificate mentre le tuple no

# Qual è lo scopo dell'istruzione import in Python?

# ? Con l'istruzione import di Python scritta nel codice del sorgente è possibile importare dei moduli o delle classi già preesistenti in python oppure anche creati da noi ed importarli da foglio a foglio in parole povere, trasportando con se tutti i metodi classi e funzioni al suo interno, può essere usati anche con la parola from che viene utilizzata per importata una specifica da un modulo ad esempio.

# Cosa si intende per "passaggio di argomenti per riferimento"?

# ? non mi ricordo al momento la definizione, me lo andrò a rivedere


# ! 1) primo bug
# def somma(a, b): 
#     print(a - b) 

# L'unico bug che mi viene in mente è il fatto che la funzione somma dovrebbe fare un addizione di a e b quindi dobbiamo sostituire il segno meno "-" con il segno più "+" nel print per ottenere cosi la somma dei due numeri che passeremo alla funzione

# ! 2) secondo bug

# for i in range(10) 
#     print(i)   

# In questo ciclo for mancano i : punti per poter far partire il ciclo, bisognerebbe quindi scrivere -> for i in range(10):

# ! 3) terzo bug

# x = [1, 2, 3] 
# y = x[3] 

# In questo caso avremo un IndexError per out of range poichè la lista assegnata ad x a come ultimo indice il 2 che corrisponde al valore 3, poichè gli indicizazzione parte sempre da 0

# ! 4) quarto bug

# if x = 5: 
#    print("x è 5") 

# In questo caso il codice darà un errore poichè si sta cercando di assegnare una variabile all'interno della condizione if .

# ! 5) quinto bug

def f(): 
   g()  
   def g(): 
     print("Ciao") 
     f() 

# In questo caso l'errore sta nel fatto che fa funzione g() a riga 150 venga richiamata nel codice ancora prima di essere stata definita.


# ! Per ciascuna delle seguenƟ sezioni di codice, descrivi cosa fa.

# ! 1)
# def f(n): 
#  return n if n <= 1 else f(n-1) + f(n-2) 


# Non mi ricordo cosa fa questa funzione, mi sembra una ricorsione sicuramente

# ! 2)

# print("Ciao".replace("C", "c")) 

# In questa riga di codice viene utilizzato il metodo delle stringhe .replace che in questo caso specifico sostituisce la C maiusc con quella minusc c , più in generale il metodo replace accetta in entrata il primo valore che deve sostituire e sopo la virgola accetta il valore che deve andare a mettere al posto del primo

# ! 3)

# x = [i ** 2 for i in range(5)] 

# print(x)

# In questa riga di codice troviamo una list comprension dove tramite il ciclo for viene restituita una lista di numeri elevati al quadrato in un range di 5 quindi avremo come output : [0,1,4,9,16]

# ! 4)

# def f(x=[]): 
#    x.append(1) 
#    return x 

# Questa funzione prende come parametro d'entrata una lista dove tramite il metodo append verrà ritorna la lista con i valori che metteremo noi + il valore 1 alla fine e quindi all'indice -1 della lista che ritornerà x

# ! 5)

# x = {i: chr(i) for i in range(65, 91)} 

# print(x)

# Questo dizionario al suo interno ha una coppia chiave valore dove tramite un ciclo for viene assegnato ad ogni giro del ciclo a partire dal numero 65 fino ad arrivare al numero 90 la corrispettiva lettera per i numeri all'interno del range creando cosi delle chiavi valore.


# ! Scrivi una funzione che accetta una stringa e restituisce la stessa stringa, ma con le lettere invertite.

# def inverti(stringa):
#    return stringa[::-1]

# print(inverti("lavorare"))

# ! Crea una funzione che accetta una lista di numeri e restituisce la somma di tutti i numeri nella lista


# def somma_numeri(x=[]):
#     somma = 0
#     for numero in x:
#        somma += numero
#     return somma 
        
# print(somma_numeri([1,2,3,4,5]))    

# ! Crea una funzione che accetta un numero e restituisce True se il numero è primo, altrimenti False.

# def is_primo(numero):
#     if numero <= 1:
#         return False
#     for i in range(2, numero):
#         if numero % i == 0:
#             return False
#     return True

# print(is_primo(7))
# print(is_primo(10))


#! Scrivi una funzione che accetta una stringa e restituisce un dizionario dove le chiavi sono caratteri unici nella 
#! stringa e i valori sono il numero di occorrenze di ogni carattere.

# def funzione(stringa):
#    stringa = {lettera : ord(lettera) for lettera in stringa }
#    return stringa

# print(funzione("aiuto"))


#! Crea una funzione che accetta due stringhe e restituisce True se una stringa è un'anagramma dell'altra, 
#! altrimenti False.

# def anagramma(stringa1, stringa2):
#     if len(stringa1) != len(stringa2):
#         return False
#     for carattere in stringa1:
#         if carattere not in stringa2:
#             return False
#         stringa2 = stringa2.replace(carattere, '', 1)
#     return True  
          
# print(anagramma("attore","teatro"))  

# print(anagramma("ciao", "piero"))


#! Cosa si intende per ereditarietà in Python?

#? L'ereditarietà in python deriva dal fatto che è possibile trasmettere dalla classe padre ad una classe figlia i valori dati al padre precedentemente, con la possibilità di poterli pure modificare

#! Cosa sono le eccezioni in Python e come vengono gesƟte?

#! Come funziona l'incapsulamento in Python?

#! Come si crea un modulo in Python? 

#! Cosa sono le funzioni di ordine superiore in Python? 

# ? sono quelle funzioni che assumono altre funzioni come parametri oppure che restituiscono una funzione.                Ad Esempio .map() e .filter()

#! Come si crea una classe in Python? 

# ? una classe in Python si crea con la parola chiave class e viene sempre scritta con la prima lettera maiuscola dove al suo interno vengono definiti tutti i suoi argomenti contenenti all' interno 

# Es: class Attivita():
          # def __init__(self, descrizione, inizio, fine, note):
            # self.descrizione = descrizione
            # self.inizio = inizio 
            # self.fine = fine
            # self.note = note

#! Cosa sono le list comprehension in Python? 

# ? le list comprension su python permettono di scrivere un espressione tramite delle condizioni e con un ciclo for al proprio interno , in grado di creare automaticamente una lista con determinati valori.

# ! Come si legge e si scrive su un file in Python? 

# ? per leggere un file su python si usa with open("nome_file", "r"): mentre per scrivere si usa with open("nome_file", "w"):
   




     


       

 

