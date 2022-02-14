# 딕셔너리는 배열 또는 해시라고 한다 (대응관계)

dic = {'name': 'jun', 'phone': '01052020896', 'birth':'0413'}

# 요소의 추가
a = {1 : 'a'}
a[2] = 'b'
print(a)

a['name'] = 'pey'
print(a)

a[3] = [1, 2, 3]
print(a)

# 딕셔너리 요소 삭제
del a[1]
print(a)