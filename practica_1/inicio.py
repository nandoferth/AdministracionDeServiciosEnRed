from os import system
from v1SnmpGet import consultaSNMP

def resumen():
    comunidad = []
    host = []
    with open("agentes.txt", "r") as agentes:
        for agente in agentes:
            arr = agente.split()
            comunidad.append(arr[0])
            host.append(arr[1])
    nodos = len(comunidad)
    if nodos != 0:
        print("Número de dispositivos (agentes) que están en monitoreo: ", nodos)
        print("###########################################################")
        for nodo in range(nodos):
            response = system("ping -c 1 " + host[nodo])
            if response != 0:
                estado = "DOWN"
                print("Estado de conectividad con el agente '", comunidad[nodo], "': ", estado)
            else:
                print("Estado de conectividad con el agente '", comunidad[nodo], "': UP")
            print("###########################################################")
            interfaces = consultaSNMP(comunidad[nodo], host[nodo], "1.3.6.1.2.1.2.1.0")
            print("Número de interfaces de red del agente '", comunidad[nodo], "' : ", interfaces)
            print("###########################################################")
            for interfaz in range(int(interfaces)):
                ifDescr = consultaSNMP(comunidad[nodo], host[nodo], "1.3.6.1.2.1.2.2.1.2." + str(interfaz + 1))
                ifAdmin = consultaSNMP(comunidad[nodo], host[nodo], "1.3.6.1.2.1.2.2.1.7." + str(interfaz + 1))
                if ifAdmin != "1":
                    ifAdmin = "DOWN"
                else:
                    ifAdmin = "UP"
                if interfaz == 10:
                    break
                if ifDescr[:2] == "0x":
                    ifDescrDec = bytes.fromhex(ifDescr[2:])
                    print(str(interfaz + 1) + ". Estado administrativo: " + ifAdmin + "\t\t\tDescripción: " + ifDescrDec.decode("ASCII"))
                else: print(str(interfaz + 1) + ". Estado administrativo: " + ifAdmin + "\t\t\tDescripción: " + ifDescr)

            print("###########################################################")
    else:
        print("No hay agentes.")
    return

#resumen()

