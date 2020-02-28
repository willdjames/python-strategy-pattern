#!/usr/bin/env python3
# test_jokenpo.py
import jokenpo as jp
from constantes import PEDRA, PAPEL, TESOURA, EMPATE
from objetos import Pedra, Tesoura, Papel


def test_pedra_tesoura() -> None:
    assert jp.jokeenpoo(Pedra(), Tesoura()) == PEDRA

def test_pedra_papel() -> None:
    assert jp.jokeenpoo(Pedra(), Papel()) == PAPEL

def test_pedra_pedra() -> None:
    assert jp.jokeenpoo(Pedra(), Pedra()) == EMPATE


def test_tesoura_papel() -> None:
    assert jp.jokeenpoo(Tesoura(), Papel()) == TESOURA

def test_tesoura_tesoura() -> None:
    assert jp.jokeenpoo(Tesoura(), Tesoura()) == EMPATE

def test_tesoura_pedra() -> None:
    assert jp.jokeenpoo(Tesoura(), Pedra()) == PEDRA


def test_papel_tesoura() -> None:
    assert jp.jokeenpoo(Papel(), Tesoura()) == TESOURA

def test_papel_papel() -> None:
    assert jp.jokeenpoo(Papel(), Papel()) == EMPATE 

def test_papel_pedra() -> None:
    assert jp.jokeenpoo(Papel(), Pedra()) == PAPEL
