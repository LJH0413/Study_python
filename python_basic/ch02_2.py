# ch02-2
# 파이썬 완전 기초
# 파이썬 변수

# 기본 선언
n = 700 #-> n에다 700을 넣어라
print(n)
print(type(n))

print()

#동시 선언
x = y = z = 500
print(x, y, z)

print()

# 선언
var = 75
var = "change Value"
print(var)
print(type(var))

print()

# object reference
# 변수값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔출력

# 예)1
print(300)
print(int(300))

print()

# 예)2
n = 777
print(n, type(n))
print()

# 예)3
m = n
print(m, n)
print(type(m), type(n))

print()

# id(identity)확인 : 고유값
i = 800
j = 655

print(id(i))
print(id(j))
print()

j = 800

print(id(i))
print(id(j))
print()

# 다양한 변수 선언
# camel case : numberOFBsgOne -> 매서드
# Pascal case : NumberOFBsgOne -> 클래스
# snake case : number_of_college_ex

# 허용하는 변수 선언법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE = 8

# 예약어는 변수명으로 불가능
"""
False  def  if  raise
None  del  import  return
True  elif  in  try
and  else  is  while
as  except  lambda  with
assert finally  nonlocal  yield
break  for  not  class  form  or  continue
global  pass  
"""