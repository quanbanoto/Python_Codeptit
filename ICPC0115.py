a = [1,1,2,6,24,120,720,5040,40320, 362880]

def krish_number(n):
    l = len(n)
    s = 0
    for i in n:
        s += a[int(i)]
    if n == str(s):
        return "Yes"
    return "No"

for t in range(int(input())):
    print(krish_number(input()))

    