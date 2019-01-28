def binarysearch(lst,tgt):
    start = 0
    end = len(lst)
    if(tgt > lst[len(lst)-1]):
        print("Your number is greater than the max number")
    while(start < end):
        if(tgt == lst[end//2]):
            print("found " + str(tgt))
            break
        if(tgt < lst[end//2]):
            end = end//2
        else:
            start = end//2

if __name__ == "__main__":
    lst = []
    for i in range(1,101):
        lst.append(i)
    binarysearch(lst,10)
        
            



