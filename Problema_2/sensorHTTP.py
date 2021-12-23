
# https://docs.python-requests.org/es/latest/user/quickstart.html

import requests
from time import time

class SensorHTTP:

    def __init__(self, ip) -> None:
        self.ip = ip

    def getStatusCode(self):
        try:
            response = requests.get("http://" + self.ip)
            return response.status_code
        except:
            return 5000
    
    def getTiempoRespuesta(self):
        inicio = time()
        self.getStatusCode()
        final = (time() - inicio)*1000
        return final

    def getBytesRecibido(self):
        r = requests.get("http://" +self.ip , stream=True)
        return len(r.raw.read())

    def getAnchoBandaDescarga(self):
        inicio = time()
        bytesRecibido = self.getBytesRecibido()
        final = time() - inicio
        kB = bytesRecibido/1000
        return (kB/final)

    def getStatus(self):
        if self.getStatusCode() == 200:
            return "Up"
        return "Down"

# obj = SensorHTTP("50.50.50.2")
# status = obj.getStatus()
# if status == "Up":
#     print(obj.getTiempoRespuesta())
#     print(obj.getBytesRecibido())
#     print(status)
#     print(obj.getAnchoBandaDescarga())
# else:
#     print(status)