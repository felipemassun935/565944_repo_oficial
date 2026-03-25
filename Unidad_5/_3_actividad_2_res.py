

nombres = []

    
def pedirNombre():
    print("Bienvenidos!") 
    while  True:
        nombre = input("Ingrese el nombre de un estudiante: ")
        if len(nombre) > 10 :
            print("No es nombre!")
            nombre = input("Ingrese el nombre de un estudiante: ")
        if nombre == "salir":
            break
            
        nombres.append(nombre)
    return print(nombres) 

try:
    pedirNombre(nombres)
except:
    ValueError
    print("Error de valor!", ValueError)
    
    
