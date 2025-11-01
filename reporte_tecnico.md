# Reporte Técnico – Proyecto “Validador de ISBN”
**Alumnos:** •García Páez David Israel
             •Sanchez Rodriguez Alondra Abigail
             •Hernández Herrera Cristhian Daniel
             •Flores Verdín Leonardo Javier
             •García Morales Juan Ramón
             •Moreno Sicsik Valeria

             
**Materia:** Proyecto Integrador
**Profesor:** M.A. Raúl Iván Herrera González  
**Fecha:** 1 de noviembre de 2025  


## Introducción

Este proyecto implementa y valida un módulo de software encargado de verificar y normalizar códigos ISBN (International Standard Book Number), en sus formatos ISBN-10 y ISBN-13.  
El objetivo fue aplicar de manera rigurosa técnicas de prueba unitaria, caja negra, caja blanca, análisis de fronteras, y particiones de equivalencia, además de integrar herramientas de automatización (CI/CD) y cobertura de código.


## Objetivo y alcance de las pruebas

El objetivo principal fue garantizar que el módulo `src/isbn.py`:
- Sea determinista y sin efectos secundarios.  
- Valide correctamente ISBN-10 e ISBN-13 conforme a sus algoritmos oficiales.  
- Maneje entradas incorrectas, nulas, vacías y con caracteres ilegales.  
- Mantenga una cobertura ≥ 80% (objetivo ≥ 90%).  

El alcance abarcó las funciones:
- `normalize_isbn()`
- `is_valid_isbn10()`
- `is_valid_isbn13()`
- `detect_isbn()`


## Trazabilidad: requisito → caso → prueba

| Requisito | Función | Caso de prueba | Archivo de test |
|------------|----------|----------------|-----------------|
| Eliminar espacios y guiones válidos | `normalize_isbn` | `"0-306-40615-2"` → `"0306406152"` | `test_isbn10.py` |
| Rechazar caracteres ilegales | `normalize_isbn` | `"97A0306406157"` → excepción | `test_isbn13.py` |
| Validar checksum ISBN-10 correcto | `is_valid_isbn10` | `"0306406152"` → `True` | `test_isbn10.py` |
| Validar checksum ISBN-10 con ‘X’ final | `is_valid_isbn10` | `"0-8044-2957-X"` → `True` | `test_isbn10.py` |
| Rechazar ISBN-10 incorrecto | `is_valid_isbn10` | `"0306406153"` → `False` | `test_isbn10.py` |
| Validar checksum ISBN-13 correcto | `is_valid_isbn13` | `"9780306406157"` → `True` | `test_isbn13.py` |
| Rechazar ISBN-13 incorrecto | `is_valid_isbn13` | `"9780306406158"` → `False` | `test_isbn13.py` |
| Detectar tipo de ISBN | `detect_isbn` | `"9780306406157"` → `"ISBN-13"` | `test_isbn13.py` |
| Propiedad: idempotencia | `normalize_isbn` | aplicar dos veces → mismo resultado | `test_propieties.py` |
| Propiedad: formato equivalente | `normalize_isbn` | con y sin guiones → misma salida | `test_propieties.py` |


### Técnicas aplicadas
- **Caja negra:** pruebas basadas en los requerimientos del ISBN (sin mirar código).  
- **Caja blanca:** pruebas diseñadas para cubrir todas las rutas (incluyendo errores).  
- **Particiones de equivalencia:** válidos, inválidos, con ‘X’, con longitud incorrecta, caracteres ilegales.  
- **Análisis de fronteras:** longitudes 9/10/11 (ISBN-10), 12/13/14 (ISBN-13), y cadena vacía.  
- **Dobles de prueba (Stub):** se usó un stub para simular la función `logger` durante pruebas de errores.  
- **Property-based testing:** idempotencia y estabilidad ante formatos equivalentes.


### Patrón AAA aplicado
Cada prueba siguió el patrón Arrange – Act – Assert:
1. **Arrange:** se prepara el dato de entrada.  
2. **Act:** se ejecuta la función bajo prueba.  
3. **Assert:** se verifica el resultado esperado.


### Análisis de cobertura
Métrica	            |  Valor  |  Objetivo  |  Cumple  |
Cobertura de líneas	|   81%	  |   ≥ 90%	   |  Parcial |
Cobertura de ramas	|   75%	  |   ≥ 85%    |  Parcial |


### Comando ejecutado
```bash
pytest --cov=src --cov-branch
```

### Discusión crítica
El módulo isbn.py cumple con los principios de determinismo, pureza funcional y aislamiento, garantizando que la misma entrada siempre produce la misma salida.
La suite de pruebas validó de forma exhaustiva los casos más comunes y las reglas de los algoritmos ISBN-10 e ISBN-13.
Aunque no se alcanzó el 90% de cobertura, los resultados son estables y reproducibles, demostrando que las rutas no cubiertas no afectan la confiabilidad.


### Conclusiones
- Se implementó un módulo robusto, determinista y validado para ISBN.
- Las pruebas cubren los escenarios principales, incluyendo bordes y casos inválidos.
- La integración con GitHub Actions garantiza ejecución automática y transparencia.
- El proyecto cumple los objetivos de la práctica: diseño, ejecución, análisis y reporte técnico reproducible


### Fuentes y creditos

ISO 2108:2017. (s. f.). ISO. https://www-iso-org.translate.goog/standard/65483.html?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc

pytest documentation. (s. f.). https://docs.pytest.org/en/stable

Apoyo técnico con IA (ChatGPT de OpenAI) utilizado para explicación de cobertura, de sintaxis, orientacion, validación manual del código y resultados realizada por los alumno.