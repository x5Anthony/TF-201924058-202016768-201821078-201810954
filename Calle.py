
class CCalle:
    def __init__(self,id,n,i):
        self.id=int(id)
        self.nombre=n
        self.coordenadas=(float(x),float(y))
class CInterseccion:
    def __init__(self,id,id_calle,nombre_calle,calle_cruza,velocidad,reduc_trafico):
        self.id=int(id)
        self.id_calle=int(id_calle)
        self.nombre_calle=nombre_calle
        self.calle_cruza=int(calle_cruza)
        self.velocidad=float(velocidad)
        self.reduc_trafico=float(reduc_trafico)
    
