def isHappy(n):
    lst = []
    sum = 0
    while(sum != 1):
        while(n != 0):
            dig = n % 10
            n //= 10
            sum += dig**2
        n = sum
        if(n == 1):
            return True
        if(n in lst):
            return False
        else:
            lst.append(n)
        sum = 0

if __name__ == "__main__":
    print(isHappy(19))