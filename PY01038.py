def check(n):
    cnt = 0
    if int(n) % 7 == 0:
        return n
    while cnt <= 1000:
        m = int(n[::-1])
        n = str(m + int(n))
        if int(n) % 7 == 0:
            return n;
        cnt += 1
    return -1

for i in range(int(input())):
   print(check(input()))
