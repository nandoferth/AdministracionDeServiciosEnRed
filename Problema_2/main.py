
from hiloDemonio import updateHilo

from reporte import generarReporte
from RRDtool import RDDGraphv
from os import system

if __name__ == "__main__":
    updateHilo()

    while 1:
        print("Crear reporte \n")
        host = input()

        print("Preparando imagenes...")
        RDDGraphv(host, "CargaCPU", "CPU", "80")
        RDDGraphv(host, "CargaRAM", "RAM", "90")
        RDDGraphv(host, "CargaAlmacenamiento", "Almacenamiento", "90")
        print("Imagenes listas!")

        generarReporte(host)
        print("Reporte listo")
        system("clear")