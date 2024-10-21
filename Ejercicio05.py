#Los alumnos de Hogwarts se han dividido en dos casas, Gryffindor y Slytherin, de acuerdo al sexo y el nombre. Gryffindor está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y Slytheryn por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
nombre = str(input("Cual es tu nombre? "))
sexo = str(input("Como te identificas? Hombre o mujer? "))
if sexo=="mujer".lower():
    if nombre.lower() < "m":
        casa = "Gryffindor"
    else:
        casa= "Slytherin"
else:
    if nombre.lower() > "n":
        casa = "Gryffindor"
    else:
        Casa = "Slytherin"
print("Tu perteneces a la casa " + casa)