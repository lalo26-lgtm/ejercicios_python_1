print("CÁLCULO DE GANANCIA POR VENTA DE UVA")
print("=" * 40)

µtry:
    precio_inicial = int(input("Introduce el precio inicial por kilo de uva (en céntimos): "))
    kilos = int(input("Introduce cuántos kilos has vendido: "))
    
    tipo = input("Introduce el tipo de la uva (A/B): ").upper()
    
    if tipo not in ["A", "B"]:
        print("Error: Tipo incorrecto. Debe ser A o B.")
    else:
        tamano = input("Introduce el tamaño de la uva (1/2): ")
        
        if tamano not in ["1", "2"]:
            print("Error: Tamaño incorrecto. Debe ser 1 o 2.")
        else:
            if tipo == "A":
                if tamano == "1":
                    precio_inicial += 20  # Sumar 20 céntimos
                else:  # tamano == "2"
                    precio_inicial += 30  # Sumar 30 céntimos
            else:  # tipo == "B"
                if tamano == "1":
                    precio_inicial -= 30  # Restar 30 céntimos (según especificación)
                else:  # tamano == "2"
                    precio_inicial -= 50  # Restar 50 céntimos (según especificación)
            
            ganancia_centimos = precio_inicial * kilos
            ganancia_euros = ganancia_centimos / 100
            
            print("\n" + "=" * 40)
            print(f"RESUMEN DE LA VENTA:")
            print(f"Tipo de uva: {tipo}")
            print(f"Tamaño: {tamano}")
            print(f"Kilos vendidos: {kilos} kg")
            print(f"Precio por kilo final: {precio_inicial} céntimos")
            print(f"Ganancia total: {ganancia_centimos} céntimos")
            print(f"Ganancia total: {ganancia_euros:.2f} €")
            
except ValueError:
    print("Error: Debes introducir valores numéricos válidos para precio y kilos.")
