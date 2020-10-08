import configparser


CONFIG = configparser.ConfigParser()

def get_ipAdress():
    CONFIG.read("settings.ini")
    ipAdress = CONFIG["Host"]["ip"]
    return ipAdress

def get_port():
    CONFIG.read("settings.ini")
    port = CONFIG["Host"]["port"]
    return int(port)

def get_dir():
    CONFIG.read("settings.ini")
    dir = CONFIG["Host"]["dir"]
    return dir