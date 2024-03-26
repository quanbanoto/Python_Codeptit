for i in range(int(input())):
    n = input()
    s = 1
    for i in n:
        if int(i) != 0:
            s *= int(i)
    print(s)
