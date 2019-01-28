import sys
def reverseStr(word):
    if(len(word) == 1):
        return(word)
    for i in range(int(len(word)/2)):
        word[i],word[len(word)-i-1] = word[len(word)-i-1], word[i]
    return(word)

def reverse(sentence):
    i = 0
    wordlen = 0
    while(i <= len(sentence)):
        if(i == len(sentence)):
           str = reverseStr(sentence[i-wordlen:i])
           tmp = sentence[0:i-wordlen] + str + sentence[i::]
           sentence = tmp
           break
        if(sentence[i] == ' ' and wordlen != 0):
            str = reverseStr(sentence[i-wordlen:i])
            tmp = sentence[0:i-wordlen] + str + sentence[i::]
            sentence = tmp
            wordlen = 0
            i += 1
            continue
        wordlen += 1
        i += 1
    return("".join(reverseStr(sentence)))

#x = ['w','o','r','d',' ','i','s',' ','c','o','o','l']
x = sys.argv[1]
rev = reverse(list(x))
print(rev)
