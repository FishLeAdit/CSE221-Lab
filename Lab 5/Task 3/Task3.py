# %%
def dfs(graph,nd,vst,stack):
    vst[nd]= True
    for neighbour in graph[nd]:
        if not vst[neighbour]:
            dfs(graph,neighbour,vst,stack)
    stack.append(nd)

# %%
def sccdfs(transposed_graph,node,visited,scc):
    visited[node] = True
    scc.append(node)
    for neighbour in transposed_graph[node]:
        if not visited[neighbour]:
            sccdfs(transposed_graph,neighbour,visited,scc)

# %%
#SAMPLE1
f1  = open('input3_1.txt','r')
inf = f1.read().split('\n')

firstline = inf[0].split(' ')
nc = int(firstline[0])
np = int(firstline[1])

edg = []
for i in range(1,np+1):
    z = inf[i].split(' ')
    a,b = int(z[0]),int(z[1])
    edg.append([a,b])
print(nc,np)
print(edg)

graph = [[] for i in range(nc+1)]
for x,y in edg:
    graph[x].append(y)

stack = []
vst = [False]*(nc+1)
for nd in range(1,nc+1):
    if not vst[nd]:
        dfs(graph,nd,vst,stack)

transposed_graph = [[] for i in range (len(graph))]
for x in range(len(graph)):
    for y in graph[x]:
        transposed_graph[y].append(x)

visited = [False]*(nc+1)
scc_comp = []
while stack:
    node = stack.pop()
    if not visited[node]:
        scc = []
        sccdfs(transposed_graph,node,visited,scc)
        scc_comp.append(scc)

scc_comp.sort()

print(scc_comp)
print("------------")
f2 = open('output3_1.txt','w')

for i in scc_comp:
    print(i)
    a = ' '.join(str(a) for a in i)
    f2.write(a)
    f2.write('\n')
f2.close()

# %%
#SAMPLE2
f1  = open('input3_2.txt','r')
inf = f1.read().split('\n')

firstline = inf[0].split(' ')
nc = int(firstline[0])
np = int(firstline[1])

edg = []
for i in range(1,np+1):
    z = inf[i].split(' ')
    a,b = int(z[0]),int(z[1])
    edg.append([a,b])
print(nc,np)
print(edg)

graph = [[] for i in range(nc+1)]
for x,y in edg:
    graph[x].append(y)

stack = []
vst = [False]*(nc+1)
for nd in range(1,nc+1):
    if not vst[nd]:
        dfs(graph,nd,vst,stack)

transposed_graph = [[] for i in range (len(graph))]
for x in range(len(graph)):
    for y in graph[x]:
        transposed_graph[y].append(x)

visited = [False]*(nc+1)
scc_comp = []
while stack:
    node = stack.pop()
    if not visited[node]:
        scc = []
        sccdfs(transposed_graph,node,visited,scc)
        scc_comp.append(scc)

scc_comp.sort()

print(scc_comp)
print("------------")
f2 = open('output3_2.txt','w')

for i in scc_comp:
    print(i)
    a = ' '.join(str(a) for a in i)
    f2.write(a)
    f2.write('\n')
f2.close()

# %%
#SAMPLE3
f1  = open('input3_3.txt','r')
inf = f1.read().split('\n')

firstline = inf[0].split(' ')
nc = int(firstline[0])
np = int(firstline[1])

edg = []
for i in range(1,np+1):
    z = inf[i].split(' ')
    a,b = int(z[0]),int(z[1])
    edg.append([a,b])
print(nc,np)
print(edg)

graph = [[] for i in range(nc+1)]
for x,y in edg:
    graph[x].append(y)

stack = []
vst = [False]*(nc+1)
for nd in range(1,nc+1):
    if not vst[nd]:
        dfs(graph,nd,vst,stack)

transposed_graph = [[] for i in range (len(graph))]
for x in range(len(graph)):
    for y in graph[x]:
        transposed_graph[y].append(x)

visited = [False]*(nc+1)
scc_comp = []
while stack:
    node = stack.pop()
    if not visited[node]:
        scc = []
        sccdfs(transposed_graph,node,visited,scc)
        scc_comp.append(scc)

print(scc_comp)

scc_comp.sort()

print(scc_comp)
print("------------")
f2 = open('output3_3.txt','w')

for i in scc_comp:
    print(i)
    a = ' '.join(str(a) for a in i)
    f2.write(a)
    f2.write('\n')
f2.close()

# %%



