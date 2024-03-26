n = list(map(int, input().split()))

while n != [0, 0, 0, 0]:
    cnt = 0
    while not(n[1] == n[2] == n[3] == n[0]):
        x = n[0]
        n[0] = abs(n[0] - n[1])
        n[1] = abs(n[1] - n[2])
        n[2] = abs(n[2] - n[3])
        n[3] = abs(n[3] - x)
        cnt += 1
    print(cnt)
    n = list(map(int, input().split()))