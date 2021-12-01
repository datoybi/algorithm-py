'''
baekjoon online judge
<open>tag<close>

<ab cd>ef gh<ij kl>
<ab cd>fe hg<ij kl>


<int><max>2147483647<long long><max>9223372036854775807
<int><max>7463847412<long long><max>7085774586302733229
'''


str = ['e', 'f', ' ', 'g', 'h', '<']
result = ''
lst = list()
tmp = list()

for i in range(len(str)):
    print(i)
    print(tmp)

    if str[i] == ' ':
        print('here1 : ' , tmp)
        # lst.append(tmp)
        for t in tmp:
            lst.append(t)
        lst.append(' ')
        tmp = []  

    if str[i] == '<':
        print('here2 : ' , tmp)
        for t in tmp:
            lst.append(t)
        # lst.append(tmp)
        tmp = []   

    else: 
        tmp.insert(0, str[i])

print(lst)

