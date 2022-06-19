from base64 import decode, encode
from grafo import nodo
from grafo import grafo
from Calle import CCalle
from Calle import CInterseccion
from grafo import arista
import csv
from datetime import datetime
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
    hora_actual.time()
    with open("calles.csv",encoding="utf-8") as f:
        reader=csv.reader(f,delimiter=";")
        for row in reader:
            listacalles.append(CCalle(row[0],row[1],row[2]))
    for callesita in listacalles:
        grafito.añadir_nodo(nodo(callesita))
    with open("intersecciones.csv",encoding="utf-8") as f:
        reader=csv.reader(f,delimiter=";")
        for row in reader:
            listaintersecciones.append(CInterseccion(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[11],row[12],row[9],row[10]))
    for interseccion in listaintersecciones:
        if es_horapunta(hora_actual):
            grafito.añadir_arista(arista(grafito.nodos[interseccion.get_idcalle()-1],grafito.nodos[interseccion.get_idcalleorigen()-1],interseccion.costo2))
        else:
            grafito.añadir_arista(arista(grafito.nodos[interseccion.get_idcalle()-1],grafito.nodos[interseccion.get_idcalleorigen()-1],interseccion.costo1))
    


