#progaram que hace una division 
# si el divisor es 0 que termine o que dija que no se puede

num_1 = int(input('íngresa un numero'))
num_2 = int(input('ingresa otro numero: '))

if num_2 == 0:
	print('no se puede dividir entre 0')
else:
	divi = num_1 / num_2
	print('la division es:', divi)