class MinStack:

    def __init__(self):
        self.allStack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        if not self.minStack:
            self.minStack.append(val)
        elif val <= self.minStack[-1]:
            self.minStack.append(val)
        
        self.allStack.append(val)
            

    def pop(self) -> None:
        if self.allStack:
            val = self.allStack.pop()
            if self.minStack and val == self.minStack[-1]:
                self.minStack.pop()
        
    def top(self) -> int:
        if self.allStack:
            return self.allStack[-1]
        # will have to ask interviewer how they want me to handle this
        return None
        

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        # will have to ask interviewer how they want me to handle this
        return None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()