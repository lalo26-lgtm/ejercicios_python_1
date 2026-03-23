
if __name__ == "__main__":
    num_filas = 5
    num_cols = 5
    matriz = [] 
    
    print("--- Llenando la cuadrícula 5x5 ---")
    for fila in range(num_filas):
        fila_actual = [] 
        for col in range(num_cols):
            numero = int(input(f"Introduce el número de la fila {fila+1} y columna {col+1}: "))
            fila_actual.append(numero)
            
        matriz.append(fila_actual)


    print("\n--- Sumas por Fila ---")
    for fila in range(num_filas):
        suma = 0
        for col in range(num_cols):
            suma = suma + matriz[fila][col] 
        print(f"La suma de los elementos de la fila {fila+1} es: {suma}")


    print("\n--- Sumas por Columna ---")
    for col in range(num_cols):
        suma = 0
        for fila in range(num_filas):
            suma = suma + matriz[fila][col]
        print(f"La suma de los elementos de la columna {col+1} es: {suma}") 