# Popola, in modo casuale, una lista di 500 valori interi positivi compresi tra 1 e 100Calcola la media aritmetica di questi valori utilizzando la specifica funzione del modulo statistics
# Implementa una funzione che calcoli la media aritmetica di una collezione di interi e la restituisca come valore. Assicurarti che in input venga passata una lista o una tupla e, in caso contrario, la funzione deve restituire il valore -1 per indicare un errore. Anche in caso di input "vuoto" dev'essere restituito -1

import random,statistics


# def media_casuali():

#     casuali= []
    
#     for numero in range(1,501):
#         numero = random.randint(1,100)
#         casuali.append(numero)
#         # print(casuali)

#     media =int(statistics.mean(casuali))
#     if isinstance(casuali,list) or isinstance(casuali,tuple):
#         return media
#     else:
#         return -1

     
# print(media_casuali())


# Popola, in modo casuale, una lista di 500 valori interi positivi compresi tra 1 e 100Calcola la mediana di questi valori utilizzando la specifica funzione del modulo statistics
# Implementa una funzione che calcoli la mediana di una collezione di interi e la restituisca come valore. Assicurarti che in input venga passata una lista o una tuplae, in caso contrario, la funzione deve restituire il valore -1 per indicare un errore. Anche in caso di input "vuoto" dev'essere restituito -1



# def mediana_casuali():

#     casuali= []
    
#     for numero in range(1,501):
#         numero = random.randint(1,100)
#         casuali.append(numero)
#         # print(casuali)

#     mediaana =int(statistics.median(casuali))
#     if isinstance(casuali,list) or isinstance(casuali,tuple):
#         return mediana
#     else:
#         return -1

     
# print(mediana_casuali())


# eser 3

# Popola, in modo casuale, una lista di 500 valori interi positivi compresi tra 1 e 100Calcola la moda di questi valori utilizzando la specifica funzione del modulo
# statistics
# Implementa una funzione che calcoli la moda di una collezione di interi e la
# restituisca come valore. Assicurarti che in input venga passata una lista o una tuplae, in caso contrario, la funzione deve restituire il valore -1 per indicare un errore. Anche in caso di input "vuoto" dev'essere restituito -1


# def moda_casuali():

#     casuali= []
    
#     for numero in range(1,501):
#         numero = random.randint(1,100)
#         casuali.append(numero)
#         # print(casuali)

#     moda =int(statistics.mode(casuali))
#     if isinstance(casuali,list) or isinstance(casuali,tuple):
#         return moda
#     else:
#         return -1

     
# print(moda_casuali())








# eser 4

# Implementa una funzione che restituisca la media ponderata di un insieme di valori numerici
# Deve accettare in input due collezioni, della stessa lunghezza: una che rappresenta i valori e l'altra che rappresenta i "pesi". Assicurarti che in input vengano passati una lista o una tupla e, in caso contrario, la funzione deve restituire il valore -1 per indicare un errore. Dev'essere restituito -1 anche in caso di input "vuoto" e nel caso in cui i due input non siano della stessa lunghezza
# Genera in modo casuale una lista di 30 numeri interi positivi da 18 a 30 (voti univ.)Genera in modo casuale una lista di 30 numeri interi positivi i cui valori possono essere: 3, 6, 9, 12 (crediti univers.)
# Esegui la funzione passando le due liste come argomenti

# nella media ponderata i valori sono moltiplicati per i rispettivi pesi e quindi sommati, per poi essere divisi per la somma dei pesi

# def media_ponderata():

#     voti= []
#     crediti=[]
    
#     for numero in range(1,31):
#         numero = random.randint(18,30)
#         voti.append(numero)
#     print(voti)
#     for numero in range (1,31):
#         numero = random.randrange(3,13,3)   
#         crediti.append(numero)  
#     print(crediti)

#     media = sum(list(map(lambda x,y : x*y,voti,crediti)))/sum(crediti)
#     if isinstance(voti,list) or isinstance(voti,tuple):
#         return media
#     else:
#         return -1

     
# print(media_ponderata())

# eser 5 che trova anche la seconda moda

def moda_casuali():

    casuali= []
    
    for numero in range(1,20):
        numero = random.randint(1,10)
        casuali.append(numero)
    print(sorted(casuali))
    
    
    moda = statistics.mode(casuali)
    print(moda)
    casuali2 = [x for x in casuali if x != moda]
    print(sorted(casuali2))
    moda2 = statistics.mode(casuali2)
    
    if isinstance(casuali,list) or isinstance(casuali,tuple):
        return moda2 
    else:
        return -1

     
print(moda_casuali())
    

    

    