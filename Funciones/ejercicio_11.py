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
    return dias

def calcular_dia_juliano(day, month, year):
    diaj = 0
    for mes in range(1, month):
        diaj = diaj + dias_del_mes(mes, year)
    diaj = diaj + day
    return diaj

def leer_fecha():
    day = int(input("Día: "))
    month = int(input("Mes: "))
    year = int(input("Año: "))
    return day, month, year

resultado = leer_fecha()
d = resultado[0]
m = resultado[1]
a = resultado[2]

print("Día Juliano:", calcular_dia_juliano(d, m, a))