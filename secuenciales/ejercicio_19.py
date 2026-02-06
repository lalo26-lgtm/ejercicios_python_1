correctas = int(input("Dime cantidad de respuestas correctas: "))
incorrectas = int(input("Dime cantidad de respuestas incorrectas: "))
blanco = int(input("Dime cantidad de respuestas en blanco: "))

puntos = correctas * 5 + incorrectas * (-1) + blanco * 0

print("Puntos obtenidos:", puntos)
