# text = "hello"

# stack = []

# for ch in text:
#     stack.append(ch)

# result = ""

# while stack:
#     result += stack.pop()

# print(result)

a="frog"
stack=[]
for ch in a:
    stack.append(ch)
print(stack)


reverse=""
while stack:
    z=stack.pop()
    reverse=reverse+z
print(reverse)