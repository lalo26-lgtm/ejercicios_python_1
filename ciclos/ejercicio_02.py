import random

hidden = random.randint(1, 100)

intentos = 1

while intentos <= 100:
        num = int(input('Adivina el numero: '))
        if num == hidden:
                print('¡Adivinaste!')
                print('En', intentos, 'intentos')
                break
        elif num < hidden:
                print('El numero es mayor')
        else:
                print('El numero es menor')
        intentos += 1
else:
        print('¡Perdiste! El numero era', hidden)  
