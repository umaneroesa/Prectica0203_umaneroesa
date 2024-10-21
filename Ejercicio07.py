#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
numero = int(input("Inserte un numero entero "))
for x in range(1,numero+1):
    print("*" * x)