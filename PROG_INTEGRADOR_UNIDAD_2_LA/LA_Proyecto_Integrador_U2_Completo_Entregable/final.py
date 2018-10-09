import re
print("Lenguajes y Autómatas U2|Proyecto Integrador|\n\"###PROGRAMAS###\".")
def UNO():
	print("Lenguajes y Autómatas U2|Proyecto Integrador\n\"ENCONTRAR PALABRAS SIMILARES\".")
	archivo = open("archivo4.txt", "r")
	for linea in archivo.readlines():
		print (linea)
	splitValues = linea.split(" ")
	coincidencia = input("Palabras que coincidan con:")
	print("Se encontraron las siguientes coincidencias:")
	for i in range(len(splitValues)):
		if(re.search(r"\b"+re.escape(coincidencia)+"*[a-zA-Z]+",splitValues[i])):
			if(i==0):
				print("Se encontraron las siguientes coincidencias:")
			try:
				print(re.search(r"\b"+re.escape(coincidencia)+"*[a-zA-Z]+",splitValues[i]).group())
			except AttributeError:
				print(re.search(r"\b"+re.escape(coincidencia)+"*[a-zA-Z]+",splitValues[i]))
				archivo.close()
def DOS():
	print("Lenguajes y Autómatas U2|Proyecto Integrador\n\"BUSCAR UNA PALABRA ESPECIFICA Y REEMPLAZAR TODAS SUS APARICIONES\".")
	archivo = open("archivo4.txt", "r")
	for linea in archivo.readlines():
		print (linea)
		splitValues =linea.split(" ")
		palabraReemplazar = input("¿Que palabra desea reemplazar?")
		reemplazo = input("¿Por cual desea reemplazarlo?")
		print("Se encontraron las siguientes coincidencias:")
		for i in range(len(splitValues)):
			if(re.search(r""+re.escape(palabraReemplazar)+"",splitValues[i])):
				if(i==0):
					print("Se encontraron las siguientes coincidencias:")
				try:
					splitValues[i] = reemplazo
				except AttributeError:
					archivo.close()
		for i in range(len(splitValues)):
			print(splitValues[i],end=" ")
def TRES():
	print("Lenguajes y Autómatas U2|Proyecto Integrador\n\"ELIMINAR PALABRAS REPETIDAS SEGUIDAS\".")
	archivo = open("archivo4.txt", "r")
	for linea in archivo.readlines():
		print (linea)
		splitValues = linea.split(" ")
		palabraDelRepetido = input("Eliminar las repeticiones de:")
		contador = 0
		print("Se encontraron las siguientes coincidencias:")
		for i in range(len(splitValues)):
			if(re.search(r""+re.escape(palabraDelRepetido)+"",splitValues[i])):
				if(i==0):
					print("Se encontraron las siguientes coincidencias:")
				try:
					contador=contador+1
					if(contador>1):
						splitValues[i]=""
				except AttributeError:
					archivo.close()
		for i in range(len(splitValues)):
			if(splitValues[i]==""):
				print(splitValues[i],end="")
			print(splitValues[i],end=" ")
def CUATRO():
	print("Lenguajes y Autómatas U2|Proyecto Integrador\n\"CONVERTIR LAS PALABRAS DE MAYUSCULAS A MINUSCULAS Y VICEVERSA\".")
	archivo = open("archivo4.txt", "r")
	for linea in archivo.readlines():
		print (linea)
		splitValues = linea.split(" ")
		print("Se encontraron las siguientes coincidencias:")
		for i in range(len(splitValues)):
			if(re.search("[A-Z]*[A-Z]",splitValues[i])):
				print(splitValues[i].lower())
				if(re.search("[a-z]*[a-z]",splitValues[i])):
					print(linea.upper())
					print(splitValues[i].upper())
				try:
					re.search("[a-z]*[a-z]",splitValues[i]).group()
				except AttributeError:
					archivo.close()
def CINCO():
	print("Lenguajes y Autómatas U2|Proyecto Integrador\n\"ENCONTRAR UNA EXPRESION MATEMATICA COMO FORMULAS\".")
	archivo = open("archivo4.txt", "r")
	for linea in archivo.readlines():
		print (linea)
		splitValues = linea.split(" ")
		for i in range(len(splitValues)):
			if(re.search("[a-z0-9](\\d*|[+*/().-=]|np\\d+|\\s+)*",splitValues[i])):
				if(i==0):
					print("Se encontraron las siguientes coincidencias:")
				try:
					print(re.search("[a-z0-9](\\d*|[+*/().-=]|np\\d+|\\s+)*",splitValues[i]).group())
				except AttributeError:
					print(re.search("[a-z0-9](\\d*|[+*/().-=]|np\\d+|\\s+)*",splitValues[i]))
					archivo.close()
while True:
	print("1.-ENCONTRAR PALABRAS SIMILARES.")
	print("2.-ELIMINAR PALABRAS REPETIDAS SEGUIDAS.")
	print("3.-BUSCAR UNA PALABRA ESPECIFICA Y REEMPLAZAR TODAS SUS APARICIONES.")
	print("4.-CONVERTIR LAS PALABRAS DE MAYUSCULAS A MINUSCULAS Y VICEVERSA.")
	print("5.-ENCONTRAR UNA EXPRESION MATEMATICA COMO FORMULAS.")
	Opcion = input("Elige una opcion:")
	if Opcion.strip() == 'uno':
		UNO()
	if Opcion.strip() == 'dos':
		DOS()
	if Opcion.strip() == 'tres':
		TRES()
	if Opcion.strip() == 'cuatro':
		CUATRO()
	if Opcion.strip() == 'cinco':
		CINCO()