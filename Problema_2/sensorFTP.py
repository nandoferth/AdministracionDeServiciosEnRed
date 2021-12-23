# https://docs.python.org/es/3/library/ftplib.html
# Fernando Vizcaino Lopez

from ftplib import FTP
from time import time

class SensorFTP:
    
    def __init__(self, ip) -> None:
        try:
            self.ftp = FTP(ip)
            self.status = "UP"
        except ConnectionRefusedError:
            self.status = "DOWN"
    
    def login(self, user, passwd):
        try: 
            self.ftp.login(user, passwd)
        except:
            print("Inicio de sesión incorrecta")
    
    def getTiempoRespuestaServidor(self):
        inicio = time()
        self.getRespuestaServidor()
        final = (time() - inicio)*1000
        return final
    
    def getRespuestaServidor(self):
        return self.ftp.getwelcome()
    
    
    def printSupervisaCambiosFicheros(self, argument):
        self.ftp.cwd(argument)
        return self.ftp.retrlines("LIST")
        # return self.ftp.dir(argument)
    
    def getStatus(self):
        return self.status

# obj = SensorFTP("40.40.40.2")
# status = obj.getStatus()