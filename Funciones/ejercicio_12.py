def es_bisiesto(year):
    if (year % 4 == 0 and not (year % 100 == 0)) or year % 400 == 0:
        bisiesto = True
    else:
        bisiesto = False
    return bisiesto

def dias_del_mes(month, year):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        dias = 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        dias = 30
    elif month == 2:
        if es_bisiesto(year):
            dias = 29
        else:
            dias = 28
    else:
        dias = 0
    return dias

def validar_fecha(day, month, year):
    if day < 1 or day > dias_del_mes(month, year):
        esvalida = False
    else:
        esvalida = True
    return esvalida

def calcular_dia_juliano(day, month, year):
    diaj = 0
    for mes in range(1, month):
        diaj = diaj + dias_del_mes(mes, year)
    diaj = diaj + day
    return diaj

def leer_fecha():
    fechavalida = False
    while fechavalida == False:
        day = int(input("Día: "))
        month = int(input("Mes: "))
        year = int(input("Año: "))
        
        fechavalida = validar_fecha(day, month, year)
        
        if fechavalida == False:
            print("Fecha no válida")
            
    return day, month, year

resultado = leer_fecha()
d = resultado[0]
m = resultado[1]
a = resultado[2]

print("Día Juliano:", calcular_dia_juliano(d, m, a))

