import re
from os import system, name
from codificar import *

def clear():
    if name == 'nt':
        _ = system('cls')

def menu():
    titulo = "Bienvenido al menú de encriptación"
    print("\n", titulo.center(50,"-"), "\n")
    opciones = ["Cifrado por sustitución", "Cifrado por transposición", "Cifrado por código telefónico", "Cifrado por Codificación Binaria"]
    subsecciones1=["Cifrado César", "Cifrado por llave", "Sustitución Vigenére", "Sustitución mediante XOR y llave"]
    subsecciones2 = ["Palabra inversa", "Mensaje inverso"]
    contador = 1
    for opcion in opciones:
        print(str(contador)+"."+str(opcion))
        contador+=1
        #Elegir opciones
    opcion = int(input("Digite una opción del menú: "))
    if opcion == 1:
        clear()
        print("\n",opciones[0].center(50, "-"))
        contador = 1
        for seccion in subsecciones1:
            print(str(contador)+"."+str(seccion))
            contador+=1
        opcion = int(input("Digite una opción de la sección: "))
        if opcion == 1:
            clear()
            print("\n",subsecciones1[0].center(50, "-"))
        elif opcion == 2:
            clear()
            print("\n",subsecciones1[1].center(50, "-"))
        elif opcion == 3:
            clear()
            print("\n",subsecciones1[2].center(50, "-"))
        elif opcion == 4:
            clear()
            print("\n",subsecciones1[0].center(50, "-"))
    elif opcion == 2:
        clear()
        print("\n",opciones[1].center(50, "-"))
        contador = 1
        for seccion in subsecciones2:
            print(str(contador)+"."+str(seccion))
            contador+=1
        opcion = int(input("Digite una opción de la sección: "))
        if opcion == 1:
            clear()
            print("\n",subsecciones2[0].center(50, "-"))
        elif opcion == 2:
            clear()
            print("\n",subsecciones2[1].center(50, "-"))
    elif opcion == 3:
        clear()
        print("\n",opciones[2].center(50, "-"))
    elif opcion == 4:
        clear()
        print("\n",opciones[3].center(50, "-"))

menu()