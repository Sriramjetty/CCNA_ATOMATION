class Interface:
    def __init__(self,name,status):
        self.name = name
        self._status = status
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self,value):
        if value not in ["up","down"]:
            raise ValueError("Status must be up or down")
        self._status = value
    

eth0 = Interface("eth0","up")
eth0.status = "down" ## setter will automatically validate (Status Property +++ setter is available (if yes) status(self,value))
print(eth0.status)

