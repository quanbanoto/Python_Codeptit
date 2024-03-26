for i in range(0, int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    sum  = 0
    for i in range(3):
        sum += min(a)
        a.remove(min(a))
    print(sum)
