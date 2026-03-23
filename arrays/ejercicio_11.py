

if __name__ == "__main__":
    num_filas = 5
    num_cols = 5
    matriz = []  
    

    for fila in range(num_filas):
        fila_actual = []
        for col in range(num_cols):
            
            if fila == col or fila == (num_filas - 1) - col:
                fila_actual.append(1)
            else:
                fila_actual.append(0)
            
        matriz.append(fila_actual)

    print("--- Matriz con Diagonales en X ---")
    for fila in range(num_filas):
        for col in range(num_cols):
            
            print(matriz[fila][col], end=" ")
        print()
        