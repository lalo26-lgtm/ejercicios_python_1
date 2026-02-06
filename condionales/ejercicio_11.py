ladoA = float(input("Introduce longitud lado A: "))
ladoB = float(input("Introduce longitud lado B: "))
ladoC = float(input("Introduce longitud lado C: "))

if (abs(ladoA**2 + ladoB**2 - ladoC**2) < 1e-9 or
    abs(ladoB**2 + ladoC**2 - ladoA**2) < 1e-9 or
    abs(ladoC**2 + ladoA**2 - ladoB**2) < 1e-9):
    print("Triángulo Rectángulo")

if (ladoA == ladoB and ladoA != ladoC) or \
   (ladoB == ladoC and ladoB != ladoA) or \
   (ladoC == ladoA and ladoC != ladoB):
    print("Triángulo Isósceles")

elif ladoA == ladoB == ladoC:
    print("Triángulo Equilátero")

else:
    print("Triángulo Escaleno")
