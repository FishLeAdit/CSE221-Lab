# %%

inf = open("input3_1.txt", "r")
otf = open("output3_1.txt", "w")

line_1 = inf.readline()
line_1_list = line_1.split()
nc = int(line_1_list[0].strip("\n"))
ec = int(line_1_list[1].strip("\n"))

graph = {}

for i in range(ec):
    line = inf.readline()
    line_list = line.split(" ")

    x = int(line_list[0])
    y = int(line_list[1])

    if x not in graph.keys():
        graph[x] = [y]
    else:
        graph[x] = graph[x] + [y]
    if y not in graph.keys():
        graph[y] = [x]
    else:
        graph[y] = graph[y] + [x]

visited = [0] * nc
parent = []

def DFS_Visit(graph, node):
    visited[int(node) - 1] = 1
    parent.append(node)

    for i in graph[node]:
        if visited[int(i) - 1] == 0:
            DFS_Visit(graph, i)


def DFS(graph, ep):
    for i in graph.keys():
        if visited[int(i) - 1] == 0:
            DFS_Visit(graph, i)
DFS(graph, ec)

for i in parent:
    otf.write(f'{str(i)} ')

inf.close()
otf.close()


# %%
#task3
inf = open("input3_2.txt", "r")
otf = open("output3_2.txt", "w")

line_1 = inf.readline()
line_1_list = line_1.split()
nc = int(line_1_list[0].strip("\n"))
ec = int(line_1_list[1].strip("\n"))

graph = {}

for i in range(ec):
    line = inf.readline()
    line_list = line.split(" ")

    x = int(line_list[0])
    y = int(line_list[1])

    if x not in graph.keys():
        graph[x] = [y]
    else:
        graph[x] = graph[x] + [y]
    if y not in graph.keys():
        graph[y] = [x]
    else:
        graph[y] = graph[y] + [x]

visited = [0] * nc
parent = []

def DFS_Visit(graph, node):
    visited[int(node) - 1] = 1
    parent.append(node)

    for i in graph[node]:
        if visited[int(i) - 1] == 0:
            DFS_Visit(graph, i)


def DFS(graph, ep):
    for i in graph.keys():
        if visited[int(i) - 1] == 0:
            DFS_Visit(graph, i)
DFS(graph, ec)

for i in parent:
    otf.write(f'{str(i)} ')

inf.close()
otf.close()


# %%
#task3
inf = open("input3_3.txt", "r")
otf = open("output3_3.txt", "w")

line_1 = inf.readline()
line_1_list = line_1.split()
nc = int(line_1_list[0].strip("\n"))
ec = int(line_1_list[1].strip("\n"))

graph = {}

for i in range(ec):
    line = inf.readline()
    line_list = line.split(" ")

    x = int(line_list[0])
    y = int(line_list[1])

    if x not in graph.keys():
        graph[x] = [y]
    else:
        graph[x] = graph[x] + [y]
    if y not in graph.keys():
        graph[y] = [x]
    else:
        graph[y] = graph[y] + [x]

visited = [0] * nc
parent = []

def DFS_Visit(graph, node):
    visited[int(node) - 1] = 1
    parent.append(node)

    for i in graph[node]:
        if visited[int(i) - 1] == 0:
            DFS_Visit(graph, i)


def DFS(graph, ep):
    for i in graph.keys():
        if visited[int(i) - 1] == 0:
            DFS_Visit(graph, i)
DFS(graph, ec)

for i in parent:
    otf.write(f'{str(i)} ')

inf.close()
otf.close()


# %%
#task3
inf = open("input3_4.txt", "r")
otf = open("output3_4.txt", "w")

line_1 = inf.readline()
line_1_list = line_1.split()
nc = int(line_1_list[0].strip("\n"))
ec = int(line_1_list[1].strip("\n"))

graph = {}

for i in range(ec):
    line = inf.readline()
    line_list = line.split(" ")

    x = int(line_list[0])
    y = int(line_list[1])

    if x not in graph.keys():
        graph[x] = [y]
    else:
        graph[x] = graph[x] + [y]
    if y not in graph.keys():
        graph[y] = [x]
    else:
        graph[y] = graph[y] + [x]

visited = [0] * nc
parent = []

def DFS_Visit(graph, node):
    visited[int(node) - 1] = 1
    parent.append(node)

    for i in graph[node]:
        if visited[int(i) - 1] == 0:
            DFS_Visit(graph, i)


def DFS(graph, ep):
    for i in graph.keys():
        if visited[int(i) - 1] == 0:
            DFS_Visit(graph, i)
DFS(graph, ec)

for i in parent:
    otf.write(f'{str(i)} ')

inf.close()
otf.close()



