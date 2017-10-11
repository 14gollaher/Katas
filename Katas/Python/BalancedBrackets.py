def is_matched(expression):
    validState = True
    openCloseSymbols = {'(': ')', '{': '}', '[': ']' }
    openingStack = []

    for letter in expression:
        if letter in openCloseSymbols.keys():
            openingStack.append(letter)
        else:
            if letter is not openCloseSymbols[openingStack.pop()]:
                return False
    return True

t = int(input().strip())

for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
