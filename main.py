import numpy as np
import re

# 1
with open('task1.txt', 'a+') as m_file:
    m_file.write('Сохранить этот текст в файл. Прочитать матрицу из файла.\n' +
                 "Hайдите для этой матрицы сумму всех элементов, максимальный и минимальный элемент (число)\n" +
                 "3,4,17,-3\n" + "5,11,-1,6\n" + "0,2,-5,8\n")
with open('task1.txt', 'r+') as m_file:
    str_f = m_file.read()

lst_f = []
i = 0
while i < len(str_f):
    if str_f[i].isdigit() or str_f[i] == '-':
        index = i
        index_end = str_f.find('\n', i, len(str_f))
        if index_end != -1:
            lst_f.append(str_f[index:index_end])
            i = index_end
    i += 1

matrix = []
nums = []
for i in range(len(lst_f)):
    nums = lst_f[i].split(',')
    matrix.append([int(item) for item in nums])
print('Matrix:\n', matrix)

arr = np.array(matrix, int)
asum = np.sum(arr)
amax = np.amax(arr)
amin = np.amin(arr)
print('Sum of elements:', asum, 'Max element:', amax, 'Minimum element:', amin, sep='\n')

# 2
def run_length_encoding(x):
    elem=x[0]
    counter=0
    elems = []
    counters = []
    for i in range(len(x)):
        if x[i] == elem:
            counter+=1
        else:
            counters.append(counter)
            elem=x[i]
            counter=1
        if not x[i] in elems:
            elems.append(x[i])
    counters.append(counter)
    print('Numbers:', np.array(elems, int), 'Counters:', np.array(counters, int), sep='\n')

x = np.array([2, 2, 2, 3, 3, 3, 5])
run_length_encoding(x)

# 3
def normal_matrix():
    nums=[]
    for i in range(10):
        nums.append(np.random.normal(0,1,4))
    mas=np.array(nums, float)
    part_mas=np.array(nums[0:5], float)
    print('10 elements of a normal distribution:', mas, '5 elements of a normal distribution:', part_mas, sep='\n')
    print('Max element:', np.amax(mas), 'Minimum element:', np.amin(mas), 'An average:', np.average(mas) , sep='\n')
normal_matrix()

# 4
def max_element_after_zero(x):
    nums=[]
    for i in range(len(x)-1):
        if x[i]==0:
            nums.append(x[i+1])
    max_elem= np.max(nums)
    print('Maximum element after zeros:\n', max_elem)

x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])

max_element_after_zero(x)

#5
def get_log_density(dots_X, size: tuple, EX, lenght_vector, cov_matrix):
    return np.log(np.linalg.det(cov_matrix)) - lenght_vector * np.log(2 * np.pi) - 0.5 * (
                dots_X - EX).T @ np.linalg.inv(cov_matrix) @ (dots_X - EX)


# 6
a = np.arange(16).reshape(4, 4)
b = np.array(a[0], int)
a[0], a[2] = a[2], a[0]

print('Changed array:\n',a)

# 7
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt('./archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', delimiter=',', dtype='object')


def run_length_encoding2(matrix):
    elems = []
    for i in range(len(matrix)):
        if not matrix[i][3] in elems:
            elems.append(matrix[i][3])

    y = np.array(elems, str)
    print('Unique values:\n', y)
    counter = [0] * (len(y))
    for i in range(len(y)):
        for t in range(len(matrix[:, 3])):
            counter[i] += np.count_nonzero(y[i] == re.sub('[^.\d]', '', str(matrix[t][3])))

    print('Amounts of unique element:\n', counter)


run_length_encoding2(iris)

# 8
x=np.array([0,1,2,0,0,4,0,6,9], int)
task8 = np.nonzero(x)
print('Non-zero elements indices: ', task8)

