suma = 0
cont = 0

while True:
    print("Número (0 para salir):")
    num = int(input())
    suma = suma + num
    
    if num != 0:
        cont = cont + 1
    
    if num == 0:
        break

if cont != 0:
    media = suma / cont
else:
    media = 0

print("Suma:", suma)
print("Media:", media)
