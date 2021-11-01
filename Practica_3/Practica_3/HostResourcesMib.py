from SNMPget import consultaSNMP
from datetime import datetime, timedelta

def getIfInNUnicastPkts(comunidad, host, interface):
    ifInNUnicastPkts = consultaSNMP(comunidad, host, "1.3.6.1.2.1.2.2.1.12")
    return ifInNUnicastPkts

def getIfOutNUnicastPkts(comunidad, host, interface):
    ifOutNUnicastPkts = consultaSNMP(comunidad, host, "1.3.6.1.2.1.2.2.1.18")
    return ifOutNUnicastPkts

def getTcpInSegs(comunidad, host):
    tcpInSegs = consultaSNMP(comunidad, host, "1.3.6.1.2.1.6.10.0")
    return tcpInSegs

def getTcpOutSegs(comunidad, host):
    tcpOutSegs = consultaSNMP(comunidad, host, "1.3.6.1.2.1.6.11.0")
    return tcpOutSegs

def getUdpInDatagrams(comunidad, host):
    udpInDatagrams = consultaSNMP(comunidad, host, "1.3.6.1.2.1.7.1.0")
    return udpInDatagrams

def getUdpOutDatagrams(comunidad, host):
    udpOutDatagrams = consultaSNMP(comunidad, host, "1.3.6.1.2.1.7.4.0")
    return udpOutDatagrams

def getNombreDispositivo(comunidad, host):
    return consultaSNMP(comunidad, host, "1.3.6.1.2.1.1.5.0")

def getTiempoActividad(comunidad, host):
    time = consultaSNMP(comunidad, host, "1.3.6.1.2.1.1.3.0")
    times = timedelta(seconds=int(time))
    return times

def getComunidad(comunidad, host):
    return "FernandoCompany"

# print(getTcpInSegs("FernandoCompany", "127.0.0.1"))