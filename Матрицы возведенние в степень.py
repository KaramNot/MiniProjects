n = int(input())  # квадратная матрица
mat1 = [] # 1-я матрица, заполнение
for i in range(n): 
    x = input().split()
    mat1.append(x)
for i in range(n):
    for j in range(n):
        mat1[i][j]=int(mat1[i][j])
        
mat2 = mat1.copy() # 2-я матрица, заполнение

k = int(input()) #степень в которую возводим

for _ in range(k-1):
    mat3 = [[0]*n for _ in range(n)] # 3-я матрица, обнуленная каждый раз
    for i in range(n): 
        for j in range(n):
            for r in range(n):
                mat3[i][j]+=(mat1[i][r])*(mat2[r][j])
    mat2 = mat3.copy()

        
for i in range(n):  #ввывод матрицы
    for j in range(n):
        print(str(mat3[i][j]).ljust(3), end=" ")
    print()
