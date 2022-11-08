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
mul_m = 1
start_index = my_list.index(min(my_list))
end_index = my_list.index(max(my_list))
if start_index > end_index:
    start_index, end_index= end_index, start_index
print(f'start_index= {start_index}, end_index= {end_index}')
for i in range(start_index+1, end_index):
    print(f'{my_list[i]}',end='')
    mul_m *= my_list[i]
for i in range(0, len(my_list)):
    if start_index > my_list[i] > 0:
        start_index = i
    if end_index < my_list[i]>0:
        end_index[1] += i
sum = 0
if start_index > end_index:
    start_index, end_index= end_index, start_index
print(f'start_index= {start_index}, end_index= {end_index}')
for i in range(start_index+1, end_index):
    print(f'{my_list[i]}',end='')
    sum *= my_list[i]
print(f'sum neg {sum_list[0]}')
print(f'sum even {sum_list[1]}')
print(f'sum odd {sum_list[2]}')
print(f'sum even 3 index {mul}')
print(f'\nMul={mul_m}')
print(f'\nsum={mul_m}')
