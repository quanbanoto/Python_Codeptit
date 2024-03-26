for x in range(int(input())):
    n = int(input())
    a = []
    for i in range(1005):
        a.append(0)
    for i in range(n):
        x = int(input())
        a[x] += 1
    m = max(a)
    for i in range(1005):
        if a[i] == m:
            print(i)
            break
    

# 3
# 3
# 999
# 999
# 19
# 4
# 13
# 333
# 333
# 13
# 3
# 11
# 12
# 13