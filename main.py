# 1
def format_string():
    str1 = str(input('Форматирование строки. Введите строчку: '))
    letter = str1[0]
    counter = 0
    res = []
    for i in range(len(str1)):
        if letter != str1[i]:
            res.append(letter)
            if counter > 1:
                res.append(str(counter))
            letter = str1[i]
            counter = 1
        else:
            counter = counter + 1
    res.append(letter)
    if counter > 1:  # учитываю последнюю букву в строке, по-другому не получилось придумать алгоритм :(
        res.append(str(counter))
    return "".join(res)


# 1.1
def unformat_string():
    str1 = str(input('Разформатирование строки. Введите строчку: '))
    res = []
    for i in range(len(str1)):
        if i < len(str1) - 1 and str1[i + 1].isdigit():
            res.append(str(str1[i] * int(str1[i + 1])))
        else:
            if not str1[i].isdigit():
                res.append(str(str1[i]))
    return "".join(res)


# 3

def format_string2(string):
    res = []
    for i in range(len(string)):
        if string[i] != ' ':
            res.append(string[i])
    res.sort()
    letter = res[0]
    str_res = []
    num_res = []
    counter = 0
    for i in range(len(res)):
        if letter != res[i]:
            str_res.append(letter)
            num_res.append(str(counter))
            letter = res[i]
            counter = 1
        else:
            counter = counter + 1
    str_res.append(letter)
    num_res.append(str(counter))

    return num_res, str_res



def three_most_popular_symbols():
    str1 = str(input('Часто встречающиеся символы. Введите строчку: '))
    num_res, str_res = format_string2(str1)
    for i in range(len(num_res)):
        for j in range(i + 1, len(num_res)):
            if num_res[i] < num_res[j]:
                num_res[i], num_res[j] = num_res[j], num_res[i]
                str_res[i], str_res[j] = str_res[j], str_res[i]
    print("Наиболее часто встречающиеся символы:\n {0} - {1} раз\n {2} - {3} раз\n {4} - {5} раз".format(
                    str_res[0],
                    num_res[0],
                    str_res[1],
                    num_res[1],
                    str_res[2],
                    num_res[2]))

#4

WORDS = { 0: '',
    1: 'один', 2: 'два', 3: 'три',
    4: 'четыре', 5: 'пять', 6: 'шесть',
    7: 'семь', 8: 'восемь', 9: 'девять',
    10: 'десять', 11: 'одиннадцать', 12: 'двенадцать',
    13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать',
    16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать',
    19: 'девятнадцать', 20: 'двадцать', 30: 'тридцать',
    40: 'сорок', 50: 'пятьдесят', 60: 'шестьдесят',
    70: 'семьдесят', 80: 'восемьдесят', 90: 'девяносто',
    100: 'сто', 200: 'двести', 300: 'триста', 400: 'четыреста',
    500: 'пятьсот', 600: 'шестьсот', 700: 'семьсот', 800: 'восемьсот',
    900: 'девятьсот'}


def write_num():
    num = int(input('Как пишется число. Введите число от 1 до 1000: '))
    if(num < 20):
        return WORDS[num]
    ones = num % 10
    if num // 10:
        tens = (num % 100) - ones
    if num // 100:
        hundreds= (num // 100)*100

    if num // 10 and num // 100:
        if tens+ones < 20:
            return " ".join((WORDS[hundreds], WORDS[tens+ones])).title()
        return " ".join((WORDS[hundreds], WORDS[tens], WORDS[ones])).title()
    elif num // 10:
        return " ".join((WORDS[tens], WORDS[ones])).title()


if __name__ == '__main__':
    print(format_string())
    print(unformat_string())
    print(write_num())
