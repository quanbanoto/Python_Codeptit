def chan_le(n):
    l = len(n)
    s = 0
    i = 0
    while i < l - 1:
        if abs(int(n[i]) - int(n[i + 1])) != 2:
            return "NO"
        s += int(n[i])
        i += 1
    s += int(n[i])
    if s % 10 != 0:
        return "NO"
    return "YES"



for i in range(int(input())):
    print(chan_le(input()))