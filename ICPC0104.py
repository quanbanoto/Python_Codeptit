n = int(input())

while n > 0:
    s = input()
    res = 10 ** 18
    x = 0
    le = len(s)
    for i in range(0, le - 1):
        if s[i].isdigit():
            x = x * 10 + int(s[i])
            if s[i + 1].isalpha():
                res = min(x, res)
                x = 0
    print(res)
