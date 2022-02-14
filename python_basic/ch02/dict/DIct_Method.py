# Make Key List
a = {'name':'jun', 'phone':'01052020896', 'birth':'0413'}

print(a.keys())

for k in a.keys():
    print(k)

print()

# list로 반환
print(list(a.keys()))

# make value list (values)
print(a.values())

print()

# key, value 쌍 얻기 (items)
print(a.items())

print()

# key: value 쌍 모두 지우기 (clear)
a.clear()
print(a)

print()

# key로 value 얻기 (get)
a = {'name':'jun', 'phone':'01052020896', 'birth':'0413'}
print(a.get('name'))
print(a.get('phone'))

print()

# 찾으려는 key값이 없을 경우 디폴트값 대신 가져오고 싶을 때 get(x, '디폴트값')
print(a.get('foo', 'bar'))

print()

# 해당 key안에 딕셔너리가 있는지 조사 (in)
print('name' in a)

print('email' in a)