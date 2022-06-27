import networkx as nx
import matplotlib.pyplot as plt
class nodo:
    def __init__(self,i):
        self.item=i#item, en este caso será la clase calle
	self.id = i.id#id de la calle
	self.vecinos = []
	self.visitado = False
	self.padre = None
	self.costo = float('inf')
    def agregarVecino(self, vecino, peso):
	if vecino not in self.vecinos:#agrega solo el id del vecino y su peso
		self.vecinos.append([vecino, peso])
class grafo:
    def __init__(self):
	self.vertices = {}#diccionario de vertices
    def agregarVertice(self, i):		
	if i.id not in self.vertices:
		self.vertices[i.id] = nodo(i)#solo agrega las id de los vecinos
    def agregarArista(self, a, b, p):
		
	if a in self.vertices and b in self.vertices: #solo agregas las id de los vecinos
		self.vertices[a].agregarVecino(b, p)
		self.vertices[b].agregarVecino(a, p)

    def camino(self, b):
	camino = []
	actual = b
	while actual != None:
		camino.insert(0, actual)
		actual = self.vertices[actual].padre
	G=nx.Graph()
	for i in range(len(camino)-1):
		G.add_edge(self.vertices[camino[i]].item.nombre,self.vertices[camino[i+1]].item.nombre)
	pos = nx.layout.planar_layout(G)
	nx.draw_networkx(G, pos)
	labels = nx.get_edge_attributes(G, 'weight')
	nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
	plt.title("Deberia seguir esta ruta con un peso de "+ str(self.vertices[b].costo))
	plt.show()
	return [camino, self.vertices[b].costo]

	def minimo(self, nv):
		if len(nv) > 0:
			m = self.vertices[nv[0]].costo
			v = nv[0]
			for e in nv:
				if m > self.vertices[e].costo:
					m = self.vertices[e].costo
					v = e
			return v
		return None
	def dibujar_grafica(self):
		G=nx.Graph()
		for vertice in self.vertices:
			for vecino in self.vertices[vertice].vecinos:
				G.add_edge(self.vertices[vertice].item.nombre,self.vertices[vecino[0]].item.nombre,weight=vecino[1])
		pos = nx.layout.circular_layout(G)
		nx.draw_networkx(G, pos)
		labels = nx.get_edge_attributes(G, 'weight')
		nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
		plt.title("Representacion de las calles")
		plt.show()
	def dijkstra(self, a):
		if a in self.vertices:
			self.vertices[a].costo = 0
			actual = a
			noVisitados = []
			for v in self.vertices:
				if v != a:
					self.vertices[v].costo = float('inf')
				self.vertices[v].padre = None
				noVisitados.append(v)
				self.vertices[v].visitado=False
			while len(noVisitados) > 0:
				for vec in self.vertices[actual].vecinos:
					if self.vertices[vec[0]].visitado == False:
						if self.vertices[actual].costo + vec[1] < self.vertices[vec[0]].costo:
							self.vertices[vec[0]].costo = self.vertices[actual].costo + vec[1]
							self.vertices[vec[0]].padre = actual
				self.vertices[actual].visitado = True
				noVisitados.remove(actual)
				actual = self.minimo(noVisitados)
		else:
			return False





        
