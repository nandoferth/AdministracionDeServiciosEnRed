
from paramiko import SSHClient, AutoAddPolicy, ssh_exception

class SensorSSH:

    def __init__(self, username, password, ip) -> None:
        self.username = username
        self.password = password
        self.ip = ip


    def getStatus(self):
        try:
            ssh_client = SSHClient()
            ssh_client.set_missing_host_key_policy(AutoAddPolicy())
            ssh_client.connect(self.ip, 22, self.username, self.password)
            return "Up"
        except ssh_exception.NoValidConnectionsError:
            return "Down"
        except ssh_exception.AuthenticationException:
            return "Down"

# obj = SensorSSH("fer", "29121996", "50.50.50.2")

# print(obj.getStatus())