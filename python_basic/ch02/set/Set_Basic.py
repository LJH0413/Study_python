s1 = set([1,2,3])
print(s1)

s2 = set("Hello")
print(s2)

print()

# set의 특징
# 중복을 허용하지 않는다
# 순서가 없다
l1 = list(s1)
print(l1)
print(l1[0])

print()

t1 = tuple(s1)
print(t1)
print(t1[1])

print("-------------------------")


x1 = set([1, 2, 3, 4, 5, 6])
x2 = set([4, 5, 6, 7, 8, 9])

# 교집합 (&)
print(x1 & x2)

print()

# 합집합
# 중복된 값은 한개씩 표현
print(x1 | x2)
print(x1.union(x2))

print()

# 차집합
print(x1 - x2)
print(x2 - x1)
print(x1.difference(x2))
print(x2.difference(x1))