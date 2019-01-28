import sys
#codes = {}

def firstrecurring(str):
    lst = []
    for i in range(len(str)):
        if(str[i] in lst):
            return(str[i])
        lst.append(str[i])


def fibonacci(num):
    a = 0
    b = 1
    curr = 0
    count = 0
    while(b < num):
        print(b)
        count += b
        curr = a + b
        a = b
        b = curr
    return(count)

def squared(base,exp):
    num = 1
    while(exp > 0):
        num *= base
        exp -= 1
    return(num)
print(firstrecurring('ABCBDA'))
print(fibonacci(int(sys.argv[1])))
print(squared(3,3))
