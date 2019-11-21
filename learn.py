import re
with open('in.txt', mode='r') as f:
    s=f.read()
    s1 = re.split(r'\s', s) #利用正则函数进行分割
    while '' in s1:
        s1.remove('')
    for i in s1:
        # if i == ' ': print(i, end='')
        # else: print(i+',', end='')
        print(i+',', end=' ')
    print()