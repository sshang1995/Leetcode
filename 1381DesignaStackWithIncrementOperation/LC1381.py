class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.size = maxSize

    def push(self, x: int) -> None:
        if len(self.stack)< self.size:
            self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop() if self.stack else -1
        

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val
            
#TC: O(n)
#Sp: O(n)

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

#optimize
class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.size = maxSize
        self.inc = []

    def push(self, x: int) -> None:
        if len(self.stack)< self.size:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self) -> int:
        if not self.stack:
            return -1
        # inc[0:i] will need to increment, we save value at inc[i] and pass that value to previous one before pop
        if len(self.inc) > 1:
            self.inc[-2] += self.inc[-1]
        return self.stack.pop() + self.inc.pop()

    def increment(self, k: int, val: int) -> None:
        if self.inc:
            self.inc[min(k,len(self.stack)) -1] += val
            

#TC:O(1)
#SC: O(N)

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
