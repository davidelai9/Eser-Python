import time, os, json
from attivita import Attivita


def menu_iniziale():
    """
    Stampa il menù iniziale del programma
    """
    os.system("cls")
    print("*"*30)
    print("Fai una scelta")
    print("1: Crea un'attività")
    print("2: Modifica un'attività")
    print("3: Chiudi un'attività")
    print("4: Visualizzia le attività da finire")
    print("5: Visualizzia le attività finite")
    print("6: Cerca un attività")
    print("7: Chiudi il programma")
    print("*"*30)

def salva(lista):
    ''' Salva su un file tutta la lista passata '''
    with open("salvataggio.json", "w") as f:
        json.dump([att.__dict__ for att in lista],f)

def carica():
    '''Prende dal file un salvataggio e ritorna su una lista gli oggetti del file '''
    lista = []
    try:
        with open("salvataggio.json", "r") as f:
            dizionari = json.load(f)
            for dizionario in dizionari:
                oggetto = Attivita(dizionario["descrizione"], dizionario["inizio"], dizionario["fine"], dizionario["note"])
                lista.append(oggetto)
    except FileNotFoundError:
        print("Non ho trovato alcun salvataggio, assicurati che il file sia nella stessa cartella del programma")
    """except:
        print("Qualcosa è andato storto")"""
    
    return lista

def crea_attivita(descrizione, note):
    """
    Crea un'attivita e la aggiunge all'agenda
    """
    
    att = Attivita(descrizione, time.ctime(), None, note)
    agenda.append(att)
    salva(agenda)

def stampa_agenda(lista):
    ''' Stampa le attività all'interno della lista'''
    i = 1
    for attivita in lista:
        print(f"{i}: {attivita.riassunto()}")
        i += 1

def modifica_attivita():
    """
    Procedura per modifica la descrizione o le note d
    """
    while agenda:
        while True:
            try:
                os.system("cls")
                stampa_agenda(agenda)
                indice = int(input("Quale attività vuoi modificare? (premi 0 per tornare al menu iniziale) ")) # ci sono due problemi qua
                att = agenda[indice-1]
                break
            except ValueError:
                print("Mi devi dare un numero")
            except IndexError:
                print(f"Ci sono solo {len(agenda)} attività tra cui scegliere, scegli un numero adatto")
        
        if indice == 0:
            break
        else:
            while True:
                scelta = input("Cosa vuoi modificare:\n1: Descrizione\n2: Note\n3:Torna alla scelta\n")
                if scelta == "1":
                    modifica = input("Dammi la nuova descrizione: ")
                    att.descrizione = modifica
                    salva(agenda)
                    print("Ho modificato la descrizione")
                elif scelta == "2":
                    modifica = input("Dammi la nuova nota: ")
                    att.note = modifica
                    salva(agenda)
                    print("Ho modificato la nota")
                elif scelta == "3":
                    break
                else:
                    print("Puoi scegliere solo 1, 2 o 3")

    if not agenda:
        input("Non hai attività premi INVIO per tornare al menu iniziale")

def da_finire():
    ''' restituisce una lista contenente le attività da finire'''
    return list(filter(lambda x : not x.is_closed(), agenda))

def finite():
    ''' restituisce una lista contenente le attività finite'''
    return list(filter(lambda x : x.is_closed(), agenda))


def finisci_attivita():
    while da_finire():  
        att_da_finire = da_finire()
        while True:
            try:
                os.system("cls")

                stampa_agenda(att_da_finire)

                indice = int(input("Quale attività vuoi finire? (premi 0 per tornare al menu iniziale) "))

                att = att_da_finire[indice -1]
                break
            except ValueError:
                print("Mi devi dare un numero")
            except IndexError:
                print(f"Ci sono solo {len(agenda)} attività tra cui scegliere, scegli un numero adatto")
        
        if indice == 0:
            break
        else:
            while True:
                scelta = input("Sei sicuro di voler chiudere l'attività?  si/no ")
                if scelta == "si":
                    att.finisci()
                    salva(agenda)
                    input("Ho chiuso l'attività, premi invio per tornare al menù precedente ")
                    break
                elif scelta == "no":
                    break
                else:
                    print("Non hai digitato ne si ne no")


    if not da_finire():
        input("Non hai attività premi INVIO per tornare al menu iniziale")


def ricerca():
    os.system("cls")
    chiave = input("Dammi un criterio di ricerca: ").lower()

    for att in agenda:
        if chiave in att.descrizione.lower():
            att.stampa()

            input("Per continuare la ricerca premi invio: ")

    input("Non ho trovato niente premi invio per tornare al menù principale")        
        
    


agenda = carica()
while True:
    menu_iniziale()
    scelta = input("\nCosa vuoi fare?  ")
    if scelta == "1": #Creare attivita
        os.system("cls")
        descrizione = input("Cosa devi fare? ") 
        note = input("Se vuoi aggiungi delle note: ") 
        crea_attivita(descrizione, note)
    elif scelta == "2": #Modificare attivita
        modifica_attivita()
    elif scelta == "3": #Finire attivita
        finisci_attivita()  
    elif scelta == "4": #Visualizza da finire
        os.system("cls")
        stampa_agenda(da_finire())
        input("premi invio per tornare al menu iniziale")
    elif scelta == "5": #Visualizza finite
        os.system("cls")
        stampa_agenda(finite())
        input("premi invio per tornare al menu iniziale")
    elif scelta == "6": #Ricerca
        ricerca()
    elif scelta == "7": #Uscita dal programma
        break
    else:
        print("Non hai scelto tra 1-7")
