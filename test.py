import sys
def r_list(r_square):
    lst = []
    for i in range(r_square,0,-1):
        lst.append(i**2)
    return(lst)


print(r_list(int(sys.argv[1])))
