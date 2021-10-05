A = int(input())
B = int(input())
C = int(input())

num_list = []

for i in str(A*B*C):
    num_list.append(int(i))

print(num_list.count(0))
print(num_list.count(1))
print(num_list.count(2))
print(num_list.count(3))
print(num_list.count(4))
print(num_list.count(5))
print(num_list.count(6))
print(num_list.count(7))
print(num_list.count(8))
print(num_list.count(9))
########## input ##########
# 150
# 266
# 427
########## output ##########
# 3
# 1
# 0
# 2
# 0
# 0
# 0
# 2
# 0
# 0
