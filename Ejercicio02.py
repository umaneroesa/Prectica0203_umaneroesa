#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
n = float(input("Introduce el primer numero "))
m = float(input("Introduce el segundo numero "))
if n==0:
    print("Error")
elif m==0:
    print("Error")
else: 
    print(n/m)