"""ESTRUCTURAS DE DATOS
PROGRAMACIÓN DE SOFTWARE
SANTIAGO VELÁSQUEZ
SENA:CGMLTI
FICHA:2502640
ERICK GRANADOS
2020"""

"""
5.1. Más sobre listas
El tipo de dato lista tiene algunos métodos mas. Son los siguientes:

    list.append(x)
    Agrega un ítem u objeto al final de la lista. 
    Equivale a a[len(a):] = [x].
    ----------------------------------------------
    list.extend(iterable)
    Extiende la lista agregándole todos los ítems u objetos 
    del iterable. 
    Equivale a a[len(a):] = iterable.
    ----------------------------------------------
    list.insert(i, x)
    Inserta un ítem en una posición dada. 
    El primer argumento es el índice del ítem delante del cual se insertará, por lo tanto a.insert(0, x) inserta al principio de la lista y a.insert(len(a), x) equivale a a.append(x).
    ----------------------------------------------
    list.remove(x)
    Quita el primer ítem de la lista cuyo valor sea x. Lanza un ValueError si no existe tal ítem.
    ----------------------------------------------
    list.pop([i])
    Quita el ítem en la posición dada de la lista y lo retorna. Si no se especifica un índice, a.pop() quita y retorna el último elemento de la lista.
    ----------------------------------------------
    list.clear()
    Elimina todos los elementos de la lista. Equivalente a del a[:].
    ----------------------------------------------
    list.index(x[, start[, end]])
    Retorna el índice basado en cero del primer elemento cuyo valor sea igual a x. Lanza una excepción ValueError si no existe tal elemento.

    Los argumentos opcionales start y end son interpretados como la notación de rebanadas y se usan para limitar la búsqueda a un segmento particular de la lista. El índice retornado se calcula de manera relativa al inicio  de la secuencia completa en lugar de con respecto al argumento start.
    ----------------------------------------------
    list.count(x)
    Retorna el número de veces que x aparece en la lista.
    ----------------------------------------------
    list.sort(*, key=None, reverse=False)
    Ordena los elementos de la lista in situ (los argumentos pueden ser usados para personalizar el orden de la lista, ver sorted() para su explicación).
    ----------------------------------------------
    list.reverse()
    Invierte los elementos de la lista in situ.
    ----------------------------------------------
    list.copy()
    Retorna una copia superficial de la lista. Equivalente a a[:].
    ----------------------------------------------
    EJEMPLOS Y SU RESPECTIVA EXPLICACIÓN:"""

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

""""----------------------------------------------
    >>> fruits.count('apple')
    2
        La función .count ('x') retorna la cantidad de elementos iguales a 'x'
    ----------------------------------------------
    >>> fruits.index('banana')
    3
        La función .index retorna la posición en la que se encuentra el elemento 'x'.
    >>> fruits.index('banana', 4) 
    6
        La función .index retorna la posición en la que se encuentra el elemento 'x' contando desde la posición 4, por tal motivo se salta el la primer posición de banana y retorna la posición de la segunda.
    ----------------------------------------------
    >>> fruits.reverse()
    >>> fruits
    ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
        La función .reverse() retorna toda la lista, la diferencia es que el orden de los elementos es al contrario.
    ---------------------------------------------
    >>> fruits.append('grape')
    >>> fruits
    ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
        La función .append retorna toda la lista, adicionalmente le agrega el elemento definido en 'x' y lo agrega en la última posición de la lista.
    ----------------------------------------------
    >>> fruits.sort()
    >>> fruits
    ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
        La función .sort ordena los elementos por orden alfabetico.
        Otra cosa que puedes observar es que no todos los datos se pueden ordenar o comparar. Por ejemplo, [None, 'hello', 10] no se puede ordenar ya que los enteros no se pueden comparar con strings y None no se puede comparar con los otros tipos. También hay algunos tipos que no tienen una relación de orden definida. Por ejemplo, 3+4j < 5+7j no es una comparación válida.
    ----------------------------------------------
    >>> fruits.pop()
    'pear'
        La función .pop quita de la lista el elemento definido en 'x' y lo reotrna, en caso de que no se defina un elemento en 'x' como se puede ver anteriormente la función quita el ultimo elemento de la lista y lo retorna.
    
    ----------------------------------------------
    5.1.1 Usando listas como pilas

    Los métodos de lista hacen que resulte muy fácil usar una lista como una pila, donde el último elemento añadido es el primer elemento retirado («último en entrar, primero en salir»). Para agregar un elemento a la cima de la pila, utiliza append(). Para retirar un elemento de la cima de la pila, utiliza pop() sin un índice explícito. Por ejemplo:
    ----------------------------------------------"""
