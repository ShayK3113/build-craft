import json

configFilePath = "config.json"

class Config:
    class __config:
        def __init__(self):
            with open(configFilePath) as f:
                data = json.load(f)
                self.host = data["host"]
                self.port = int(data["port"])
                self.password = data["password"]

    instance = None
    def __init__(self):
        if not Config.instance:
            Config.instance = Config.__config()
       
    def Host(self):
        return self.instance.__getattribute__("host")

    def Port(self):
        return self.instance.__getattribute__("port")

    def Password(self):
        return self.instance.__getattribute__("password")



