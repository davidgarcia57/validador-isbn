import pytest
from src.isbn import normalize_isbn, detect_isbn

"""
Pruebas de propiedades (property-based testing) y uso de un stub simple.
"""

def test_normalize_isbn_idempotente():

    ejemplo = "978-0-306-40615-7"
    resultado_1 = normalize_isbn(ejemplo)
    resultado_2 = normalize_isbn(resultado_1)
    assert resultado_1 == resultado_2


def test_detect_isbn_estable_frente_a_formato_equivalente():

    isbn_con_guiones = "978-3-16-148410-0"
    isbn_sin_guiones = "9783161484100"
    assert detect_isbn(isbn_con_guiones) == detect_isbn(isbn_sin_guiones)


#Ejemplo de stub
class StubLogger:

    def __init__(self):
        self.mensajes = []
    def info(self, mensaje):
        self.mensajes.append(mensaje)

def test_stub_logger_funciona():
    
    logger = StubLogger()
    logger.info("Validando ISBN")
    assert "Validando ISBN" in logger.mensajes
