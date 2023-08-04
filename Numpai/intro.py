import numpy as np

arr1 = np.array([1,2,3,4])  # !funzione per costruire un array ( il suo nome è VETTORE)

arr2 = np.array([1,2,3,4,5,"6",True]) #! trasforma tutto in stringhe perchè non può avere tipi di dato differenti

arr3 = np.array([[1,2,3,4,],[5,6,7,8,],[9,10,11,12]]) #! Bidimensionali che si chiamano matrici che possono essere sommati contemporaneamente a un vettore
#? in arr3 devono avere la stessa dimensione gli array degli array in parole semplici il stesso numero di elementi dentro

# print(arr2)

# print(arr3)

# print(arr3 + arr1)

#? shape rapprsenta in caso di vettore il numero degli elementi in caso di matrici rappresenta righe con il primo parametro e con il secondo le colonne

# print("Shape:", arr1.shape)

# print("Shape 2 :", arr3.shape)


# for elemento in arr1:
#     print("Elem ", elemento)

# print(arr1[2]) #? slicing uguale parte sempre da 0 e si possono usare i [:] ecc..

# print(arr3[1][2])

# print(arr3[1,2])

# ? per suddividere un array monodimensionale il uno bidimensionale quindi un Vettore in una Matrice

print("Matrice:", np.reshape(arr1, (2,2)))


# ? ciclare array bidimensionali

righe, colonne = np.shape(arr3)

# for j in range(righe):
#     for k in range(colonne):
#         print(arr3[j][k])


# vettore = np.array([23,45,67,89,100])

# print(vettore > 50)

# altro_vettore = vettore > 50

# print(altro_vettore)

# a = np.array([[11,22,33],[44,55,66]])

# # a[1,:] = 1

# print(a)

# ? appiattisce un array il metodo flatten()

# array_flat = a.flatten()

# print(array_flat)

# ? il metodo concatenate con all'intern0o una tupla con gli array e dopo specificare l'asse

aa= np.array([[11,22], [33,44]])

bb= np.array([[22,55],[100,200]])

cc = np.concatenate((aa,bb),axis=0)

print(cc)

dd = np.concatenate((aa,bb),axis=1)

print(dd)


# ? con il sort() gli puoi ordinare sempre tupla con all'interno l'asse


