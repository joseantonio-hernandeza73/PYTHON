# CADENAS

nombre ="Jose Antonio"
apellido = "Hernandez Alcantara"
frase = "Esto es una simple frase"

# Contar los caracteres de las cadenas
longitud = len(nombre)
print(longitud)

# OJO Cuenta los caracteres en blanco tambien
lon2 = len(frase)
print(lon2)

print(apellido[0])
print(apellido[10])

# Dividir segmentos de palabras

palabras = frase.split()
print(palabras)

# Mayusculas y minusculas
mayusculas = apellido.upper()
mayu01 = frase.upper()
print(mayusculas)
print(mayu01)

minus = apellido.lower()
print(minus)

# Remplazo de Texto

mensa = "Hola, Mundo"
cambio = mensa.replace("Hola","Hola Antonio")
print(mensa)
print(cambio)

# Separar una cadena

for x in apellido:
    print(x)








