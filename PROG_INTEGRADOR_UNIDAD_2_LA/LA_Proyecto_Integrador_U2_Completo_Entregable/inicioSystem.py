import os, sys, re
print("Lenguajes y Autómatas U2|Ejercicios Exp. Regulares|\n\"###PROGRAMAS###\".")
archivo = open("archivo4.txt", "r")
for linea in archivo.readlines():
    while True:
        os.system('cls')
        print("1.-PALABRAS")
        print("2.-Almacenar  Contactos")
        print("3.-Actulizar Contactos")
        print("4.Eliminar Contacto")
        print("5.-Salir")
        print (linea)
    #Para poder mas facil manejar el proceso de errores
    try:
        Opcion = int(input("Inserte la opcion a elegir: "))
        # es cuando metes lo que no te pide el programa que agas 
        #cuando metes alguna otra cosa como letras y eso te manda
        # el error o bine tanmbien cunado se pasa de los numeros
        # que estan en le menu marca el error por que en este 
        #momento te estan pidiendo  que eligas una opcion con numeros que son
    except:
        print("opcion no valida")
        imput()
        continue
    if Opcion == 1:
        print("Lenguajes y Autómatas U2|Ejercicios Exp. Regulares|Br. Luis Adrián Balam Espadas.\n\"Las palabras que tengan una longitud de 7 letras o más\".")
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
        break
    elif Opcion == 2:
        break
    elif Opcion == 3:
        break
    elif Opcion == 4:
        break
    elif Opcion == 5:
        #finaliza y lo buelve a empezar
        break
    else :
        print("Opcion no Valida")
    input()

    archivo.close()