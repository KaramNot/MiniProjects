import random
s = []
for i in range(1, 76):
    s.append(i)
x = random.sample(s, 25)
x[12]=0
mat = [[0]*5 for _ in range(5)]
count=0
for i in range(5):
    for j in range(5):
        mat[i][j]=x[count]
        count+=1

for i in range(5):
    for j in range(5):
        print(str(mat[i][j]).ljust(3), end=" ")
    print()
