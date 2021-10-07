import pytest
from functions import suma

def test_suma_1(): 
    assert suma(3, 4) == 7
def test_suma_2(): 
    assert suma(3, -4) == -1
def test_suma_3(): 
    assert suma(3, -3) == 0