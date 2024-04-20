class Pais(object):
    __longitude = 0
    __latitude = 0
    __nome = ""

    def __init__(self, latitude, longitude, nome):
        self.__longitude = longitude 
        self.__latitude = latitude 
        self.__nome = nome 

    def get_longitude(self):
        return self.__longitude
    
    def get_latitude(self):
        return self.__latitude
    
    def get_nome(self):
        return self.__nome

    def lancar_missel(self, lat, long, inimigo):
        if inimigo.get_latitude() == lat and inimigo.get_longitude() == long:
            print("BOOOMM!!")
            return True
        else: 
            print("Fail...")
            print(inimigo.get_latitude())
            return False


pais1 = Pais(234, 1234, "Israel")
pais2 = Pais(287, 1235, "Irã")
pais1.lancar_missel(287, 1235, pais2)