### Muestra la edad.

edad = int(input("Por favor ingresa tu edad : "))
if edad < 0:
    print("Edad No valida. Por favor introduce una correcta : ")
elif edad <=12 :
    print("Eres un niño")
elif edad <=18 :
    print("Eres un joven")
elif edad < 65 :
    print("Eres un adulto")
else:
    print("Eres un viejo")