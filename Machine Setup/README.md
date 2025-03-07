# Configuración de la Máquina de Turing para Fibonacci

Este documento describe la configuración de la Máquina de Turing utilizada para calcular la sucesión de Fibonacci. La configuración está almacenada en el archivo `turing_c.json`, que define los estados, transiciones y reglas de operación de la máquina.

---

## Estructura del Archivo `turing_c.json`
El archivo está estructurado en **tres secciones principales**:

1. **Definición de Estados**
2. **Estados Inicial y Final**
3. **Reglas de Transición**

---

## 🔹 1️⃣ Definición de Estados
```json
"estados": [
  "q0",
  "qCheck",
  "qSum",
  "qUpdate",
  "qDecrement",
  "qAccept"
]
```
Esta sección define los estados de la Máquina de Turing:
- `q0` → Estado inicial, verifica si `n ≤ 2`.
- `qCheck` → Verifica si el contador (`n`) es mayor que 0.
- `qSum` → Realiza la suma de `Tape2` y `Tape3`.
- `qUpdate` → Actualiza los valores en la cinta.
- `qDecrement` → Reduce el contador `n`.
- `qAccept` → Estado final (cuando el cálculo termina).

---

## 🔹 2️⃣ Estados Inicial y Final
```json
"e_ini": "q0",
"e_end": ["qAccept"]
```
- `e_ini`: Define que la máquina **siempre empieza en `q0`**.
- `e_end`: Define que el estado de **aceptación (final)** es `qAccept`.

---

## 🔹 3️⃣ Reglas de Transición
Cada estado tiene condiciones o acciones que determinan el siguiente estado de la máquina.

### Estado Inicial (`q0`)
```json
"q0": {
  "condicion": "IF_N_LE_2",
  "si_cumple": "qAccept",
  "si_no_cumple": "qCheck"
}
```
- **Si `n ≤ 2`**, la máquina salta a `qAccept` (termina).
- **Si `n > 2`**, pasa a `qCheck` para continuar.

### Verificación (`qCheck`)
```json
"qCheck": {
  "condicion": "IF_COUNTER_GT_0",
  "si_cumple": "qSum",
  "si_no_cumple": "qAccept"
}
```
- **Si `n > 0`**, pasa a `qSum`.
- **Si `n ≤ 0`**, termina en `qAccept`.

### Suma (`qSum`)
```json
"qSum": {
  "accion": "SUM_TAPE2_TAPE3_TO_TAPE4",
  "siguiente": "qUpdate"
}
```
- **Realiza la operación:** `Tape4 = Tape2 + Tape3`.
- **Luego, pasa a `qUpdate`**.

### Actualización (`qUpdate`)
```json
"qUpdate": {
  "accion": "TAPE2_EQUALS_TAPE3_AND_TAPE3_EQUALS_TAPE4",
  "siguiente": "qDecrement"
}
```
- **Desplaza los valores en la cinta:**
  - `Tape2 ← Tape3`
  - `Tape3 ← Tape4`
- Luego, pasa a `qDecrement`.

###  Decremento (`qDecrement`)
```json
"qDecrement": {
  "accion": "COUNTER_MINUS_1",
  "siguiente": "qCheck"
}
```
- **Resta 1 al contador `n`**.
- **Regresa a `qCheck`**.

###  Estado Final (`qAccept`)
```json
"qAccept": {
  "accion": "STOP"
}
```
- **Detiene la ejecución de la máquina.**

---

##  Resumen en Tabla
| Estado       | Condición / Acción                        | Siguiente Estado |
|-------------|---------------------------------|-----------------|
| `q0`       | `IF_N_LE_2` → `qAccept` | `qCheck` si `n > 2` |
| `qCheck`   | `IF_COUNTER_GT_0` → `qSum` | `qAccept` si `n ≤ 0` |
| `qSum`     | `SUM_TAPE2_TAPE3_TO_TAPE4` | `qUpdate` |
| `qUpdate`  | `TAPE2_EQUALS_TAPE3_AND_TAPE3_EQUALS_TAPE4` | `qDecrement` |
| `qDecrement` | `COUNTER_MINUS_1` | `qCheck` |
| `qAccept`  | `STOP` | - |

---

##  Conclusión
Este archivo define la Máquina de Turing para calcular Fibonacci mediante **estados y transiciones bien estructurados**. Su diseño permite representar la lógica del cálculo de Fibonacci de manera sencilla y eficiente.

