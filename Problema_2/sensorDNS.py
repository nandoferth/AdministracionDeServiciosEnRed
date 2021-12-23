# https://www.thegeekstuff.com/2014/01/install-dns-server/
# https://dnspython.readthedocs.io/en/stable/installation.html
# https://programmerclick.com/article/8131998611/

from dns import resolver

class SensorDNS:

    def __init__(self, ip, dominio) -> None:
        self.ip = ip
        self.dominio = dominio

    def getStatus(self):
        try:
            A = resolver.query(self.dominio,'A')
            return "Up"
        except:
            return "Down"

        # for i in A.response.answer:
        #         for j in i.items:
        #                 print(j.address)


# obj = SensorDNS("30.30.30.2", "ns.dnsfernando.net")
# print(obj.getStatus())
# print(getTiempoResp("ns.dnsfernando.net"))