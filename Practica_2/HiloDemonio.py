from threading import Thread
from time import sleep
from RRDtool import RRDUpdate, RRDCreate, RDDGraphv
from HostResourcesMib import gethrRAMUsed, gethrProcessorLoad, gethrAlmacenamiento
from os import system

def empezarMonitorearAgentes(comunidad, host, SysOpe):
    RRDCreate(host, "CargaCPU", "CPU")
    RRDCreate(host, "CargaRAM", "RAM")
    RRDCreate(host, "CargaAlmacenamiento", "Almacenamiento")
    if SysOpe == "W":
        valorPhysMem = "3"
        valorProLoad = "6"
        valorAlmaMem = "1"
    else:
        valorPhysMem = "1"
        valorProLoad = "196608"
        valorAlmaMem = "3"

    while 1:
        RAM_dato = gethrRAMUsed(comunidad, host, valorPhysMem)
        CPU_dato = gethrProcessorLoad(comunidad, host, valorProLoad)
        Alamacenamiento_dato = gethrAlmacenamiento(comunidad, host, valorAlmaMem)

        RRDUpdate(host, str(RAM_dato), "RAM")
        RRDUpdate(host, str(CPU_dato), "CPU")
        RRDUpdate(host, str(Alamacenamiento_dato), "Almacenamiento")
        sleep(10)
    return False

def updateHilo():
    hiloW = Thread(target=empezarMonitorearAgentes, args=("FernandoCompany", "192.168.100.40", "W"))
    hiloW.start()
    hiloL = Thread(target=empezarMonitorearAgentes, args=("FernandoCompany", "192.168.100.80", "L"))
    hiloL.start()
    print("Se está monitortoreando los agentes")

updateHilo()

def main():
    while 1:
        print("1. Para ver las graficas de agente en Windows.\n2. Para ver las graficas de agente en Linux.")

        opcion = int(input())
        if (opcion == 1):
            RDDGraphv("192.168.100.40", "CargaCPU", "CPU", "80")
            RDDGraphv("192.168.100.40", "CargaRAM", "RAM", "90")
            RDDGraphv("192.168.100.40", "CargaAlmacenamiento", "Almacenamiento", "90")
        elif(opcion == 2):
            RDDGraphv("192.168.100.80", "CargaCPU", "CPU", "80")
            RDDGraphv("192.168.100.80", "CargaRAM", "RAM", "90")
            RDDGraphv("192.168.100.80", "CargaAlmacenamiento", "Almacenamiento", "90")
        input("Por favor presione la tecla Enter para continuar.")
        system('clear')
main()
# def update(num_hilo, host, wait):
#   while 1:
#         print("Hilo:", num_hilo, ", Host: ", host)
#         time.sleep(wait)