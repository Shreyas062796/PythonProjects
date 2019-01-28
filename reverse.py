import sys
def reverse(str):
    str = list(str)
    start = 0
    end = len(str)-1
    while(start < end):
        str[start],str[end] = str[end],str[start]
        start += 1
        end -= 1
    return("".join(str))

def isPalindrome(str):
    if(str == reverse(str)):
        return(str + " is a palindrome")
    return(str + " isn't a palindrome")
if __name__ == '__main__':
    reverse(sys.argv[1])
    print(isPalindrome(sys.argv[1]))
