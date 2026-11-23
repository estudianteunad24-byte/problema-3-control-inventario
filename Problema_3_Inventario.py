
# PROBLEMA 3: CONTROL DE INVENTARIO
# Nombre: Daniela Bermudez
# Grupo_213022_937 
# Programa: Ing Industrial

# Funcion para calcular la cantidad a solicitar
def calcular_reabastecimiento(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0


# Matriz para almacenar los articulos
inventario = []

# Solicitar la cantidad de articulos
cantidad = int(input("Ingrese la cantidad de articulos: "))

# Ciclo para ingresar los datos
for i in range(cantidad):
    print("\nIngrese los datos del articulo", i + 1)

    codigo = input("Codigo del articulo: ")
    nombre = input("Nombre del articulo: ")
    stock_actual = int(input("Stock actual: "))
    stock_minimo = int(input("Stock minimo requerido: "))

    # Agregar los datos a la matriz
    inventario.append([
        codigo, nombre, stock_actual, stock_minimo
    ])


# Procedimiento para mostrar los resultados
def mostrar_inventario(inventario):

    print("\n===== REPORTE DE REABASTECIMIENTO =====")

    for articulo in inventario:
        codigo = articulo[0]
        nombre = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]

        cantidad_pedir = calcular_reabastecimiento(
            stock_actual, stock_minimo
        )

        print("\nCodigo:", codigo)
        print("Articulo:", nombre)
        print("Stock actual:", stock_actual)
        print("Stock minimo:", stock_minimo)
        print("Cantidad a solicitar:", cantidad_pedir)

        if cantidad_pedir > 0:
            print("Estado: Necesita reabastecimiento")
        else:
            print("Estado: Stock suficiente")


# Ejecutar el programa
mostrar_inventario(inventario)

