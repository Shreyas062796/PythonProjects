#create a dictionary
#populate the key as letter value count
 
import sys

def isEqual(str1,str2):
    dict = {}
    #makes both the words lowercase
    str2 = str2.lower()
    str1 = str1.lower()
    #gets list of distinct letters
    setstr2 =  set(str2.lower())
    if(len(str1) != len(str2) or str1 is None or str2 is None):
        return(False)
    for i in range(len(str1)):
        if(str1[i].lower() in dict):
            dict[str1[i]] += 1
        else:
            dict[str1[i]] = 1
    #checks if two words are equal
    for letter in setstr2:
        if(letter not in dict or str2.count(letter) != dict[letter]):
            return(False)
    return(True)
#z in str2 
#what if there is letters in str2 that are not in str1

#takes 2 command line arguments
if __name__ == "__main__":
    equals = isEqual(sys.argv[1],sys.argv[2])
    print(equals)
