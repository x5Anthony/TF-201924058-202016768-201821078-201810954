![UPC](/assets/upc-logo.png)

## Complejidad Algorítmica -Trabajo Final
#### “Informe del Trabajo Final”

### Docente: Patricia Daniela Reyes Silva

### Seccion: WS6B

### Integrantes:

##### - u201924058-Nilton Torres Rojas
##### - u202016768-Bruno Paz De Noboa Arana
##### - u201821078-Franchesco Alexis Soto Morales
##### - u201810954-Anthony Ramon Manco Cuellar


## **1. Introduccion**

El presente trabajo representa las calles de una ciudad como las aristas de un grafo y sus intersecciones como nodos. Con esta información se busca conseguir un algoritmo que permita calcular la ruta óptima de un punto inicial 'A' a un punto destino 'B', considerando factores de peso, como el tráfico o la hora del día.

## **2. Objetivos**

* Para este proyecto que consiste en desarrollar un sistema que nos permita encontrar la ruta más corta entre dos puntos de una ciudad, detectamos los siguientes objetivos.
* En primer lugar, tenemos que aprender a usar herramientas para la planificación y control del proyecto como GitHub.
* Reforzar conocimientos sobre grafos dinámicos y librerías que nos ayuden a implementar estos.
* Implementar un grafo con los datos brindados en él dataset
* Aprender a usar herramientas que nos brinden una interfaz gráfica para poder representar el grafo y los algoritmos implementados por el grupo.

## **3. Area de la ciudad**

* Descripción de la ciudad elegida 
El área se encuentra en el Cono Norte de Lima en el distrito de Comas, pertenece a la urbanización El Retablo. Debido a la cercanía de uno de los integrantes del grupo a la zona y a su familiaridad con ella, nos resultó factible su elección. Adicionalmente tenemos información de primera mano acerca a los tiempos de congestión vehicular de tal modo que nos permitirá realizar pruebas más realistas.
* Imagen estática de la ciudad o porción de ciudad elegida

[![Sin-t-tulo.png](https://i.postimg.cc/FzfkLBZK/Sin-t-tulo.png)](https://postimg.cc/YLHSc8Tc)


## **4. Descripcion del conjunto de datos**
* Datos consignados por calle
1.	ID de la calle.
2.	Nombre de la calle.
3.	Coordenadas de la calle

[![segundo.png](https://i.postimg.cc/L4ZbR6tr/segundo.png)](https://postimg.cc/PNT4QHF4)

* Datos consignados por calle
1.	ID de la intercesión 
2.	ID donde se encuentra la intersección 
3.	Nombre de la calle
4.	ID de la calle con la que se cruza
5.	Velocidad permitida
6.	Reducción de velocidad en caso de tráfico de hora punta

[![tercero.png](https://i.postimg.cc/JnhCPwSR/tercero.png)](https://postimg.cc/xkBZ1Z0Z)


## **5. Grafo de la ciudad**
Un nodo representa una calle y una arista representa una intersección. Los vértices representan las calles de la ciudad. El costo de las aristas es el tiempo que le toma al usuario recorrerla.

[![cuarto.png](https://i.postimg.cc/FRS8P9D5/cuarto.png)](https://postimg.cc/Fd9TzXMD)


## **6. Diseño del sistema de trafico**
* Cómo se incorpora tráfico por horas en calles o segmentos de calles

[![quinto.png](https://i.postimg.cc/BvBMtXYv/quinto.png)](https://postimg.cc/2q34K8fp)

* Cómo se calcula el peso de arista en base a su longitud y factor de trafico

[![Sextopng.png](https://i.postimg.cc/PxNYhx09/Sextopng.png)](https://postimg.cc/k63BvnJv)
Calculamos el peso con una simple fórmula: T=D/V (T: Tiempo, D: Distancia, V: Velocidad).
Si observamos con cuidado, notamos que en caso de que sea hora punta, la velocidad se verá afectada por el factor tráfico, que disminuirá su valor.


* Cómo se incorpora tráfico por horas en calles o segmentos de calles

Como vimos en los ejemplos anteriores, notamos que el programa recibe la hora en la cual se ejecuta el código, acto seguido procede a realizar los cálculos y validaciones


* Algoritmos utilizados para calcular la ruta más corta y dos rutas alternativas

Algoritmo de Dijskra: Para el proyecto implementamos el algoritmo de Dijkstra debido a que no es posible encontrar un peso negativo en nuestras aristas. Este algoritmo nos ayudará a determinar el camino más corto desde un nodo origen hacia el resto los vértices en un grafo.

* Implementación de visual del mapa y las rutas a partir del grafo y algoritmo seleccionado
[![cuarto.png](https://i.postimg.cc/FRS8P9D5/cuarto.png)](https://postimg.cc/Fd9TzXMD)

Ejemplo de una ruta:

[![octavo.png](https://i.postimg.cc/9M65f0Fz/octavo.png)](https://postimg.cc/tZNmSX6H)

* Interfaz grafica


*Enlaces: a repositorios de GitHub / a video de presentacion

* GitHub:https://github.com/x5Anthony/TF-201924058-202016768-201821078-201810954
* Video:


## **7. Conclusiones**
En conclusión, gracias a este trabajo final logramos implementar un algoritmo que nos brinde la ruta optima considerando factores de hora y tráfico. También obtuvimos conocimientos en el trabajo colaborativo usando GitHub.

