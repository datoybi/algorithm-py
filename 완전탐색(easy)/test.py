'''
int& a*[]&, b, c*;


int&&[]* a;
int& b;
int&* c;
'''
lst = ['a*[]&']

print(lst[0][4:5])
print(lst[0][len(lst[0])-1:len(lst[0])])
