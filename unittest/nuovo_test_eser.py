import  unittest, random


def cifrario(stringa,numero):
    if len(stringa) == 0:
        return 0
    else:
        return "a"



class TestFunzione(unittest.TestCase):
    def test_01_stringa_vuota(self):
        self.assertEqual(cifrario("", 0),0)

    def test_02_verifica_input_stringa(self):
        self.assertIsInstance(cifrario("ciao",0),str)

    def test_03_verifica_input_lettera(self):
        self.assertTrue(cifrario("3",0))
        




if __name__ == '__main__':
    unittest.main()



# parola = input("Dammi una parola da decifrare: ").lower()

# numero = random.randint(3,5)



# def cifrario(stringa,numero):
#     lettere = []
#     for lettera in stringa:
#         shift = ord(lettera) + numero
#         lettere.append(shift)
        
#     return lettere
        
    
# print(cifrario(parola,numero))    

# def parola_nascosta(stringa):
#     lettere2 = []
#     for lettera in stringa:
#         shift = chr(lettera)
#         lettere2.append(shift)
#     return lettere2   

# parola_segreta = "".join(parola_nascosta(cifrario(parola,numero)))

# print(f"La parola cifrata è {parola_segreta}")


# def decifrario(stringa,numero):
#     lettere = []
#     for lettera in stringa:
#         shift = chr(ord(lettera) - numero)
#         lettere.append(shift)
#     return  "".join(lettere)

# print(f"Questa è la parola originale: {decifrario(parola_segreta, numero)}")    