n = int(input())
s = []
for i in range(n):
    x=[]
    for j in range(i+1):
        if j==0 or j==i:
            x.append(1)
        else:
            x.append(s[i-1][j-1]+s[i-1][j])
    s.append(x)

for i in range(n):
    for j in range(n-i-1):
        print(' ', end="")
    for j in range(i+1):
        print(s[i][j], end=" ")
    print()
