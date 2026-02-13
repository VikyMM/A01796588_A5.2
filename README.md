# Actividad 5.2 – Ejercicio de programación 2 (Compute Sales)

## Descripción
Este proyecto implementa el programa `computeSales.py`, el cual calcula el costo total de ventas a partir de dos archivos JSON:
1) Un catálogo de precios (ProductList / priceCatalogue).
2) Un registro de ventas (Sales).

El programa:
- Calcula el total por venta (SALE) y el gran total.
- Maneja datos inválidos (productos no encontrados, campos faltantes o cantidades inválidas) sin detener la ejecución.
- Muestra resultados en pantalla y los guarda en `SalesResults.txt`.
- Incluye el tiempo de ejecución.

## Estructura del proyecto
- `computeSales.py` – Programa principal.
- `SalesResults.txt` – Archivo de salida generado.
- `TC1/`, `TC2/`, `TC3/` – Casos de prueba (archivos JSON).
- `evidence/` – Evidencias (capturas de ejecución, flake8 y pylint).

## Requisitos
- Python 3.x
- Paquetes:
  - flake8
  - pylint

Instalación:
```bash
python -m pip install flake8 pylint
## Evidencias

### 1️⃣ Análisis con flake8 (0 errores)
![Flake8](evidence/evidence_01.jpg)

### 2️⃣ Análisis con pylint (10.00/10)
![Pylint](evidence/evidence_02.jpg)

### 3️⃣ Ejecución TC1
![TC1](evidence/evidence_03.jpg)

### 4️⃣ Ejecución TC2
![TC2](evidence/evidence_04.jpg)

### 5️⃣ Ejecución TC3 (con manejo de errores)
![TC3](evidence/evidence_05.jpg)
