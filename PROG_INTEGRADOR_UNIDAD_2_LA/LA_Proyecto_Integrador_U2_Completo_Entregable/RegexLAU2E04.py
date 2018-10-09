# encoding: utf-8
import re, os, sys
print("Lenguajes y Autómatas U2|Ejercicios Exp. Regulares|Br. Luis Adrián Balam Espadas.\n\"Expresiones encerradas entre comillas\".")

archivo = open("archivo4.txt", "r")
for linea in archivo.readlines():
	print (linea)

	splitValues = linea.split(" ")

for i in range(len(splitValues)):
    if(re.search("('.*')|(\".*\")*",splitValues[i])):
        if(i==0):
            print("Se encontraron las siguientes coincidencias:")
        try:
            print(re.search("('.*')|(\".*\")*",splitValues[i]).group())
        except AttributeError:
            print(re.search("('.*')|(\".*\")*",splitValues[i]))
archivo.close() 