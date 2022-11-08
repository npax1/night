import random
size=int(input("size"))
begin = int(input("begin"))
end = int(input("end"))
my_list=list()
for i in range (size):
    my_list.append(random.randint(begin,end))
for i in range(0, len(my_list)):
    print(f'{my_list}')
print()
mul = 1
for i in range(0, len(my_list), 3):
    print(f'{mul} * {my_list[i]}[(i)]=', end='')
    mul +=my_list[i]
    print(mul)

sum_list = [0] * 3
for i in my_list:
    if i < 0:
        sum_list[0] += i
    if i % 2 == 0:
        sum_list[1] += i
    if i % 2 != 0:
        sum_list[2] += i
start_index = mylist.index()
print(f'sum neg {sum_list[0]}')
print(f'sum even {sum_list[1]}')
print(f'sum odd {sum_list[2]}')
print(f'sum even 3 index {mul}')