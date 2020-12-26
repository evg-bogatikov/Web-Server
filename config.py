import configparser


CONFIG = configparser.ConfigParser()


def getHost():
    CONFIG.read("settings.ini")
    host = CONFIG["Host"]["host"]
    host = host.split()
    return host

def getHostLength():
    CONFIG.read("settings.ini")
    host = CONFIG["Host"]["host"]
    host = host.split()
    return len(host)

def getPort():
    CONFIG.read("settings.ini")
    port = CONFIG["Host"]["port"]
    return int(port)

def getDir():
    CONFIG.read("settings.ini")
    dir = CONFIG["Host"]["dir"]
    dir = dir.split()
    return dir

def getBufSize():
    CONFIG.read("settings.ini")
    bufSize = CONFIG["Host"]["bufSize"]
    return int(bufSize)