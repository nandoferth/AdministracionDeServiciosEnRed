
from Dispositivos import agregar
from HiloDemonio import empezarMonitorearAgentes
from os import system
from Reporte import generarReporte

def menu():
    try:
        print("[1] Agregar dispositivo")
        print("[2] Generar Reporte")
        opcion = int(input())
        return opcion
    except KeyboardInterrupt:
        print("Se interrumpió  el flujo.")


if __name__ == '__main__':
    empezarMonitorearAgentes()
    while 1:
        input("Presione la tecla Enter para continuar.\n")
        system("clear")
        opcion = menu()

        if (opcion == 1):
            print("Nombre del HOST o la dirección IP: ")
            host = input()
            print("Nombre de la comunidad: ")
            comunidad = input()

            agregar(comunidad, host)

        elif (opcion == 2):
            print("Escribe el host a la dirección  IP del dispositivo a monitorizar.\n")
            host = input()
            generarReporte(host)
