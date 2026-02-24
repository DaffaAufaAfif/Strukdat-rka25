x = input()
stack = []
relation = {'{':'}','}':'{',
            '(':')',')':'(',
            '[':']',']':'['}
for i in x:
    if not stack:
        stack.append(i)
    else:
        if relation[stack[-1]] == i:
            stack.pop()
        else:
            stack.append(i)
if len(stack) == 0:
    print("Valid")
else:
    print("Invalid")