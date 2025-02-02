"""
Este programa transforma numeros desde un archivo de texto a sus 
representaciones binarias y hexadecimales. 
"""

import sys
import time


def leer_archivo(ruta_archivo):
    """Lee un archivo y extrae numeros validos, manejando errores."""
    numeros = []
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            try:
                numeros.append(int(linea.strip()))
            except ValueError:
                print(f"Advertencia: Se ignoro un dato invalido :( -> {linea.strip()}")
    return numeros


def convertir_a_binario(numero):
    """Convierte un numero decimal a binario usando operaciones basicas."""
    if numero == 0:
        return "0"
    binario = ""
    while numero > 0:
        binario = str(numero % 2) + binario
        numero //= 2
    return binario


def convertir_a_hexadecimal(numero):
    """Convierte un numero decimal a hexadecimal usando operaciones basicas."""
    if numero == 0:
        return "0"
    hex_digitos = "0123456789ABCDEF"
    hexadecimal = ""
    while numero > 0:
        hexadecimal = hex_digitos[numero % 16] + hexadecimal
        numero //= 16
    return hexadecimal


def guardar_resultados(nombre_archivo, resultados, duracion):
    """Guarda los resultados en un archivo."""
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("=== Resultados de Conversion ===\n")
        for num, binario, hexadecimal in resultados:
            archivo.write(f"Decimal: {num}, Binario: {binario}, Hexadecimal: {hexadecimal}\n")
        archivo.write(f"\nTiempo de ejecucion: {duracion:.6f} segundos\n")


def principal():
    """Ejecuta el programa principal."""
    if len(sys.argv) != 2:
        print("Uso correcto: python convertNumbers.py archivo.txt")
        sys.exit(1)

    archivo_entrada = sys.argv[1]
    inicio_tiempo = time.time()

    try:
        lista_numeros = leer_archivo(archivo_entrada)
        if not lista_numeros:
            print("Error: No se encontraron numeros validos en el archivo.")
            sys.exit(1)

        resultados = []
        for num in lista_numeros:
            binario = convertir_a_binario(num)
            hexadecimal = convertir_a_hexadecimal(num)
            resultados.append((num, binario, hexadecimal))

        tiempo_total = time.time() - inicio_tiempo

        print("\n=== Resultados de Conversion ===")
        for num, binario, hexadecimal in resultados:
            print(f"Decimal: {num}, Binario: {binario}, Hexadecimal: {hexadecimal}")

        guardar_resultados("ConvertionResults.txt", resultados, tiempo_total)

    except FileNotFoundError:
        print(f"Error: No se encontro el archivo '{archivo_entrada}'.")
        sys.exit(1)


if __name__ == "__main__":
    principal()
