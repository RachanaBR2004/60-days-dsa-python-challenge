str='{[()]}'
stack=[]
valid=True
d={
    ')':'(',
    ']':'[',
    '}':'{'
}
for cha in str:
    if cha in '{[(':
        stack.append(cha)
    else:
        if not stack:
            valid=False
            break
        if stack[-1]!=d[cha]:
            valid=False
            break
        else:
            stack.pop()
if stack:
    valid=False

print(valid)
            
        

    
