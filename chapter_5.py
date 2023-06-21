# python入门到实践第五章

# 5.1
print('practice 5.1')
car = 'subaru'
print("Is car == 'subaru' ? I predict True.")
print(car == 'subaru')
print("Is car == 'audi' ? I predict False.")
print(car == 'audi')

# 5.2
print()
print('practice 5.2')
str_1 = 'a'
str_2 = 'b'
print(str_1 == str_2)
print(str_1 != str_2)
name = 'Zhang Peng'
print(name.lower() == 'zhang peng')
print(name == 'zhang peng')
lists = ['a', 'b', 'c']
print('a' in lists)
print('a' not in lists)

# 5.3
print()
print('practice 5.3')
alien_color = 'green'
if 'green' == alien_color:
    print('获得5分')

# 5.4
print()
print('practice 5.4')
if 'green' == alien_color:
    print('获得5分')
else:
    print('获得10分')

# 5.5
print()
print('practice 5.5')
if 'green' == alien_color:
    print(5)
elif 'yellow' == alien_color:
    print(10)
elif 'red' == alien_color:
    print(15)

# 5.6
print()
print('practice 5.6')
age = 2
if age < 2:
    print('婴儿')
elif age < 4:
    print('幼儿')
elif age < 13:
    print('儿童')
elif age < 18:
    print('少年')
elif age < 65:
    print('中青年人')
else:
    print('老年人')

# 5.7
print()
print('practice 5.7')
favorite_fruits = ['apple', 'banana', 'tomato']
if 'apple' in favorite_fruits:
    print('You really like apple')
if 'banana' in favorite_fruits:
    print('You really like banana')
if 'tomato' in favorite_fruits:
    print('You really like tomato')
if 'strawberry' in favorite_fruits:
    print('You really like strawberry')

# 5.8
print()
print('practice 5.8')
users = ['tom', 'jerry', 'bob', 'admin', 'jk']
for user in users:
    if user == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print(f'Hello {user}, thank you for logging in again')

# 5.9
print()
print('practice 5.9')
users = []
print(users)
if users:
    print('We have users!')
else:
    print('We need to find some users!')

# 5.10
print()
print('practice 5.10')
current_users = ['tom', 'jerry', 'bob', 'JK', 'Long']
current_copy_users = [user.lower() for user in current_users]
new_users = ['long', 'tom', 'tony']
for user in new_users:
    if user in current_copy_users:
        print(f'{user},yes')
    else:
        print(f'{user},no')

# 5.11
print()
print('practice 5.11')
numbers = [number for number in range(1, 10)]
for val in numbers:
    if val == 1:
        print(f'{val}st')
    elif val == 2:
        print(f'{val}nd')
    elif val == 3:
        print(f'{val}rd')
    else:
        print(f'{val}th')