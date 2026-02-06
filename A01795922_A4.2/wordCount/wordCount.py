# pylint: disable=invalid-name
"""
Programa para contar la frecuencia de palabras en un archivo de texto.
Refactorizado para cumplir con PEP8 y eliminar conflictos de complejidad.
"""

import sys
import time


def extract_words(line):
    """
    Algoritmo básico para extraer palabras de una cadena.
    Resuelve: too-many-nested-blocks al aislar la lógica de caracteres.
    """
    words = []
    current_word = ""
    for char in line:
        if char in (' ', '\t', '\n', '\r'):
            if current_word:
                words.append(current_word)
                current_word = ""
        else:
            current_word += char
    if current_word:
        words.append(current_word)
    return words


def compute_frequencies(file_path):
    """
    Lee el archivo y calcula las frecuencias.
    Resuelve: too-many-locals y broad-exception-caught.
    """
    word_counts = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, 1):
                try:
                    words = extract_words(line)
                    for word in words:
                        word_counts[word] = word_counts.get(word, 0) + 1
                except (UnicodeDecodeError, ValueError) as err:
                    print(f"Error procesando línea {line_number}: {err}")
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no existe.")
        return None
    except IOError as err:
        print(f"Error de lectura en el archivo: {err}")
        return None
    return word_counts


def save_results(output_content):
    """
    Guarda el resultado en el archivo WordCountResults.txt.
    """
    try:
        with open("wordCount/salidas/WordCountResults.txt", "w", encoding="utf-8") as f_out:
            f_out.write(output_content)
    except IOError as err:
        print(f"Error al escribir el archivo de resultados: {err}")


def main():
    """
    Función principal que coordina la ejecución.
    Resuelve: too-many-branches y trailing-whitespace.
    """
    start_time = time.time()

    if len(sys.argv) < 2:
        print("Uso: python wordCount.py fileWithData.txt")
        return

    counts = compute_frequencies(sys.argv[1])
    if counts is None:
        return

    elapsed_time = time.time() - start_time

    # Formateo de salida
    results = ["-" * 35, f"{'Palabra':<20} | {'Frecuencia':<10}", "-" * 35]
    for word in sorted(counts.keys()):
        results.append(f"{word:<20} | {counts[word]:<10}")
    results.append("-" * 35)
    results.append(f"Tiempo transcurrido: {elapsed_time:.6f} segundos")

    final_output = "\n".join(results)
    print(final_output)
    save_results(final_output)


if __name__ == "__main__":
    main()
