cadena = input('Ingrese una cadena de texto:\n')
subcadena = input('Ingrese una subcadena:\n')
if cadena.startswith(subcadena):
    print(cadena, 'Si comineza con ', subcadena)
else:
    print(cadena, 'No comienza con ', subcadena)