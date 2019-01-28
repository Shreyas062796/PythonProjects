import random
def printNums():
	for i in range(1,100):
		if(i % 3 == 0 and i % 7 == 0):
			print("OpenSource")
			continue
		elif(i % 3 == 0):
			print("Open")
			continue
		elif(i % 7 == 0):
			print("Source")
		print(i)

def getIntegers(lst):
	sumofInts = 0
	for i in range(len(lst)):
		if(lst[i].isdigit()):
			sumofInts += int(lst[i])
	return(sumofInts)

def getIntegersRecursive(lst,index,s):
	if(index == -1):
		return(s)
	if(lst[index].isdigit()):
		s += int(lst[index])
	return(getIntegersRecursive(lst,index-1,s))


def rand5():
	return(random.randint(0,5))

def rand7():
	num = rand5() + rand5()
	if(num > 7):
		return(num - 3)
	return(num)
if __name__ == "__main__":
	#arr = ["132","asra","hello","431","23"]
	#print(getIntegersRecursive(["132","asra","hello","431","23"],len(arr)-1,0))
	counts = {}
	for i in range(200):
		num = rand7()
		if(num in counts):
			counts[num] += 1
		else:
			counts[num] = 1
	print(counts)
	# print(getIntegers(["132","asra","hello","431","23"]))
	#printNums()