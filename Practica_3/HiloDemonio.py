from threading import Thread
from time import sleep
from RRDtool import RRDActualizar, RRDCrear
from HostResourcesMib import getTcpInSegs, getTcpOutSegs, getUdpInDatagrams, getUdpInDatagrams
from Dispositivos import get_ip_dispositivos
from os import system

# https://rico-schmidt.name/pymotw-3/threading/
def worker(comunidad, host):
    i = 1
    while 1:
        # RRDActualizar(host, "IfInNUnicastPkts", "N:" + str(getIfInNUnicastPkts(comunidad,host, "1", )))
        # RRDActualizar(host, "IfOutNUnicastPkts", "N:" + str(getIfOutNUnicastPkts(comunidad,host, "2", )))
        RRDActualizar(host, "TcpInSegs", "N:" + str(getTcpInSegs(comunidad,host)))
        RRDActualizar(host, "TcpOutSegs", "N:" + str(getTcpOutSegs(comunidad,host)))
        RRDActualizar(host, "UdpInDatagrams", "N:" + str(getUdpInDatagrams(comunidad,host)))
        RRDActualizar(host, "UdpOutDatagrams", "N:" + str(getUdpInDatagrams(comunidad,host)))
        sleep(1)


def empezarMonitorearAgentes():
    hosts = get_ip_dispositivos()
    comunidad = "FernandoCompany"
    print(f'Numero de agentes: {len(hosts)}')
    if len(hosts) != 0:
        for host in hosts:
            print(f'\tPreparando: {host}')
            t = Thread(target=worker, args=(comunidad, host, ))
            t.start()
            t._stop
            print(f'\t Listo: {host}')
            sleep(3)
