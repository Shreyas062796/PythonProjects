def addStrings(num1, num2):
    num1 = list(num1)
    num2 = list(num2)
    carry = 0
    sum = 0
    if(len(num1) > len(num2)):
        for i in range(len(num1)-len(num2)):
            num2 = ['0'] + num2
    else:
        for i in range(len(num2)-len(num1)):
            num1 = ['0'] + num1
    i = len(num1)-1
    while(i >= 0):
        sum = int(num1[i]) + int(num2[i]) + int(carry)
        carry = sum // 10
        num1[i] = str(sum % 10)
        i-=1
    if(carry != 0):
        num1 = [str(carry)] + num1
    return("".join(num1))
if __name__ == "__main__":
    print(addStrings("1","324"))