numero = int(input("Por favor, introduce un numero entero : "))

match numero:
    case 0: 
        print("El numero es un cero")
    case numero if numero % 2 == 0:
        print("El numero es par.")
    case numero if numero % 2 != 0:
        print("El numero no es par.")
    case _:
        print("Numero no reconocido")    

