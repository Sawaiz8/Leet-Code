class PermutationIterator:

    def __init__(self, s):
        from math import factorial
        self.string = s
        self.totalPermutations = factorial(len(s))
        self.tailIterator = ""
        self.mainStart = 0
        self.permutationsForward = self.string[:self.mainStart] + self.string[self.mainStart + 1:]
        
    def nextPermutation(self):
        if len(self.string) == 1:
            self.totalPermutations -= 1
            return self.string
        
        if self.tailIterator == "":
            self.tailIterator = PermutationIterator(self.permutationsForward)

        while self.tailIterator.hasMorePermutation():
            nex = self.tailIterator.nextPermutation()
            self.totalPermutations -= 1
            current = self.string[self.mainStart] + nex
            return current
        
        self.mainStart += 1
        self.permutationsForward = self.string[ :self.mainStart] + self.string[self.mainStart + 1: ]
        self.tailIterator = PermutationIterator(self.permutationsForward)
        return self.nextPermutation()
        
    def hasMorePermutation(self):
        if self.totalPermutations != 0:
            return True
        return False



itera = PermutationIterator("eat")
while itera.hasMorePermutation():
    print(itera.nextPermutation())

def permutations(s):
    results = []
    if len(s) == 1: #Figure out the base case first
        return [s[0]]
    else: #Dont get shiekh on using loops in solving questions is PYthon for everyone and for starting to solve a complex problem
        for i in range(len(s)): 
            permutationsForward = s[:i] + s[i + 1:]
            permu = permutations(permutationsForward)
            for per in permu:
                results.append(s[i] + per)
    return results

print(permutations("eat"))


### EXERCISE 11.15
def main():
    NUM_ELEMENTS = 4
    lstOfNumbers = list(range(1, NUM_ELEMENTS + 1))
    while nextPermutation(lstOfNumbers):
        print(lstOfNumbers) #Prints permutated lst of numbers   

def nextPermutation(lstOfNumbers):
    i = len(lstOfNumbers) - 1 #TOTAL INDEXES 
    while i > 0:
        if lstOfNumbers[i - 1] < lstOfNumbers[i]: #IF 2ND LAST NUMBER IS LESS THAN LAST NUMBER 
            j = len(lstOfNumbers) - 1 #Last index j
            while lstOfNumbers[i -1] > lstOfNumbers[j]: #If last index j number less than sencond last number
                j = j - 1
            swap(lstOfNumbers, i-1, j)
            reverse(lstOfNumbers, i, len(lstOfNumbers) -1)
            return True
        i = i - 1
    return False

def reverse(lstOfNumbers, i, j): #Reverses a section of a lst depending on the starting point i and ending point j 
    while i < j:
        swap(lstOfNumbers, i, j)
        i += 1
        j -= 1

def swap(lstOfNumbers, i ,j): #Swaps two numbers at i and j index
    temp = lstOfNumbers[i]
    lstOfNumbers[i] = lstOfNumbers[j]
    lstOfNumbers[j] = temp

def newPermutations(s):
    print(s)
    lstOfNumbers = list(range(0, len(s)))
    while nextPermutation(lstOfNumbers):
        string = ""
        for i in lstOfNumbers:
            string += s[i]
        print(string)

newPermutations("sawz")


