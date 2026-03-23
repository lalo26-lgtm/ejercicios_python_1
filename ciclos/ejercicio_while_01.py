
factorial = 1
n1 = int(input("Introduce un numero: "))
i = 1
while i <= n1:
	factorial *= i
	i += 1

print("El factorial de ",n1," es ",factorial)