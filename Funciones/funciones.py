'''
print("un texto") -> imprime un texto en terminal
int("5") -> convierte un valor a entero
input("Texto") -> permite al usuario ingresar un valor
len(objeto) -> devuelve la longitud de una cadena
range(5) -> genera una secuencia de números
'''

'''
Podemos crear funciones
Definir la funcion
def nombre_funcion(parametros):
    instrucciones
    return algo

LLamar o ejecutar
nombre_funcion()
'''

#Sin parametros ni retorno

def hello():
    print("Hello!")

hello()
hello()
hello()

#Con parrametros y sin retorno
def hello_2(name):
    print("Hello ", name)

hello_2("Ironman")
hello_2("Spiderman")
hello_2("Batman")

#Con parametros y retorno
def duplica(num):
    return num * 2

doble = duplica(15)
print("El doble de 15 es", doble)

def suma(num1, num2):
    return num1 + num2  

    resultado = suma(16, -26)
    print(resultado)

    def fullname(name, ap_pat, ap_mat):
        return f"{name} {ap_pat} {ap_mat}"

        print(fullname("Juan", "Perez", "Gomez")) 

    print(fullname("Gomez", "Perez", "Juan"))
    
    print(fullname(ap_mat="Gomez",
                   ap_pat="Perez",
                   name="Juan"))


def get_hero(name, hero = "Spiderman"):
    return f"{name} es {hero}"

    print(get_hero("Peter Parker"))
    print(get_hero("Aura"))
    print(get_hero("Bruce Wayne", "Batman"))

    
