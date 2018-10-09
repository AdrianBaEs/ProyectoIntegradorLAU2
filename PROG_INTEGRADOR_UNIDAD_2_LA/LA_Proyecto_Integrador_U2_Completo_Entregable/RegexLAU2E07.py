# encoding: utf-8
import re
print("Lenguajes y Autómatas U2|Ejercicios Exp. Regulares|Br. Luis Adrián Balam Espadas.\n\"Detección de números de teléfono en México\".")
archivo = open("archivo4.txt", "r")
for linea in archivo.readlines():
	print (linea)
splitValues = linea.split(" ")
print("Se encontraron las siguientes coincidencias:")
for i in range(len(splitValues)):
    if(re.search("(^9[0-9]{9})",splitValues[i])):
        if(i==0):
            print("Se encontraron las siguientes coincidencias:")
        try:
            print(re.search("(^9[0-9]{9})",splitValues[i]).group())
        except AttributeError:
            print(re.search("(^9[0-9]{9})",splitValues[i]))
            archivo.close()