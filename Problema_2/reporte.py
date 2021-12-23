from os import system
from dns.rdatatype import PTR
from fpdf import FPDF
from HostResourcesMib import *
from time import sleep

from sensorFTP import SensorFTP
from sensorDNS import SensorDNS
from sensorHTTP import SensorHTTP
from sensorSSH import SensorSSH

path = "/home/fernando/Documents/redes3/Problema_2/"

def generarReporte(host):
    pdf = FPDF("P", "cm", "Letter")
    pdf.add_page()
    pdf.set_font("helvetica", "", 12)
    
    if (host != "40.40.40.2"):
        now = datetime.now()
        format = now.strftime('Día :%d, Mes: %m, Año: %Y, Hora: %H, Minutos: %M, Segundos: %S')

        pdf.cell(2, 1, "No. de Equipo: " + getNombreDispositivo("FernandoCompany", host), ln=True)
        pdf.cell(2, 1, "Integrantes: ", ln=True)
        pdf.cell(2, 1, "Fecha de elaboración: " + format, ln=True)
        pdf.cell(2, 1, "Sistema Operativo del Servidor: " + getSistemaOperativoServidor("FernandoCompany", host), ln=True)
        pdf.cell(2, 1, "Tiempo de actividad del servidor: " + str(getTiempoActividadServidor("FernandoCompany", host)), ln=True)
        pdf.cell(2, 1, "Número de interfaces: " + getNumeroInterfaces("FernandoCompany", host), ln=True)
    pdf.cell(2, 1, "_________________________________________________________________________________________________________", ln=True)
    # pdf.cell(2, 2, "UdpInDatagrams", ln=True)
    pdf.image(path + host + "/carga_Almacenamiento.png", type='', link='')
    pdf.cell(2, 1, "Información gráfica de uso de Disco Duro", ln=True)
    # pdf.cell(2,2,ln=True)

    # pdf.cell(2, 2, "UdpOutDatagrams", ln=True)
    pdf.image(path + host + "/carga_CPU.png", type='', link='')
    pdf.cell(2, 1, "Información gráfica del CPU", ln=True)
    # pdf.cell(2, 2, ln=True)

    # pdf.cell(2, 3, "TcpInSegs", ln=True)
    pdf.image(path + host + "/carga_RAM.png", type='', link='')
    pdf.cell(2, 1, "Información gráfica de uso de memoria RAM", ln=True)
    # pdf.cell(2,2,ln=True)
    pdf.cell(2, 1, "_________________________________________________________________________________________________________", ln=True)

    pdf.cell(2, 1, "Supervisión de Servidores", ln=True)
    
    if (host != "40.40.40.2"):
        pdf.cell(6, 1, "Sensor FTP", ln=True)
        obj = SensorFTP(host)
        status = obj.getStatus()
        if status == "UP":
            obj.login("fer", "29121996")
            pdf.cell(2, 1, "Tiempo de respuesta del servidor: " + str(obj.getTiempoRespuestaServidor()), ln=True)
            pdf.cell(2, 1, "Respuesta del servidor: " + obj.getRespuestaServidor(), ln=True)
            pdf.cell(2, 1, "Status FTP: " + status, ln=True)
            pdf.cell(2, 1, "Recuento de archivos de un directorio seleccionado: " + obj.printSupervisaCambiosFicheros("/home/fer/Documentos"), ln=True)
        else:
            pdf.cell(2, 1, "Status FTP: " + status, ln=True)

    
        pdf.cell(6, 1, "Sensor DNS", ln=True)
        obj = SensorDNS(host, "ns.dnsfernando.net")
        status = obj.getStatus()
        if status == "UP":
            pdf.cell(2, 1, "Status DNS: " + status, ln=True)
        pdf.cell(2, 1, "Status DNS: " + status, ln=True)

        pdf.cell(6, 1, "Sensor SSH", ln=True)
        obj = SensorSSH("fer", "29121996", host)

        status = obj.getStatus()
        if status == "Up":
            pdf.cell(2, 1, "Status SSH: " + status, ln=True)
        else:
            pdf.cell(2, 1, "Status SSH: " + status, ln=True)

    pdf.cell(6, 1, "Sensor HTTP", ln=True)
    obj = SensorHTTP(host)
    status = obj.getStatus()
    if status == "Up":
        pdf.cell(2, 1, "Tiempo de respuesta (carga): " + str(obj.getTiempoRespuesta()), ln=True)
        pdf.cell(2, 1, "Bytes ha recibido: " + str(obj.getBytesRecibido()), ln=True)
        pdf.cell(2, 1, "Status HTTP: " + status, ln=True)
        pdf.cell(2, 1, "Ancho de banda de descarga (velocidad): " + str(obj.getAnchoBandaDescarga(  )), ln=True)
    else:
        pdf.cell(2, 1, "Status HTTP: " + status, ln=True)


    # pdf.cell(2, 4, "TcpOutSegs", ln=True)
    # pdf.image(path + host + "/carga_TcpOutSegs.png", x=2, y=18, w=10, h=0, type='', link='')
    # pdf.cell(2,2,ln=True)
    # print("Reporte creado LIsto")
    pdf.output(name = path + host + "/Reporte.pdf")
    return True

# generarReporte("50.50.50.2")