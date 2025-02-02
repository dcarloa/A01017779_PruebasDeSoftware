"""
Este programa necesita un archivo externo de texto, el cual sera analizado
y se determinaran valores estadisticos del mismo.
"""

import sys
import time


def leer_archivo(ruta_archivo):
    """Lee un archivo y extrae numeros validos, manejando errores."""
    valores_purificados = []
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            try:
                valores_purificados.append(float(linea.strip()))
            except ValueError:
                print(f"Advertencia: Se ignoro un dato invalido -> {linea.strip()}")
    return valores_purificados


def calcular_promedio(lista):
    """Calcula la media aritmetica."""
    return sum(lista) / len(lista)


def calcular_mediana(lista):
    """Calcula la mediana."""
    lista_ordenada = sorted(lista)
    longitud = len(lista_ordenada)
    mitad = longitud // 2
    if longitud % 2 == 0:
        return (lista_ordenada[mitad - 1] + lista_ordenada[mitad]) / 2
    return lista_ordenada[mitad]


def calcular_moda(lista):
    """Calcula la moda."""
    frecuencias = {}
    for num in lista:
        frecuencias[num] = frecuencias.get(num, 0) + 1
    frecuencia_maxima = max(frecuencias.values())
    modas = [k for k, v in frecuencias.items() if v == frecuencia_maxima]
    return modas[0] if len(modas) == 1 else modas


def calcular_varianza(lista, promedio_general):
    """Calcula la varianza."""
    return sum((x - promedio_general) ** 2 for x in lista) / len(lista)


def calcular_desviacion(varianza_general):
    """Calcula la desviacion estandar."""
    return varianza_general ** 0.5


def calcular_rango(lista):
    """Calcula el rango de los valores."""
    return max(lista) - min(lista)


def calcular_coef_var(desviacion, promedio_general):
    """Calcula el coeficiente de variacion."""
    return (desviacion / promedio_general) * 100


def guardar_resultados(nombre_archivo, resultados, duracion):
    """Guarda los resultados en un archivo."""
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("=== Resultados Estadisticos ===\n")
        for clave, valor in resultados.items():
            archivo.write(f"{clave}: {valor}\n")
        archivo.write(f"\nTiempo de ejecucion: {duracion:.6f} segundos\n")


def principal():
    """Ejecuta el programa principal."""
    if len(sys.argv) != 2:
        print("Uso correcto: python calculo_estadisticas.py datos.txt")
        sys.exit(1)

    archivo_entrada = sys.argv[1]
    inicio_tiempo = time.time()

    try:
        registro_numerico = leer_archivo(archivo_entrada)
        if not registro_numerico:
            print("Error: No se encontraron datos numericos validos.")
            sys.exit(1)

        promedio_general = calcular_promedio(registro_numerico)
        mediana_general = calcular_mediana(registro_numerico)
        moda_general = calcular_moda(registro_numerico)
        varianza_general = calcular_varianza(registro_numerico, promedio_general)
        desviacion_general = calcular_desviacion(varianza_general)
        rango_general = calcular_rango(registro_numerico)
        coeficiente_variacion = calcular_coef_var(desviacion_general, promedio_general)

        resultados = {
            "Media": promedio_general,
            "Mediana": mediana_general,
            "Moda": moda_general,
            "Varianza": varianza_general,
            "Desviacion estandar": desviacion_general,
            "Rango": rango_general,
            "Coef. de Variacion (%)": coeficiente_variacion,
        }

        tiempo_total = time.time() - inicio_tiempo
        resultados["Tiempo de Ejecucion"] = f"{tiempo_total:.6f} segundos"

        print("\n=== Resultados Estadisticos ===")
        for clave, valor in resultados.items():
            print(f"{clave}: {valor}")

        guardar_resultados("ResultadosEstadisticas.txt", resultados, tiempo_total)

    except FileNotFoundError:
        print(f"Error: No se encontro el archivo '{archivo_entrada}'.")
        sys.exit(1)


if __name__ == "__main__":
    principal()
