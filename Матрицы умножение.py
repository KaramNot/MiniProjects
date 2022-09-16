s = input().split()  # 1-я матрица, заполнение
n = int(s[0])
m = int(s[1])
mat1 = []
for i in range(n): 
    x = input().split()
    mat1.append(x)
for i in range(n):
    for j in range(m):
        mat1[i][j]=int(mat1[i][j])

x = input() #пробел

s = input().split() # 2-я матрица, заполнение
m = int(s[0])
k = int(s[1])
mat2 = []
for i in range(m): 
    x = input().split()
    mat2.append(x)
for i in range(m):
    for j in range(k):
        mat2[i][j]=int(mat2[i][j])

mat3 = [[0]*k for _ in range(n)] # 3-я матрица, заполнение
for i in range(n): 
    for j in range(k):
        for r in range(m):
            mat3[i][j]+=(mat1[i][r])*(mat2[r][j])
        

        
for i in range(n):  #ввывод матрицы: 3
    for j in range(k):
        print(str(mat3[i][j]).ljust(3), end=" ")
    print()
