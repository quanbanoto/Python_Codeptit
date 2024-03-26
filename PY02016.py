def xuat_hien_nhieu_nhat(a, n):
    s = set({})
    a = list(a)
    for i in a:
        s.add(i)
    for i in s:
        if 2 * a.count(i) > n:
            return i
    return "NO"


for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(xuat_hien_nhieu_nhat(a, n))
