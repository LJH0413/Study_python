# chapter02-1
# 파이썬 완전 기초
# print 사용법
# 참조 : https://www.python-course.eu/python3_formatted_output.php

# 기본출력
print('python start!')
print("python start!")
print("""Python Start!""")
print('''Python Start!''')

print() #print()는 줄바꿈

# separator 옵션
# sep='i' i안에 문자로 나눔
# 문자열간의 연결
print('P', 'y', 't', 'h', 'o', 'n', sep='')
print('P', 'y', 't', 'h', 'o', 'n', sep='|')
print('010', '7777', '2222', sep='-')
print('python', 'google.com', sep='@')

print()

# end옵션 -> 줄바꿈 여부, 하나의 라인으로 연결 할 수 있다
print('welcome to', end=' ')
print('IT news', end=' ')
print('Web Site')

print()

# file 옵션
import sys
print('Learn Python', file=sys.stdout)

# format 사용 (d, s, f)
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))

# %s
print('%10s' % ('nice',))
print('{:>10}'.format('nice'))

print('%-10s' % ('nice',))
print('{:10}'.format('nice'))

print('{:_<10}'.format('nice'))
print('{:^10}'.format('nice'))

print('%.5s' % ('pythonstudy',))
print('{:.5}'.format('pythonstudy'))
print('{:10.5}'.format('pythonstudy'))

# %d
print('%d %d' % (1, 2))
print('{} {}'.format(1, 2))

print('%4d' % (42,))
print('{:4d}'.format(42))

# %f
print('%f' % (3.141592653589793,))
print('{:f}'.format(3.141592653589793))

print('%06.2f' % (3.141592653589793,))
print('{:06.2f}'.format(3.141592653589793))