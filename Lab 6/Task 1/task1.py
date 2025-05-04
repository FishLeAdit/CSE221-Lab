from queue import PriorityQueue

f1=open('input1_2.txt','r')
f2=open('output1_2.txt','w')

n,m=map(int,f1.readline().strip().split())
adj_lst = [ [] for i in range(n) ]

for i in range(m):
  u , v , w = map(int,f1.readline().strip().split())
  adj_lst[u-1].append((v-1 , w))

source = int(f1.readline()) - 1
q = PriorityQueue()
distance = [float("inf")] * n
distance[source] = 0
q.put((0 , source))

while not q.empty():
  d, u = q.get()
  if d > distance[u]:
    continue
  for v , w in adj_lst[u]:
    if distance[v] > w + distance[u]:
        distance[v] = distance[u] + w
        q.put((distance[v] , v))

for val in distance:
  if val == float("inf"):
    w='-1'+ ' '
    f2.write(w)
  else:
    w=str(val) + ' '
    f2.write(w)
    