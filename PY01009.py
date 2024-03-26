s = input()
chuThuong = 0
for i in s:
    if(i.islower()):
        chuThuong += 1

if chuThuong >= len(s)/2:
    print(s.lower())
else:
    print(s.upper())