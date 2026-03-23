
if __name__ == "__main__":
    num_filas = 5
    num_cols = 15
    matriz = []  
    
    for fila in range(num_filas):
        fila_actual = []
        for col in range(num_cols):
            
            if fila == 0 or fila == num_filas - 1 or col == 0 or col == num_cols - 1:
                fila_actual.append(1) 
            else:
                fila_actual.append(0) 
                
        matriz.append(fila_actual)

    print("--- Perímetro de Seguridad ---")
    for fila in range(num_filas):
        for col in range(num_cols):
            print(matriz[fila][col], end=" ") 
        print()