# append 리스트에 요소 추가
a = [1, 2, 3]
a.append(4)
print(a)
# 리스트 안에는 어떤 자료형도 추가 가능
a.append([5, 6])
print(a)

print()

# sort -> 정렬
b = [1, 4, 3, 2]
print(b)
b.sort()
print(b)

c = ['a', 'o', 'l', 'f']
c.sort()
print(c)

print()

# reverse -> 리스트 뒤집기 (정렬이 아닌 그대로)
d = ['u', 'a', '기준', 'b', 'h']
d.reverse()
print(d)

# index(x) -> 리스트의 x의 값의 위치
print(d.index('a'))

# insert(x, y) -> 리스트 x번째의 y를 삽입
e = [1, 2, 3]
e.insert(0, 4)
print(e)

print()

# remove(x) -> 리스트에서 첫번째로 나오는 x를 삭제
f = [1, 2, 3, 1, 2, 3]
f.remove(3)
print(f)

# pop -> 리스트의 맨 마지막 요소를 돌려주고 삭제
e.pop()
print(e)
print()

# count(x) -> 리스트의 x가 몇개 있는지 출력
print(f.count(1))

print()

# extend(x) -> x에는 리스트만 가능 원래 리스트에 x리스트를 더함
h = [1, 2, 3]
h.extend([4, 5])
print(h)
