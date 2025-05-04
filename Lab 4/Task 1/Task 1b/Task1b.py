# %%
def graphadj(n,m,let):
    dic = {}
    for i in range(n+1):
        dic[i] = []
    print(dic)

    for i in range(1,len(let)):
        lin = let[i].split(" ")
        n1 = int(lin[0])
        n2 = int(lin[1])
        mc = int(lin[2])
        x = (n2,mc)
        dic[n1].append(x)

    return(dic)

# %%
f1 = open("input1b_1.txt",'r')
let = f1.read().split("\n")
print(let)

firstline = let[0].split(' ')
n = int(firstline[0])
m = int(firstline[1])
print(n,m)
print("~ ~ ~ ~")

z = graphadj(n,m,let)

f2 = open("output1b_1.txt",'w')

for i in range (len(z)):
    print(f"{i}:{z[i]}")
    f2.write(f"{i}:{z[i]}\n")
f2.close()


# %%
f1 = open("input1b_2.txt",'r')
let = f1.read().split("\n")
print(let)

firstline = let[0].split(' ')
n = int(firstline[0])
m = int(firstline[1])
print(n,m)
print("~ ~ ~ ~")

z = graphadj(n,m,let)

f2 = open("output1b_2.txt",'w')

for i in range (len(z)):
    print(f"{i}:{z[i]}")
    f2.write(f"{i}:{z[i]}\n")
f2.close()


# %%
f1 = open("input1b_3.txt",'r')
let = f1.read().split("\n")
print(let)

firstline = let[0].split(' ')
n = int(firstline[0])
m = int(firstline[1])
print(n,m)
print("~ ~ ~ ~")

z = graphadj(n,m,let)

f2 = open("output1b_3.txt",'w')

for i in range (len(z)):
    print(f"{i}:{z[i]}")
    f2.write(f"{i}:{z[i]}\n")
f2.close()



