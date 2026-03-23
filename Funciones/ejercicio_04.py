def convertir_espaciado(cad):
    cad_con_espacios = ""
    for letra in cad:
        cad_con_espacios += letra + " "
    return cad_con_espacios

if __name__ == "__main__":
    mensaje = input("Introduce una cadena: ")
    print("La cadena con espacio:")
    print(convertir_espaciado(mensaje))