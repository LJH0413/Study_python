# count = 해당 문자의 개수
a = "hobby"
count_a = a.count('b')
len_a = len(a)
print(count_a)
print(len_a)

# find = 해당 문자의 위치
b = "Python is the best choice"
b_find_b = b.find('b')
b_find_k = b.find('k')
print(b_find_b)
print(b_find_k)
# if not exist return -1

# index = 위치 알려주기
c = "Life is too short"
c_index_t = c.index('t')
# c_index_k = c.index('k')
# index method is not exist return error message (stack trace)
print(c_index_t)



