def minRemoveToMakeValid(self, s: str) -> str:
    n = len(s)
    invalid = set()
    stack = []
    for i in range(n):
        if s[i] not in '()':
            continue
        elif s[i] == '(':
            stack.append(i)
        elif s[i] == ')' and not stack:
            invalid.add(i)
        else:
            stack.pop()
    for index in stack:
        invalid.add(index)
        
    stringbuilder = []
    for i in range(n):
        if i not in invalid:
            stringbuilder.append(s[i])
    
    return ''.join(stringbuilder)