"""
Módulo isbn.py
--------------
Este módulo implementa funciones puras para validar y detectar ISBN-10 e ISBN-13.

Requisitos:
- Sin efectos secundarios.
- Sin librerías externas.
- Determinista (misma entrada = misma salida).
- Soporta entradas con guiones o espacios.
"""

def normalize_isbn(isbn_crudo: str) -> str:

    if not isbn_crudo:
        raise ValueError("La cadena de ISBN está vacía o es None.")

    #Eliminar espacios y guiones
    isbn_normalizado = isbn_crudo.replace("-", "").replace(" ", "")

    #Validar caracteres permitidos
    if not isbn_normalizado[:-1].isdigit():
        raise ValueError("Los primeros caracteres deben ser dígitos.")
    
    #Si hay una 'X' solo puede estar al final y representa un 10 en ISBN-10
    if "X" in isbn_normalizado[:-1]:
        raise ValueError("La 'X' sólo se permite en la última posición para ISBN-10.")

    #Los caracteres válidos finales son digitos o 'X'
    if not (isbn_normalizado[-1].isdigit() or isbn_normalizado[-1] == "X"):
        raise ValueError("Último carácter inválido en ISBN.")

    return isbn_normalizado


def is_valid_isbn10(isbn: str) -> bool:

    try:
        isbn_limpio = normalize_isbn(isbn)
    except ValueError:
        return False

    if len(isbn_limpio) != 10:
        return False

    total = 0
    for i in range(9):
        if not isbn_limpio[i].isdigit():
            return False
        total += int(isbn_limpio[i]) * (10 - i)

    # Último carácter puede ser 'X' = 10
    ultimo_caracter = 10 if isbn_limpio[-1] == "X" else int(isbn_limpio[-1])
    total += ultimo_caracter

    return total % 11 == 0


def is_valid_isbn13(isbn: str) -> bool:

    try:
        isbn_limpio = normalize_isbn(isbn)
    except ValueError:
        return False

    if len(isbn_limpio) != 13 or not isbn_limpio.isdigit():
        return False

    total = 0
    for i, caracter in enumerate(isbn_limpio):
        digito = int(caracter)
        if i % 2 == 0:
            total += digito
        else:
            total += digito * 3

    return total % 10 == 0


def detect_isbn(isbn: str) -> str:

    try:
        normalized = normalize_isbn(isbn)
    except ValueError:
        return "INVALIDO"

    if len(normalized) == 10 and is_valid_isbn10(isbn):
        return "ISBN-10"
    elif len(normalized) == 13 and is_valid_isbn13(isbn):
        return "ISBN-13"
    else:
        return "INVALIDO"
