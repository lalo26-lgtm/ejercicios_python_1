print("CÁLCULO DE COSTOS PARA VIAJE ESCOLAR")
print("=" * 50)

try:
    num_alumnos = int(input("¿Cuántos alumnos participan en la actividad?: "))
    
    if num_alumnos <= 0:
        print("Error: El número de alumnos debe ser un valor positivo.")
    else:
        if num_alumnos >= 100:
            coste_por_alumno = 65
        elif num_alumnos >= 50:  # 50-99
            coste_por_alumno = 70
        elif num_alumnos >= 30:  # 30-49
            coste_por_alumno = 95
        else:  # menos de 30
            coste_por_alumno = 4000 / num_alumnos
        
        if num_alumnos >= 30:
            coste_autobus = num_alumnos * coste_por_alumno
        else:
            coste_autobus = 4000  # Costo fijo para menos de 30 alumnos
        
        print("\n" + "=" * 50)
        print(f"RESUMEN DE COSTOS:")
        print(f"Número de alumnos: {num_alumnos}")
        print(f"Costo por alumno: {coste_por_alumno:.2f} €")
        print(f"Costo total del autobús: {coste_autobus:.2f} €")
        
        if num_alumnos < 30:
            print("\nNOTA: Para grupos menores de 30 alumnos, se aplica una tarifa fija de 4000 € para el autobús.")
            
except ValueError:
    print("Error: Debes introducir un número entero válido.")
