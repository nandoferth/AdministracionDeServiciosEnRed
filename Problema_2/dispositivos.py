def getIpsDispositivos():
    try:
        file = open("agentes.txt", "r")
        ips = []
        for dispositivos in file:
            dispositivos_data = list(dispositivos.split(" "))
            ips.append(dispositivos_data[1])
        return ips
    except FileNotFoundError:
        file = open("agentes.txt", "w")
        return []
    finally:
        file.close()