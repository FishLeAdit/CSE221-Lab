f1 = open("input1_2.txt",'r')
n,k = map(int, f1.readline().split())
queries = []
for i in range(k):
    line = f1.readline().split()
    query = [int(x) for x in line]
    queries.append(query)

def lfcs(n,queries):
    parent = [-1]*(n+1)
    sizes = [1]*(n+1)

    def find(x):
        if parent[x] == -1:
            return x
        parent[x] = find(parent[x])
        return parent[x]
    
    def union(x,y):
        x_root = find(x)
        y_root = find(y)
        if x_root != y_root:
            if sizes[x_root] < sizes[y_root]:
                parent[x_root] = y_root
                sizes[y_root] += sizes[x_root]
            else:
                parent[y_root] = x_root
                sizes[x_root] += sizes[y_root]

    result = []

    for i in range(len(queries)):
        a, b = queries[i]
        union(a, b)
        result.append(sizes[find(a)])

    return result


fcs = lfcs(n,queries)




op = open("output1_2.txt",'w')

for size in fcs:
    op.write(str(size)+'\n')

f1.close()
op.close()