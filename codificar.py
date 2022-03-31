from os import system, name
from funciones import *
from menu import *

continuar = 1
while continuar == 1:
    clear()
    menu()
    continuar = int(input("¿Desea continuar?"))