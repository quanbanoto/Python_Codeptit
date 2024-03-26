t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    cnt = 0
    for i in range(0, n - 3):
        if a[i] > 0:
            break
        else:
            l = i + 1
            r = n - 1
            while l < r:
                if a[l] + a[i] + a[r] == 0:
                    cnt += 1
                    
                elif a[l] + a[i] + a[r] > 0:
                    r -= 1
                else:
                    l += 1
    print(cnt)
    t -= 1
