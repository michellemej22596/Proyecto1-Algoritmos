import time
import numpy as np
import matplotlib.pyplot as plt
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from turing import CintaUnicaTuring


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "..", "turing_c.json")


if not os.path.exists(CONFIG_PATH):
    raise FileNotFoundError(f"Error: No se encontró el archivo de configuración en {CONFIG_PATH}")

def medir_tiempos(max_n=50):
    """Tiempos de ejecución de la Máquina de Turing para Fibonacci."""
    valores = list(range(1, max_n + 1))
    tiempos = []

    for n in valores:
        inicio = time.perf_counter()
        maquina = CintaUnicaTuring(CONFIG_PATH, n)
        maquina.run()
        fin = time.perf_counter()
        tiempos.append(fin - inicio)

    return valores, tiempos

def generar_grafico_complejidad(valores, tiempos):
    """Comparación con notaciones Big-O, Big-Theta y Big-Omega."""
    n = np.array(valores)
    t_real = np.array(tiempos)

 
    O_n = n / np.max(n) * np.max(t_real)  
    Theta_n = np.polyfit(n, t_real, 1)[0] * n  
    Omega_n = (n / np.max(n)) * (np.min(t_real) + (np.max(t_real) - np.min(t_real)) * 0.1)  

  
    plt.figure(figsize=(10, 6))
    plt.scatter(n, t_real, color="blue", label="Datos observados", s=10)
    plt.plot(n, O_n, "--", label="Big-O (O(n)) - Peor caso", color="red")
    plt.plot(n, Theta_n, "-", label="Big-Theta (Θ(n)) - Caso promedio", color="orange", linewidth=2)
    plt.plot(n, Omega_n, "--", label="Big-Omega (Ω(n)) - Mejor caso", color="green")

    plt.xlabel("Número de Fibonacci (n)")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.title("Comparación de Complejidad Asintótica (O, Θ, Ω)")
    plt.legend()
    plt.grid()

   
    results_dir = os.path.join(BASE_DIR, "..", "results")
    os.makedirs(results_dir, exist_ok=True)
    
    output_path = os.path.join(results_dir, "big_o_theta_omega_comparison.png")
    plt.savefig(output_path)
    print(f" Gráfico guardado en {output_path}")
    plt.show()

def imprimir_analisis(valores, tiempos):
    """Escribe en consola el análisis del comportamiento del algoritmo."""
    print("\n--- ANÁLISIS DE COMPLEJIDAD (O, Θ, Ω) ---")
    
    coef_O = np.polyfit(valores, tiempos, 1)[0]  
    coef_Theta = np.mean(tiempos)  
    coef_Omega = np.min(tiempos)  

    print(f"Coeficiente Big-O (peor caso) O(n): {coef_O:.6f}")
    print(f"Coeficiente Big-Theta (caso promedio) Θ(n): {coef_Theta:.8f}")
    print(f"Coeficiente Big-Omega (mejor caso) Ω(n): {coef_Omega:.8f}")

 
    print("\n Evaluación de Complejidad:")
    if coef_O > 0 and coef_O < 1e-6:
        print("El algoritmo parece tener complejidad O(n), lo cual es eficiente para esta tarea.")
    elif coef_O > 1e-6:
        print(" La complejidad podría ser mayor que O(n), revisa los tiempos en la gráfica.")
    else:
        print(" Podría haber ruido en la medición, revisa el dataset.")

def main():
    valores, tiempos = medir_tiempos(100) 
    imprimir_analisis(valores, tiempos)
    generar_grafico_complejidad(valores, tiempos)

if __name__ == "__main__":
    main()