stack = [3, 4, 5]
"""----------------------------------------------
    >>> stack.append(6)
    >>> stack.append(7)
    >>> stack
    [3, 4, 5, 6, 7]
        La función .append() es para agregar un elemento definido entre los parentesis.
    ----------------------------------------------
    >>> stack.pop()
    7
        La función .pop es para retirar un elemento en la psocición definida en los paréntesis, en este caso no se define una ubicación por lo tanto el sistema retirará el último elemento agregado de la pila.
    ----------------------------------------------
    >>> stack
    [3, 4, 5, 6]
        Aquí podemos ver que el ultimo elemento que era 7 fue retirado por pop.
    ----------------------------------------------
    >>> stack.pop()
    6
        Ahora se retira el ultimo elemento actual que sería el elemento 6.
    ----------------------------------------------
    >>> stack.pop()
    5
        De igual forma se retira el último dígito de la pila.
    ----------------------------------------------
    >>> stack
    [3, 4]
        
    ----------------------------------------------
    5.1.2 Usando listas como colas
    También es posible usar una lista como una cola, donde el primer elemento añadido es el primer elemento retirado («primero en entrar, primero en salir»); sin embargo, las listas no son eficientes para este propósito. Agregar y sacar del final de la lista es rápido, pero insertar o sacar del comienzo de una lista es lento (porque todos los otros elementos tienen que ser desplazados por uno).

    Para implementar una cola, utiliza collections.deque el cual fue diseñado para añadir y quitar de ambas puntas de forma rápida. Por ejemplo:
"""
from collections import deque
queue = deque(["Eric", "John", "Michael"])
"""
    >>> queue.append("Terry")   
        A continuación se agrega a Terry
    ----------------------------------------------        
    >>> queue.append("Graham")  
        Tambien se agrega a Graham, cabe mencionar que estos dos nuevos elementos quedan al final de la lista porque es una cola o una fila para ser más específico.
    ----------------------------------------------        
    >>> queue.popleft()                
    'Eric'
        Ahora se retira un elemento con .popleft lo cual hace que se retire el primer elemento de la lista que en este caso es 'Eric'.
    ----------------------------------------------
    >>> queue.popleft()                
    'John'
        Se hace lo mismo con popleft, ya que no hay una posición especificada entre los paréntesis se retira el primer elemento.
    ----------------------------------------------
    >>> queue                          
    deque(['Michael', 'Terry', 'Graham'])
        Finalmente así queda la cola.
    ----------------------------------------------
    5.1.3. Comprensión de listas
    Las comprensiones de listas ofrecen una manera concisa de crear listas. Sus usos comunes son para hacer nuevas listas donde cada elemento es el resultado de algunas operaciones aplicadas a cada miembro de otra secuencia o iterable, o para crear un segmento de la secuencia de esos elementos para satisfacer una condición determinada.

    Por ejemplo, asumamos que queremos crear una lista de cuadrados, como:"""

squares = []
for x in range(10):
    squares.append(x**2)

squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
"""""
    Esto crea (o sobreescribe) una variable llamada x que sigue existiendo luego de que el bucle haya terminado. 
    ----------------------------------------------
    Una lista de comprensión consiste de corchetes rodeando una expresión seguida de la declaración for y luego cero o más declaraciones for o if. El resultado será una nueva lista que sale de evaluar la expresión en el contexto de los for o if que le siguen. Por ejemplo, esta lista de comprensión combina los elementos de dos listas si no son iguales:"""
