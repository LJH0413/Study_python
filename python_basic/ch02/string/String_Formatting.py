# 숫자 대입 %d
# 문자열 대입 %s
d1 = "I eat %d apples." % 3
s1 = "I eat %s apples." % "five"
print(d1)
print(s1)

number = 10
day = "one"
x1 = "i ate %d apples, so i was sick for %s days" %(number, day)
print(x1)

# 포매팅 연산자 %d와%를 같이 쓸때는는 %% 사용
# s2 = "Error is %d%" % 98
s2 = "Error is %d%%" % 98

print(s2)