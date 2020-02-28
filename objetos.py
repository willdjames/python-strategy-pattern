#!/usr/bin/env python3
# objetos.py
from __future__ import annotations
from abc import ABC, abstractmethod
from constantes import PEDRA, PAPEL, TESOURA, EMPATE

class Objeto(ABC):

    sinal: str

    @abstractmethod
    def contra(self, objeto: Objeto) -> str:
        pass


class Pedra(Objeto):

    def __init__(self) -> None:
        self.sinal = PEDRA
    
    def contra(self, objeto: Objeto) -> str:
        resultado = EMPATE

        if objeto.sinal == TESOURA:
            resultado = self.sinal

        elif objeto.sinal == PAPEL:
            resultado = PAPEL
        
        return resultado


class Tesoura(Objeto):

    def __init__(self) -> None:
        self.sinal = TESOURA

    def contra(self, objeto: Objeto) -> str:
        resultado = EMPATE
        
        if objeto.sinal == PAPEL:
            resultado = self.sinal

        elif objeto.sinal == PEDRA:
            resultado = PEDRA
        
        return resultado


class Papel(Objeto):

    def __init__(self) -> None:
        self.sinal = PAPEL
    
    def contra(self, objeto: Objeto) -> str:
        resultado = EMPATE
        
        if objeto.sinal == PEDRA:
            resultado = self.sinal
        
        elif objeto.sinal == TESOURA:
            resultado = TESOURA
        
        return resultado