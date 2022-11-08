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

result_list_even= list()
result_list_odd= list()
result_list_neg= list()
result_list_pos= list()

for i in my_list:
    if i % 2 == 0:
        result_list_even.appeng(i)
    if i % 2 == 0:
        result_list_odd.appeng(i)
    if i % 2 == 0:
        result_list_neg.appeng(i)
    if i % 2 == 0:
        result_list_pos.appeng(i)
print(f'listeven:{result_list_even}')
print(f'listodd:{result_list_odd}')
print(f'listneg:{result_list_neg}')
print(f'listpos:{result_list_pos}')
