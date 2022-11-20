#1
def write_read_file():
    sum=1
    f=open('input.txt')
    str1=f.read()
    f.close()
    for i in range(len(str1)):
        if str1[i]!=' ':
            sum=sum*int(str1[i])
    str_sum=str(sum)
    f2=open('output.txt', 'w')
    f2.write(str_sum)
    f2.close()
    return
#2
def read_num_write_sorted_num():
    lst=[]
    f=open('input2.txt')
    f2=open('output2.txt', 'w')
    for i in range(10):
        str1=f.readline()
        num=int(str1[:-1])
        lst.append(num)
        lst.sort(key=int)
    for i in range(10):
        f2.write(str(lst[i]))
        f2.write('\n')
    f.close()
    f2.close()
    return

#3
def kids():
    lst_names=[]
    lst_age=[]
    f=open('kids.txt')
    f1=open('youngest.txt', 'w')
    f2=open('oldest.txt', 'w')
    str1=f.read()
    k=0
    count=0
    for i in range(len(str1)):
        if(str1[i]==' '):
            lst_names.append(str1[k:i])
            count+=1
            k=i+1
        if str1[i]=='\n':
            lst_age.append(int(str1[k:i]))
            k=i+1
    min=100
    min_index=-1
    max_index=-1
    max=-1
    for i in range(len(lst_age)):
        if lst_age[i]>max:
            max=lst_age[i]
            max_index=i
        if lst_age[i]<min:
            min=lst_age[i]
            min_index=i
    youngest=lst_names[2*min_index] + ' ' + lst_names[2*min_index+1] + ' ' + str(lst_age[min_index])
    oldest=lst_names[2*max_index] + ' ' + lst_names[2*max_index+1] + ' ' + str(lst_age[max_index])

    f1.write(youngest)
    f2.write(oldest)

    return

if __name__ == '__main__':
    write_read_file()
    read_num_write_sorted_num()
    kids()