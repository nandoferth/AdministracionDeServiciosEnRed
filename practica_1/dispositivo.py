from os import mkdir
import shutil

from RRDtool import crear

def agregar(host, vSnmp, comunidad, puerto):
    f = open("agentes.txt", "a+")
    f.write(comunidad + " " + host + " " + vSnmp + " " + puerto + '\n')
    f.close()
    try:
        mkdir(host)
        crear(host, 'inMCast')
    except OSError as e:
        print(f"Error:{e.strerror}")
    return True

def eliminar(host):
    with open("agentes.txt", "r") as f:
        agentes = f.readlines()
    f.close()
    with open("agentes.txt", "w") as f:
        for agente in agentes:
            print(agente.split()[1])
            if agente.split()[1] != host:
                f.write(agente)
            else:
                print("Eliminado agente " , host , "...")
    f.close()
    try:
        shutil.rmtree(host)
    except OSError as e:
        print(f"Error:{e.strerror}")

    return

#agregar("192.168.100.60", "v1", "Nodo3Agente", "8080")
#eliminar("234fre43")