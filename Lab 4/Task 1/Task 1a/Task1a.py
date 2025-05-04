# %%
#Task 1a_1

f1 = open("input1a_1.txt",'r')
let = f1.read().split("\n")
print(let)

firstline = let[0].split(' ')
n = int(firstline[0])
m = int(firstline[1])
print(n,m)

adj_mat = []
for i in range(n+1):
  row = [0]*(n+1)

  adj_mat.append(row)

print('----')
print(adj_mat)
print('---')
for i in let[1:]:
  i = i.split(' ')
  u = int(i[0])
  v = int(i[1])
  w = int(i[2])
  print(u,v,w)

  adj_mat[u][v] = w
print(adj_mat)

f2  = open("output1a_1.txt",'w')
for i in adj_mat:
    for j in i:
        f2.write(f"{str(j)} ")
    f2.write('\n')
f2.close()

# %%
#Task 1a_2

f1 = open("input1a_2.txt",'r')
let = f1.read().split("\n")
print(let)

firstline = let[0].split(' ')
n = int(firstline[0])
m = int(firstline[1])
print(n,m)

adj_mat = []
for i in range(n+1):
  row = [0]*(n+1)

  adj_mat.append(row)

print('----')
print(adj_mat)
print('---')
for i in let[1:]:
  i = i.split(' ')
  u = int(i[0])
  v = int(i[1])
  w = int(i[2])
  print(u,v,w)

  adj_mat[u][v] = w
print(adj_mat)

f2  = open("output1a_2.txt",'w')
for i in adj_mat:
    for j in i:
        f2.write(f"{str(j)} ")
    f2.write('\n')
f2.close()


