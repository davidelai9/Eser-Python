# #? Tipi fondamentali :
#! Serie
#! Dataframe

import pandas as pd

serie1 = pd.Series([1,'2',False,0.,(11,22,33)])

# print(serie1[0])

dati= [11,22,33,44,55,66]
indice= ["A","B","C","D","E","F"]
serie2 = pd.Series(data=dati, index=indice)

# print(serie2)

serie3 = pd.Series({'AAA':0.5, 'BBB': -1, 'CCC':15})

# print(serie3[0])

# ? cicliamo

for key, value in serie3.items():
    print(key,value)

#? cicliamo diversamente

serie4 = serie3[['AAA','CCC']]

print(serie4)





