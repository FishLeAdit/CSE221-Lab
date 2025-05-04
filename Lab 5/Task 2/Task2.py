# %%
#SAMPLE1
f1  = open('input2_1.txt','r')
inf = f1.read().split('\n')

firstline = inf[0].split(' ')
nc = int(firstline[0])
np = int(firstline[1])

mark = [0]*(nc+1)

prq = []
for i in range(1,np+1):
    z = inf[i].split(' ')
    a,b = int(z[0]),int(z[1])
    prq.append([a,b])
print(prq)

graph = [[] for i in range(nc+1)]

for p in prq:
    graph[p[0]].append(p[1])
    mark[p[1]] += 1
print(graph)
print(mark)

queue = []
for crs in range(1,nc+1):
    if mark[crs] == 0:
        queue.append(crs)
print(queue)

ord = []
while queue:
    crs = min(queue)
    queue.remove(crs)
    ord.append(crs)
    for neighbour in graph[crs]:
        mark[neighbour] -= 1
        if mark[neighbour] == 0:
            queue.append(neighbour)

f2 = open('output2_1.txt','w')
print('---------------------------')
if len(ord) == nc:
    print(ord)
    a = ' '.join(str(a) for a in ord)
    f2.write(a)
    f2.write('\n')
else:
    print("IMPOSSIBLE")
    f2.write("IMPOSSIBLE")

f2.close()






# %%
#SAMPLE2
f1  = open('input2_2.txt','r')
inf = f1.read().split('\n')

firstline = inf[0].split(' ')
nc = int(firstline[0])
np = int(firstline[1])

mark = [0]*(nc+1)

prq = []
for i in range(1,np+1):
    z = inf[i].split(' ')
    a,b = int(z[0]),int(z[1])
    prq.append([a,b])
print(prq)

graph = [[] for i in range(nc+1)]

for p in prq:
    graph[p[0]].append(p[1])
    mark[p[1]] += 1
print(graph)
print(mark)

queue = []
for crs in range(1,nc+1):
    if mark[crs] == 0:
        queue.append(crs)
print(queue)

ord = []
while queue:
    crs = queue.pop(0)
    ord.append(crs)
    for neighbour in graph[crs]:
        mark[neighbour] -=1
        if mark[neighbour] == 0:
            queue.append(neighbour)
print('---------------------------')
f2 = open('output2_2.txt','w')
print('---------------------------')
if len(ord) == nc:
    print(ord)
    a = ' '.join(str(a) for a in ord)
    f2.write(a)
    f2.write('\n')
else:
    print("IMPOSSIBLE")
    f2.write("IMPOSSIBLE")

f2.close()





# %%
#SAMPLE3#SAMPLE1
f1  = open('input2_3.txt','r')
inf = f1.read().split('\n')

firstline = inf[0].split(' ')
nc = int(firstline[0])
np = int(firstline[1])

mark = [0]*(nc+1)

prq = []
for i in range(1,np+1):
    z = inf[i].split(' ')
    a,b = int(z[0]),int(z[1])
    prq.append([a,b])
print(prq)

graph = [[] for i in range(nc+1)]

for p in prq:
    graph[p[0]].append(p[1])
    mark[p[1]] += 1
print(graph)
print(mark)

queue = []
for crs in range(1,nc+1):
    if mark[crs] == 0:
        queue.append(crs)
print(queue)

ord = []
while queue:
    crs = queue.pop(0)
    ord.append(crs)
    for neighbour in graph[crs]:
        mark[neighbour] -=1
        if mark[neighbour] == 0:
            queue.append(neighbour)
print('---------------------------')
f2 = open('output2_3.txt','w')
print('---------------------------')
if len(ord) == nc:
    print(ord)
    a = ' '.join(str(a) for a in ord)
    f2.write(a)
    f2.write('\n')
else:
    print("IMPOSSIBLE")
    f2.write("IMPOSSIBLE")

f2.close()




