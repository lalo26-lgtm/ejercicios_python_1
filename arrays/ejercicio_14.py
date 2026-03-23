
if __name__ == "__main__":
    precios = []
    cantidades = []

    print("--- Sistema de Inventario y Ventas ---")

    print("\nRegistro de Precios:")
    for i in range(5):
        precio = float(input(f"Ingrese Precio del Articulo {i+1}: $"))
        precios.append(precio)

    print("\nRegistro de Cantidades por Sucursal:")
    for sucursal in range(4):
        print(f"-- Sucursal {sucursal+1} --")
        cant_articulos = []
        for art in range(5):
            cant = float(input(f"Ingrese Cantidad de Articulo {art+1}: "))
            cant_articulos.append(cant)
        
        cantidades.append(cant_articulos)

    print("\n--- Reporte de Inventario ---")
    print("Cantidades totales por artículos en todas las sedes:")
    for art in range(5):

        suma_art = cantidades[0][art] + cantidades[1][art] + cantidades[2][art] + cantidades[3][art]
        print(f"Total articulo {art+1}: {suma_art} unidades")

    articulos_sucursal2 = sum(cantidades[1])
    print(f"\nTotal de artículos en la Sucursal 2: {articulos_sucursal2}")

    print(f"Cantidad exacta en Sucursal 1, Articulo 3: {cantidades[0][2]}")

    mayor_rec = 0
    num_mayor = 0
    total_empresa = 0

    print("\n--- Reporte Financiero ---")
    for sucursal in range(4):
        total_sucursal = 0
        
        for art in range(5):
            total_sucursal = total_sucursal + (cantidades[sucursal][art] * precios[art])
            
        print(f"Recaudación Sucursal {sucursal+1}: ${total_sucursal}")

        if total_sucursal > mayor_rec:
            mayor_rec = total_sucursal
            num_mayor = sucursal + 1
        total_empresa = total_empresa + total_sucursal
        
    print("\n========================================")
    print(f"Recaudación total de la empresa: ${total_empresa}")
    print(f"Sucursal de Mayor Recaudación: Sucursal {num_mayor}")