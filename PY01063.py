for i in range(int(input())):
    s = input()
    n = input()
    lenS = len(s)
    lenN = len(n)
    cnt = 0
    i = 0
    while i < lenS:
        if s[i : i + lenN] == n:
            cnt += 1
            i += lenN
        else:
            i += 1
    print(cnt)
