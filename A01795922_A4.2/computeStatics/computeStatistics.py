# pylint: disable=invalid-name
"""
Programa para calcular estadísticas descriptivas.
Lectura desde la carpeta 'archivos' y escritura en 'salidas'.
"""

import sys
import time
import os


def calculate_stats(data):
    """Calcula todas las estadísticas y las devuelve en un diccionario."""
    mean = sum(data) / len(data)

    sorted_data = sorted(data)
    n = len(data)
    median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2 if n % 2 == 0 \
        else sorted_data[n // 2]

    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    mode = max(freq, key=freq.get)

    variance = sum((x - mean) ** 2 for x in data) / n
    return mean, median, mode, variance, variance ** 0.5


def read_data(file_name):
    """Lee los datos del archivo en la carpeta 'archivos'."""
    input_path = os.path.join("computeStatics/archivos", file_name)
    numbers = []
    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    val = line.strip()
                    if val:
                        numbers.append(float(val))
                except ValueError:
                    print(f"Error: Dato inválido omitido: {val}")
    except FileNotFoundError:
        print(f"Error: El archivo '{input_path}' no fue encontrado.")
    return numbers


def save_results(results_text):
    """Guarda los resultados en la carpeta 'salidas'."""
    if not os.path.exists("computeStatics/salidas"):
        os.makedirs("computeStatics/salidas")
    output_path = os.path.join("computeStatics/salidas", "StatisticsResults.txt")
    with open(output_path, "w", encoding="utf-8") as out_file:
        out_file.write(results_text)


def main():
    """Función principal simplificada para evitar exceso de variables locales."""
    start_time = time.time()

    if len(sys.argv) < 2:
        print("Uso: python computeStatistics.py nombre_archivo.txt")
        return

    file_name = sys.argv[1]
    data = read_data(file_name)

    if not data:
        return

    mean, median, mode, var, std = calculate_stats(data)
    elapsed = time.time() - start_time

    output = (
        f"Resultados para: {file_name}\n"
        f"Media: {mean}\n"
        f"Mediana: {median}\n"
        f"Moda: {mode}\n"
        f"Varianza: {var}\n"
        f"Desviación Estándar: {std}\n"
        f"Tiempo: {elapsed:.4f} seg\n"
    )

    print(output)
    save_results(output)


if __name__ == "__main__":
    main()

