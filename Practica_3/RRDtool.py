from rrdtool import create, update, graph, last, graphv
from time import time
from os.path import exists
path = "/home/fernando/Documentos/AdministracionDeserviciosEnRed-main/Practica_3/"

def RRDCrear(host, flujo):
    inicio = str(time()).split('.')[0]
    pathCreateRRD = path + host + "/trend" + flujo + ".rrd"

    return create(pathCreateRRD,
                          "--start", inicio,
                          "--step", "60",
                          "DS:" + flujo + ":COUNTER:600:U:U",
                          "RRA:AVERAGE:0.5:1:30",
                          "RRA:AVERAGE:0.5:6:180")

def RRDActualizar(host, flujo, valor):
    # print(host, flujo, valor)
    pathRRD = path + host + "/trend" + flujo + ".rrd"
    try:
        file = open(pathRRD, "r")
        file.close()
    except FileNotFoundError:
        RRDCrear(host, flujo)
    finally:
        update(pathRRD, valor)


def RRdGrafica(host, flujo, InOut):
    pathImg = path + host + "/carga_" + flujo + ".png"
    pathRRD = path + host + "/trend" + flujo + ".rrd"
    tiempo_inicial = int(time()) - (60 * 8)

    ret = graph(pathImg,
                 "--start",str(tiempo_inicial),
                # "--end","1635710400",
                 "--vertical-label="+'Bytes/s',
                 "DEF:MY"+InOut+"="+pathRRD+":"+flujo+":AVERAGE",
                 "VDEF:Max"+InOut+"=MY"+InOut+",MAXIMUM",
                 "AREA:MY"+ InOut +"#00FF00:"+InOut,)

    print("Host: ", host, "Grafica: ", flujo, " : OK")


