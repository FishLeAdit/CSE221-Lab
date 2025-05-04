# %%

import numpy as np

inf = open("input6_1.txt","r")
otf = open("output6_1.txt","w")

line_1 = inf.readline().split(" ")
line_1 = list(map(int, line_1))
rc, cc = line_1[0], line_1[1]

graph = np.ones([rc, cc], dtype=str)
ri = 0

for line in inf:
    line_content = line.strip()
    line_list = [i for i in line_content]
    for col in range(len(line_list)):
        graph[ri][col] = line_list[col]
    ri += 1

def jumanji_max_diamond(rc, cc, graph):
    def dfs(row, col):
        if row < 0 or row >= rc or col < 0 or col >= cc or graph[row][col] == '#' or visited[row][col]:
            return 0

        visited[row][col] = True
        diamonds = 0

        if graph[row][col] == 'D':
            diamonds = 1

        diamonds += dfs(row + 1, col)
        diamonds += dfs(row - 1, col)
        diamonds += dfs(row, col + 1)
        diamonds += dfs(row, col - 1)

        return diamonds

    visited = [[False for _ in range(cc)] for _ in range(rc)]
    max_diamonds = 0

    for i in range(rc):
        for j in range(cc):
            if graph[i][j] == '.' and not visited[i][j]:
                max_diamonds = max(max_diamonds, dfs(i, j))

    return max_diamonds

result = jumanji_max_diamond(rc, cc, graph)
otf.write(str(result))

inf.close()
otf.close()


# %%

import numpy as np

inf = open("input6_2.txt","r")
otf = open("output6_2.txt","w")

line_1 = inf.readline().split(" ")
line_1 = list(map(int, line_1))
rc, cc = line_1[0], line_1[1]

graph = np.ones([rc, cc], dtype=str)
ri = 0

for line in inf:
    line_content = line.strip()
    line_list = [i for i in line_content]
    for col in range(len(line_list)):
        graph[ri][col] = line_list[col]
    ri += 1

def jumanji_max_diamond(rc, cc, graph):
    def dfs(row, col):
        if row < 0 or row >= rc or col < 0 or col >= cc or graph[row][col] == '#' or visited[row][col]:
            return 0

        visited[row][col] = True
        diamonds = 0

        if graph[row][col] == 'D':
            diamonds = 1

        diamonds += dfs(row + 1, col)
        diamonds += dfs(row - 1, col)
        diamonds += dfs(row, col + 1)
        diamonds += dfs(row, col - 1)

        return diamonds

    visited = [[False for _ in range(cc)] for _ in range(rc)]
    max_diamonds = 0

    for i in range(rc):
        for j in range(cc):
            if graph[i][j] == '.' and not visited[i][j]:
                max_diamonds = max(max_diamonds, dfs(i, j))

    return max_diamonds

result = jumanji_max_diamond(rc, cc, graph)
otf.write(str(result))

inf.close()
otf.close()


# %%

import numpy as np

inf = open("input6_3.txt","r")
otf = open("output6_3.txt","w")

line_1 = inf.readline().split(" ")
line_1 = list(map(int, line_1))
rc, cc = line_1[0], line_1[1]

graph = np.ones([rc, cc], dtype=str)
ri = 0

for line in inf:
    line_content = line.strip()
    line_list = [i for i in line_content]
    for col in range(len(line_list)):
        graph[ri][col] = line_list[col]
    ri += 1

def jumanji_max_diamond(rc, cc, graph):
    def dfs(row, col):
        if row < 0 or row >= rc or col < 0 or col >= cc or graph[row][col] == '#' or visited[row][col]:
            return 0

        visited[row][col] = True
        diamonds = 0

        if graph[row][col] == 'D':
            diamonds = 1

        diamonds += dfs(row + 1, col)
        diamonds += dfs(row - 1, col)
        diamonds += dfs(row, col + 1)
        diamonds += dfs(row, col - 1)

        return diamonds

    visited = [[False for _ in range(cc)] for _ in range(rc)]
    max_diamonds = 0

    for i in range(rc):
        for j in range(cc):
            if graph[i][j] == '.' and not visited[i][j]:
                max_diamonds = max(max_diamonds, dfs(i, j))

    return max_diamonds

result = jumanji_max_diamond(rc, cc, graph)
otf.write(str(result))

inf.close()
otf.close()


# %%

import numpy as np

inf = open("input6_4.txt","r")
otf = open("output6_4.txt","w")

line_1 = inf.readline().split(" ")
line_1 = list(map(int, line_1))
rc, cc = line_1[0], line_1[1]

graph = np.ones([rc, cc], dtype=str)
ri = 0

for line in inf:
    line_content = line.strip()
    line_list = [i for i in line_content]
    for col in range(len(line_list)):
        graph[ri][col] = line_list[col]
    ri += 1

