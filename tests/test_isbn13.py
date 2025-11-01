import pytest
from src.isbn import is_valid_isbn13

"""
Pruebas unitarias para la función is_valid_isbn13.
Cubren casos válidos, inválidos, y fronteras de longitud/caracteres.
"""

# --- Casos válidos ---
@pytest.mark.parametrize("isbn_valido", [
    "9780306406157",
    "978-3-16-148410-0"
])
def test_isbn13_valido(isbn_valido):
    assert is_valid_isbn13(isbn_valido) is True


# --- Casos inválidos ---
@pytest.mark.parametrize("isbn_invalido", [
    "9780306406156",  # checksum incorrecto
    "978030640615",   # longitud 12
    "97803064061570", # longitud 14
    "97803064A6157",  # carácter ilegal
])
def test_isbn13_invalido(isbn_invalido):
    assert is_valid_isbn13(isbn_invalido) is False
