text = "({[]})"

stack = []
pairs = {
    ")": "(",
    "}": "{",
    "]": "["
}

balanced = True

for ch in text:
    if ch in "({[":
        stack.append(ch)

    elif ch in ")}]":
        if not stack:
            balanced = False
            break

        top = stack.pop()

        if top != pairs[ch]:
            balanced = False
            break

if stack:
    balanced = False

if balanced:
    print("Balanced")
else:
    print("Not balanced")