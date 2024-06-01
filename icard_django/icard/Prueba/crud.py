#Def y creacion clases
#Variaebles
ids = []
nombres = []
edades = []
salir = 0

#creacion de clases:
class persona:
    def __init__(self, id, nombre, edad):
        self.id = id
        self.nombre = nombre
        self.edad = edad

    
    def func(self):
        print(f"\nid: {self.id,} \nNombre: {self.nombre} \nedad: {self.edad} ")

while True:
    salir = int(input("digite 1 si quiere ingresar un usuario o 2 si quiere salir"))
    if salir == 1:
        id = int(input("Digite su id "))
        nombre = str(input("Digite su niombre "))
        edad = int(input("Digite su edad "))
        
    elif salir == 2:

        p1 = persona(id=ids, nombre=nombres, edad=edades)
        p1.func()

        break
    else:
        print("Digite un valor valido")




p1 = persona(id=ids, nombre=nombres, edad=edades)

p1.func()



