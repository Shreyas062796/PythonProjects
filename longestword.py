#this is some of the work that I have done in python
def vowelUseDict(t):
       dic = {}
       vowels = 'aeiou'
       words = t.split()
       for vowel in vowels:
              count = 0
              for word in words:
                     if vowel in word:
                            count += 1
              dic[vowel] = count
       return dic
text = 'like a vision she dances across the porch as the radio plays'
print(vowelUseDict(text))

def longestWord(inFile,outFile):
       inputfile = open(inFile,'r')
       outputfile = open(outFile,'w')
       lines = inputfile.readlines()
       inputfile.close()
       for line in lines:
              words = line.split()
              greatest = 0
              for word in words:
                     if len(word) > greatest:
                            greatest = len(word)
              outputfile.write(len(greatest))
              outputfile.write(" ")
              outputfile.write("\n")
       outputfile.close()
s
       
       
