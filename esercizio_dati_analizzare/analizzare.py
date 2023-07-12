import xlrd, statistics,collections

from collections import Counter

nome_file = "C:/Users/Oba 9/Desktop/Generation/Pyton/Python/esercizio_dati_analizzare/dati_da_analizzare.xls"

apri = xlrd.open_workbook(nome_file)

foglio = apri.sheet_by_index(0)


#! printa tutto il foglio     
# for row in range(foglio.nrows):
#     for column in range(foglio.ncols):
#         print(foglio.cell(row, column).value)

#! Usando Set per stampare i non duplicati all' interno della colonna E quella di genere
# stringhe_differenti = set(colonna_genere)
# for stringa in stringhe_differenti:
#     print(stringa)
# unica_stringa = "".join(stringa)
# print(unica_stringa.count(unica_stringa))

colonna_genere = foglio.col_values(4)
print(colonna_genere)


#? Codice Dario

# import xlrd, statistics, collections
# from collections import Counter

nome_file= "C:/Users/Oba 9/Desktop/Generation/Pyton/Python/esercizio_dati_analizzare/dati_da_analizzare.xls"
workbook=xlrd.open_workbook(nome_file)
foglio = workbook.sheet_by_index(0)
for riga in range(0,1):
    for colonna in range(foglio.ncols):
        print(foglio.cell(riga, colonna).value)
colonna_genere=foglio.col_values(4)
colonna_paese=foglio.col_values(6)

print(colonna_genere)
conta_male=0
conta_female=0
for e in colonna_genere:
    if "Male" in colonna_genere:
        conta_male+=1
        # print(conta_male)
    elif "Female" in colonna_genere:
        conta_female+=1
        print(conta_female)
print(conta_male)
print(conta_female)
print(colonna_genere.count("Male"))
print(colonna_genere.count("Female"))

conta_genere = Counter(colonna_genere)
lista_genere = [(elemento, conta_genere[elemento]) for elemento in conta_genere]

print(lista_genere)

conta_paese = Counter(colonna_paese)
lista_paese = [(elemento, conta_paese[elemento]) for elemento in conta_paese]
print(lista_paese)



