# 7.1
print('practice 7.1')
# car = input('please enter car:')
# print(f"Let me see if I can find you a {car}")

# 7.2
print()
print('practice 7.2')
# number = input('please enter number:')
#
# if int(number) > 8:
#     print('no vacancies')
# else:
#     print('have vacancies')

# 7.4
print()
print('practice 7.4')

# while True:
#     pizza = input('please enter:')
#     if pizza == 'quit':
#         break
#     else:
#         print(f'添加{pizza}')

# 7.5
print()
print('practice 7.5')
# while True:
#     age = input('please enter:')
#     if age == 'quit':
#         break
#     age = int(age)
#     if age < 3:
#         print(0)
#     elif age < 12:
#         print(10)
#     else:
#         print(15)

# 7.6
print()
print('practice 7.6')


# 7.8
print()
print('practice 7.8')
sandwich_orders = ['a', 'b', 'c']
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)
    print(f'I made your {sandwich} sandwich')
for item in finished_sandwiches:
    print(item)

# 7.9
print()
print('practice 7.9')
print('a 卖完了')
sandwich_orders = ['a', 'b', 'c', 'a', 'd']
while 'a' in sandwich_orders:
    sandwich_orders.remove('a')
print(sandwich_orders)

# 7.10
print()
print('practice 7.10')
dict = {}
active = True
while active:
    name = input('your name:')
    place = input('place:')
    dict[name] = place
    result = input('yes/no:')
    if result == 'no':
        active = False
print(dict)