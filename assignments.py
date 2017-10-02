#This is some of the work that I have done in python
import string
def punctuationinText(file_name):
    d = {}
    filename = open(file_name, 'r')
    lines = filename.readlines()
    filename.close()
    punctuation = string.punctuation
    for punc in punctuation:
        count = 0
        if punc in lines:
            count = lines.count(punc)
            d[punc] = count
    return d
def letterCount(filename):
    Conscount = 0
    vowcount = 0
    inF = open(filename, 'r')
    lines = inF.readlines()
    inF.close()
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiou'
    if consonants in lines:
        Conscount = lines.count(consonants)
        d['consonants'] = Conscount
    if vowels in lines:
        Vowcount = lines.count(vowels)
        d['vowels'] = Vowcount
    return d

def countVowels(inFile):
    vow = {}
    Vowels = 'aeiou'
    inputfile = open(inFile,'r')
    read = inputfile.readlines()
    for vowel in Vowels:
        count = 0
        if vowel in read:
            count = read.count(vowel)
            vow[vowel] = count
    return vow

def NumOfCapitalwords(file_name):
    newfile = open(file_name, 'r')
    lines =  newfile.readlines()
    newfile.close()
    for line in lines:
        words = line.split()
        for word in words:
            count = 0
            if word[0].upper():
                count = lines.count(word)
                d[word] = count
    return d
    
answer = " "
while(answer != "ton"):
    print("wrong answer")
    answer = input("Answer this riddle? Forward I am heavy backwards I am not. What am I?")
print("you got it correct")    

