def reverseWords(self, s: str) -> str:
    
    string = self.stripWhitespace(s)
    self.reverseChars(0, len(string) - 1, string)
    
    start = end = 0
    while end < len(string):
        if string[end] == ' ':
            self.reverseChars(start, end - 1, string)
            start = end + 1
        end += 1
    self.reverseChars(start, end - 1, string)

    return ''.join(string)
    

def reverseChars(self, i, j, arr):
    while i <= j:
        temp = arr[j]
        arr[j] = arr[i]
        arr[i] = temp
        i += 1
        j -= 1
        
def stripWhitespace(self, string):
    res = []
    left = 0
    right = len(string) - 1
    
    # strip leading whitespace
    while left <= right and string[left] == ' ':
        left += 1
        
    #strip trailing whitespace
    while left <= right and string[right] == ' ':
        right -= 1
    
    # remove extra spaces
    while left <= right:
        if string[left] != ' ':
            res.append(string[left])
        elif res[-1] != ' ':
            res.append(string[left])
        left += 1
    
    return res 