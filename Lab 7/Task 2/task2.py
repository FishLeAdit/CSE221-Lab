f1 = open('input2_2.txt','r')
n,m = map(int, f1.readline().split())
edges = [tuple(map(int,f1().split())) for _ in range(m)]

def find(parent,i):
    if parent[i] == i:
        return i
    return find(parent,parent[i])

def union(parent,rank,x,y):
    x_root = find(parent,x)
    y_root = find(parent,y)
    if rank[x_root]<rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root]>rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1
    

def kruskal(edges,n):
    edges.sort(key=lambda x:x[2])
    mst = []
    parent = [i for i in range(n)]
    rank = [0]*n

    for edge in edges:
        u,v,w = edge
        if find(parent,u) != find(parent,v):
            mst.append(edge)
            union(parent,rank,u,v)
    return mst

def mmc(edges,n):
    mst = kruskal(edges,n)
    tc = sum(edge[2] for edge in mst)
    mc = [max(edge[2] for edge in edges if edge != e) for e in mst]

    return tc-max(mc)

result = mmc(edges,n)

f2= open("output2_2.txt",'w')
f2.write(result)