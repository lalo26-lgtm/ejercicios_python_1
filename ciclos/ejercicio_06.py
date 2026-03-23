
num1 = int(input("Coloca el número 1: "))
num2 = int(input("Coloca el número 2: "))


if num1 % 2 == 1:
    num1 = num1 + 1

for i in range(num1, num2 + 1, 2):
    print(i, "es par")
