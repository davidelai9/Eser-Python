
# ! Sara potrebbe chiedervi se avete aperto file excel in python


import xlrd



file_da_leggere = "C:/Users/Oba 9/Desktop/Generation/Pyton/Python/esercizio_dati_analizzare/dati_da_analizzare.xls"

work_book = xlrd.open_workbook(file_da_leggere)

work_sheet = work_book.sheet_by_index(0)  #? mi trova il primo foglio del file tramite l'index 0 

numero_righe = work_sheet.nrows #? mi fornisce il numero di righe

numero_colonne = work_sheet.ncols #? mi fornice il numero delle colonne

nome_foglio = work_sheet.name #? mi restituisce il nome del foglio

# print(work_sheet.row_values(11))  #? ti fa vedere la dodicesima riga cosa contiene perchè l'indice parte da zero cosi come per le colonne

contenuto = []
for riga in range(numero_righe):
    contenuto.append(work_sheet.row_values(riga))
    # print(work_sheet.row_values(riga))

print(contenuto[100]) # ottieni la riga cento

gender = contenuto[100][4]

print(gender)