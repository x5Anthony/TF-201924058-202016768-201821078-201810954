from Calle import CCalle
from Calle import CInterseccion
import csv
from datetime import datetime
from grafo import grafo
import math
def es_horapunta(hora_actual)->bool:
    #horas punta para calcular el tráfico
    #hora punta en la mañana
    horapunta_mañanainicio = hora_actual.time()
    horapunta_mañanainicio=horapunta_mañanainicio.replace(hour=6,minute=0,second=0,microsecond=0)
    horapunta_mañanafin=hora_actual.time()
    horapunta_mañanainicio=horapunta_mañanafin.replace(hour=8,minute=0,second=0,microsecond=0)

    #hora punta tarde
    horapunta_tardeinicio = hora_actual.time()
    horapunta_tardeinicio=horapunta_tardeinicio.replace(hour=1,minute=0,second=0,microsecond=0)
    horapunta_tardefin=hora_actual.time()
    horapunta_tardefin=horapunta_tardefin.replace(hour=4,minute=0,second=0,microsecond=0)
    #hora punta noche
    horapunta_nocheinicio = hora_actual.time()
    horapunta_nocheinicio=horapunta_nocheinicio.replace(hour=7,minute=0,second=0,microsecond=0)
    horapunta_nochefin=hora_actual.time()
    horapunta_nochefin=horapunta_nochefin.replace(hour=10,minute=0,second=0,microsecond=0)

    return (hora_actual.time()>horapunta_mañanainicio and hora_actual.time()<horapunta_mañanafin) or (hora_actual.time()>horapunta_tardeinicio and hora_actual.time()<horapunta_tardefin) or (hora_actual.time()>horapunta_nocheinicio and hora_actual.time()<horapunta_nochefin)
if __name__=="__main__":
    listacalles=[]
    listaintersecciones=[]
    grafito=grafo()
    #obteniendo hora actual
    hora_actual=datetime.now()
    horapunta=es_horapunta(hora_actual)
    with open("calles.csv",encoding="utf-8") as f:
        reader=csv.reader(f,delimiter=";")
        for row in reader:
            listacalles.append(CCalle(row[0],row[1],row[2]))
    for callesita in listacalles:
        grafito.agregarVertice(callesita)
    with open("intersecciones.csv",encoding="utf-8") as f:
        reader=csv.reader(f,delimiter=";")
        for row in reader:
            listaintersecciones.append(CInterseccion(row[0],row[1],row[2],row[3],row[4],row[5]))
    for interseccion in listaintersecciones:
        if(horapunta):
            ##esto es para calcular el peso
            peso=(math.dist(listacalles[interseccion.id_calle-1].coordenadas,listacalles[interseccion.calle_cruza-1].coordenadas)/(interseccion.velocidad*interseccion.reduc_trafico))
            grafito.agregarArista(interseccion.id_calle,interseccion.calle_cruza,peso)
        else:
            peso=(math.dist(listacalles[interseccion.id_calle-1].coordenadas,listacalles[interseccion.calle_cruza-1].coordenadas)/(interseccion.velocidad))
            grafito.agregarArista(interseccion.id_calle,interseccion.calle_cruza,peso)
    grafito.dibujar_grafica()
    validador=True
    for v in grafito.vertices:
        print(v,grafito.vertices[v].item.nombre)
    
    origen=input("Introduzca el Id de la calle donde se encuentra: ")
    origen=int(origen)
    destino=input("Introduzca el Id de la calle a donde quiere dirigirse: ")
    destino=int(destino)
    grafito.dijkstra(origen)
    print(grafito.camino(destino))
    


