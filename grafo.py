class nodo:
    def __init__(self,item):
        self.item=item
        self.listaady=[]
    def añadir_ady(self,nodo):
        self.listaady.append(nodo)
    def mostrar(self):
        print("La calle:", self.item.get_name())
        for v in self.listaady:
            print("Cruza con:", v.item.get_name())
class arista:
    def __init__(self,nodo_origen,nodo_destino,peso) -> None:
        self.nodo_origen=nodo_origen
        self.nodo_destino=nodo_destino
        self.nodo_origen.añadir_ady(self.nodo_destino)
        self.nodo_destino.añadir_ady(self.nodo_origen)
        self.peso=peso
    def get_nodo_origen(self):
        temp=self.nodo_origen
        return temp
    def get_nodo_final(self):
        temp=self.nodo_destino
        return temp
class grafo:
    def __init__(self):
        self.nodos = []
        self.aristas = []
        self.cantidad_nodos = 0
        self.cantidad_aristas=0

    def añadir_nodo(self, n):
        self.nodos.append(n)
        self.cantidad_nodos += 1

    def añadir_arista(self, arista):
        self.aristas.append(arista)
        self.cantidad_aristas+=1





        
