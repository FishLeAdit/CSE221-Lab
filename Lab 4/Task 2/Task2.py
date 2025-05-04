# %%
#task2
inf = open("input2_1.txt","r")
otf = open("output2_1.txt","w")

line_1 = inf.readline().strip().split(" ")
vc, ec = int(line_1[0]), int(line_1[1])

graph = {}
for i in range(vc+1):
  graph[i] = []

for line in inf:
  line_list = line.strip().split(' ')
  line_list = list(map(int, line_list))
  for key in graph:
    if key == line_list[0]:
      graph[key].append(line_list[1])
      graph[line_list[1]].append(key)
inf.close()

def BFS(sv, al):
  level = {sv:0}
  i = 1
  brd = [sv]
  while brd:
    next_level = []
    for vertex in brd:
      for neighbour in al[vertex]:
        if neighbour not in level:
          level[neighbour] = i
          next_level.append(neighbour)
    brd = next_level
    i += 1
  for vertex in level.keys():
    otf.write(f"{str(vertex)} ")

BFS(1, graph)
otf.close()


# %%
#task2
inf = open("input2_2.txt","r")
otf = open("output2_2.txt","w")

line_1 = inf.readline().strip().split(" ")
vc, ec = int(line_1[0]), int(line_1[1])

graph = {}
for i in range(vc+1):
  graph[i] = []

for line in inf:
  line_list = line.strip().split(' ')
  line_list = list(map(int, line_list))
  for key in graph:
    if key == line_list[0]:
      graph[key].append(line_list[1])
      graph[line_list[1]].append(key)
inf.close()

def BFS(sv, al):
  level = {sv:0}
  i = 1
  brd = [sv]
  while brd:
    next_level = []
    for vertex in brd:
      for neighbour in al[vertex]:
        if neighbour not in level:
          level[neighbour] = i
          next_level.append(neighbour)
    brd = next_level
    i += 1
  for vertex in level.keys():
    otf.write(f"{str(vertex)} ")

BFS(1, graph)
otf.close()


# %%
#task2
inf = open("input2_3.txt","r")
otf = open("output2_3.txt","w")

line_1 = inf.readline().strip().split(" ")
vc, ec = int(line_1[0]), int(line_1[1])

graph = {}
for i in range(vc+1):
  graph[i] = []

for line in inf:
  line_list = line.strip().split(' ')
  line_list = list(map(int, line_list))
  for key in graph:
    if key == line_list[0]:
      graph[key].append(line_list[1])
      graph[line_list[1]].append(key)
inf.close()

def BFS(sv, al):
  level = {sv:0}
  i = 1
  brd = [sv]
  while brd:
    next_level = []
    for vertex in brd:
      for neighbour in al[vertex]:
        if neighbour not in level:
          level[neighbour] = i
          next_level.append(neighbour)
    brd = next_level
    i += 1
  for vertex in level.keys():
    otf.write(f"{str(vertex)} ")

BFS(1, graph)
otf.close()


# %%
#task2
inf = open("input2_4.txt","r")
otf = open("output2_4.txt","w")

line_1 = inf.readline().strip().split(" ")
vc, ec = int(line_1[0]), int(line_1[1])

graph = {}
for i in range(vc+1):
  graph[i] = []

for line in inf:
  line_list = line.strip().split(' ')
  line_list = list(map(int, line_list))
  for key in graph:
    if key == line_list[0]:
      graph[key].append(line_list[1])
      graph[line_list[1]].append(key)
inf.close()

def BFS(sv, al):
  level = {sv:0}
  i = 1
  brd = [sv]
  while brd:
    next_level = []
    for vertex in brd:
      for neighbour in al[vertex]:
        if neighbour not in level:
          level[neighbour] = i
          next_level.append(neighbour)
    brd = next_level
    i += 1
  for vertex in level.keys():
    otf.write(f"{str(vertex)} ")

BFS(1, graph)
otf.close()



