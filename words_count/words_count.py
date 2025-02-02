"""
Este programa cuenta la frecuencia de palabras distintas en un archivo de texto.
"""

import sys
import time


def leer_archivo(ruta_archivo):
    """Lee un archivo y extrae palabras validas, manejando errores."""
    palabras = []
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                palabras.extend(procesar_linea(linea))
    except FileNotFoundError:
        print(f"Error: No se encontro el archivo '{ruta_archivo}'.")
        sys.exit(1)
    return palabras


def procesar_linea(linea):
    """Procesa una linea eliminando caracteres especiales y separando palabras."""
    palabras_procesadas = []
    palabra_actual = ""
    for caracter in linea:
        if caracter.isalnum() or caracter == "'":
            palabra_actual += caracter.lower()
        else:
            if palabra_actual:
                palabras_procesadas.append(palabra_actual)
                palabra_actual = ""
    if palabra_actual:
        palabras_procesadas.append(palabra_actual)
    return palabras_procesadas


def contar_palabras(lista_palabras):
    """Cuenta la frecuencia de cada palabra usando un diccionario."""
    frecuencia = {}
    for palabra in lista_palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia


def guardar_resultados(nombre_archivo, frecuencia, duracion):
    """Guarda los resultados en un archivo."""
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("=== Resultados del Conteo de Palabras ===\n")
        for palabra, cantidad in sorted(frecuencia.items()):
            archivo.write(f"{palabra}: {cantidad}\n")
        archivo.write(f"\nTiempo de ejecucion: {duracion:.6f} segundos\n")


def principal():
    """Ejecuta el programa principal."""
    if len(sys.argv) != 2:
        print("Uso correcto: python wordCount.py archivo.txt")
        sys.exit(1)

    archivo_entrada = sys.argv[1]
    inicio_tiempo = time.time()

    lista_palabras = leer_archivo(archivo_entrada)
    if not lista_palabras:
        print("Error: No se encontraron palabras validas en el archivo.")
        sys.exit(1)

    frecuencia_palabras = contar_palabras(lista_palabras)

    tiempo_total = time.time() - inicio_tiempo

    print("\n=== Resultados del Conteo de Palabras ===")
    for palabra, cantidad in sorted(frecuencia_palabras.items()):
        print(f"{palabra}: {cantidad}")

    guardar_resultados("WordCountResults.txt", frecuencia_palabras, tiempo_total)


if __name__ == "__main__":
    principal()
