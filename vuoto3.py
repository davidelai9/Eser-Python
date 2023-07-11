# try:

class Attivita():
    def __init__(self,descrizione,inizio,fine,note):
        self.descrizione = descrizione
        self.inizio = inizio
        self.fine = fine
        self.note = note
    def stampa(self):
        print(self.descrizione)    
        
agenda = []
    
with open("prova.txt","r") as f:
    while True:
        a = f.readline()
        # print(a)
        if a != "":
            a  = a.strip()
            print(a)
            b = a.split("|")
            # print(b)
            attivita = Attivita(b[0],b[1],b[2],b[3])
            agenda.append(attivita)
        else:
            break    
            
agenda[0].stampa()
agenda[1].stampa()
agenda[2].stampa()
            

# except FileNotFoundError:
#     pass

