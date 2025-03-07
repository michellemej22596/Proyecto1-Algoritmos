import sys
import os
import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from turing import CintaUnicaTuring


CONFIG_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "turing_c.json"))


RESULTS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "results"))


os.makedirs(RESULTS_DIR, exist_ok=True)

def medir_tiempos(max_n):
    """Ejecuta la máquina para diferentes valores de n y mide el tiempo."""
    tiempos = []
    valores = list(range(1, max_n + 1))

    print("\n **Datos dprueba:**")
    for n in valores:
        inicio = time.perf_counter()
        maquina = CintaUnicaTuring(CONFIG_PATH, n)
        resultado, _ = maquina.run()
        fin = time.perf_counter()

        tiempo_total = fin - inicio
        tiempos.append(tiempo_total)
        print(f"  - Fibonacci({n}) = {resultado}, Tiempo: {tiempo_total:.8f} s")

    return valores, tiempos

def generar_dispersión(valores, tiempos):
    """Gráfico de dispersión."""
    scatter_path = os.path.join(RESULTS_DIR, "scatter_plot.png")
    plt.figure(figsize=(8, 5))
    plt.scatter(valores, tiempos, color='blue', label="Datos observados", alpha=0.7)
    plt.xlabel("Número de Fibonacci (n)")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.title("Tiempo de ejecución de la Máquina de Turing")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.savefig(scatter_path)
    plt.close()
    print(f" Imagen guardada: {scatter_path}")

def generar_regresión(valores, tiempos, grado=1):
    if len(valores) > 1:
        valores = valores[1:]  
        tiempos = tiempos[1:]  

    coeficientes = np.polyfit(valores, tiempos, deg=grado)
    polinomio = np.poly1d(coeficientes)
    valores_suavizados = np.linspace(min(valores), max(valores), 100)
    tiempos_predichos = polinomio(valores_suavizados)

    tiempos_ajustados = polinomio(valores)
    r2 = r2_score(tiempos, tiempos_ajustados)

    eq_str = " + ".join([f"{coef:.6f}x^{i}" if i > 0 else f"{coef:.6f}" for i, coef in enumerate(reversed(coeficientes))])
    
    regression_path = os.path.join(RESULTS_DIR, "regression_plot.png")
    plt.figure(figsize=(8, 5))
    plt.scatter(valores, tiempos, color='blue', label="Datos observados", alpha=0.7)
    plt.plot(valores_suavizados, tiempos_predichos, color='red', linewidth=2, label=f"Regresión grado {grado}")
    
    ecuacion_texto = f"$y = {eq_str}$\n$R^2 = {r2:.4f}$"
    plt.text(min(valores) + 2, max(tiempos) * 0.8, ecuacion_texto, fontsize=10, bbox=dict(facecolor='white', alpha=0.8))

    plt.xlabel("Número de Fibonacci (n)")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.title("Ajuste de regresión polinomial")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.savefig(regression_path)
    plt.close()
    
    print(f"\n **Ecuación de la regresión:**")
    print(f"   y = {eq_str}")
    print(f" **Coeficiente de determinación R²:** {r2:.4f}")
    print(f" Imagen guardada: {regression_path}")

def menu():
    """Menú interactivo para elegir qué análisis realizar."""
    while True:
        print("\n **Análisis Empírico**")
        print("1. Medir tiempos de ejecución")
        print("2. Generar gráfico de dispersión")
        print("3. Generar regresión polinomial")
        print("4. Ejecutar todo")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ").strip()
        
        if opcion == "1":
            valores, tiempos = medir_tiempos(100)
        elif opcion == "2":
            valores, tiempos = medir_tiempos(100)
            generar_dispersión(valores, tiempos)
        elif opcion == "3":
            valores, tiempos = medir_tiempos(100)
            generar_regresión(valores, tiempos)
        elif opcion == "4":
            valores, tiempos = medir_tiempos(100)
            generar_dispersión(valores, tiempos)
            generar_regresión(valores, tiempos)
        elif opcion == "5":
            print(" Saliendo del análisis empírico.")
            break
        else:
            print(" Opción inválida, intenta nuevamente.")

if __name__ == "__main__":
    menu()