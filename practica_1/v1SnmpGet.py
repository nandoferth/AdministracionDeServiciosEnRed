from pysnmp.hlapi import *
from binascii import unhexlify
def consultaSNMP(comunidad, host, oid):
    iterator = getCmd(
        SnmpEngine(),
        CommunityData(comunidad, mpModel=0),
        UdpTransportTarget((host, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(oid))
    )

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        print(errorIndication)

    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

    else:
        for varBind in varBinds:
            varB = (' = '.join([x.prettyPrint() for x in varBind]))
            resultado = varB.split()[2]
    return resultado

#print(consultaSNMP("FernandoCompany", "192.168.100.40", "1.3.6.1.2.1.2.1.0"))
print(consultaSNMP("FernandoCompany", "192.168.100.40", "1.3.6.1.2.1.4.9.0"))
#ifDescr = consultaSNMP("Nodo1Agente", "192.168.100.40", "1.3.6.1.2.1.2.2.1.2.1")
#ifDescrDec = bytes.fromhex(ifDescr[2:])
#print(ifDescrDec.decode("ASCII"))