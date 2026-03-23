def login(nombre, password, intentos):
    if nombre == "usuario1" and password == "asdasd":
        eslogin = True
    else:
        eslogin = False
        intentos = intentos + 1
    return eslogin, intentos

cuantasveces = 0
entrar = False

while entrar == False and cuantasveces < 3:
    usuario = input("Usuario: ")
    clave = input("Password: ")
    
    resultado = login(usuario, clave, cuantasveces)
    entrar = resultado[0]
    cuantasveces = resultado[1]
    
    if entrar == False:
        print("Error. Nombre de usuario o contraseña incorrecta.")

if entrar == True:
    print("Bienvenidos al sistema")
else:
    print("No has entrado en el sistema")