def triangleArea(sidelength):
    if sidelength <= 1:
        return sidelength
    else:
        smallerSideLength = sidelength - 1
        smallerArea = triangleArea(smallerSideLength)
        area = smallerArea + sidelength
        return area

print(triangleArea(4))

# area == size always
# area = smallerArea + sidelengtH

def pow2(n):

    if n <= 0:
        return 1
    else:
        return 2 * pow2(n-1)
    

print(pow2(3))

def palindrome(s, low, high):

    if high - low == 1:
        return True
    else:
        return s[0] == s[-1] and palindrome(s, low+1, high-1)


print(palindrome("I did it", 0 , 3))

def isPalindrome(text):
    length = len(text)

    if length <= 1:
        return True
    else:
        first = text[0].lower()
        last = text[length - 1].lower()
        if first.isalpha() and last.isalpha():
            if first == last:
                shorter = text[1: length - 1]
                return isPalindrome(shorter)
            else:
                return False
        elif not last.isalpha():
            shorter = text[0: length -1]
            return isPalindrome(shorter)
        else:
            shorter = text[1: length]
            return isPalindrome(shorter)


class rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        if self.width == 1:
            return self.height
        else:
            smallerRectangle = rectangle(self.width - 1, self.height)
            areasmaller = smallerRectangle.getArea()
            area = self.height + areasmaller 
            return area


a = rectangle(2,2)
s = a.getArea()
print(s)

class square:

    def __init__(self, length):
        self.length = length

    def getArea(self):
        if self.length == 0:
            return self.length * self.length
        else:
            smallerSquare = square(self.length - 1)
            return smallerSquare.getArea() + 2* (self.width) - 1


def reverse(string):
    if len(string) == 1:
        return string
    else:
        return reverse(string[1:len(string)]) + string[0]  

from time import time
starttime = time()
print(reverse("Hello!"))
endtime = time() 
elapsed = endtime - starttime           
print(elapsed)

def reverse2(string, low = 0, high = -1): #I wrote the same code just a bit differently using -1 indexes
    if len(string) == high * -1 * 2:
        return string[high] + string[low]
    elif len(string) == low + high * -1:
        return string[high]
    else:
        return string[high] + reverse2(string, low + 1, high - 1) + string[low]

from time import time
starttime = time()
print(reverse2("Hello!"))
endtime = time() 
elapsed = endtime - starttime           
print(elapsed)


def reverse3(string, low, high):
    if high == low:
        return string[low]
    elif high - low == 1:
        return string[high] + string[low]
    else:
        return string[high] + reverse3(string, low + 1, high -1) + string[low]
    
def reverseNew(string):
    return reverse3(string, 0, len(string) - 1)

from time import time
starttime = time()
print(reverseNew("Hello!"))
endtime = time() 
elapsed = endtime - starttime           
print(elapsed)

def find(text, string):
    if len(string) == 0:
        return True
    elif len(text) == 0:
        return False
    elif string[0] == text[0]:
        return find(text[1:], string[1:])
    elif string[0] != text[0]:
        return False
    else:
        return find(text[1:], string)

from time import time
starttime = time()
print(find("fjsal;sipghsdajk", "sip"))
endtime = time() 
elapsed = endtime - starttime           
print(elapsed)

def find2(text, string, startText = 0, startString = 0):
    
    if len(string) == startString:
        return True
    elif len(text) == startText:
        return False
    elif text[startText] == string[startString]:
        return find2(text, string, startText + 1, startString + 1)     
    elif text[startText] != string[startString] and startString != 0:
        startText =  startText - startString + 1
        return find2(text, string, startText, 0)
    else:
        return find2(text, string, startText + 1, 0)

    
from time import time
starttime = time()
print(find2("fjsal;sipghsdajk", "sip", 0, 0))
endtime = time() 
elapsed = endtime - starttime           
print(elapsed)

#Copied from net. Im doing the smae thing in find2 but im also doing the work of start's with on my own.
#Also a better way to end the loop early would be to use this breaking condition where you compare length of text with string
def find3(text, string):

    if (len(text) < len(string)):
        return False
    if text.startswith(string):
        return True
    return find3(text[1:], string)

from time import time
starttime = time()
print(find3("aasipgsdg", "sip"))
endtime = time() 
elapsed = endtime - starttime           
print(elapsed)


def largest(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        value = largest(lst[1:])
        return lst[0] if lst[0] > value else value


print(largest([33,5,19,21]))

def areaOfPolygon(x, y):
    if len(x) == 3:
        area = abs(x[0]*y[1] + x[1]*y[2] + x[2]*y[0] - x[1]*y[0] - x[2]*y[1] - x[0]*y[2]) / 2
        print(area)
        return area   
    else:
        area = abs(x[0]*y[1] + x[1]*y[2] + x[2]*y[0] - x[1]*y[0] - x[2]*y[1] - x[0]*y[2]) / 2 + areaOfPolygon(x[1:], y[1:])
        print(area)
        return area
    
print(areaOfPolygon(x = [4,2,9,11], y = [10,2,7,2]))

def areaTri(p):
    if len(p) != 3:
        return -1
    area = 0
    for i in range(3):
        f,s = i, (i+1) % 3
        area += p[f][0] * p[s][1] * p[f][1]
    area = abs(area) /2
    return area

print(areaOfPolygon(x = [4,2,9,11], y = [10,2,7,2]))

#His was better because it was adapting to the situation by using Tuples as coordinates and it was dealing with the coordinate problem better too.
#It saw a pattern I didn't. Mine was based on the assumption that I'll get coordinates in order of trianagles which wont be the case.
def areaOfPolygon2(p): 
    if len(p) == 3:
        return areaTri(p)
    else:
        return int(areaTri(p[0:2] + p[-1] + areaPoly(p[1:])))



def squareRootGuess(x, g):
    if x - 0.5 <= (g**2) <= x + 0.005:
        return g
    elif g >= x//2:
        return "Not found"
    else:
        return squareRootGuess(x, g+1)

print(squareRootGuess(225, 0))


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

print(permutations("abc"))
    
