horapartida = int(input("Hora de salida (HH): "))
minpartida = int(input("Minutos de salida (MM): "))
segpartida = int(input("Segundos de salida (SS): "))

segviaje = int(input("Tiempo que has tardado en segundos: "))

seginicial = horapartida * 3600 + minpartida * 60 + segpartida

segfinal = seginicial + segviaje

horallegada = (segfinal // 3600) % 24   # %24 para que no pase de 24h
minllegada = (segfinal % 3600) // 60
segllegada = (segfinal % 3600) % 60

print("Hora de llegada:", f"{horallegada:02d}:{minllegada:02d}:{segllegada:02d}")
