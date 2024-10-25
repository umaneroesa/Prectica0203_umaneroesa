#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
frase = str(input("Inserte la frase "))
letras = str(input("Inserte la letra "))
repetido=0
for i in frase:
    if i==letras:
        repetido=repetido+1
print("La letra " + letras + " aparece " + str(repetido) + " veces en la frase")