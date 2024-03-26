def so_con_thieu(a, n):
    res = 1
    for i in a:
        if i > res:
            return res
        res += 1
    return res


n = int(input())
a = list(map(int, input().split()))
a.sort()
print(so_con_thieu(a, n))