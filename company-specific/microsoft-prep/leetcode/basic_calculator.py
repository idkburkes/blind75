
# This is a partial solution to the basic calculator problem
# This solution can only handle test cases with only 1 digit integers
# This solution also doesn't work for distributing negative signs throughout parenthesis

class Solution:
    def calculate(self, s: str) -> int:
        
        stack = []
        
        # iterate through string backwards
        for i in range(len(s) - 1, -1, -1):
            char = s[i]
            if char == '(':
                # if we find an opening parenthesis, pop off stack until we find first closing
                operator = '+'
                curnum = 0
                
                # perform all operations on nums between parens
                while char != ')' and stack:
                    char = stack.pop()
                    if char.isdigit():
                        if operator == '+':
                            curnum += int(char)
                        else:
                            curnum -= int(char)
                    elif char in '+-':
                        operator = char
                    elif char == ')':
                        # remove closing paren off stack and add result back to stack
                        stack.append(str(curnum))
                        
            elif char != ' ':
                stack.append(char)
            
            
        # once we've seen the whole string perform all operations currently on stack
        res = 0
        operator = '+'
        while stack:
            char = stack.pop()
            if char.isdigit():
                if operator == '+':
                    res += int(char)
                else:
                    res -= int(char)
            elif char in '+-':
                operator = char
        
        return res
                

        
        
        
        
        