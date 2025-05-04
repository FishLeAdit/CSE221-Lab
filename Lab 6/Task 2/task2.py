from queue import PriorityQueue

f1=open('input2_3.txt','r')
f2=open('output2_3.txt','w')

n = [int (i) for i in f1.readline().strip().split()]

nodes = n[0]
cases = n[1]

matrix = {}
parent = {}
dist = {}

for i in range(nodes+1):
    parent[i+1] = None
    dist[i+1] = float('inf')
    matrix[i+1] = []

for i in range(cases):
    y=[int (i) for i in f1.readline().strip().split()]
    x1 = y[0]
    x2 = y[1]
    weight = y[2]
    matrix[x1].append((weight , x2))

s = [int(i) for i in f1.readline().strip().split()]
s1= s[0]
s2 = s[1]

def dijkstra(node):
    q=PriorityQueue()
    for i in range(nodes+1):
        parent[i+1] = None
        dist[i+1] = float('inf')
    visited=[]
    for i in range(nodes+1):
        visited.append(-1)
    q.put(node)
    while not q.empty():
        visited[node[1]] = 0
        m = q.get()
        distance = m[0]
        for i , j in matrix[m[1]]:
            if (visited[j] == -1 and j != s1) or i+distance<visited[j]:
                visited[j] = distance+i
                q.put((distance+i , j))
    return visited

alice = dijkstra((0 , s1))
bob = dijkstra((0 , s2))

result = []

for k in range(len(alice)):
    if alice[k]!=-1 and bob[k]!=-1:
        result.append((max(alice[k] , bob[k]) , k))
        
if len(result)!=0:
    ans=min(result)
    time,node=ans[0],ans[1]
    w1='Time ' +str(time)
    w2='Node ' +str(node)
    w=w1+'\n'+w2
    f2.write(w)
else:
    f2.write('Impossible')