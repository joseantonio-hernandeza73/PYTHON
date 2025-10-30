#conteo Inverso con While
# Contador = 10

#while Contador  >= 1:
#    print(Contador)
#    Contador -= 1
#print("FELIZ AÑO NUEVO") 

suma = 0
numero = int(input("Ingresa un número positivo (ó un número negativo para salir) :"))

while numero >= 0:
    suma += numero
    numero -= 1
print("La suma es igual a :",suma)


