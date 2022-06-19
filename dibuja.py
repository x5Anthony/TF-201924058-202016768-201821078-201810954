from math import sqrt
import matplotlib.pyplot as plt
import networkx as nx



class Dupla: 
    def _init_(self, x, y):
        self.x = x
        self.y = y

def CalcDis(Dup1, Dup2):
    return sqrt(pow((Dup1.x - Dup2.x), 2) + pow((Dup1.y - Dup2.y), 2))  
G = nx.Graph() 
vertices_G = ['1', '2', '3', '4', '5', '6', '7']
G.add_nodes_from(vertices_G)
aristas_G = [('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('1', '6'), ('1', '7')]

G.add_edges_from(aristas_G)
ubica = {'1': (5, 4), '2': (4, 3), '3': (5, 2), '4': (11, 3), '5': (18, 5), '6': (4, 6), '7': (12, 7)}

puntoA = Dupla()
puntoA.x = ubica['1'][0]
puntoA.y = ubica['1'][1]
puntoB = Dupla()
puntoB.x = ubica['2'][0]
puntoB.y = ubica['2'][1]
puntoC = Dupla()
puntoC.x = ubica['3'][0]
puntoC.y = ubica['3'][1]
puntoD = Dupla()
puntoD.x = ubica['4'][0]
puntoD.y = ubica['4'][1]
puntoE = Dupla()
puntoE.x = ubica['5'][0]
puntoE.y = ubica['5'][1]
puntoF = Dupla()
puntoF.x = ubica['6'][0]
puntoF.y = ubica['6'][1]
puntoG = Dupla()
puntoG.x = ubica['7'][0]
puntoG.y = ubica['7'][1]

Puntos = {'1': puntoA, '2': puntoB, '3': puntoC, '4': puntoD, '5': puntoE, '6': puntoF, '7': puntoG}

cont: int = 0
for i in aristas_G:
    Pa = Puntos[aristas_G[cont][0]]
    Pb = Puntos[aristas_G[cont][1]]
    G.edges[i]['distancia'] = CalcDis(Pa, Pb)*100
   
    print('La distancia entre ', aristas_G[cont], G.edges[i],'[METROS]')
    cont = cont + 1
nx.draw(G, pos=ubica, node_color='gray', with_labels=True)

plt.show()