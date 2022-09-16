x = input("какую систему мы переводим? 2/10 \n")
if x=='2':
    n=int(input('введи число \n'))
    print(bin(n))
if x=='10':
    n=input('введи число \n')
    print(int(n, 2))
