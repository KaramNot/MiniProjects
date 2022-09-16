def draw_triangle(fill, base):
    for i in range(base):
        if i<base//2+1:
            for j in range(i+1):
                print(fill, end='')
            print()
        if i>base//2:
            for j in range(i, base):
                print(fill, end='')
            print()

fill = input()
base = int(input())
draw_triangle(fill, base)
