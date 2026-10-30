operations = ["5", "2", "C", "D", "+"]
stack=[]
for i in operations:
    if i not in "CD+":
        stack.append(int(i))
    elif i=='C':
        stack.pop()
    elif i=='D':
        stack.append(stack[-1]*2)
    else:
        stack.append(stack[-1]+stack[-2])
print(sum(stack))

