head = "Python"
tail = " is Fun"
print(head + tail)

# 문자열 곱하기
print(head * 2)

# 문자열 길이 구하기
# -0 = 0
# -n은 뒤에서부터 n번째, 0 -1, -2, ... 순
a = "life is too short, you need Python"
print(len(a))
print(a[2])
print(a[-1])
print(a[12])

b = a[0] + a[1] + a[2] + a[3]
c = a[12:17]
# [n:m] = n <= x < m
print(b)
print(c)