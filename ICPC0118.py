def cung_hoang_dao(a: int, b: int):
    if b == 1:
        if a <= 19:
            return "Ma ket"
        return "Bao Binh"
    if b == 2:
        if a <= 18:
            return "Bao Binh"
        return "Song Ngu"
    if b == 3:
        if a <= 20:
            return "Song Ngu"
        return "Bach Duong"
    if b == 4:
        if a <= 19:
            return "Bach Duong"
        return "Kim Nguu"
    if b == 5:
        if a <= 20:
            return "Kim Nguu"
        return "Song Tu"
    if b == 6:
        if a <= 20:
            return "Song Tu"
        return "Cu Giai"
    if b == 7:
        if a <= 22:
            return "Cu Giai"
        return "Su Tu"
    if b == 8:
        if a <= 22:
            return "Su Tu"
        return "Xu Nu"
    if b == 9:
        if a <= 22:
            return "Xu Nu"
        return "Thien Binh"
    if b == 10:
        if a <= 22:
            return "Thien Binh"
        return "Thien Yet"
    if b == 11:
        if a <= 22:
            return "Thien Yet"
        return "Nhan Ma"
    if b == 12:
        if a <= 21:
            return "Nhan Ma"
        return "Ma ket"

for i in range(int(input())):
    a, b = map(int, input().split())
    print(cung_hoang_dao(a, b))