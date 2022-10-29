def fact(n):
    res = 1
    while n > 1:
        res = res * n
        n = n - 1
    return res


def comb(upper_index, lower_index):
    res = fact(lower_index) / (fact(upper_index) * fact(lower_index - upper_index))
    return int(res)

# 1
def task1():
    print('Первое задание - Треугольник Паскаля: ', end='\n')
    print("Введите число: ", end='')
    n = int(input())
    counter = n
    for i in range(n + 1):
        print(counter * ' ', end='')
        for j in range(n + 1):
            var = comb(j, i)
            if j == 1 and i == 0:
                var = 0
            if var != 0:
                print(var, end=" ")
        counter = counter - 1
        print(end='\n')


# 2
def task2():
    print("Второе задание - Треугольник Серпинского: ", end='\n')
    print("Введите число: ", end='')
    n = int(input())
    triangle = ['.']
    for i in range(n):
        white_space = ' ' * (2 ** i)
        triangle = [white_space + x + white_space for x in triangle] + [x + ' ' + x for x in triangle]
    print("\n".join(triangle))


if __name__ == '__main__':
    task1()
    task2()
