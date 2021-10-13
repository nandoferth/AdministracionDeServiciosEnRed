from rrdtool import create, update, graphv, last, OperationalError

path = "/home/linuxlite/Documents/practicas/Practica_2/"

def RRDCreate(host, nivel, nivel_nombre):
    # nivel: cargaCPU, cargaRAM, cargaAlmacenamiento
    # nivel_nombre: CPU, RAM Almacenamiento
    pathCreate = path + host + "/trend"+nivel_nombre+".rrd"
    ret = create(
        pathCreate,
        "--start", 'N',
        "--step", '60',
        "DS:"+nivel+":GAUGE:600:U:U",
        "RRA:AVERAGE:0.5:1:24"
    )
    if ret:
        print("error()")
        return False
    return True

def RDDGraphv(host, nivel, nivel_nombre, umbral):
    # nivel: cargaCPU, cargaRAM, cargaAlmacenamiento
    # nivel_nombre: CPU, RAM Almacenamiento
    pathImg = path + host + "/carga_"+nivel_nombre+".png"
    pathRRD = path + host + "/trend"+nivel_nombre+".rrd"
    tiempo_final = int(last(pathRRD))
    tiempo_inicial = tiempo_final - 600
    ret = graphv(
        pathImg,
        "--start", str(tiempo_inicial),
        "--end", str(tiempo_final),
        "--vertical-label=Carga de " + nivel_nombre,
        '--lower-limit', '0',
        '--upper-limit', '100',
        "--title=Uso del "+ pathRRD +" del agente Usando SNMP y RRDtools \n Detección de umbrales",

        "DEF:muestras=" + pathRRD + ":"+ nivel +":AVERAGE",

        "VDEF:cargaMAX=muestras,MAXIMUM",
        "VDEF:cargaMIN=muestras,MINIMUM",
        "VDEF:cargaSTDEV=muestras,STDEV",
        "VDEF:cargaLAST=muestras,LAST",

        "CDEF:umbral=muestras,"+umbral+",LT,0,muestras,IF",
        "LINE5:muestras#00FF00:Carga " +nivel_nombre,
        "AREA:umbral#FF9F00:Carga "+nivel_nombre+" mayor que "+umbral,
        "HRULE:"+umbral+"#FF0000:Umbral "+umbral+"% - 99%",

        "PRINT:cargaLAST:%6.2lf",
        "GPRINT:cargaMIN:%6.2lf %SMIN",
        "GPRINT:cargaSTDEV:%6.2lf %SSTDEV",
        "GPRINT:cargaLAST:%6.2lf %SLAST"
    )

    return True

def RRDUpdate(host, nivel_dato, nivel_nombre):
    pathRRD = path + host + "/trend"+nivel_nombre+".rrd"
    update(pathRRD, "N:"+nivel_dato)