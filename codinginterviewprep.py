import requests
import sys 
def test():
    fib = 2
    num1 = 1
    num2 = 2
    while(num2 <= 4000000 and num1 <= 4000000):
        if((num1 + num2) % 2 == 0):
            fib += (num1 + num2)  
        temp = num1
        num1 = num2
        num2 = temp  + num2
    print(fib)

def largestPalindrome():
    large = 0
    for i in range(1,1000):
        for x in range(1,1000):
            curr = i * x
            if(str(curr) == str(curr)[::-1] and curr > large):
                large = curr
    print(large)

def largestPrimeFactor(x):
    largest = 0
    factors = []
    prime = False
    for i in range(1,x+1):
        if(x%i == 0):
            for j in range(1,i+1):
                if(i%j == 0):
                    factors.append(j)
            print(factors)
            if((len(factors) == 1 or len(factors) == 2) and max(factors) > largest):
                largest = max(factors)
            factors = []
    print(largest)

def smallestMultiple():
    largest = 1
    cur = 1
    number = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055112540698747158523863050715693290963295227443043557166896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
    for i in range(len(number)-12):
        sub = number[i:i+13]
        print(sub)
        for i in range(len(sub)):
            cur *= int(sub[i])
        if(cur > largest):
            largest = cur
        cur = 0
    print(largest)

class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

class Tree:
    def __init__(self):
        self.root = None

    def addNode(self,node,value):
        if(node == None):
            self.root = Node(value)
        else:
            if(value < node.value):
                if(node.left == None):
                    node.left = Node(value)
                else:
                    self.addNode(node.left,value)
            else:
                if(node.right == None):
                    node.right = Node(value)
                else:
                    self.addNode(node.right,value)

    def printInorder(self,node):
        if(node != None):
            self.printInorder(node.left)
            print(node.value)
            self.printInorder(node.right)

def BFSBinaryTree():
    v = len(graph)
    visited = [False] * (v)
    for i in range(v):
        if(visited[i] == False):
            visited[i] = True
            #keep traversing until you reach the end 

def DFS(graph, start):
    visited,stack = set(), [start]
    while stack:
        if(vertex not in visited):
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return(visited)

#[1,2,3,4] tg = 4
#[3,2,]
def findTarget(lst,target):
    comps = []
    for num in lst:
        if(num in comps):
            return(num,target-num)
        comps.append(target-num)
    return(0)

def BinarySearch(target):
    #divide and conquer type algorithm
    lst = []
    for i in range(1,201):
        lst.append(i)
    start = 0
    end = len(lst)-1
    while(start < end):
        mid = (start + end) // 2
        if(mid == target):
            return(mid)
        if(target < mid):
            end = mid
        else:
            start = mid
        print(mid)
    return(0)

def reverseString():
    string =  "lasah"
    string = list(string)
    left = 0
    right = len(string)-1
    while left < right:
        string[left], string[right] = string[right], string[left]
        left += 1
        right -= 1
    print("".join(string))

# def squared(base,exp):
#     tmp = 1
#     num = 1
#     if(exp == 0):
#         print(1)
#         return(1)
#     elif(exp == 1):
#         print(base)
#         return(base)
#     while(tmp <= exp):
#         num *= base
#         tmp += 1
#     print(num)
# def factorial(num):
#     if(num == 0):
#         return(1)
#     return(fact)


# def factorial(n):
#     if n == 1:
#         return(1)
#     else:
#         return(n * factorial(n-1))

def squared(num,exp):
    if(exp == 0):
        return(1)
    else:
        return(num * squared(num,exp-1))


def graphDFS(graph,node,visited):
    

if __name__ == "__main__":
    # BinarySearch(198)
    # reverseString()
    # getMLBatheletes()
    #test()
    # print(factorial(3))
    visted = 
    graphDFS({1:[2,3],2:[4,5],3:[2,],4:[2,3],5:[1]},1,)
    print(squared(2,-1))
#    largestPalindrome()
 #   largestPrimeFactor(600851475143)
    # testTree = Tree()
    # testTree.addNode(testTree.root, 200)
    # testTree.addNode(testTree.root, 300)
    # testTree.addNde(testTree.root, 100)
    # testTree.addNode(testTree.root, 30)
    # testTree.printInorder(testTree.root
    # graph = {'A': set(['B', 'C']),
    #      'B': set(['A', 'D', 'E']),
    #      'C': set(['A', 'F']),
    #      'D': set(['B']),
    #      'E': set(['B', 'F']),
    #      'F': set(['C', 'E'])}
    # print(findTarget([1,2,3,5,5,6,30],36))
