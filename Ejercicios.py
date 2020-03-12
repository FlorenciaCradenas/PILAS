print('EJERCICIO PILAS')
lista_2=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(lista_2)
lista_2.remove('d')
lista_2.remove('g')
lista_2.remove('j')
lista_2.remove('m')
lista_2.remove('o')
lista_2.remove('r')
lista_2.remove('u')
lista_2.remove('x')
print(lista_2)

print('EJERCICIO COLAS')
from collections import deque
cola = deque()
cola=deque(['Luis Manuel', 'Luis Angel', 'Sebastian', 'Jenifer', 'Cesar','Monica', 'Patricia','Teresa', 'Isabel','Monse' ])
print(cola)
cola.popleft()
cola.popleft()
cola.popleft()
cola.popleft()
cola.popleft()
print(cola.popleft())
cola.appendleft('Cesar')
cola.appendleft('Jenifer')
cola.appendleft('Sebastian')
cola.appendleft('Luis Angel')
cola.appendleft('Luis Manuel')
print(cola)

print('EJERCICIO COLAS DE PRIORIDAD')
import heapq
c1 = []
print('EN UNA SALA DE URGENSIAS LAS PERSONAS INGRESADAS TIENEN DISTINTAS PRIORIDADES:\n 1 Rojo o critico \n 2 Amarillo o urgente \n 3 Verde o no urgente ')
heapq.heappush(c1, (3,'Monica'))
heapq.heappush(c1, (2,'Sebastian'))
heapq.heappush(c1, (4,'Florencia'))
heapq.heappush(c1, (1,'Luis A'))

while c1:
    print(heapq.heappop(c1))
