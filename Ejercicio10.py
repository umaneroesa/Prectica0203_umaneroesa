#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
contraseña="123456"
usuario =" "
while usuario != contraseña:
    usuario= str(input("Introduzca la contraseña "))
print("Contraseña correcta")