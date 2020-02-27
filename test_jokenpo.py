#!/usr/bin/env python3
# test_jokenpo.py
import jokenpo as jp
from constantes import PEDRA, PAPEL, TESOURA, EMPATE
from objetos import Pedra, Tesoura, Papel


def test_pedra_tesoura():
    assert jp.jokeenpoo(Pedra(), Tesoura()) == PEDRA

def test_pedra_papel():
    assert jp.jokeenpoo(Pedra(), Papel()) == PAPEL

def test_pedra_pedra():
    assert jp.jokeenpoo(Pedra(), Pedra()) == EMPATE


def test_tesoura_papel():
    assert jp.jokeenpoo(Tesoura(), Papel()) == TESOURA

def test_tesoura_tesoura():
    assert jp.jokeenpoo(Tesoura(), Tesoura()) == EMPATE

def test_tesoura_pedra():
    assert jp.jokeenpoo(Tesoura(), Pedra()) == PEDRA


def test_papel_tesoura():
    assert jp.jokeenpoo(Papel(), Tesoura()) == TESOURA

def test_papel_papel():
    assert jp.jokeenpoo(Papel(), Papel()) == EMPATE 

def test_papel_pedra():
    assert jp.jokeenpoo(Papel(), Pedra()) == PAPEL
