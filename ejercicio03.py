#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
x = int(input("Escribe un numero entero "))
if x % 2 == 0:
    print(str(x) + " es par")
else:
    print(str(x) + " es impar")