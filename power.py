import sys
def calculatePower(base,exponent):
    count = 0
    answer = 1
    while(count < exponent):
        answer *= base
        count += 1
    return(answer)
if __name__ == "__main__":
    print(calculatePower(int(sys.argv[1]),int(sys.argv[2])))
