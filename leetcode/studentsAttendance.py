def checkRecord(s):
    #P=present
    #A=absent
    #L=late
    #if num of A > 1 or more than 2 consecutive lates
    abs_count = 0
    for i in range(len(s)):
        if(s[i] == 'A'):
            abs_count += 1
        if(s[i] == 'L' and i+2 < len(s)):
            if(s[i:i+3] == "LLL"):
                return False
    if(abs_count > 1):
        return False
    return True
if __name__ == "__main__":
    print(checkRecord("PPALLP"))