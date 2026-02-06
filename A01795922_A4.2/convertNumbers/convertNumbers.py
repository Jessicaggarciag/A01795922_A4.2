# pylint: disable=invalid-name
"""
Programa para convertir números a binario y hexadecimal.
Recibe la ruta del archivo directamente desde la línea de comandos.
"""

import sys
import time
import os


def to_binary(n):
    """Convierte un entero a binario mediante divisiones sucesivas."""
    if n == 0:
        return "0"
    is_neg = n < 0
    num = abs(int(n))
    bin_str = ""
    while num > 0:
        bin_str = str(num % 2) + bin_str
        num //= 2
    return "-" + bin_str if is_neg else bin_str


def to_hexadecimal(n):
    """Convierte un entero a hexadecimal mediante divisiones sucesivas."""
    if n == 0:
        return "0"
    is_neg = n < 0
    num = abs(int(n))
    chars = "0123456789ABCDEF"
    hex_str = ""
    while num > 0:
        hex_str = chars[num % 16] + hex_str
        num //= 16
    return "-" + hex_str if is_neg else hex_str


def read_data(file_path):
    """Lee datos desde la ruta proporcionada por el usuario."""
    valid_nums = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    clean_line = line.strip()
                    if clean_line:
                        valid_nums.append(int(float(clean_line)))
                except ValueError:
                    print(f"Error: '{clean_line}' no es un número válido.")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta: {file_path}")
    return valid_nums


def save_results(content):
    """Guarda los resultados en la carpeta 'salidas'."""
    if not os.path.exists("salidas"):
        os.makedirs("salidas")
    out_path = os.path.join("salidas", "ConvertionResults.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    """Función principal."""
    start = time.time()
    if len(sys.argv) < 2:
        print("Uso: python convertNumbers.py ruta/al/archivo.txt")
        return

    input_arg = sys.argv[1]
    numbers = read_data(input_arg)

    if not numbers:
        return

    # Construcción de la tabla de resultados
    header = f"{'ITEM':>5} | {'NÚMERO':>12} | {'BINARIO':>20} | {'HEX':>10}"
    sep = "-" * 55
    lines = [f"Resultados para: {input_arg}", sep, header, sep]

    for i, n in enumerate(numbers, 1):
        lines.append(f"{i:>5} | {n:>12} | {to_binary(n):>20} | {to_hexadecimal(n):>10}")

    elapsed = time.time() - start
    lines.append(sep)
    lines.append(f"Tiempo de ejecución: {elapsed:.4f} segundos")

    final_output = "\n".join(lines)
    print(final_output)
    save_results(final_output)


if __name__ == "__main__":
    main()
