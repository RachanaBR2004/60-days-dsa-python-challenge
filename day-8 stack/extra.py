a = [4, 5, 2, 10, 8]

stack = []
result = [-1] * len(a)

for i in range(len(a)):
    while stack and a[i] > a[stack[-1]]:
        index = stack.pop()
        result[index] = a[i]

    stack.append(i)

print(result)