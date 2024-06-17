import statistics

# Filtros mejorados

# Filtro para duplicar los números
def duplicar_numeros(lista_numeros):
    try:
        return [2 * num for num in lista_numeros]
    except TypeError as e:
        print(f"Error en duplicar_numeros: {e}")
        return []

# Filtro para filtrar solo números pares
def filtrar_pares(lista_numeros):
    try:
        return [num for num in lista_numeros if num % 2 == 0]
    except TypeError as e:
        print(f"Error en filtrar_pares: {e}")
        return []

# Filtro para calcular la media
def calcular_media(lista_numeros):
    try:
        return statistics.mean(lista_numeros)
    except statistics.StatisticsError as e:
        print(f"Error en calcular_media: {e}")
        return float('nan')

# Filtro para calcular la desviación estándar
def calcular_desviacion_estandar(lista_numeros):
    try:
        return statistics.stdev(lista_numeros)
    except statistics.StatisticsError as e:
        print(f"Error en calcular_desviacion_estandar: {e}")
        return float('nan')

# Función para aplicar los filtros
def aplicar_filtros(lista_numeros, lista_filtros):
    try:
        resultado = lista_numeros
        for filtro in lista_filtros:
            resultado = filtro(resultado)
        return resultado
    except Exception as e:
        print(f"Error en aplicar_filtros: {e}")
        return []

# Lista de números de ejemplo
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Lista de filtros a aplicar
filtros = [duplicar_numeros, filtrar_pares, calcular_media, calcular_desviacion_estandar]

# Aplicar los filtros y mostrar el resultado final
resultado_final = aplicar_filtros(numeros, filtros)
print("Números de entrada:", numeros)
print("Resultado final después de aplicar los filtros:", resultado_final)
