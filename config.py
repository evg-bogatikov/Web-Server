import configparser


class Config:
    def __init__(self):
        self.CONFIG = configparser.ConfigParser()

    def getHost(self):
        self.CONFIG.read("settings.ini")
        host = self.CONFIG["Host"]["host"]
        host = host.split()
        return host

    def getPort(self):
        self.CONFIG.read("settings.ini")
        port = self.CONFIG["Host"]["port"]
        return int(port)

    def getDir(self):
        self.CONFIG.read("settings.ini")
        dir = self.CONFIG["Host"]["dir"]
        dir = dir.split()
        return dir

    def getBufSize(self):
        self.CONFIG.read("settings.ini")
        bufSize = self.CONFIG["Host"]["bufSize"]
        return int(bufSize)
