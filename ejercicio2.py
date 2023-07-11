#pedir al usuario que ingrese los datos de profundidad del pozo, distancia ascendida durante el dia y distancia ascendida durante la noche
H = float(input("ingrese la profundidad del pozo: "))
Ld = float(input("ingrese la distancia ascendida durante el dia: "))
Ln = float(input("ingrese la distancia ascendida durante la noche: "))

#Verificamos que Ln sea mayor que Ld
if Ln > Ld:
    print("el caracol no puede salir del pozo")

#creamos una variable llamada distancia ascendida
distancia_ascendida = 0
dias = 0

while distancia_ascendida < H:
    distancia_ascendida += Ld
    if distancia_ascendida >= H:
        break
    distancia_ascendida -= Ln
    dias += 1

print("El caracol sale del pozo en", dias, "dias")