
from SNPMget import consultaSNMP
from datetime import datetime, timedelta

def gethrStorageAllocationsUnits(comunidad, host, valorPhyMe):
    hrStorageAllocationsUnits = consultaSNMP(comunidad, host, "1.3.6.1.2.1.25.2.3.1.4."+valorPhyMe)

    return hrStorageAllocationsUnits

def gethrStorageSize(comunidad, host, valorPhyMe):
    hrStorageSize = consultaSNMP(comunidad, host, "1.3.6.1.2.1.25.2.3.1.5."+valorPhyMe)

    return hrStorageSize

def gethrStorageUsed(comunidad, host, valorPhyMe):
    hrStorageUsed = consultaSNMP(comunidad, host, "1.3.6.1.2.1.25.2.3.1.6."+valorPhyMe)

    return hrStorageUsed

def gethrRAMUsed(comunidad, host, valorPhyMe):
    hrStorageAllocationsUnits = int(gethrStorageAllocationsUnits(comunidad, host, valorPhyMe))
    hrStorageSize = int(gethrStorageSize(comunidad, host, valorPhyMe))
    hrStorageUsed = int(gethrStorageUsed(comunidad, host, valorPhyMe))
    RAMUsed = hrStorageAllocationsUnits * hrStorageUsed
    RAMTot = hrStorageSize*hrStorageAllocationsUnits
    TotRamUsed = (RAMUsed/RAMTot)*100

    return TotRamUsed

def gethrProcessorLoad(comunidad, host, valorProLoad):
    hrProcessorLoad = consultaSNMP(comunidad, host, "1.3.6.1.2.1.25.3.3.1.2."+valorProLoad)

    return hrProcessorLoad

def gethrAlmacenamiento(comunidad, host, valorAlMem):
    hrStorageAllocationsUnits = int(gethrStorageAllocationsUnits(comunidad, host, valorAlMem))
    hrStorageSize = int(gethrStorageSize(comunidad, host, valorAlMem))
    hrStorageUsed = int(gethrStorageUsed(comunidad, host, valorAlMem))
    AlmacenamientoUsed = hrStorageAllocationsUnits * hrStorageUsed
    AlmacenamientoTot = hrStorageSize * hrStorageAllocationsUnits
    TotAlmacenamientoUsed = (AlmacenamientoUsed / AlmacenamientoTot) * 100

    return TotAlmacenamientoUsed

def getNombreDispositivo(comunidad, host):
     return consultaSNMP(comunidad, host, "1.3.6.1.2.1.1.5.0")

def getTiemoActiviad(comunidad, host):
    time = consultaSNMP(comunidad, host, "1.3.6.1.2.1.1.3.0")
    times = timedelta(seconds=int(time))
    return times

def getComunidad(comunidad, host):
    return "FernandoCompany"



#print(getNombreDispositivo("FernandoCompany", "192.168.100.40")) #79
#print(getTiemoActiviad("FernandoCompany", "192.168.100.40")) #79

#print(getNombreDispositivo("FernandoCompany", "192.168.100.79")) #79
#print(getTiemoActiviad("FernandoCompany", "192.168.100.79")) #79

#print(gethrRAMUsed("FernandoCompany", "192.168.100.40", "3"))
#print(gethrProcessorLoad("FernandoCompany", "192.168.100.40", "6"))
#print(gethrAlmacenamiento("FernandoCompany", "192.168.100.75", "1"))
#print(gethrRAMUsed("FernandoCompany", "192.168.100.75", "1"))
#print(gethrProcessorLoad("FernandoCompany", "192.168.100.75", "196608"))
# 196608, 6
#print(gethrAlmacenamiento("FernandoCompany", "192.168.100.75", "3"))
