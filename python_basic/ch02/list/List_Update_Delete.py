# 초기화 및 선언으로 수정
a = [1, 2, 3]
a[2] = 4
print(a)

# 삭제 -> del 함수 사용
# del 객체(모든자료형)
del a[1]
print(a)

# 슬라이싱 기법으로 요소 여러개 삭제
b = [1, 2, 3, 4, 5]
del b[2:]
print(b)


