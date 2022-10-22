
    # 1 (невнимательно прочитал условие, сделал программу для n чисел, а не для трех)
def task1():
    print('Первое задание:', end='\n')
    print('Введите число элементов в массиве:', end=' ')
    n = int(input())
    numbers = [0]*n
    print('Введите массив из n элементов:', end=' ')
    numbers = input().split()

    counter = 0
    for i in range(n):
        for j in range(i+1, n):
            if numbers[i] == numbers[j]:
                counter = counter+1
    print('Совпадающих чисел:', end=' ')
    print(counter)

    # 2
def task2():
    print(end='\n')
    print('Второе задание - лесенка с использованием чисел:', end='\n')
    print('Введите число элементов в массиве:', end=' ')
    n = int(input())
    for i in range(n):
        for j in range(n-n+i+1):
            print(j+1, end='')
        print('')

    # 3
def task2_second():
    print(end='\n')
    print('Третье задание - лесенка с использованием строчки:', end='\n')
    print('Введите число элементов в массиве:', end=' ')
    n = int(input())
    numbers = ''
    for j in range(1, n+1):
        numbers = numbers + str(j) + ' '*(len(str(n))-len(str(j))+1)
        print(numbers, end='\n')

    #4
def task2_third():
    print(end='\n')
    print('Четвертое задание - пирамидка:', end='\n')
    print('Введите число элементов в массиве:', end=' ')

    n = int(input())
    for i in range(1, n + 1, 1):
        print(((n - i) * len(str(n)))*' ', end="")
        for j in range(1, i, 1):
            print(j, end=(len(str(n)) - len(str(j))) * ' ')
        for k in range(i, 0, -1):
            print(k, end=(len(str(n)) - len(str(k))) * ' ')
        print((n - i) * (len(str(n)) - len(str(i))) * ' ')



if __name__ == '__main__':
    task1()
    task2()
    task2_second()
    task2_third()
