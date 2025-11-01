# Plan de Pruebas – Módulo Validador de ISBN

**Alumnos:** •García Páez David Israel
             •Sanchez Rodriguez Alondra Abigail
             •Hernández Herrera Cristhian Daniel
             •Flores Verdín Leonardo Javier
             •García Morales Juan Ramón
             •Moreno Sicsik Valeria

## Objetivo general

Diseñar y ejecutar una suite de pruebas que valide la correcta funcionalidad, robustez y pureza del módulo `isbn.py`, encargado de normalizar y validar códigos ISBN-10 e ISBN-13.  
El plan asegura que las pruebas cubran tanto los casos esperados (happy path) como los errores (unhappy path), utilizando técnicas de **caja negra, caja blanca, particiones de equivalencia, análisis de fronteras y dobles de prueba.

## Alcance

El alcance abarca todas las funciones puras del módulo:

| Función | Descripción | Tipo de prueba |
|----------|--------------|----------------|
| `normalize_isbn(cadena)` | Elimina espacios y guiones, valida caracteres permitidos. | Caja negra / Frontera |
| `is_valid_isbn10(cadena)` | Verifica el algoritmo ISBN-10 (checksum con pesos 10–1). | Caja negra / Blanca |
| `is_valid_isbn13(cadena)` | Verifica el algoritmo ISBN-13 (pesos 1 y 3 alternos). | Caja negra / Blanca |
| `detect_isbn(cadena)` | Determina si una entrada es ISBN-10, ISBN-13 o inválida. | Caja negra / Blanca |

Quedan fuera de alcance:
- Pruebas de rendimiento o estrés.
- Integración con servicios externos (no aplica en este proyecto).

## Supuestos

- Las entradas deben ser cadenas de texto (str), otras clases de datos serán tratadas como inválidas.  
- El módulo no interactúa con el sistema ni archivos (sin efectos secundarios).  
- Los ISBN de ejemplo se asumen reales y tomados de fuentes válidas.  
- El entorno de ejecución es Python 3.13+ con `pytest` y `pytest-cov`.

---

## Riesgos identificados

| Riesgo | Impacto | Mitigación |
|--------|----------|------------|
| No alcanzar 90% de cobertura | Medio | Añadir casos que cubran errores y validaciones. |
| Casos límite no detectados | Medio | Aplicar análisis de fronteras y property testing. |
| Errores en formato de entrada | Bajo | Uso de `normalize_isbn()` previo a validación. |
| Falsos positivos en checksum | Bajo | Pruebas cruzadas de ISBN válidos e inválidos. |

### Particiones de Pruebas

## ISBN-10

| Partición | Descripción | Ejemplo | Resultado esperado |
|------------|--------------|----------|---------------------|
| Válido (solo dígitos) | ISBN correcto de 10 dígitos | `"0306406152"` | `True` |
| Válido con ‘X’ final | ‘X’ representa valor 10 | `"0-8044-2957-X"` | `True` |
| Inválido por checksum | Suma no divisible entre 11 | `"0306406153"` | `False` |
| Inválido por longitud | Menor o mayor a 10 dígitos | `"030640615"` | `False` |
| Inválido por carácter | Contiene letras o símbolos | `"03064A6152"` | Excepción |

## ISBN-13

| Partición | Descripción | Ejemplo | Resultado esperado |
|------------|--------------|----------|---------------------|
| Válido | 13 dígitos, checksum correcto | `"9780306406157"` | `True` |
| Inválido por checksum | Suma no divisible entre 10 | `"9780306406158"` | `False` |
| Inválido por longitud | Menor o mayor a 13 dígitos | `"978030640615"` | `False` |
| Inválido por carácter | Letras o símbolos no permitidos | `"97803A6406157"` | Excepción |


## Análisis de fronteras

| Tipo | Límite inferior | Valor de frontera | Límite superior | Resultado esperado |
|------|-----------------|------------------|-----------------|---------------------|
| ISBN-10 | 9 dígitos | 10 dígitos | 11 dígitos | Solo 10 dígitos válidos |
| ISBN-13 | 12 dígitos | 13 dígitos | 14 dígitos | Solo 13 dígitos válidos |
| Cadena vacía | `""` | - | - | Inválido |
| Con guiones/espacios | `"0-306-40615-2"` | `"0306406152"` | - | Normalizado correctamente |

---

## Métricas objetivo

| Métrica | Objetivo | Estado actual | Comentario |
|----------|-----------|----------------|-------------|
| Cobertura de líneas | ≥ 90% | 81% | Aumentar con casos de error |
| Cobertura de ramas | ≥ 85% | 75% | Parcialmente cumplido |
| Casos totales | ≥ 15 | 19 | ✅ Cumplido |
| Casos exitosos | 100% | 19/19 | ✅ Cumplido |

---

## Estrategia de ejecución

1. Ejecutar localmente con:
   ```bash
   pytest --cov=src --cov-branch --cov-report=html
   ```

### Herramientas y entorno
**Lenguaje:** Python 3.13.2
**Framework de pruebas:** pytest 8.4.2
**Cobertura:** pytest-cov 7.0.0
**Editor:** Visual Studio Code
**Repositorio:** GitHub con ramas e issues
**CI/CD:** GitHub Actions (Ubuntu-latest)

### Conclusión

El plan de pruebas garantiza que el módulo isbn.py se evalúe de forma completa, sistemática y reproducible.
Las pruebas cubren los casos más críticos y los límites definidos en los algoritmos ISBN-10 e ISBN-13, logrando un nivel de confianza alto en su correcto funcionamiento.
El uso de integración continua asegura trazabilidad, evidencia y automatización constante del proceso de validación.
