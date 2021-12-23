from threading import Thread
from time import sleep
from RRDtool import RRDUpdate, RRDCreate, RDDGraphv
from HostResourcesMib import gethrRAMUsed, gethrProcessorLoad, gethrAlmacenamiento
from os import system
from dispositivos import getIpsDispositivos

def empezarMonitorearAgentes(comunidad, host):
    # RRDCreate(host, "CargaCPU", "CPU")
    # RRDCreate(host, "CargaRAM", "RAM")
    # RRDCreate(host, "CargaAlmacenamiento", "Almacenamiento")

    while 1:
        RAM_dato = gethrRAMUsed(comunidad, host)
        CPU_dato = gethrProcessorLoad(comunidad, host)
        Alamacenamiento_dato = gethrAlmacenamiento(comunidad, host)

        RRDUpdate(host, str(RAM_dato), "RAM")
        RRDUpdate(host, str(CPU_dato), "CPU")
        RRDUpdate(host, str(Alamacenamiento_dato), "Almacenamiento")
        sleep(2)
    return False

def updateHilo():
    for ip in getIpsDispositivos():
        hilo = Thread(target=empezarMonitorearAgentes, args=("FernandoCompany", ip))
        hilo.start()

# updateHilo()