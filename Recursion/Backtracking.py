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


def main():
    solve([])


COLUMNS = "abcd"
NQUEENS = len(COLUMNS)
ACCEPT = 1
CONTINUE = 2
ABANDON = 3


def solve(partialSolution):
    exam = examine(partialSolution)
    if exam == ACCEPT:
        print(partialSolution)
    elif exam != ABANDON:
        for p in extend(partialSolution):
            solve(p)

def examine(partialSolution):
    for i in range(0, len(partialSolution)):
        for j in range(i + 1, len(partialSolution )):
            if attacks(partialSolution[i], partialSolution[j]):
                return ABANDON
    if len(partialSolution) == NQUEENS:
        return ACCEPT
    else:
        return CONTINUE

def attacks(p1,p2):
    column1 = COLUMNS.index(p1[0]) + 1 #Extract column from notation
    row1 = int(p1[1]) #Extract row from notation
    column2 = COLUMNS.index(p2[0]) + 1 #Extract column from notation
    row2 = int(p2[1]) #Extract row from notation
    return (row1 == row2 or column1 == column2 or abs(row1 - row2) == abs(column1 - column2))

def extend(partialSolution):
    #returns a list of lists with possible solutions [[a1],[b1],[c1],[d1]] for that row.(in this case row 1)
    results = []
    row = len(partialSolution) + 1
    for column in COLUMNS:
        newSolution = list(partialSolution) #With this it makes a copy of the original list. Remember only reference is transfered if you dont use list()
        newSolution.append(column + str(row)) #Add a queen in this copy of the grid
        results.append(newSolution)
    return results 


def subStrings(string, find = False): #Failed attempt
    lst = []
    if find:
        lst.append(string[0])
        hold = string[0]
        for i in range(1, len(string)):
            lst.append(hold + string[i])
            hold = hold + string[i]
        return lst
    else:
        for i in range(len(string)):
            lst += subStrings(string[i:], True)
        lst.append("")
        return lst

print(subStrings("sawaiz"))

def subString(string): #Correct approach
    if len(string) == 0:
        return [string]
    else:
        lst = []
        for i in range(1, len(string) + 1):
            lst.append(string[:i])
        return lst + subString(string[1:])

print(subString("rum"))





                    
        
            
