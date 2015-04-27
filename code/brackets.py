def checkio(data):
    stack = []  # Yes, we can use deque
    pairs = {'(': ')', '[': ']', '{': '}'}
    for token in data:
        if token in pairs.keys():
            stack.append(token)
        elif token in pairs.values():
            if stack and token == pairs[stack[-1]]:
                stack.pop()
            else:
                return False
    return not bool(stack)

assert checkio("((5+3)*2+1)")
assert checkio("{[(3+1)+2]+}")
assert not checkio("(3+{1-1)}")
assert checkio("[1+1]+(2*2)-{3/3}")
assert not checkio("(({[(((1)-2)+3)-3]/3}-3)")
assert checkio("2+3")
