def check(n):
    n = str(n).lower()
    if n[-3:] != ".py":
        return "no"
    l = len(n)
    if l < 3:
        return "no"
    for i in n:
        if (not i.isalpha()) and i != '_' and i != '.':
            return "no"
    return "yes"


print(check(input()))
