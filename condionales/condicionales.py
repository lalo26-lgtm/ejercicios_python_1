#Estructura de control if
#if else elif

'''
if exp_booleana:
	instrucciones 

if exp_booleana
    instrucciones	
 else:
 	instrucciones
 else
    instrucciones
 '''

numero = int(input("Escribe un numero: "))

if numero > 0:
 	print("Es numero positivo")
elif numero == 0:
 	print('El numero es 0')
else:
	print('Es numero negativo ')
