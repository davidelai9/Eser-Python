# __init__ = dundermethods -> metodi speciali 

class Animale:
    def __init__(self, nome, anni):
        self.nome = nome
        self.anni = anni
    
    def mangia(self):
        print(f"{self.nome} sta mangiando..")  
    
    def verso(self):
        pass

class Cane(Animale):
    def __init__(self, nome, anni, razza):
        super().__init__(nome,anni) 
        self.razza = razza
    def verso(self):
        print("sto abbaiando..")

class Gatto(Animale):
    def __init__(self, nome, anni, razza):
        super().__init__(nome,anni)
        self.razza = razza
    def verso(self):
        print("sto miagolando..")

anim = Animale("King",12)

anim2 = Animale("Ade",10)

print(f"il nome è {anim.nome}")
print("l'età è " + str(anim.anni))
print(f"l'età è {anim.anni}")
anim.nome = "Ares"
print(anim.nome)
print(anim2.nome)

anim.mangia()

# sotto classi

cane1 = Cane("Fido",2,"Bulldog")

gatto1 = Gatto("Tom",3,"Siriano")

print(cane1.nome)
print(gatto1.nome)

cane1.verso()
gatto1.verso()

