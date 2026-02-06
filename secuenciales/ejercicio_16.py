velocidad1 = float(input("Dime la velocidad del coche 1 (km/h): "))
velocidad2 = float(input("Dime la velocidad del coche 2 (más pequeña)(km/h): "))
distancia = float(input("Dime la distancia entre los coches (km): "))

if velocidad1 <= velocidad2:
    print("Error: la velocidad del coche 1 debe ser mayor que la del coche 2.")
else:
    
    tiempo_horas = distancia / (velocidad1 - velocidad2)

    
    tiempo_minutos = tiempo_horas * 60

    print("Lo alcanza en", tiempo_minutos, "minutos.")
