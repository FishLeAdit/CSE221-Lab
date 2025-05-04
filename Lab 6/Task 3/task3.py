import math
from queue import PriorityQueue

f1 = open("input3_1.txt",'r')
f2= open("output3_1.txt",'w')
n , m = list(map(int,f1.readline().split(' ')))


def Graph(n , m):
    adjancy_list = [None]*(n+1)
    for i in range(m):
        e1,e2,e3 = list(map(int,f1.readline().split(" ")))
        if adjancy_list[e1]==None:
            adjancy_list[e1] = [(str(e2),e3)]
        else:
            adjancy_list[e1].append((str(e2),e3))

    return adjancy_list

def dijsktra(s , graph , c):
    dis_list = [math.inf] * (n+1)
    q = PriorityQueue()
    q.put((c , s)) 
    while not q.empty():
        cost , source = q.get()
        if dis_list[int(source)] > cost:   
            dis_list[int(source)] = cost
            if graph[int(source)] != None:
                for neighbour in graph[int(source)]:  
                    source , up_cost = neighbour
                    q.put((up_cost,source))
            else:
                pass
        else:
            pass
    return dis_list

adj_list = Graph(n , m)
val = dijsktra(1 , adj_list , 0)
maximum = -1

for v in range(1,len(val)):
    if val[v] == math.inf:
        f2.write('Impossible')
        break
    else:
        if maximum <val[v]:
            maximum = val[v]
f2.write(str(maximum))