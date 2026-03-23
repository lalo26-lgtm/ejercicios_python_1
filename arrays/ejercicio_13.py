
if __name__ == "__main__":
    tam_conductores_max = 10
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    
    nombres = []    
    matriz_kms = [] 
    
    print("--- Sistema de Flotilla ---")
    
    while True:
        num_conductores = int(input("¿Cuántos conductores tiene la empresa?: "))
        if num_conductores <= tam_conductores_max:
            break 
        else:
            print(f"Como máximo puedo guardar la información de {tam_conductores_max} conductores.\n")

    for i in range(num_conductores):
        nombre = input(f"\nNombre del conductor {i+1}: ")
        nombres.append(nombre)
        
        kms_semana = [] 
        
        for dia in dias:
            km = int(input(f"¿Cuántos km ha realizado el {dia}?: "))
            kms_semana.append(km)
            
        kms_semana.append(0) 
        
        matriz_kms.append(kms_semana)

    for i in range(num_conductores):
        suma_kms = 0
        for j in range(7):
            suma_kms = suma_kms + matriz_kms[i][j]
            
        matriz_kms[i][7] = suma_kms

    print("\n--- Reporte Final ---")
    for i in range(num_conductores):
        print(f"{nombres[i]} ha realizado {matriz_kms[i][7]} kms en total.")