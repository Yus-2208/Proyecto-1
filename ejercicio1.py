#se crea una variable llamada intentos para contar cuantos intentos ha realizado el usuario para ingresar un numero valido
intentos = 0

#El while es para que mientras la variable intentos sea menor que tres se cumplira los que esta dentro del ciclo
while intentos < 3:
    N = int(input("ingrese el valor de N para generar numeros aleatorios: "))
    if N > 0:
        numeros_aleatorios = []
        for _ in range(10):
            N_cuadrado = N ** 2
            N_str = str(N_cuadrado)
            while len(N_str) < 8:
                N_str = '0' + N_str
            N = int(N_str[2:6]) 
            numeros_aleatorios.append(N_cuadrado / 100000000)
        print("Numeron aleatorios generados: ", numeros_aleatorios)

    elif N <= 0000:
        print("el numero tiene que ser mayor a 0")

    else:
        print("El numero debe tener almenos 4 digitos")
    intentos += 1

if intentos == 3:
    print("Ha alcansado en numero maximo de intentos")