# eser 1
# Scrivi una funzione che prenda in input due numeri interi e restituisca la loro 
# somma



# eser 2
# Scrivi una funzione che prenda in input una stringa e restituisca la sua lunghezza

# eser 3
# Scrivi una funzione che prenda in input una lista di numeri interi e restituisca la 
# somma di tutti gli elementi

# eser 4
# Scrivi una funzione che prenda in input una lista di numeri interi e restituisca la 
# lista ordinata in ordine crescente

# eser 5
# Scrivi una funzione che prenda in input una lista di stringhe e restituisca la lista 
# ordinata in ordine alfabetico

# def ordina_stringa(mia_lista):
#     mia_lista_min = [stringa.lower() for stringa in mia_lista]
       
#     return sorted(mia_lista_min)

# print(ordina_stringa(["ciao", "Noi","Babbo"]))


# eser 6
# Scrivi una funzione che prenda in input una lista di numeri interi e restituisca la 
# media

# def media(mia_lista):
#     mia_lista_interi = [int(elemento) for elemento in mia_lista]
#     return sum(mia_lista_interi)/len(mia_lista_interi)

# print(media([3,45,2.8,"345"]))

# eser 7
# Scrivi una funzione che prenda in input una stringa e restituisca True se è un 
# palindromo, False altrimenti

# def palindroma(stringa):
#     if stringa == stringa[::-1]:
#         return True
#     else: 
#         return False   

# print(palindroma("ciaoo"))    

# ? oppure

# def palindroma(stringa):
#     return stringa == stringa[::-1]

# print(palindroma("anna")) 

# eser 8
# Scrivi una funzione che prenda in input una lista di numeri interi e restituisca True
# se contiene almeno un numero pari, False altrimenti

# def num_pari(mia_lista):
#     mia_lista_interi = [int(elemento) for elemento in mia_lista]
    
#     mia_lista_interi_pari = [int(elemento) for elemento in mia_lista_interi if elemento %2==0 ]
#     if len(mia_lista_interi_pari):
#            return True
#     else:
#            return False
   

# print(num_pari([5,4,5,6,7,8,]))

# # ? oppure

# numeri = [3,1,5,3,8,1,5,]

# def pari(numeri):
#     for i in numeri:
#         if i %2 == 0:
#             print(i)
#             print(numeri.index(i))
#             return True
#     return False
# print(pari(numeri))    


# eser 9
# Scrivi una funzione che prenda in input una lista di stringhe e restituisca una nuova 
# lista con le stringhe che hanno una lunghezza superiore a 5

# def stringhe(mia_lista):
#     mia_lista_str = [elemento for elemento in mia_lista if len(str(elemento))> 5]

#     return mia_lista_str
    
# print(stringhe(["ciao","noi","carrara","Giordana",1 ,233455]))


# eser 10
# Scrivi una funzione che prenda in input una lista di numeri interi e restituisca una 
# nuova lista con solo i numeri divisibili per 3

# def num_div_3(mia_lista):
#     mia_lista_interi_3 = [int(elemento) for elemento in mia_lista if int(elemento) %3==0 ] 
#     return mia_lista_interi_3

# print(num_div_3([9,4,5,6,2,"15",27]))   

# eser 11
# Scrivi una funzione che prenda in input una stringa e restituisca la stessa stringa 
# con le vocali rimosse

# def no_vocali(stringa):
#     for elemento in "aeiou":
#         stringa = stringa.replace(elemento, "") # replace è un metodo di stringa che rimpiazza quello che mettiamo come secondo parametro
#     return stringa
# print(no_vocali("stringa"))     

# ! eser 12

# Scrivi una funzione che prenda in input una lista di interi e restituisca una lista 
# nuova contenente gli elementi della prima ma senza duplicati


     
