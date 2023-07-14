import numpy as np

arr1 = np.array([1,2,3,4])  # !funzione per costruire un array ( il suo nome è VETTORE)

arr2 = np.array([1,2,3,4,5,"6",True]) #! trasforma tutto in stringhe perchè non può avere tipi di dato differenti

arr3 = np.array([[1,2,3,4,],[5,6,7,8,],[9,10,11,12]]) #! Bidimensionali che si chiamano matrici che possono essere sommati contemporaneamente a un vettore
#? in arr3 devono avere la stessa dimensione gli array degli array in parole semplici il stesso numero di elementi dentro

print(arr2)

print(arr3)

print(arr3 + arr1)


