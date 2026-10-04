class MinStack:

    def __init__(self):
        self.values=[]
        self.min=[]

    def push(self, value: int) -> None:
        self.values.insert(0,value)
        if not self.min or value <= self.min[-1]:
            self.min.append(value)

    def pop(self) -> None:
        if self.values:
            poped=self.values.pop(0)
            if poped == self.min[-1]:
                self.min.pop()

    def top(self) -> int:
        if (len(self.values)==0):
            raise Exception('Stack is empty')
        else:
            return self.values[0]

    def getMin(self) -> int:
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna