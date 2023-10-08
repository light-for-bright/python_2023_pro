# D.1
size = int(input("Введите размер доски: "))
for i in range(size):
    for j in range(size):
        if (i + j) % 2 == 0:
            print("#", end=' ')
        else:
            print(" ", end=' ')
    print()

# D.2
height = int(input("Введите высоту пирамиды: "))
for i in range(1, height + 1):
    for j in range(height - i):
        print(" ", end='')
    for k in range(1, 2 * i):
        print(i, end='')
    print()
