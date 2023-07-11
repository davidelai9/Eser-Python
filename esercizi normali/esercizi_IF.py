# Scrivi un programma che prenda in input un valore e determini se è interpretabile 
# come numero
# * Suggerimento *
# Documentarsi sui metodi di stringa:
# isalnum() 
# isdigit()
# isnumeric()


# numero = input("Digita un numero: ")

# if numero[0] == "-":
#    if numero[1:].isnumeric():
#     print(" Questo è un valore numerico")
#    else:
#     print("questo nn è un valore numerico")    
# else:
#      if numero[1:].isnumeric():
#         print(" Questo è un valore numerico")
#      else:
#         print("questo nn è un valore numerico")
    
      

# eser 2  
# Scrivi un programma che prenda in input un numero intero e verifichi se è positivo, 
# negativo o zero

# valore = int(input("scrivi un numero: "))

# if valore > 0:
#     print("questo è un numero positivo")
# elif valore < 0:
#     print("questo è un numero negativo")
# else:
#     print("questo numero è 0")   


# eser 3

# Scrivi un programma che prenda in input un numero intero e determini se è pari o 
# dispari

# numero= int(input("digita un numero"))

# if numero %2 == 0:
#     print("questo numero è pari")
# else:
#     print("questo numero è dispari")


# eser 4

# stringa = input("scrivi una parola: ")

# if stringa.islower():
#     print("questa stringa è in minuscolo")
# else:
#     print("la stringa contiene anche maiuscola")  

# eser 5   

# vocale = input(" scrivi una parola: ")

# if vocale[0] in ["a","b","i","u","o","A","E","O","U","I"]:
#     print("la parola inizia con una vocale")
# else:
#     print("la parola nn inizia con una vocale")

# eser 6

# Scrivi un programma che prenda in input due numeri e li assegni a due variabili: se 
# il valore della prima variabile è minore di quello della seconda, inverti i valori nelle 
# variabili

# a = int(input("dammi il primo numero : "))

# b = int(input("dammi il secondo numero : "))

# if a < b:
#     a,b = b,a
    
# print(a , b)

# eser 7

# Scrivi un programma che prenda in input tre numeri e determini il maggiore tra i 
# tre
# (non usare sequenze ma solo tipi int)

# a = int(input("Dammi il primo numero: "))

# b = int(input("Dammi il secondo numero: "))

# c = int(input("Dammi il terzo numero: "))

# if a < b:
#     if b < c:
#         print("il massimo è", c)
#     else:
#         print("il massimo è", b)
# else:
#     if a < c:
#         print("il massimo è", c)
#     else:
#         print("il massimo è", a)                

# eser 8

#  input tre lunghezze e determini se è possibile 
# formare un triangolo con quelle lunghezze
# Lati a,b,c
# se a+b > c e b+c>a e a+c>b allora è possibile costruire un triangolo

# a = int(input("Dammi il primo lato: "))

# b = int(input("Dammi il secondo lato: "))

# c = int(input("Dammi il terzo lato: "))

# if a +b >c and a + c>b and b + c >a:
#     print("puoi costruire un triangolo")
# else:
#     print("non puoi costruire un triangolo")

# eser 9

# Scrivi un programma che prenda in input un anno e determini se è bisestile

# a = int(input("Dammi l'anno: "))

# if (a % 4 == 0 and a %100 !=0) or a % 400 == 0:
#     print("è un anno bisestile")
# else:
#     print("non è un anno bisestile")    


#  eser 10

# vocale = input(" scrivi un carattere: ")

# if vocale[0] not in ["a","b","i","u","o","A","E","O","U","I"]:
#     print("il carattere è una consonante")
# else:
#     print("il carattere non è una consonante")

# eser 11

# Scrivi un programma che prenda in input una stringa e determini se è palindroma 
# (cioè si legge uguale da sinistra a destra e viceversa come ad es. oro)


# palindromo = input(" scrivi un stringa: ")

# if palindromo == palindromo[::-1]:
#     print("questo è un palindromo")
# else :
#     print("non è un palindromo")    

# eser 12

# Scrivi un programma che prenda in input un numero intero e verifichi se è un 
# multiplo di 3 e di 5 contemporaneamente

# numero = int(input("scrivi un numero: "))

# if numero % 3 == 0 and numero % 5 == 0:
#     print("questo è un multiplo di 3 e 5")
# else:
#     print("questo non è multiplo di 3 o 5")


# eser 13
# Scrivi un programma che prenda in input una stringa e verifichi se è un'anagramma
# di un'altra stringa (es. nipote è anagramma di pitone)

stringa = input("scrivi una parola: ")

stringa2 = "pitone"

if stringa == stringa2:
    print("è un anagramma")
else:
    print("non è un anagramma")    