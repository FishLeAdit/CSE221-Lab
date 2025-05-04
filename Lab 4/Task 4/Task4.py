# %%

inf = open("input4_1.txt","r")
otf = open("output4_1.txt","w")

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
inf.close()



rs = [False]*(vc+1)

def DFS_visit(vertex, al, visited, rs):
  visited[vertex] = True
  rs[vertex] = True

  for i in al[vertex]:
    if rs[i] == True:
      return True
    else:
      DFS_visit(i, al, visited, rs)
  rs[vertex] = False

  return False

def DFS(sv, al):
  visited = [False]*(vc+1)
  return DFS_visit(sv, al, visited, rs)

def isCyclic(sv, al):
  if DFS(sv, al):
    otf.write("Yes")
  else:
    otf.write("No")

isCyclic(1, graph)
otf.close()


# %%

inf = open("input4_2.txt","r")
otf = open("output4_2.txt","w")

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
inf.close()



rs = [False]*(vc+1)

def DFS_visit(vertex, al, visited, rs):
  visited[vertex] = True
  rs[vertex] = True

  for i in al[vertex]:
    if rs[i] == True:
      return True
    else:
      DFS_visit(i, al, visited, rs)
  rs[vertex] = False

  return False

def DFS(sv, al):
  visited = [False]*(vc+1)
  return DFS_visit(sv, al, visited, rs)

def isCyclic(sv, al):
  if DFS(sv, al):
    otf.write("Yes")
  else:
    otf.write("No")

isCyclic(1, graph)
otf.close()


# %%

inf = open("input4_3.txt","r")
otf = open("output4_3.txt","w")

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
inf.close()



rs = [False]*(vc+1)

def DFS_visit(vertex, al, visited, rs):
  visited[vertex] = True
  rs[vertex] = True

  for i in al[vertex]:
    if rs[i] == True:
      return True
    else:
      DFS_visit(i, al, visited, rs)
  rs[vertex] = False

  return False

def DFS(sv, al):
  visited = [False]*(vc+1)
  return DFS_visit(sv, al, visited, rs)

def isCyclic(sv, al):
  if DFS(sv, al):
    otf.write("Yes")
  else:
    otf.write("No")

isCyclic(1, graph)
otf.close()


# %%

inf = open("input4_4.txt","r")
otf = open("output4_4.txt","w")

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
inf.close()



rs = [False]*(vc+1)

def DFS_visit(vertex, al, visited, rs):
  visited[vertex] = True
  rs[vertex] = True

  for i in al[vertex]:
    if rs[i] == True:
      return True
    else:
      DFS_visit(i, al, visited, rs)
  rs[vertex] = False

  return False

def DFS(sv, al):
  visited = [False]*(vc+1)
  return DFS_visit(sv, al, visited, rs)

def isCyclic(sv, al):
  if DFS(sv, al):
    otf.write("Yes")
  else:
    otf.write("No")

isCyclic(1, graph)
otf.close()



