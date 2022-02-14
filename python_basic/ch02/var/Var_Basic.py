# 변수 -> 값을 담는 공간

a = 1
b = "python"
c = [1, 2, 3]
# 자바와 C와 다르게 자료형을 스스로 저장한다

# 변수는 객체를 가리키는 것
print(id(a))

# 리스트의 쉬운 복사
b = a

print(id(b))
print(id(a))

print(a is b) #a와 b가 가리키는 객체는 동일한가?

print()

# [:] 이용
x = [1, 2, 3]
y = x[:]
x[1] = 4
print(x)
print(y)

# copy 모듈 이용
from copy import copy
y = copy(x)
print(y)

print(b is a)