def jumanji_max_diamond(rc, cc, graph):
    def dfs(row, col):
        if row < 0 or row >= rc or col < 0 or col >= cc or graph[row][col] == '#' or visited[row][col]:
            return 0

        visited[row][col] = True
        diamonds = 0

        if graph[row][col] == 'D':
            diamonds = 1

        diamonds += dfs(row + 1, col)
        diamonds += dfs(row - 1, col)
        diamonds += dfs(row, col + 1)
        diamonds += dfs(row, col - 1)

        return diamonds

    visited = [[False for _ in range(cc)] for _ in range(rc)]
    max_diamonds = 0

    for i in range(rc):
        for j in range(cc):
            if graph[i][j] == '.' and not visited[i][j]:
                max_diamonds = max(max_diamonds, dfs(i, j))

    return max_diamonds

result = jumanji_max_diamond(rc, cc, graph)
otf.write(str(result))

inf.close()
otf.close()


# %%

import numpy as np

inf = open("input6_5.txt","r")
otf = open("output6_5.txt","w")

line_1 = inf.readline().split(" ")
line_1 = list(map(int, line_1))
rc, cc = line_1[0], line_1[1]

graph = np.ones([rc, cc], dtype=str)
ri = 0

for line in inf:
    line_content = line.strip()
    line_list = [i for i in line_content]
    for col in range(len(line_list)):
        graph[ri][col] = line_list[col]
    ri += 1

def jumanji_max_diamond(rc, cc, graph):
    def dfs(row, col):
        if row < 0 or row >= rc or col < 0 or col >= cc or graph[row][col] == '#' or visited[row][col]:
            return 0

        visited[row][col] = True
        diamonds = 0

        if graph[row][col] == 'D':
            diamonds = 1

        diamonds += dfs(row + 1, col)
        diamonds += dfs(row - 1, col)
        diamonds += dfs(row, col + 1)
        diamonds += dfs(row, col - 1)

        return diamonds

    visited = [[False for _ in range(cc)] for _ in range(rc)]
    max_diamonds = 0

    for i in range(rc):
        for j in range(cc):
            if graph[i][j] == '.' and not visited[i][j]:
                max_diamonds = max(max_diamonds, dfs(i, j))

    return max_diamonds

result = jumanji_max_diamond(rc, cc, graph)
otf.write(str(result))

inf.close()
otf.close()


# %%

import numpy as np

inf = open("input6_6.txt","r")
otf = open("output6_6.txt","w")

line_1 = inf.readline().split(" ")
line_1 = list(map(int, line_1))
rc, cc = line_1[0], line_1[1]

graph = np.ones([rc, cc], dtype=str)
ri = 0

for line in inf:
    line_content = line.strip()
    line_list = [i for i in line_content]
    for col in range(len(line_list)):
        graph[ri][col] = line_list[col]
    ri += 1

def jumanji_max_diamond(rc, cc, graph):
    def dfs(row, col):
        if row < 0 or row >= rc or col < 0 or col >= cc or graph[row][col] == '#' or visited[row][col]:
            return 0

        visited[row][col] = True
        diamonds = 0

        if graph[row][col] == 'D':
            diamonds = 1

        diamonds += dfs(row + 1, col)
        diamonds += dfs(row - 1, col)
        diamonds += dfs(row, col + 1)
        diamonds += dfs(row, col - 1)

        return diamonds

    visited = [[False for _ in range(cc)] for _ in range(rc)]
    max_diamonds = 0

    for i in range(rc):
        for j in range(cc):
            if graph[i][j] == '.' and not visited[i][j]:
                max_diamonds = max(max_diamonds, dfs(i, j))

    return max_diamonds

result = jumanji_max_diamond(rc, cc, graph)
otf.write(str(result))

inf.close()
otf.close()


# %%

import numpy as np

inf = open("input6_7.txt","r")
otf = open("output6_7.txt","w")

line_1 = inf.readline().split(" ")
line_1 = list(map(int, line_1))
rc, cc = line_1[0], line_1[1]

graph = np.ones([rc, cc], dtype=str)
ri = 0

for line in inf:
    line_content = line.strip()
    line_list = [i for i in line_content]
    for col in range(len(line_list)):
        graph[ri][col] = line_list[col]
    ri += 1

def jumanji_max_diamond(rc, cc, graph):
    def dfs(row, col):
        if row < 0 or row >= rc or col < 0 or col >= cc or graph[row][col] == '#' or visited[row][col]:
            return 0

        visited[row][col] = True
        diamonds = 0

        if graph[row][col] == 'D':
            diamonds = 1

        diamonds += dfs(row + 1, col)
        diamonds += dfs(row - 1, col)
        diamonds += dfs(row, col + 1)
        diamonds += dfs(row, col - 1)

        return diamonds

    visited = [[False for _ in range(cc)] for _ in range(rc)]
    max_diamonds = 0

    for i in range(rc):
        for j in range(cc):
            if graph[i][j] == '.' and not visited[i][j]:
                max_diamonds = max(max_diamonds, dfs(i, j))

    return max_diamonds

result = jumanji_max_diamond(rc, cc, graph)
otf.write(str(result))

inf.close()
otf.close()



