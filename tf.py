from base64 import decode, encode
from grafo import nodo
from grafo import grafo
from Calle import CCalle
from grafo import arista
import csv
if __name__=="__main__":
    listacalles=[CCalle]
    grafito=grafo()
    with open("calles.csv",encoding="utf-8") as f:
        reader=csv.reader(f,delimiter=";")
        for row in reader:
            listacalles.append(CCalle(row[0],row[1],row[2]))
    for callesita in listacalles:
        grafito.añadir_nodo(nodo(callesita))
    with open("intersecciones.csv",encoding="utf-8") as f:
        reader=csv.reader(f,delimiter=";")
        for row in reader:
            grafito.añadir_arista(arista(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[11],row[12]))
    grafito.mostrar()
    


