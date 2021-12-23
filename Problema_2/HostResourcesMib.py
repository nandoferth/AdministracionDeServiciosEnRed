from SNMPget import consultaSNMP
from datetime import datetime, timedelta

# No. de Equipo
def getNombreDispositivo(comunidad, host):
    try:
        return consultaSNMP(comunidad, host, "1.3.6.1.2.1.1.5.0")
    except:
        return "None"

def getComunidad(comunidad, host):
    return "FernandoCompany"

# Sistema Operativo del Servidor
def getSistemaOperativoServidor(comunidad, host):
    try:
        return consultaSNMP(comunidad, host, "1.3.6.1.2.1.1.1.0")
    except:
        return "None"

# Tiempo de actividad del servidor
def getTiempoActividadServidor(comunidad, host):
    try:
        time = consultaSNMP(comunidad, host, "1.3.6.1.2.1.1.3.0")
        times = timedelta(seconds=int(time))
        return times
    except ValueError:
        return time
    except:
        return 0

# Número de interfaces
def getNumeroInterfaces(comunidad, host):
    try:
        return consultaSNMP(comunidad, host, "1.3.6.1.2.1.2.1.0")
    except:
        return 0

# Información gráfica de uso de memoria RAM
def gethrRAMUsed(comunidad, host):
    # hrStorageAllocationsUnits = int(gethrStorageAllocationsUnits(comunidad, host, "1"))
    # hrStorageSize = int(gethrStorageSize(comunidad, host, "1"))
    # hrStorageUsed = int(gethrStorageUsed(comunidad, host, "1"))
    RAMUsed = int(consultaSNMP(comunidad, host, "1.3.6.1.4.1.2021.4.6.0"))
    RAMTot = int(consultaSNMP(comunidad, host, "1.3.6.1.4.1.2021.4.5.0"))
    TotRamUsed = (RAMUsed/RAMTot)*100

    return TotRamUsed

def gethrStorageAllocationsUnits(comunidad, host, valor):
    hrStorageAllocationsUnits = consultaSNMP(comunidad, host, "1.3.6.1.2.1.25.2.3.1.4."+valor)

    return hrStorageAllocationsUnits

def gethrStorageSize(comunidad, host, valor):
    hrStorageSize = consultaSNMP(comunidad, host, "1.3.6.1.2.1.25.2.3.1.5."+valor)

    return hrStorageSize

def gethrStorageUsed(comunidad, host, valor):
    hrStorageUsed = consultaSNMP(comunidad, host, "1.3.6.1.2.1.25.2.3.1.6."+valor)

    return hrStorageUsed

# Información gráfica del CPU
def gethrProcessorLoad(comunidad, host):
    hrProcessorLoad = consultaSNMP(comunidad, host, "1.3.6.1.4.1.2021.11.7.0")

    return hrProcessorLoad

# Información gráfica de uso de Disco Duro
def gethrAlmacenamiento(comunidad, host):
    hrStorageAllocationsUnits = int(gethrStorageAllocationsUnits(comunidad, host, "3"))
    hrStorageSize = int(gethrStorageSize(comunidad, host, "3"))
    hrStorageUsed = int(gethrStorageUsed(comunidad, host, "3"))
    AlmacenamientoUsed = hrStorageAllocationsUnits * hrStorageUsed
    AlmacenamientoTot = hrStorageSize * hrStorageAllocationsUnits
    TotAlmacenamientoUsed = (AlmacenamientoUsed / AlmacenamientoTot) * 100

    return TotAlmacenamientoUsed

# print(getNombreDispositivo("FernandoCompany", "40.40.40.2"))
# print(getSistemaOperativoServidor("FernandoCompany", "40.40.40.2"))
# print(getTiempoActividadServidor("FernandoCompany", "40.40.40.2"))
# print(getNumeroInterfaces("FernandoCompany", "40.40.40.2"))

# print(getNombreDispositivo("FernandoCompany", "192.168.122.1"))
# print(getSistemaOperativoServidor("FernandoCompany", "192.168.122.1"))
# print(getTiempoActividadServidor("FernandoCompany", "192.168.122.1"))
# print(getNumeroInterfaces("FernandoCompany", "192.168.122.1"))

# print(gethrRAMUsed("FernandoCompany", "192.168.122.1"))
# print(gethrProcessorLoad("FernandoCompany", "192.168.122.1"))
# print(gethrAlmacenamiento("FernandoCompany", "192.168.122.1"))