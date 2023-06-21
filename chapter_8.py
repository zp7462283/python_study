from module import module_8


# 8.1
def display_message():
    print('hello, python!')


display_message()


# 8.2
def favorite_book(title):
    print(f'One of my favorite books is {title}.')


favorite_book('Alice in Wonderland')


# 8.3 and 8.4
def make_shirt(size=180, example='I love Python'):
    print(f'尺码{size}, 字样{example}')


make_shirt(170, '花花公子')
make_shirt(example='海澜之家', size=165)
make_shirt()
make_shirt(175)
make_shirt(160, '呸~~~')


# 8.5
def describe_city(city, country='China'):
    print(f'{city} is in {country}')


describe_city('YunCheng')
describe_city('BeiJing')
describe_city('NewYork', 'America')


# 8.6
def city_country(city, country):
    return f'{city.title()},{country.title()}'


cityCountry = city_country('YunCheng', 'China')
print(cityCountry)
cityCountry = city_country('NewYork', 'america')
print(cityCountry)


# 8.7
def make_album(singer, album, number=None):
    result = {'singer': singer, 'album': album}
    if number:
        result['number'] = number
    return result


singerInfo = make_album('ZhouJieLun', '我也不知道啥专辑', '100')
print(singerInfo)


# 8.8
# while True:
#     singer = input('singer name:')
#     if singer == 'q':
#         break
#     album = input('album:')
#     if album == 'q':
#         break
#     info = make_album(singer, album)
#     print(info)

# 8.9
def show_messages(messages):
    for message in messages:
        print(message)


messagesList = ['a', 'b', 'c']
show_messages(messagesList)


# 8.10, 8.11
def send_messages(not_send, send):
    while not_send:
        nots = not_send.pop()
        send.append(nots)
        print(nots)


not_send = ['a', 'b', 'c']
send = []
send_messages(not_send[:], send)
print(not_send)
print(send)


# 8.12
def pizza_list(*pizzas):
    print("配料：")
    for pizza in pizzas:
        print(f"\t- {pizza}")


pizza_list('a', 'b', 'c')
pizza_list('a', 'b', 'c', 'd')
pizza_list('a', 'b', 'c', 'd', 'e')


# 8.13
def build_profile(first, last, **info):
    info['first'] = first
    info['last'] = last
    print(info)


build_profile('z', 'p', age=12, height=175)


# 8.14
car = module_8.make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
