import pytest
from src.isbn import is_valid_isbn10

"""
Este archivo contiene pruebas unitarias para la función is_valid_isbn10.
Se diseñaron usando:
- Caja negra
- Particiones de equivalencia
- Análisis de fronteras
"""

#Particiones válidas
@pytest.mark.parametrize("isbn_valido", [
    "0-306-40615-2",   
    "0471958697",      
    "0306406152",      
    "0-8044-2957-X",   
])
def test_isbn10_valido(isbn_valido):
    assert is_valid_isbn10(isbn_valido) is True


#Particiones inválidas
@pytest.mark.parametrize("isbn_invalido", [
    "0306406153",   
    "030640615",    
    "03064061525",  
    "0X06406152",   
    "03064061A2",   
])
def test_isbn10_invalido(isbn_invalido):
    assert is_valid_isbn10(isbn_invalido) is False


#Fronteras
def test_isbn10_longitud_justo_en_borde():
    assert is_valid_isbn10("0306406152")  
    assert not is_valid_isbn10("030640615")   
    assert not is_valid_isbn10("03064061525") 
