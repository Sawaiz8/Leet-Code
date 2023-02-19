def main():
    expr = input("Enter an expression:")
    tokens = tokenize(expr)
    value = expression(tokens)
    print(expr + "=" + str(value))


def tokenize(inputLine): #converts expression into lst
    result = []
    i = 0
    while i < len(inputLine):
        if inputLine[i].isdigit():
            j = i + 1
            while j < len(inputLine) and inputLine[j].isdigit():
                j = j + 1
            result.append(int(inputLine[i:j]))
            i = j
        else:
            result.append(inputLine[i])
            i = i + 1
    return result
                          
def expression(tokens):
    value = term(tokens)
    done = False
    while not done and len(tokens) > 0:
        next = tokens[0]
        if next == "+" or next == "-":
            tokens.pop(0)
            value2 = term(tokens)
            if next == "+":
                value = value + value2
            else:
                value = value - value2
        else:
            done = True
    return value


def term(tokens):
    value = factor(tokens)
    done = False
    while not done and len(tokens) > 0:
        next = tokens[0]
        if next == "*" or next == "/":
            tokens.pop(0)
            value2 = factor(tokens)
            if next == "*":
                value = value * value2
            else:
                value = value / value2
        else:
            done = True
    return value

def factor(tokens):
    next = tokens.pop(0)
    if next == "(":
        value = expression(tokens)
        tokens.pop(0)
    else:
        value = next
    return value

main()       

print(tokenize("(3+5)*2"))
