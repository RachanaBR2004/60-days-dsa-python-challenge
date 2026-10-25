path="/home//user/../documents/./"
stack=[]
for i in path.split("/"):
    if i == "" or i == ".":
        continue
    elif i=="..":
        if stack:
            stack.pop()
        else:
            pass
    else:
        stack.append(i)
result="/"+"/".join(stack)
print(result)

        