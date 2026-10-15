text = "()[]{}"
stack = []

for ch in text:
    if ch == "(" or ch == "[" or ch == "{":
        stack.append(ch)

    elif ch == ")" or ch == "]" or ch == "}":
        if len(stack) == 0:
            print("Not balanced")
            break

        top = stack.pop()

        if (ch == ")" and top != "(") or \
           (ch == "]" and top != "[") or \
           (ch == "}" and top != "{"):
            print("Not balanced")
            break
else:
    if len(stack) == 0:
        print("Balanced")
    else:
        print("Not balanced")