# %%
inf = open("input5_1.txt", "r")
otf = open("output5_1.txt", "w")

line_1 = inf.readline()
line_1_list = line_1.split()
nc = int(line_1_list[0].strip("\n"))
ec = int(line_1_list[1].strip("\n"))
destin = int(line_1_list[2].strip("\n"))
parent_dict = {}
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


def BFS(sv):
    visited = [False] * (nc + 1)
    queue = []
    queue.append(sv)
    visited[sv] = True
    parent_dict[sv] = None
    while len(queue) > 0:
        sv = queue.pop(0)
        for i in graph[sv]:
            if visited[i] == False:
                parent_dict[i] = sv
                queue.append(i)
                visited[i] = True


BFS(1)
count = -1
path = []

while destin != None:
    count += 1
    path.append(destin)
    destin = parent_dict[destin]

otf.write("Time: {}".format(str(count)))
otf.write('\n')
otf.write("Shortest Path: ")

for i in range(len(path) - 1, -1, -1):
    otf.write(f'{str(path[i])} ')

inf.close()
otf.close()


# %%
inf = open("input5_2.txt", "r")
otf = open("output5_2.txt", "w")

line_1 = inf.readline()
line_1_list = line_1.split()
nc = int(line_1_list[0].strip("\n"))
ec = int(line_1_list[1].strip("\n"))
destin = int(line_1_list[2].strip("\n"))
parent_dict = {}
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


def BFS(sv):
    visited = [False] * (nc + 1)
    queue = []
    queue.append(sv)
    visited[sv] = True
    parent_dict[sv] = None
    while len(queue) > 0:
        sv = queue.pop(0)
        for i in graph[sv]:
            if visited[i] == False:
                parent_dict[i] = sv
                queue.append(i)
                visited[i] = True


BFS(1)
count = -1
path = []

while destin != None:
    count += 1
    path.append(destin)
    destin = parent_dict[destin]

otf.write("Time: {}".format(str(count)))
otf.write('\n')
otf.write("Shortest Path: ")

for i in range(len(path) - 1, -1, -1):
    otf.write(f'{str(path[i])} ')

inf.close()
otf.close()


# %%
inf = open("input5_3.txt", "r")
otf = open("output5_3.txt", "w")

line_1 = inf.readline()
line_1_list = line_1.split()
nc = int(line_1_list[0].strip("\n"))
ec = int(line_1_list[1].strip("\n"))
destin = int(line_1_list[2].strip("\n"))
parent_dict = {}
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


def BFS(sv):
    visited = [False] * (nc + 1)
    queue = []
    queue.append(sv)
    visited[sv] = True
    parent_dict[sv] = None
    while len(queue) > 0:
        sv = queue.pop(0)
        for i in graph[sv]:
            if visited[i] == False:
                parent_dict[i] = sv
                queue.append(i)
                visited[i] = True


BFS(1)
count = -1
path = []

while destin != None:
    count += 1
    path.append(destin)
    destin = parent_dict[destin]

otf.write("Time: {}".format(str(count)))
otf.write('\n')
otf.write("Shortest Path: ")

for i in range(len(path) - 1, -1, -1):
    otf.write(f'{str(path[i])} ')

inf.close()
otf.close()


# %%
inf = open("input5_4.txt", "r")
otf = open("output5_4.txt", "w")

line_1 = inf.readline()
line_1_list = line_1.split()
nc = int(line_1_list[0].strip("\n"))
ec = int(line_1_list[1].strip("\n"))
destin = int(line_1_list[2].strip("\n"))
parent_dict = {}
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


def BFS(sv):
    visited = [False] * (nc + 1)
    queue = []
    queue.append(sv)
    visited[sv] = True
    parent_dict[sv] = None
    while len(queue) > 0:
        sv = queue.pop(0)
        for i in graph[sv]:
            if visited[i] == False:
                parent_dict[i] = sv
                queue.append(i)
                visited[i] = True


BFS(1)
count = -1
path = []

while destin != None:
    count += 1
    path.append(destin)
    destin = parent_dict[destin]

otf.write("Time: {}".format(str(count)))
otf.write('\n')
otf.write("Shortest Path: ")

for i in range(len(path) - 1, -1, -1):
    otf.write(f'{str(path[i])} ')

inf.close()
otf.close()


# %%
inf = open("input5_5.txt", "r")
otf = open("output5_5.txt", "w")

line_1 = inf.readline()
line_1_list = line_1.split()
nc = int(line_1_list[0].strip("\n"))
ec = int(line_1_list[1].strip("\n"))
destin = int(line_1_list[2].strip("\n"))
parent_dict = {}
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


def BFS(sv):
    visited = [False] * (nc + 1)
    queue = []
    queue.append(sv)
    visited[sv] = True
    parent_dict[sv] = None
    while len(queue) > 0:
        sv = queue.pop(0)
        for i in graph[sv]:
            if visited[i] == False:
                parent_dict[i] = sv
                queue.append(i)
                visited[i] = True


BFS(1)
count = -1
path = []

while destin != None:
    count += 1
    path.append(destin)
    destin = parent_dict[destin]

otf.write("Time: {}".format(str(count)))
otf.write('\n')
otf.write("Shortest Path: ")

for i in range(len(path) - 1, -1, -1):
    otf.write(f'{str(path[i])} ')

inf.close()
otf.close()



