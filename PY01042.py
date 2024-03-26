def he_co_so_3(n):
    for i in n:
        if i < '0' or i > '2':
            return "NO"
    return "YES"


for i in range(int(input())):
    print(he_co_so_3(input()))

