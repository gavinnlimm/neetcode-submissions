class MinStack:

    def __init__(self):
        self.regularStack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.regularStack.append(val)
        if not self.minStack: # if minStack is empty
            self.minStack.append(val)
        else: # if not empty
            self.minStack.append(min(val, self.minStack[-1])) # compare min and fix

    def pop(self) -> None:
        self.regularStack.pop()
        self.minStack.pop() 

    def top(self) -> int:
        return self.regularStack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]
