import time

class Attivita():
    def __init__(self, descrizione:str, inizio:str, fine, note:str):
        self.descrizione = descrizione
        self.inizio = inizio 
        self.fine = fine
        self.note = note
    
    def stampa(self):
        print("*"*17)
        print(self.descrizione.upper())
        print(f"Inizio: {self.inizio}")
        if self.fine:
            print(f"Fine: {self.fine}")
        else:
            print(f"Fine: da fare")
        print(f"Note: {self.note}")
        print("*"*17)
    
    def riassunto(self):
        if self.fine:
            stringa = f"{self.descrizione.upper()} {self.inizio} {self.fine} {self.note[:20]}"
        else:
            stringa = f"{self.descrizione.upper()} {self.inizio} Da fare {self.note[:20]}"
        return stringa
    
    def finisci(self):
        self.fine = time.strftime(format("%Y-%m-%d"))
    
    def is_closed(self):
        ''' Restituisce vero in caso l'attività sia finita altrimenti restituisce falso '''
        if self.fine:
            return True
        else:
            return False