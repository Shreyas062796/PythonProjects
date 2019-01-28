import sys

def testFunc(str):
    lst = list(str)
    for i in range(len(lst)/2):
        lst[i],lst[len(lst)-i-1] = lst[len(lst)-i-1],lst[i]
    print("".join(lst))
    return("".join(lst))
if __name__ == "__main__":
    testFunc(sys.argv[1])
