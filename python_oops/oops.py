class Router:
    total_routers = 0
    
    def __init__(self,hostname,ip,vendor,password):
        self.hostname = hostname
        self.ip = ip
        self.vendor = vendor
        self.__password = password  ## make the double underscore makes variable private also called name mangling
        Router.total_routers +=1
        
    ## Encapsulation
        def authenticate(self,input_pass):
            if input_pass == self.__password:
                return "Login Successful"
            return "Access Denide"
        
r1 = Router("R1","10.10.101.1","cisco","admin123")
print (r1.hostname)
#print(r1.password)
r2 = Router("R2","10.10.101.2","juniper","admin123")
print(r2.ip)

print(Router.total_routers)






