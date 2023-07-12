# #! Se volessi importare tutte le classi di un modulo si fa cosi:
  #? from unittest import * -> è un esempio ma funziona con tutti i moduli


import unittest

#? questo è il secondo modo invece di scrivere from richiamiamo la classe padre che proviene però da un altro modulo;
#!Guarda giù

def conta_vocali(parola):
    if len(parola) == 0:
        return 0
    else:
        conta = 0
        for vocale in parola:
            if vocale in "aeiouAEIOU":
                conta += 1

        return conta
    
#! Pallino Pallino F = F.. vanno in ordine alfabetico non in ordine di errore 


class TestContaVocali(unittest.TestCase): # tutti i metodi all'interno devo cominciare con " test_ "
    
    def test_stringa_vuota(self):

        self.assertEqual(conta_vocali(''),0)      #metodo che restituisce Vero o Falso se i due valori sono uguali o meno
    
    def test_argomento_stringa(self):
        self.assertIsInstance(conta_vocali("ciao"),int) #accetta 2 valori e se il primo è un istanza del secondo restituisce vero

    def test_conteggio_vocali(self):
        self.assertEqual(conta_vocali("ciao"),3) 
        self.assertEqual(conta_vocali("palla"),2) 
        self.assertEqual(conta_vocali("pizza"),2) 
        self.assertEqual(conta_vocali("aiuola"),5)     


if __name__ == "__main__":
    unittest.main()