

nombres = []

try:
    print("Bienvenidos!") 
    while  True:
        nombre = input("Ingrese el nombre de un estudiante: ")
        if len(nombre) > 10 or nombre.strip() == "":
            print("No es nombre!")
            nombre = input("Ingrese el nombre de un estudiante: ")
        if nombre == "salir":
            break
            
        nombres.append(nombre)
    print(nombres) 

except:
    ValueError
    print("Error de valor!", ValueError)