[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
""" 
    [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)] 
    y es equivalente a:
    >>> combs = []
>>> for x in [1,2,3]:
...     for y in [3,1,4]:
...         if x != y:
...             combs.append((x, y))
...
>>> combs
    [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
    Si la expresión es una tupla (como el (x, y) en el ejemplo anterior), debe estar entre paréntesis.
    ----------------------------------------------
    Las comprensiones de listas pueden contener expresiones complejas y funciones anidadas:

    >>> from math import pi
    [str(round(pi, i)) for i in range(1, 6)]
    ----------------------------------------------
    5.1.4. Listas por comprensión anidadas
    La expresión inicial de una comprensión de listas puede ser cualquier expresión arbitraria, incluyendo otra comprensión de listas.

    Considera el siguiente ejemplo de una matriz de 3x4 implementada como una lista de tres listas de largo 4:
    >>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
    ----------------------------------------------
    [[row[i] for row in matrix] for i in range(4)]
    El número de retorno se define en el paréntesis seguido del range.
    [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
    ----------------------------------------------
    el cual, a la vez, es lo mismo que:

>>>
>>> transposed = []
>>> for i in range(4):
...     # the following 3 lines implement the nested listcomp
...     transposed_row = []
...     for row in matrix:
...         transposed_row.append(row[i])
...     transposed.append(transposed_row)
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
En el mundo real, deberías preferir funciones predefinidas a declaraciones con flujo complejo. La función zip() haría un buen trabajo para este caso de uso:

>>>
>>> list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
Ver Desempaquetando una lista de argumentos para detalles en el asterisco de esta línea.

5.2. La instrucción del
Hay una manera de quitar un ítem de una lista dado su índice en lugar de su valor: la instrucción del. Esta es diferente del método pop(), el cual retorna un valor. La instrucción del también puede usarse para quitar secciones de una lista o vaciar la lista completa (lo que hacíamos antes asignando una lista vacía a la sección). Por ejemplo:

>>>
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]
del puede usarse también para eliminar variables:

>>>
>>> del a
Hacer referencia al nombre a de aquí en más es un error (al menos hasta que se le asigne otro valor). Veremos otros usos para del más adelante.

5.3. Tuplas y secuencias
Vimos que las listas y cadenas tienen propiedades en común, como el indizado y las operaciones de seccionado. Estas son dos ejemplos de datos de tipo secuencia (ver Tipos secuencia — list, tuple, range). Como Python es un lenguaje en evolución, otros datos de tipo secuencia pueden agregarse. Existe otro dato de tipo secuencia estándar: la tupla.

Una tupla consiste de un número de valores separados por comas, por ejemplo:

>>>
>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello!')
>>> # Tuples may be nested:
... u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
>>> # Tuples are immutable:
... t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> # but they can contain mutable objects:
... v = ([1, 2, 3], [3, 2, 1])
>>> v
([1, 2, 3], [3, 2, 1])
Como puedes ver, en la salida las tuplas siempre se encierran entre paréntesis, para que las tuplas anidadas puedan interpretarse correctamente; pueden ingresarse con o sin paréntesis, aunque a menudo los paréntesis son necesarios de todas formas (si la tupla es parte de una expresión más grande). No es posible asignar a los ítems individuales de una tupla, pero sin embargo sí se puede crear tuplas que contengan objetos mutables, como las listas.

A pesar de que las tuplas puedan parecerse a las listas, frecuentemente se utilizan en distintas situaciones y para distintos propósitos. Las tuplas son immutable y normalmente contienen una secuencia heterogénea de elementos que son accedidos al desempaquetar (ver más adelante en esta sección) o indizar (o incluso acceder por atributo en el caso de las namedtuples). Las listas son mutable, y sus elementos son normalmente homogéneos y se acceden iterando a la lista.

Un problema particular es la construcción de tuplas que contengan 0 o 1 ítem: la sintaxis presenta algunas peculiaridades para estos casos. Las tuplas vacías se construyen mediante un par de paréntesis vacío; una tupla con un ítem se construye poniendo una coma a continuación del valor (no alcanza con encerrar un único valor entre paréntesis). Feo, pero efectivo. Por ejemplo:

>>>
>>> empty = ()
>>> singleton = 'hello',    # <-- note trailing comma
>>> len(empty)
0
>>> len(singleton)
1
>>> singleton
('hello',)
La declaración t = 12345, 54321, 'hola!' es un ejemplo de empaquetado de tuplas: los valores 12345, 54321 y 'hola!' se empaquetan juntos en una tupla. La operación inversa también es posible:

>>>
>>> x, y, z = t
Esto se llama, apropiadamente, desempaquetado de secuencias, y funciona para cualquier secuencia en el lado derecho del igual. El desempaquetado de secuencias requiere que la cantidad de variables a la izquierda del signo igual sea el tamaño de la secuencia. Notá que la asignación múltiple es en realidad sólo una combinación de empaquetado de tuplas y desempaquetado de secuencias.

5.4. Conjuntos
Python también incluye un tipo de dato para conjuntos. Un conjunto es una colección no ordenada y sin elementos repetidos. Los usos básicos de éstos incluyen verificación de pertenencia y eliminación de entradas duplicadas. Los conjuntos también soportan operaciones matemáticas como la unión, intersección, diferencia, y diferencia simétrica.

Las llaves o la función set() pueden usarse para crear conjuntos. Notá que para crear un conjunto vacío tenés que usar set(), no {}; esto último crea un diccionario vacío, una estructura de datos que discutiremos en la sección siguiente.

Una pequeña demostración:

>>>
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                      # show that duplicates have been removed
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket                 # fast membership testing
True
>>> 'crabgrass' in basket
False

>>> # Demonstrate set operations on unique letters from two words
...
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # letters in both a and b
{'a', 'c'}
>>> a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}
De forma similar a las comprensiones de listas, está también soportada la comprensión de conjuntos:

>>>
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'r', 'd'}
5.5. Diccionarios
Otro tipo de dato útil incluido en Python es el diccionario (ver Tipos Mapa — dict). Los diccionarios se encuentran a veces en otros lenguajes como «memorias asociativas» o «arreglos asociativos». A diferencia de las secuencias, que se indexan mediante un rango numérico, los diccionarios se indexan con claves, que pueden ser cualquier tipo inmutable; las cadenas y números siempre pueden ser claves. Las tuplas pueden usarse como claves si solamente contienen cadenas, números o tuplas; si una tupla contiene cualquier objeto mutable directa o indirectamente, no puede usarse como clave. No podés usar listas como claves, ya que las listas pueden modificarse usando asignación por índice, asignación por sección, o métodos como append() y extend().

Es mejor pensar en un diccionario como un conjunto de pares clave:valor con el requerimiento de que las claves sean únicas (dentro de un diccionario). Un par de llaves crean un diccionario vacío: {}. Colocar una lista de pares clave:valor separada por comas dentro de las llaves agrega, de inicio, pares clave:valor al diccionario; esta es, también, la forma en que los diccionarios se muestran en la salida.

Las operaciones principales sobre un diccionario son guardar un valor con una clave y extraer ese valor dada la clave. También es posible borrar un par clave:valor con del. Si usás una clave que ya está en uso para guardar un valor, el valor que estaba asociado con esa clave se pierde. Es un error extraer un valor usando una clave no existente.

Ejecutando list(d) en un diccionario retornará una lista con todas las claves usadas en el diccionario, en el orden de inserción (si deseas que esté ordenada simplemente usa sorted(d) en su lugar). Para comprobar si una clave está en el diccionario usa la palabra clave in.

Un pequeño ejemplo de uso de un diccionario:

>>>
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
>>> list(tel)
['jack', 'guido', 'irv']
>>> sorted(tel)
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False
El constructor dict() crea un diccionario directamente desde secuencias de pares clave-valor:

>>>
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}
Además, las comprensiones de diccionarios se pueden usar para crear diccionarios desde expresiones arbitrarias de clave y valor:

>>>
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
Cuando las claves son cadenas simples, a veces resulta más fácil especificar los pares usando argumentos por palabra clave:

>>>
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'guido': 4127, 'jack': 4098}
5.6. Técnicas de iteración
Cuando iteramos sobre diccionarios, se pueden obtener al mismo tiempo la clave y su valor correspondiente usando el método items().

>>>
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
...     print(k, v)
...
gallahad the pure
robin the brave
Cuando se itera sobre una secuencia, se puede obtener el índice de posición junto a su valor correspondiente usando la función enumerate().

>>>
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
0 tic
1 tac
2 toe
Para iterar sobre dos o más secuencias al mismo tiempo, los valores pueden emparejarse con la función zip().

>>>
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}?  It is {1}.'.format(q, a))
...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
Para iterar sobre una secuencia en orden inverso, se especifica primero la secuencia al derecho y luego se llama a la función reversed().

>>>
>>> for i in reversed(range(1, 10, 2)):
...     print(i)
...
9
7
5
3
1
Para iterar sobre una secuencia ordenada, se utiliza la función sorted() la cual retorna una nueva lista ordenada dejando a la original intacta.

>>>
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for i in sorted(basket):
...     print(i)
...
apple
apple
banana
orange
orange
pear
El uso de set() en una secuencia elimina los elementos duplicados. El uso de sorted() en combinación con set() sobre una secuencia es una forma idiomática de recorrer elementos únicos de la secuencia en orden ordenado.

>>>
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(basket)):
...     print(f)
...
apple
banana
orange
pear
A veces uno intenta cambiar una lista mientras la está iterando; sin embargo, a menudo es más simple y seguro crear una nueva lista:

>>>
>>> import math
>>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
>>> filtered_data = []
>>> for value in raw_data:
...     if not math.isnan(value):
...         filtered_data.append(value)
...
>>> filtered_data
[56.2, 51.7, 55.3, 52.5, 47.8]
5.7. Más acerca de condiciones
Las condiciones usadas en las instrucciones while e if pueden contener cualquier operador, no sólo comparaciones.

The comparison operators in and not in are membership tests that determine whether a value is in (or not in) a container. The operators is and is not compare whether two objects are really the same object. All comparison operators have the same priority, which is lower than that of all numerical operators.

Las comparaciones pueden encadenarse. Por ejemplo, a < b == c verifica si a es menor que b y además si b es igual a c.

Las comparaciones pueden combinarse mediante los operadores booleanos and y or, y el resultado de una comparación (o de cualquier otra expresión booleana) puede negarse con not. Estos tienen prioridades menores que los operadores de comparación; entre ellos not tiene la mayor prioridad y or la menor, o sea que A and not B or C equivale a (A and (not B)) or C. Como siempre, los paréntesis pueden usarse para expresar la composición deseada.

Los operadores booleanos and y or son los llamados operadores cortocircuito: sus argumentos se evalúan de izquierda a derecha, y la evaluación se detiene en el momento en que se determina su resultado. Por ejemplo, si A y C son verdaderas pero B es falsa, en A and B and C no se evalúa la expresión C. Cuando se usa como un valor general y no como un booleano, el valor retornado de un operador cortocircuito es el último argumento evaluado.

Es posible asignar el resultado de una comparación u otra expresión booleana a una variable. Por ejemplo,

>>>
>>> string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
>>> non_null = string1 or string2 or string3
>>> non_null
'Trondheim'
Nota que en Python, a diferencia de C, asignaciones dentro de expresiones deben realizarse explícitamente con walrus operator :=. Esto soluciona algunos problemas comunes encontrados en C: escribiendo = en una expresión cuando se intentaba escribir ==.

5.8. Comparando secuencias y otros tipos
Las secuencias pueden compararse con otros objetos del mismo tipo de secuencia. La comparación usa orden lexicográfico: primero se comparan los dos primeros ítems, si son diferentes esto ya determina el resultado de la comparación; si son iguales, se comparan los siguientes dos ítems, y así sucesivamente hasta llegar al final de alguna de las secuencias. Si dos ítems a comparar son ambos secuencias del mismo tipo, la comparación lexicográfica es recursiva. Si todos los ítems de dos secuencias resultan iguales, se considera que las secuencias son iguales. Si una secuencia es la parte inicial de la otra, la secuencia más corta es la más pequeña. El orden lexicográfico de los strings utiliza el punto de código Unicode para ordenar caracteres individuales. Algunos ejemplos de comparación entre secuencias del mismo tipo:

(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
Observá que comparar objetos de diferentes tipos con < o > es legal siempre y cuando los objetas tenga los métodos de comparación apropiados. Por ejemplo, los tipos de números mezclados son comparados de acuerdo a su valor numérico, o sea 0 es igual a 0.0, etc. Si no es el caso, en lugar de proveer un ordenamiento arbitrario, el intérprete lanzará una excepción TypeError.
    ----------------------------------------------
    ----------------------------------------------

"""