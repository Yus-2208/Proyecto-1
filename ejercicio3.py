# Solicitar al usuario los valores de N y M 
N = int(input("Ingrese el número de filas (N): "))
M = int(input("Ingrese el número de columnas (M): "))

if N <= 0 or M <= 0:
     print("El numero ingresado en N y M tiene que ser mayor a cero")

"Creamos una matriz de tamaño N x M"
matriz = [[0] * M for _ in range(N)]

#Inicializamos el contador
numero = 1

#Recorrer la matriz en zig-zag
for i in range(N):
    
    #Verificar si la fila es par o impar para asignar los valores en orden o inversos

    if i % 2 == 0:
         for j in range(M):
              matriz[i][j] = numero
              numero += 1
    else:
        for j in range(M -1, -1, -1):
             matriz[i][j] = numero
             numero += 1

#Imprimir la matriz resultante 
for fila in matriz:
     print(fila)