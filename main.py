# 0
def higher_list():
    print('Задание 0. Введите элементы списка через пробел: ', end='')
    list1 = list(map(int, input().split()))
    list2 = []
    for i in range(len(list1)):
        if i > 0 and list1[i] > list1[i - 1]:
            list2.append(list1[i])
    print('Массив из новых элементов:', list2)


# 1
def change_elements():
    print('Задание 1. Введите элементы списка через пробел: ', end='')
    list1 = list(map(int, input().split()))
    list2 = []
    min, max = list1[0], list1[0]
    ind_max, ind_min = 0, 0
    for i in range(len(list1)):
        if list1[i] > max:
            max = list1[i]
            ind_max = i
        if list1[i] < min:
            min = list1[i]
            ind_min = i
    for i in range(len(list1)):
        list2.append(list1[i])
    list2[ind_max], list2[ind_min] = list2[ind_min], list2[ind_max]
    print('Массив из новых элементов:', list2)

# 2
def same_num():
    print('Задание 2. Введите элементы 1 списка через пробел: ', end='')
    list1 = list(map(int, input().split()))
    print('Введите элементы 2 списка через пробел: ', end='')
    list2 = list(map(int, input().split()))
    counter = 0
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                counter = counter + 1
    print('Количество совпадающих элементов в 1 и 2 списке - ', counter)


#3
def same_in_dict(str_list):
    dict1={}
    for s in str_list:
        if s in dict1:
            dict1[s]+=1
        else:
            dict1[s]=1
    return list(dict1.values())



if __name__ == '__main__':
    higher_list()
    change_elements()
    same_num()
    print('Задание 3. Выходные данные: ')
    print(same_in_dict(['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']))
    print(same_in_dict(['aaa', 'bbb', 'ccc']))
    print(same_in_dict(['abc', 'abc', 'abc']))
    print('Выходные данные совпали')