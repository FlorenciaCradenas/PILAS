# c = []
# c.append((2, 'Harry')) #2 es la prioridad
# c.append((3, 'Charles'))
# c.sort(reverse=True) #mantener el oden de prioridad
# c.append((1, 'Riya'))
# c.sort(reverse=True)
# c.append((4,'Stacy'))
# c.sort(reverse=False)
# while c:
#     print(c.pop(0))
# print(c)


import heapq
c1 = []
print('EN UNA SALA DE URGENSIAS LAS PERSONAS INGRESADAS TIENEN DISTINTAS PRIORIDADES:\n 1 Rojo o critico \n 2 Amarillo o urgente \n 3 Verde o no urgente ')
heapq.heappush(c1, (3,'Monica'))
heapq.heappush(c1, (2,'Sebastian'))
heapq.heappush(c1, (4,'Florencia'))
heapq.heappush(c1, (1,'Luis A'))

while c1:
    print(heapq.heappop(c1))

