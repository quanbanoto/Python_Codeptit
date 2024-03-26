for i in range(int(input())):
    s = input()
    l = len(s)
    n = []
    j = 0
    while(j < l):
        cnt = 1
        while j < l - 1 and s[j] == s[j+1]:
            cnt += 1
            j += 1
        n.append(str(cnt))
        n.append(s[j])
        j += 1
    print(''.join(n))
