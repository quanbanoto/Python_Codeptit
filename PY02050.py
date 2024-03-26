for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    cnt = []
    for i in range(n):
        cnt.append(1)
        j = i - 1
        while a[i] >= a[j] and j >= 0:
            cnt[i] += cnt[j]
            j -= cnt[j]
        print(cnt[i], end=" ")
    print()


