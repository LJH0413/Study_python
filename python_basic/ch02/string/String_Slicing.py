a = "202102092213Sunny"

year = a[:4]
day = a[4:8]
time = a[8:12]
weather = a[12:]

print(year)
print(day)
print(time)
print(weather)
print()

# 문자열의 변경
p = "Pithon"
p1 = p[:1]
p2 = p[2:]
print(p1 + "y" + p2)