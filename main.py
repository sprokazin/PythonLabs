import random
import os

with open('dataset_Facebook.csv') as f:
    str_f = str(f.read())

table = []
table_str = []
index = 0

for i in range(len(str_f)):
    if str_f[i] == ';':
        table_str.append(str_f[index:i])
        index = i + 1
    if str_f[i] == '\n':
        table_str.append(str_f[index:i])
        index = i + 1
        table.append(table_str)
        table_str = []
table_str.append(str_f[index:i + 1])
table.append(table_str)
amount_of_str_elem = len(table[0])


def max_len_column(amount, index2):
    max_len = 0
    for i in range(amount):
        if len(table[i][index2]) > max_len:
            max_len = len(table[i][index2])
    return max_len


def space_counter(element, max_len):
    counter = max_len - len(str(element))
    return counter + 1


def Show(type, amount=5, separator=','):
    if amount > len(table):
        print('Not enough strings in the table to show')
        return

    max_line = len(str(max(table, key=len)))
    if type == 'top':
        for i in range(amount):
            for j in range(amount_of_str_elem):
                counter = space_counter(table[i][j], max_len_column(amount, j))
                if i == 0:
                    print('\033[1m\033[34m' + table[i][j] + '\033[0m', counter * ' ', end=separator, sep='')
                else:
                    print(table[i][j], counter * ' ', end=separator, sep='')
            print(end='\n')
            print(max_line * '.')

    if type == 'bottom':
        for i in range(len(table) - amount, len(table) - 1):
            for j in range(amount_of_str_elem):
                counter = space_counter(table[i][j], max_len_column(amount, j))
                if i == 0:
                    print('\033[1m\033[34m' + table[i][j].upper() + '\033[0m', counter * ' ', end=separator, sep='')
                else:
                    print(table[i][j], counter * ' ', end=separator, sep='')
            print(end='\n')
            print(max_line * '.')

    if type == 'random':
        rand_index = random.sample([i for i in range(0, len(table))], amount)
        for i in rand_index:
            for j in range(amount_of_str_elem):
                counter = space_counter(table[i][j], max_len_column(amount, j))
                if i == 0:
                    print('\033[1m\033[34m' + table[i][j].upper() + '\033[0m', counter * ' ', end=separator, sep='')
                else:
                    print(table[i][j], counter * ' ', end=separator, sep='')
            print(end='\n')
            print(max_line * '.')

    return


def Info():
    print(amount_of_str_elem, 'x', len(table) - 1)
    counter=0
    for i in range(len(table) - 1):
        for j in range(amount_of_str_elem):
            if table[i][j] != '':
                counter+=1
        print(table[0][j], counter-1, type(table[i][j]))
        counter=0
    return


def DelNan():
    i = 0
    while i < len(table):
        j = 0
        while j < amount_of_str_elem:
            if table[i][j] == '':
                del table[i]
                i-=1
                break
            else:
                j+=1
        i+=1
    return

def MakeDS():
    if os.path.exists('./workdata') == False:
        os.mkdir('workdata')
        os.mkdir('workdata/Learning')
        os.mkdir('workdata/Testing')
    index70=int(len(table)*0.7)
    rand_index = random.sample([i for i in range(0, len(table))], index70)
    with open ('./workdata/Learning/train.csv', 'a+') as f1:
        with open('./workdata/Testing/test.csv', 'a+') as f2:
            for i in range(len(table) - 1):
                if i in rand_index:
                    for j in range(amount_of_str_elem):
                        f1.write(table[i][j]+';')
                    f1.write('\n')
                else:
                    for j in range(amount_of_str_elem):
                        f2.write(table[i][j]+';')
                    f2.write('\n')
    return

#Info()
#Show('top', 7, '| ')
#Show('bottom', 7, '|')
#Show('random', 5, '|')
#MakeDS()
#DelNan()