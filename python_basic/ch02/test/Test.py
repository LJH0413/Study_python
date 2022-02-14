# Q1
kor = 80
eng = 75
math = 55
avg = (kor + eng + math) /3
print(avg)
print()

# Q2
# if문 사용

# Q3
iden = "881120-1068234"
year = "19" +iden[:2]
print(year)
mon = iden[2:4]
print(mon)
day = iden[4:6]
print(day)
print(year + mon + day)
print()
# Q4
sex = iden[7:8]
if(sex == "1") :
    print("male")
else :
    print("female")
print()
# Q5
a = "a:b:c:d"
ar = a.replace(":", "#")
print(ar)
print()

# Q6
i = [1, 3, 5, 4, 2]
i.sort()
i.reverse()
print(i)
print()

# Q7
j = ['Life', 'is', 'too', 'short']
j = " ".join(j)
print(j)
print()

# Q8
x1 = (1, 2, 3)
x2 = (4, )
print(x1 + x2)
print()

# Q10
w = {'a':90, 'b':80, 'c':70}
print(w['b'])
print()

# Q11
L = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5]
L1 = set(L)
print(L1)

# Q12
