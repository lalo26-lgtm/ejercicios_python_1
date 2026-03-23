def centrar(Frase):
    message = ' ' * (40 - len(Frase) // 2)
    message += Frase
    print(message)
    message = ' ' * (40 - len(Frase) // 2)
    message += '=' * len(Frase)
    print(message)
   

    
if __name__ == '__main__':
    message_1 = input('Ingrese un texto a centrar: ')
    message_2 = input('Ingrese un texto a centrar: ')
    print()
    centrar(message_1)
    centrar(message_2)






    
