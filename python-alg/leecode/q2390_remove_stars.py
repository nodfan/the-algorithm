def removeStars(s):
    stack = []

    for char in s:
        if char == "*":
            if stack:
                stack.pop()
        else:
            stack.append(char)

    return ''.join(stack)


s = "leet**cod*e"
print(removeStars(s))
