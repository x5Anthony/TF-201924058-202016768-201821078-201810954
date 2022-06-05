class nodo:
    def __init__(self,item):
        self.item=item
        self.listaady=[]
    def añadir_ady(self,nodo):
        self.listaady.append(nodo)
class arista:
    def __init__(self,id,id_calle,nombre_calle,id_calleorigen,id_callefinal,id_aristaorigen,id_aristafinal,distancia,velocidadd,lat,longi):
        self.item=int(id)
        self.id_calle=int(id_calle)
        self.nombre_calle=nombre_calle
        self.id_calleorigen=int(id_calleorigen)
        self.id_callefinal=int(id_callefinal)
        self.id_aristaorigen=int(id_aristaorigen)
        self.id_aristafinal=int(id_aristafinal)
        self.distancia=distancia
        self.velocidad=int(velocidadd)
        self.costo1=70
        self.costo2=10000
        self.latitud=lat
        self.longitud=longi
    def get_idcalle(self):
        temp=self.id_calle
        return temp
    def get_idcalleorigen(self):
        temp=self.id_calleorigen
        return temp
class grafo:
    def __init__(self):
        self.nodos=[]
        self.arista=[]
        self.cantidad=0
    def añadir_nodo(self,n):
        self.nodos.append(n)
        self.cantidad+=1
    def añadir_arista(self,arista):
        self.arista.append(arista)
        self.nodos[arista.get_idcalle()].añadir_ady(self.nodos[arista.get_idcalleorigen()])
        self.nodos[arista.get_idcalleorigen()].añadir_ady(self.nodos[arista.get_idcalle()])
    def mostrar(self):
        for n in self.nodos:
            print(n.item.mostrar())





        
