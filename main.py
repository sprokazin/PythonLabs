#1
def non_rep_num():
    print('Задание 1. Введите элементы списка через пробел: ', end='')
    num_list = list(map(int, input().split()))
    num_set = set(num_list)
    print('Количество неповторяющихся элементвой списка - ', len(num_set))

#2
def sub_set():
    print('Задание 2. Введите элементы 1 множества через пробел: ', end='')
    set1=set(map(int, input().split()))
    print('Введите элементы 2 множества через пробел: ', end='')
    set2=set(map(int, input().split()))
    if set.intersection(set1, set2) == set1 and set1!= set2:
        print('True')
    else:
        print('False')

#3
def cities_game():
    n=int(input('Задание 3. Введите количество названных городов: '))
    cities_set = set()
    for i in range(n):
        new_city=input('Введите город: ')
        if new_city in cities_set:
            print('REPEAT')
        else:
            cities_set.add(new_city)
            print('OK')


if __name__ == '__main__':
    non_rep_num()
    sub_set()
    cities_game()