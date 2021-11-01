from fpdf import FPDF
from RRDtool import RRdGrafica
from time import sleep
path = "/home/fernando/Documentos/AdministracionDeserviciosEnRed-main/Practica_3/"


def generarReporte(host):
    RRdGrafica(host, "UdpInDatagrams", "in")
    RRdGrafica(host, "UdpOutDatagrams", "out")
    RRdGrafica(host, "TcpInSegs", "in")
    RRdGrafica(host, "TcpOutSegs", "out")
    print("Preparando Imágenes  para el reporte...")
    sleep(20)
    print("Pegando Imagenes...")
    pdf = FPDF("P", "cm", "Letter")
    pdf.add_page()
    pdf.set_font("helvetica", "", 16)

    pdf.cell(2, 1, "Host: "+ host + " Comunidad: FernandoCompany", ln=True)
    pdf.cell(2, 2, "UdpInDatagrams", ln=True)
    pdf.image(path + host + "/carga_UdpInDatagrams.png", x=2, y=3.5, w=10, h=0, type='', link='')
    pdf.cell(2,2,ln=True)

    pdf.cell(2, 2, "UdpOutDatagrams", ln=True)
    pdf.image(path + host + "/carga_UdpOutDatagrams.png", x=2, y=8, w=10, h=0, type='', link='')
    pdf.cell(2, 2, ln=True)

    pdf.cell(2, 3, "TcpInSegs", ln=True)
    pdf.image(path + host + "/carga_TcpInSegs.png", x=2, y=13, w=10, h=0, type='', link='')
    pdf.cell(2,2,ln=True)

    pdf.cell(2, 4, "TcpOutSegs", ln=True)
    pdf.image(path + host + "/carga_TcpOutSegs.png", x=2, y=18, w=10, h=0, type='', link='')
    pdf.cell(2,2,ln=True)
    print("Reporte creado LIsto")
    pdf.output(name = "Reporte "+host+".pdf")