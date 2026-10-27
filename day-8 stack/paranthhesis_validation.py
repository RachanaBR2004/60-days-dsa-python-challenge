str='{[()]}'
stack=[]
for ch in str:
    if ch in '{[(':
        stack.append(ch)
