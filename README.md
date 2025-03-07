# Proyecto 1 - Simulación de Máquina de Turing para Fibonacci

## Descripción
Este proyecto implementa una **Máquina de Turing de una cinta** que simula el cálculo de la sucesión de Fibonacci. Adicionalmente, se realiza un **análisis empírico de rendimiento**, midiendo los tiempos de ejecución y generando gráficos de **complejidad asintótica (Big-O, Theta y Omega)**.

---

## Estructura del Proyecto

```
PROYECTO1-ALGORITMOS/
│── main.py                     # Punto de entrada principal
│── turing.py                   # Implementación de la Máquina de Turing
│── turing_c.json               # Archivo de configuración de la Máquina de Turing
│── README.md                   # Documentación del proyecto
│── .gitignore                  # Archivos a excluir en control de versiones
│── analisis/                    # Carpeta para análisis empírico
│    ├── analisiscomplejidad.py  # Script para análisis de complejidad
│    ├── tiempoAnalisis.py       # Script para medir tiempos de ejecución
│── __pycache__/                 # Caché de Python
```

---

## Instalación y Dependencias

### 1️⃣ Requisitos Previos
- **Python 3.x**
- **Bibliotecas necesarias**: numpy, matplotlib

Para instalar las dependencias, ejecutar:
```sh
pip install numpy matplotlib
```

---

## Ejecución del Proyecto

### 1️⃣ Simulación de la Máquina de Turing
Para ejecutar la simulación de Fibonacci:
```sh
python main.py
```
Esto carga la configuración desde `turing_c.json` y muestra el proceso paso a paso de la Máquina de Turing.

### 2️⃣ Medición de Tiempos de Ejecución
Para ejecutar la medición del tiempo de ejecución:
```sh
python analisis/tiempoAnalisis.py
```
Esto ejecutará pruebas con diferentes tamaños de entrada y generará datos de ejecución.

### 3️⃣ Análisis de Complejidad y Gráficos
Para generar los gráficos de complejidad:
```sh
python analisis/analisiscomplejidad.py
```
Esto generará gráficos de dispersión con la notación **Big-O, Theta y Omega** en `analisis/big_o_plot.png`.

---

## Funcionalidades Implementadas

### ✅ Entrada de Datos
- Permite ingresar la cadena de entrada en base a la convención establecida.

### ✅ Simulación de la Máquina de Turing
- Ejecuta una Máquina de Turing configurada en `turing_c.json`.
- Muestra paso a paso el estado de la cinta y la posición de la cabeza lectora.

### ✅ Análisis de Rendimiento
- Mide tiempos de ejecución para diferentes tamaños de entrada.
- Genera gráficos de dispersión con la notación **Big-O, Theta y Omega**.
- Ajusta los datos a una **regresión polinomial/exponencial**.

---

## Resultados

Una vez ejecutado el análisis, se generará un gráfico de complejidad
