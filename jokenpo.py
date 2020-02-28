#!/usr/bin/env python3
# jokenpo.py
from objetos import Objeto

def jokeenpoo(jogardor1: Objeto, jogardor2: Objeto) -> str:
    return str(jogardor1.contra(jogardor2))
        