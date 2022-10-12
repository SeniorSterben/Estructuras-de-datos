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
    
    ----------------------------------------------
"""