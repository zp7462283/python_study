# 6.1
print('practice 6.1')
info = {
    'first_name': 'z',
    'last_name': 'p',
    'age': 10,
    'city': '山西'
}
print(info.get('first_name'))
print(info.get('last_name'))
print(info.get('age'))
print(info.get('city'))

# 6.2
print()
print('practice 6.2')
friend_number = {
    'a': 1,
    'b': 2,
    'c': 3
}
for val, key in friend_number.items():
    print(f'{val} like number {key}')

# 6.5
print()
print('practice 6.5')
dictionary = {
    'nile': 'egypt'
}
for key, val in dictionary.items():
    print(f'The {key.title()} runs through {val.title()}')

# 6.6
print()
print('practice 6.6')
isExist = ['tom', 'long']
dictionary = {
    'tom': 1,
    'long': 2,
    'tony': 3
}
for key in dictionary.keys():
    if key in isExist:
        print('Thank you')
    else:
        print('no')

# 6.7
print()
print('practice 6.7')
peoples = [
    {
        'name': 'tom'
    },
    {
        'name': 'tony'
    },
    {
        'name': 'long'
    }
]
for people in peoples:
    print(people)

# 6.8
print()
print('practice 6.8')
pets = [
    {
        'type': 'cat',
        'name': 'tony'
    },
    {
        'type': 'dog',
        'name': 'tom'
    }
]
for pet in pets:
    print(f"{pet['name']}, {pet['type']}")

# 6.9
print()
print('practice 6.9')
likes = {
    'tom': [1, 2, 3],
    'tony': ['a', 'b', 'c']
}
for key, val in likes.items():
    print(f"{key} like:")
    for location in val:
        print(location)


# 6.10
print()
print('practice 6.10')
like_numbers = {
    'tom': [1, 2, 3],
    'tony': [4, 5, 6]
}
for key, val in like_numbers.items():
    print(f"{key} like:")
    for number in val:
        print(number)

# 6.11
print()
print('practice 6.11')
cities = {
    'new_york': {
        'country': 'america',
        'population': 1000,
        'fact': 'free'
    },
    'xian': {
        'country': 'china',
        'population': 2000,
        'fact': 'big'
    }
}
for city, city_info in cities.items():
    print(f'城市是{city}')
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']
    print(f"\t国家是{country}")
    print(f"\t人口是{population}")
    print(f"\t事实是{fact}")