from inicio import resumen
from dispositivo import agregar, eliminar
from RRDtool import grafica, actualiza
from os import system
def main():
    while 1:
        print("1. Inicio.\n2. Agregar dispositivo.\n3. Eliminar dispositivos.\n4. Reporte de información del dispositivo.\n")

        opcion = int(input())

        if (opcion == 1):
            resumen()
        elif (opcion == 2):
            print("Nombre del host o direccón IP: ")
            nombre = input()
            print("Version SNMP: ")
            version = input()
            print("Nombre de la comunidad: ")
            comunidad = input()
            print("Puerto: ")
            puerto = input()
            agregar(nombre, version, comunidad, puerto)
        elif (opcion == 3):
            f = open("agentes.txt", "r")
            if len(f.readlines()) != 0:
                print("Escribe la dirección IPV4 a eliminar.")
                for line in f:
                    print(line)
                host = input()
                eliminar(host)
        elif (opcion==4):
            grafica("Nodo1Agente", "3", "inMCast")
        elif(5):
            actualiza("Nodo1Agente", "inMCast")
        input("Por favor presione la tecla Enter para continuar.")
        system('clear')

main()
