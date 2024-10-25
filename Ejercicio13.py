#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
x = "salir"
frase = str(input("Introduzca algo "))
while x != frase:
    print(frase)
    frase= str(input("Introduzca algo "))
