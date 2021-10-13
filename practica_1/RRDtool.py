from rrdtool import create, update, graph
from time import time

def crear(host, grafica):
    inicio = str(time()).split('.')[0]
    return create(host + "/" + grafica + ".rrd",
                  "--start", inicio,
                  "--step", '60',
                  "DS:" + grafica + ":COUNTER:600:U:U",
                  "RRA:AVERAGE:0.5:6:576",
                  "RRA:AVERAGE:0.5:1:144")

def actualiza(comuniada, host):
    while 1:
        # 1
        update(comuniada + '/inMCast.rrd', "N:0")

        # 2)

#crear("Nodo1Agente", "inMCast")
# actualiza("Nodo1Agente", "3434")

def grafica(comunidad, timpo, grafica):
    ahora = int(time())
    final = ahora - 60
    inicial = final - (60 * int(timpo))
    graph(comunidad + "/"+grafica+ ".png",
                     "--start",str(inicial),
 #                   "--end","N",
                     "--vertical-label="+'Bytes/s'+"",
                     "DEF:"+grafica+"="+comunidad+"/"+grafica+".rrd:"+grafica+":AVERAGE",
                     "DEF:"+grafica+"="+comunidad+"/"+grafica+".rrd:"+grafica+":AVERAGE",
                     "AREA:"+grafica+"#FF0000:"+grafica+"\r")