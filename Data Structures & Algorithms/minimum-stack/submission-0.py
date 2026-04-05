class MinStack:

    def __init__(self):
        self.mystack = []
        self.myminstack = []

    def push(self, val: int) -> None:
        self.mystack.append(val)
        if not self.myminstack:
            self.myminstack.append(val)
        elif val <  self.myminstack[-1]:
            self.myminstack.append(val)
        else:
            self.myminstack.append(self.myminstack[-1])

    def pop(self) -> None:
        self.mystack.pop()
        self.myminstack.pop()

    def top(self) -> int:
        return self.mystack[-1]

    def getMin(self) -> int:
        return self.myminstack[-1]
        
