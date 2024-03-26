def bien_doi_ve_1(n):
    if n == 1:
        return 1
    cnt = 1
    while n != 1:
        if n % 2 == 0:
            n/=2
        else:
            n = n*3 + 1
        cnt+=1
    return cnt

n = int(input())
while n != 0:
    print(bien_doi_ve_1(n))
    n = int(input())