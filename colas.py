from collections import deque
cola = deque()
# print(cola)
#
# cola = deque(['Azul', 'Morado', 'Verde', 'Naranja'])
# print(cola)
#
# cola.append('Turqueza') #meter elementos
# print(cola)
#
# print(cola.popleft()) # para sacar elementos de la cola
# print(cola)
#
# import queue
# cola2 = queue.Queue(maxsize=2)
# cola2.put('Azul')
# list(cola2.queue)
# print(list(cola2.queue))
#
# cola2.get() #saca elemetos
# print(list(cola2.queue))
#
# import queue
# cola2 = queue.Queue(maxsize=10)
# cola2.put(1)
#
# list(cola2.queue)
# print(list(cola2.queue))
#
# cola2.get(6) #saca elemetos
# print(list(cola2.queue))
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