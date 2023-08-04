import pandas as pd

# righe = [0,1,2,3,4]
# colonne = ['A','B','C']
# nostri_dati = [[1,2,3],(4,5,6,),{9,8,7},[0.1,5,12],[3,4,4]]

# df = pd.DataFrame(data= nostri_dati, index=righe, columns=colonne )

# print(df)

# # ? modifichiamo indice ad esempio

# # print(df.set_index(keys='C'))
# # print(df.set_index(keys='C', drop= False)) #!per default drop è impostato a True

# df.set_index(keys='C', inplace= True)#!per default inplace è impostato a false

# print(df)

# df.reset_index(inplace= True ,drop= True ) #! reset_index rimuove l'indice 

# print(df)

#? Prelevo dal file adesso

df2 = pd.read_csv('C:/Users/Oba 9/Desktop/Generation/Pyton/python/pandas/INCIDENTI RILEVATI DA POLIZIA LOCALE DA ANNO 1991 - Foglio1.csv')

print(df2)

df2.set_index(keys='anno', inplace= True) #! ricorda metti inplace True per far sparire l'indice predefinito ed in questo caso anno diventa l'indice

print(df2)

print(df2['totale']) #! in questo caso nei data frame puoi estrapolare la colonna ma non la riga a mo di index

print(df2.iloc[0]) #! con iloc ottieni la riga a mo di index , ma puoi richiamarli solo tramite indici predefiniti ma non con quelli che hai modificato tu in questo caso gli anni.

print(df2.loc[1991]) #! mentre con loc possiamo richiamare la riga in base all'indice che diamo noi. 

print(df2.loc[[1992, 1996,2014]]) #! permette di prendere più righe insieme con una parentesi dentro la parentesi

print(df2[['totale', 'deceduti']]) #! in questo caso più colonne

print(df2.loc[1992]['totale']) #! battaglia navale per resistuire il valore partendo dalla riga e poi la colonna

print(df2.loc[1992,'totale']) #! oppure cosi come su numpy


#? ATTENZIONE guardiamo le condizioni 

# print (df2 == 6) #! in pratica è un tasto CERCA che restituisce False dove la condizione non è soddisfatta e True dove c'è il 6

# print(df2[df2 == 6]) #! qui vedremo NAN dove non c'è il 6 e stampato il 6 dove è presente

print(df2["feriti"].dtype )

# print(df2[ df2['deceduti'] > 4 ]) #! qui invece impostiamo la condizione dove i deceduti sono maggiori di 4

# ? in pandas & = AND ; | = OR ; ~ = NOT


print(df2[(df2['deceduti'] > 4) & (df2['feriti'] > 600 )]) 


# ? metodo isin

print(df2[df2['deceduti'].isin([4])]) #! che ci stampa tutti i deceduti che hanno valore 4

# ? Modificare colonne 

print(df2.columns) #! restituisce tutti i nomi delle colonne

print(df2.index) #! restituisce tutte le righe

df2.rename(columns={'mortali': 'ciao'}, inplace=True ) #! con chiave valore modifico mortali in ciao ma sempre usando inplace True

print(df2)

df2.drop(labels='ciao', axis= 1, inplace=True) #! con axis specifico l'asse che essendo 1 è quello delle colonne mentre lo 0 sarebbe delle righe

print(df2)

df2['nuova_colonna'] = 0 #! per aggiungere una colonna con tutti i valori 0 in queste caso 

print(df2)

df2['nuova_colonna'] = df2['deceduti'] * 4 #! in questo caso moltiplichiamo i deceduti * 4 

print(df2)

#? Convertire

df2['feriti'] = df2['feriti'].astype('float64')

print(df2['feriti'].dtype)

# ? apply

nuovo_df = df2.apply(lambda x : x*2) #! in questo caso con apply moltiplica tutte le righe * 2 , df2.apply(lambda x : x*2,1) mettendo come secondo valore 1 ci spostiamo nelle colonne

print(nuovo_df)

nuovo_df = df2['deceduti'].apply(lambda x : x*2) # ! in questo caso modifico solo la colonna deceduti

print(nuovo_df)

#! RICORDA PER USARE QUELLO DI SOTTO AVEVAMO AGGIUNTO UN % HAI DECEDUTI

# def rimuoviPercento(stringa):
#     return stringa[:-1]

# nuovo_df = df2['deceduti'].apply(rimuoviPercento)

# nuovo_df = df2['deceduti'].apply(lambda x : x[:-1]) #! rimuove il % perche lo slicing rimuove l'ultimo elemento indice poiche [:-1] cosi non abbiamo utilizzato il primo parametro quindi eliminiamo 1 mentre con il secondo gli diciamo come eliminare mentre se avessimo messo il 3 parametro sarebbe stato lo step

# print(nuovo_df)

# ? tail

print(df2.tail(5)) #! sarebbe la coda quindi partendo dal basso ci stampa gli ultimi 5

print(df2.head(5)) #! sarebbe la testa quindi partendo dall' inizio ci stampa i primi 5



