
class CCalle:
    def __init__(self,id,n,i):
        self.id=int(id)
        self.nombre=n
        self.cant_intersec=int(i)
    def get_id(self):
        temp=self.id
        return temp
    def get_name(self):
        temp=self.nombre
        return temp
class CInterseccion:
    def __init__(self, id, id_calle, nombre_calle, id_calleorigen, id_callefinal, id_aristaorigen, id_aristafinal,
                 distancia, velocidadd, lat, longi,costo1,costo2):
        self.item = int(id)
        self.id_calle = int(id_calle)
        self.nombre_calle = nombre_calle
        self.id_calleorigen = int(id_calleorigen)
        self.id_callefinal = int(id_callefinal)
        self.id_aristaorigen = int(id_aristaorigen)
        self.id_aristafinal = int(id_aristafinal)
        self.distancia = distancia
        self.velocidad = int(velocidadd)
        self.costo1 = costo1
        self.costo2 = costo2
        self.latitud = lat
        self.longitud = longi
    def set_costos(self,trafico):
        self.costo2=self.costo1*trafico


    def get_idcalle(self):
        temp = self.id_calle
        return temp

    def get_idcalleorigen(self):
        temp = self.id_calleorigen
        return temp
    