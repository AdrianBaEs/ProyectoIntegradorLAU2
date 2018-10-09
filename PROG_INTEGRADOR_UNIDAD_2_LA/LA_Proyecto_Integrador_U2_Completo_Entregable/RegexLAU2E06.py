# encoding: utf-8
import re
print("Lenguajes y Autómatas U2|Ejercicios Exp. Regulares|Br. Luis Adrián Balam Espadas.\n\"Detección de fechas\".")
archivo = open("archivo4.txt", "r")
for linea in archivo.readlines():
	print (linea)
splitValues = linea.split(" ")
print("Se encontraron las siguientes coincidencias:")
for i in range(len(splitValues)):
    if(re.search(".*([0-3][0-9].[0-1][0-9].\d).*",splitValues[i])):
        if(i==0):
            print("Se encontraron las siguientes coincidencias:")
        try:
            print(re.search(".*([0-3][0-9].[0-1][0-9].\d).*",splitValues[i]).group())
        except AttributeError:
            print(re.search(".*([0-3][0-9].[0-1][0-9].\d).*",splitValues[i]))
            archivo.close()