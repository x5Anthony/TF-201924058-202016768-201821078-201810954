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


## Contenido
1. Introducción
    - El presente trabajo representa las calles de una ciudad como las aristas de un grafo y sus intersecciones como nodos. Con esta información se busca conseguir un       algoritmo que permita calcular la ruta óptima de un punto inicial 'A' a un punto destino 'B', considerando factores de peso, como el tráfico o la hora del día.
2. Objetivos
    - Para este proyecto que consiste en desarrollar un sistema que nos permita encontrar la ruta más corta entre dos puntos de una ciudad, detectamos los siguientes         objetivos.

    - En primer lugar, tenemos que aprender a usar herramientas para la planificación y control del proyecto como GitHub.

    - Reforzar conocimientos sobre grafos dinámicos y librerías que nos ayuden a implementar estos.

    - Implementar un grafo con los datos brindados en él dataset.

    - Agregar información detallada al grafo como coordenadas, tráfico por horas y peso de la arista.

    - Implementar un algoritmo que nos devuelva la ruta más corta y 2 rutas alternativas.

    - Aprender a usar herramientas que nos brinden una interfaz gráfica para poder representar el grafo y los algoritmos implementados por el grupo.

3. Área de la ciudad
    - Descripción de la ciudad elegida: El área se encuentra en el Cono Norte de Lima en el distrito de Comas, pertenece a la urbanización El Retablo. Debido a la cercanía de uno de los integrantes del grupo a la zona y a su familiaridad con ella, nos resultó factible su elección. Adicionalmente tenemos información de primera mano acerca a los tiempos de congestión vehicular de tal modo que nos permitirá realizar pruebas más realistas.
    - Imagen estática de la ciudad o porción de ciudad elegida</ul>
    -- ![image](https://user-images.githubusercontent.com/66744988/174499196-ef1bb069-790d-4edb-bd40-248b3456f046.png)
4. Descripción del conjunto de datos
    - Datos consignados por calle
    1. ID de la calle.
    2. Nombre de la calle.
    3. Cantidad de intersecciones.
  
    - Datos consignados por intersección</ul>
    1. ID de la intercesión 
    2. ID donde se encuentra la intersección 
    3. Nombre de la calle
    4. Nombre de la calle con la que se cruza
    5. Peso de la arista (tiempo para recorrer la arista)

5. Grafo de la Ciudad
   - Un nodo representa una calle y una arista representa una intersección. Los vértices representan las calles de la ciudad .El costo de las aristas es el tiempo que      le toma al usuario recorrerla.
   - ![image](https://user-images.githubusercontent.com/66744988/174499534-c4e1156c-b1c2-454c-8b13-1236b7eee27d.png)

6. Diseño del Sistema de Trafico
    - Cómo se incorpora tráfico por horas en calles o segmentos de calles
    - Cómo se calcula el peso de arista en base a su longitud y factor de trafico
    - Cómo se actualiza el peso de la arista en función de la hora del día.
    - Algoritmos utilizados para calcular la ruta más corta y dos rutas alternativas
    - Implementación de visual del mapa y las rutas a partir del grafo y algoritmo seleccionado
    - Interfaz grafica
    - Enlaces: a repositorio de GitHub / a video de presentación.</ul>
    * https://github.com/x5Anthony/TF-201924058-202016768-201821078-201810954
7. Conclusiones 

