# %%
def dfs(graph,vst,crs,ord):
    vst[crs] = True
    for neighbour in graph[crs]:
        if not vst[neighbour]:
            dfs(graph,vst,neighbour,ord)
    ord.append(crs)

# %%
#SAMPLE1
f1  = open('input1_a1.txt','r')
inf = f1.read().split('\n')

firstline = inf[0].split(' ')
nc = int(firstline[0])
np = int(firstline[1])

prq = []
for i in range(1,np+1):
    z = inf[i].split(' ')
    a,b = int(z[0]),int(z[1])
    prq.append([a,b])
print(prq)

graph = [[] for i in range(nc+1)]

for p in prq:
    graph[p[0]].append(p[1])

vst = [False]*(nc+1)
ord = []

for crs in range (1,nc+1):
    if not vst[crs]:
        dfs(graph,vst,crs,ord)


f2 = open('output1a_1.txt','w')
print('---------------------------')
if len(ord) == nc:
    print(ord[::-1])
    x = ord[::-1]
    a = ' '.join(str(a) for a in x)
    f2.write(a)
    f2.write('\n')
else:
    print("IMPOSSIBLE")
    f2.write("IMPOSSIBLE")

f2.close()



# %%
#SAMPLE2
f1  = open('input1_a2.txt','r')
inf = f1.read().split('\n')

firstline = inf[0].split(' ')
nc = int(firstline[0])
np = int(firstline[1])

prq = []
for i in range(1,np+1):
    z = inf[i].split(' ')
    a,b = int(z[0]),int(z[1])
    prq.append([a,b])
print(prq)

graph = [[] for i in range(nc+1)]

for p in prq:
    graph[p[0]].append(p[1])

vst = [False]*(nc+1)
ord = []

for crs in range (1,nc+1):
    if not vst[crs]:
        dfs(graph,vst,crs,ord)

f2 = open('output1a_2.txt','w')
print('---------------------------')
if len(ord) == nc:
    print(ord[::-1])
    x = ord[::-1]
    a = ' '.join(str(a) for a in x)
    f2.write(a)
    f2.write('\n')
else:
    print("IMPOSSIBLE")
    f2.write("IMPOSSIBLE")

f2.close()


#WHYYYY?

# %%
#SAMPLE3
f1  = open('input1_a3.txt','r')
inf = f1.read().split('\n')

firstline = inf[0].split(' ')
nc = int(firstline[0])
np = int(firstline[1])

prq = []
for i in range(1,np+1):
    z = inf[i].split(' ')
    a,b = int(z[0]),int(z[1])
    prq.append([a,b])
print(prq)

graph = [[] for i in range(nc+1)]

for p in prq:
    graph[p[0]].append(p[1])

vst = [False]*(nc+1)
ord = []

for crs in range (1,nc+1):
    if not vst[crs]:
        dfs(graph,vst,crs,ord)

f2 = open('output1a_3.txt','w')
print('---------------------------')
if len(ord) == nc:
    print(ord[::-1])
    x = ord[::-1]
    a = ' '.join(str(a) for a in x)
    f2.write(a)
    f2.write('\n')
else:
    print("IMPOSSIBLE")
    f2.write("IMPOSSIBLE")

f2.close()




