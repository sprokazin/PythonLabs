import json
import csv
import  sys

with open(str(sys.argv[1]), 'r') as file:
    json_data = json.load(file)

table = []
for i in (json_data):
    name = str(i);

table = json_data.pop(name)
str_table = []
for i in table:
    str_table.append(i)

str_file = []
with open(name + '.csv', 'a+') as file:
    writer = csv.writer(file)
    for key, values in str_table[0].items():
        str_file.append(key)
        str_file.append(';')
    str_file.append('\n')
    for i in range(len(str_table)):
        for key, value in str_table[i].items():
            str_file.append(value)
            str_file.append(';')
        str_file.append('\n')

    i=0
    while i<len(str_file):
        if str_file[i]==';' and str_file[i+1]=='\n':
            i+=1
            continue
        else:
            file.write(str_file[i])
            i+=1

