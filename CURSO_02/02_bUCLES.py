# bUCLES

frutas = ["Manzana","Banana","Cereza","Naranja","Sandia"]
contador = 0

for fruta in frutas:
    contador += 1
    print(f"fruta #{contador} : {fruta}")
    if contador == 6:
        break
