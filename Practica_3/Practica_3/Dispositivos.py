from os import mkdir
from RRDtool import RRDCrear


def agregar(comunidad, host):
    f = open("agentes.txt", "a")
    f.write(comunidad + " " + host + " " + ".\n")
    f.close()
    try:
        mkdir(host)
        # RRDCrear(host, "IfInNUnicastPkts")
        # RRDCrear(host, "IfOutNUnicastPkts")
        RRDCrear(host, "TcpInSegs")
        RRDCrear(host, "TcpOutSegs")
        RRDCrear(host, "UdpInDatagrams")
        RRDCrear(host, "UdpOutDatagrams")

    except OSError as e:
        print(f'Error: {e.strerror}')
    return True


def get_ip_dispositivos():
    try:
        file = open("agentes.txt", "r")
        ip = []
        for dispositivos in file:
            dispositivos_data = list(dispositivos.split(" "))
            ip.append(dispositivos_data[1])
        return ip
    except FileNotFoundError:
        file = open("agentes.txt", "w")
        return []
    finally:
        file.close()
