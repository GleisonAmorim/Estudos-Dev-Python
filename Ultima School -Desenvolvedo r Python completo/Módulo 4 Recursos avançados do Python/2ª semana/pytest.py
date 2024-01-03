import pytest

def multiplicacao(x,y):
    return x*y

def test_multiplicacao():
    assert multiplicacao(10,2)==21