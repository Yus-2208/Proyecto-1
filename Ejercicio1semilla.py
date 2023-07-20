#se crea una variable llamada intentos para contar cuantos intentos ha realizado el usuario para ingresar un numero valido
intentos = 0

#El while es para que mientras la variable intentos sea menor que tres se cumplira los que esta dentro del ciclo
while intentos < 3:
    try:
        N = (input("ingrese el valor de N para generar numeros aleatorios: "))
        s = str(N)
        #Convertimos a N en un str para poder usar la funcion len() 
        log = len(s)
        #colocamos una condicion la cual es, si la longitud de N es mayor o igual a 4 se ejecuta lo que esta adentro.
        if log >= 4:
            #Creamos una lista vacia para que se guarden los numeros aleatorios
            numeros_aleatorios = []
            #Creamos un for para hallar los numeros aleatorios y que nos arroje 10 resultados
            for _ in range(10):
                #convertimos N en entero 
                N = int(N)
                N_cuadrado = N ** 2
                N_str = str(N_cuadrado)
                if len(N_str) == 8:
                    #Tomamos los cuatro numeros del medio
                    N = int(N_str[2:6])
                    numeros_aleatorios.append(N_cuadrado / 100000000)
                elif len(str(N_cuadrado)) ==4:
                    N_ss = N_cuadrado * 10000
                    N_str = str(N_ss)
                    N = int(N_str[2:6])
                    numeros_aleatorios.append(N_ss / 100000000)  
                elif len(str(N_cuadrado)) ==5:
                    N_ss = N_cuadrado * 1000
                    N_str = str(N_ss)
                    N = int(N_str[2:6])
                    numeros_aleatorios.append(N_ss / 100000000)  
                elif len(str(N_cuadrado)) == 6:
                    N_ss = N_cuadrado * 100
                    N_str = str(N_ss)
                    N = int(N_str[2:6])
                    numeros_aleatorios.append(N_ss / 100000000)
                elif len(N_str) == 7:
                    N_ss = N_cuadrado * 10
                    N_str = str(N_ss)
                    N = int(N_str[2:6])
                    numeros_aleatorios.append(N_ss / 100000000)  

            print("Numeron aleatorios generados: ", numeros_aleatorios)
            break
        #Si la longitud es menor a 4 manda un mensaje al usuario
        else:
            log < 4
            print("El numero debe tener almenos 4 digitos")
    except ValueError:
        print("debe ingresar solo numeros")
        intentos += 1
if intentos == 3:
    print("Ha alcansado en numero maximo de intentos")
    