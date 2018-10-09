# encoding: utf-8
import re
print("Lenguajes y Autómatas U2|Ejercicios Exp. Regulares|Br. Luis Adrián Balam Espadas.\n\"Las palabras que tengan una longitud de 7 letras o más\".")
archivo = open("archivo4.txt", "r")
for linea in archivo.readlines():
	print (linea)
splitValues = linea.split(" ")
print("Se encontraron las siguientes coincidencias:")
for i in range(len(splitValues)):
    if(re.search("\D[\w]{7,}",splitValues[i])):
        if(i==0):
            print("Se encontraron las siguientes coincidencias:")
        try:
            print(re.search("\D[\w]{7,}",splitValues[i]).group())
        except AttributeError:
            print(re.search("\D[\w]{7,}",splitValues[i]))
            archivo.close()