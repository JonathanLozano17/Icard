
"""
#Ejercicio 1
operacion = (((3 + 2) / (2 * 5)) ** 2 )
print (operacion)


#Ejercicio 2
num_horas = int(input("Digite el numero de horas trabajadas "))
val_horas = int(input("Digite el valor de horas trabajadas "))

print("el valor de horas trabajadas es ", (num_horas*val_horas) )


#Ejercicio 3
num = int(input("Digite un numero positivo: "))

while num <= 0:
    print("El número no es positivo.")
    num = int(input("Por favor, digite un numero positivo: "))

suma = (num * (num + 1)) / 2
print("El resultado es", suma)



#4

peso = float(input("Digite su peso en kg"))
altura = float(input("Digite su peso en metros"))

imc = round(float(peso)/float(altura)**2,2)
print("Su indice de masa corporal es: ", imc  )



#5
pan = 3.49

cantidad_pan = float(input("Digite la cantidad de pan vendido: "))

precio_pan = (pan * cantidad_pan)
precio_descuento = round(precio_pan*0.60,2)
precio_final = precio_pan - precio_descuento

print ("El precio habitual de cada barra de pan es: ", pan,"$")
print ("El precio habitual de cada barra de pan es: ", round(precio_pan,2),"$")
print ("El precio habitual de cada barra de pan es: ", round(precio_descuento,2),"$")
print ("el descuento es del 60%")
print ("el precio final es: ", round(precio_final,2))

nombre = input("Digite su nombre ")
num = int(input("Digite un numero "))
i = 1

while i <= num:
    i = i + 1
    print(f"{nombre}\n")



#bucle que itere asteriscos

numero = int(input("Digite la cantidad de asteriscos "))

print("asteriscos alineados a la derecha\n")
for i in range(1, numero + 1 ):
    espacio = numero - i
    print(" " * espacio, "*" * i)


print("asteriscos alineados a la izquierda\n")
for i in range(1, numero + 1):
    print("*" * i)


print("piramide de numeros\n")
for i in range(1, numero + 1):
    print(" " * (numero - i) + " ".join(str(j) for j in range(1, i +1)))


print("piramide de letras\n")
ascii_value = 65
for i in range(0, numero):
    print(" " * (numero - i), end=" ")
    for j in range(0, i + 1):
        alphabet = chr(ascii_value)
        print(alphabet, end=" ")
        ascii_value += 1
    print()



nombre = str(input("Digite su nombre "))

i = 1
for i in range(len(nombre) + 1):
    pass
print(f"su nombre tiene #{i} letras")


numero = str(input("Digite su numero con este formato +xx-xxxxxxxxxx-xx:: "))

caracter = 4
caracter2 = -3


numero = numero[caracter: caracter2]
print (numero)


frase = str(input("Digite su frase: "))

print(frase[::-1])

frase_invertida = ''
for i in frase:
    frase_invertida =   i + frase_invertida
    print(i)

print(frase_invertida)



fecha = input("Digite su fecha de nacimiento en formato dd/mm/aaaa: d")

print("fecha es", fecha[:2])
print("fecha es", fecha[3:5])
print("fecha es", fecha[-4:])

DIA = fecha[:fecha.find("/")]
MESAÑO = fecha[fecha.find("/")+1:]
MES = MESAÑO[:MESAÑO.find("/")]
AÑO = MESAÑO[MESAÑO.find("/")+1:]

print('Día', DIA)
print('Mes', MESAÑO)
print('Mes', MES)
print('Año', AÑO)



frase = input("Digite una frase")
letra = input("Digite una vocal en minuscula")
print(frase.replace(letra, letra.upper()))

correo = input("Digite su correo ")
correoIni = correo[:correo.find("@")]
print(f"{correoIni}@ceu.es")
print (correoIni)


precio = input("Digite el valor ")
print(precio[:precio.find(".")] + " Centavos"+ " "+ precio[precio.find(".")+1:] + "$")
"""


compra = input("Digite sus compras separadas por comas")
print(compra.replace("," , "\n"))
