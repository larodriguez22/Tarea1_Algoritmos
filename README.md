# Tarea1_Algoritmos


## Descripción

Este proyecto se centra en la visualización de grafos utilizando las bibliotecas Matplotlib, NumPy y NetworkX en Python. Proporciona herramientas para crear, dibujar y analizar grafos, lo que puede ser útil en diversas aplicaciones, como análisis de redes sociales, problemas de asignación y más.

## Características

- Creación y manipulación de grafos utilizando la biblioteca NetworkX.
- Dibujo de grafos en una ventana emergente utilizando Matplotlib.
- Análisis básico de la estructura del grafo.

## Instalación

Asegúrate de tener Python instalado en tu sistema. Luego, puedes instalar las dependencias utilizando el siguiente comando:

```bash
pip install matplotlib numpy networkx
```

## Descripcion de los enunciados

### Punto 1:
La Superintendencia Bancaria tiene un registro de préstamos que una entidad hace a otra en el país. Para simplificar, hay n entidades en el país, identificadas con los números en 1..n. El registro de préstamos cuenta con la información de una relación entre entidades p(i,j) que le permite saber si la entidad i le prestó dinero a la entidad j. La Superintendencia está interesada en detectar si hay autopréstamos en el sistema, i.e., si existe una secuencia de entidades e1, e2,…,ek, tal que:

k>1 Λ e1 = ek Λ (∀i | 1≤i<k : p(ei,ei+1))\

Dada la relación p de prestamos entre entidades, determinar si existe algún autopréstamo.

### Punto 2:

Juan quiere invitar a sus amigos a conocer su nuevo apartamento. Sin embargo tiene la dificultad de que sus amigos son algo conflictivos y entonces sabe que varias parejas de amigos se han peleado entre ellos. Debido a esto, tomó la decisión de organizar dos reuniones. Diseñe un algoritmo que determine si es posible distribuir a los amigos de Juan en dos grupos de tal manera que dentro de cada grupo no haya parejas de personas que se hayan peleado entre ellas.

### Punto 3:

Una ciudad se diseño de tal modo que todas sus calles fueran de una sola vía. Con el paso del tiempo la cantidad de habitantes de la ciudad creció y esto produjo grandes trancones en algunas de las vias debido a algunos desvíos innecesarios que tienen que tomar los habitantes de la ciudad para poder llegar a sus trabajos. Por lo tanto, el alcalde tomó la decisión de ampliar algunas vias para que puedan convertirse en doble via. Dado el mapa de la ciudad y el costo de convertir cada via actual en doble via, determinar qué vias se deben convertir, de modo que se pueda transitar de cualquier punto a cualquier punto de la ciudad por dobles vias y que el costo de la conversión sea el mínimo posible.

## Uso

### Punto 1:

Para el caso de este punto se puede correr de la siguiente manera en consola:
```bash
python "$Path_archivo_python/" "$Path_archivo_datos"
```

### Punto 2:

Para el caso de este punto se debe correr de la siguiente manera en consola:
```bash
python "$Path_archivo_python/problema_amigos.py" "$Path_archivo_datos"
```

El archivo de python se llama ```problema_amigos.py``` y se propone un ejemplo en la carpeta datos que se llamado ```peleados.txt```. La estructura del archivo a probar debe ser parecida a:

```
juan,pablo
pablo,andres
pepito,pepita
andres,pepito
juan,pepito
pepita,pablo
samuel,juan
samuel,john
john,nicolas
```

El resultado para este archivo especifico muestra por consola:

```bash
juan : ['pablo', 'pepito', 'samuel']
pablo : ['juan', 'andres', 'pepita']
andres : ['pablo', 'pepito']
pepito : ['pepita', 'andres', 'juan']
pepita : ['pepito', 'pablo']
samuel : ['juan', 'john']
john : ['samuel', 'nicolas']
nicolas : ['john']
SI
Fiesta 1: ['juan', 'andres', 'pepita', 'john']
Fiesta 2: ['pablo', 'pepito', 'samuel', 'nicolas']
```
Adicionalmente muestra el grafo generado:
![Figure_1](https://github.com/larodriguez22/Tarea1_Algoritmos/assets/53947800/01fd8258-d536-426a-a82a-c1396d4020f3)

### Punto 3:
Para el caso de este punto se puede correr dos maneras diferentes:
- Por un lado, de la siguiente manera en consola:
```bash
python "$Path_archivo_python/problema_calles.py" "$Path_archivo_datos"
```
Aqui, una vez se corra, va a salir como input lo siguiente, donde debe ser seleccionado (1):
```bash
Subio un archivo con la matriz (1) o desea generar un grafo (2): 1
```
El archivo de python se llama ```problema_calles.py``` y se propone un ejemplo en la carpeta datos que se llamado ```matriz_punto5.txt```. La estructura del archivo a probar debe ser parecida a:
```
0 10 6 5
10 0 0 15
6 0 0 4
5 15 4 0
```
Donde el resultado para este archivo especifico debe ser:

```
2 -- 3 == 4
0 -- 3 == 5
0 -- 1 == 10
Costo del Minimum Spanning Tree: 19
```
Adicionalmente muestra el grafo generado:
![Figure_2](https://github.com/larodriguez22/Tarea1_Algoritmos/assets/53947800/81963110-82f3-4ae1-b8ad-0bb641456d2b)

- Por otro lado, si quiere que se genere un grafo de forma aleatoria para hacer pruebas, se puede usar de la siguiente manera en consola:
```bash
python "$Path_archivo_python/problema_calles.py"
```
Aqui, una vez se corra, va a salir como input lo siguiente, donde debe ser seleccionado (2):
```bash
Subio un archivo con la matriz (1) o desea generar un grafo (2): 2
```
Adicionalmente, se le va a preguntar cuantos nodos se quiere generar para el nuevo grafo, por lo que seleccione un numero, para este ejemplo se selecciono:
```
Defina el maximo de nodos que quiera de la matriz: 5
```
Para este caso se selecciono 5, por lo que el resultado generado es:
```
Matriz aleatoria generada
Arcos dobles construidos en el MST:
1 -- 3 == 20
0 -- 4 == 22
2 -- 4 == 30
0 -- 1 == 40
Costo del Minimum Spanning Tree: 112
```
Y el grafo generado es:
![Figure_3](https://github.com/larodriguez22/Tarea1_Algoritmos/assets/53947800/cf3a89cc-2c42-40e2-8a0c-faf8373f1c03)
