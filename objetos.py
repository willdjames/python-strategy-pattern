# objetos.py
from constantes import PEDRA, PAPEL, TESOURA, EMPATE

class Pedra:

    def __init__(self):
        self.sinal = PEDRA
    

    def contra(self, objeto):
        resultado = EMPATE

        if objeto.sinal == TESOURA:
            resultado = self.sinal

        elif objeto.sinal == PAPEL:
            resultado = PAPEL
        
        return resultado


class Tesoura:

    def __init__(self):
        self.sinal = TESOURA

    def contra(self, objeto):
        resultado = EMPATE
        
        if objeto.sinal == PAPEL:
            resultado = self.sinal

        elif objeto.sinal == PEDRA:
            resultado = PEDRA
        
        return resultado


class Papel:

    def __init__(self):
        self.sinal = PAPEL
    
    def contra(self, objeto):
        resultado = EMPATE
        
        if objeto.sinal == PEDRA:
            resultado = self.sinal
        
        elif objeto.sinal == TESOURA:
            resultado = TESOURA
        
        return resultado