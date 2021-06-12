class MKAverage:

    def __init__(self, m: int, k: int):
        self.stream = []
        self.m = m
        self.k = k
        self.new_stream = []

    def addElement(self, num: int) -> None:
        self.stream.append(num)

    def calculateMKAverage(self) -> int:

        if len(self.stream) < self.m:
            return -1
        else:
            self.new_stream = self.stream[len(self.stream) - self.m :]
            self.new_stream = sorted(self.new_stream)
            #print(self.new_stream)
            final = self.new_stream[self.k : len(self.new_stream) - self.k]
            #print(final)
            return sum(final)//len(final)
            


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()

# TC: O(NlogN)

class MKAverage:

    def __init__(self, m: int, k: int):
        self.stream = []
        self.m = m
        self.k = k
        self.new_stream =[]
 

    def addElement(self, num: int) -> None:
        self.stream.append(num)

        
    def calculateMKAverage(self) -> int:

        if len(self.stream) < self.m:
            return -1
        else:

            self.new_stream = self.stream[len(self.stream) - self.m :]
            count = 0
            while count < self.k:
                self.new_stream.remove(min(self.new_stream))
                self.new_stream.remove(max(self.new_stream))
                count += 1
            
            return sum(self.new_stream)//len(self.new_stream)
            


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()

# TC: O(N)


import collections
import sortedcontainers
class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.que = collections.deque([])
        self.slist = sortedcontainers.SortedList()
 

    def addElement(self, num: int) -> None:
        self.que.append(num)
        self.slist.add(num)
        if len(self.que) > self.m:
            lru = self.que.popleft()
            self.slist.remove(lru)

        
    def calculateMKAverage(self) -> int:
        if len(self.que) < self.m:
            return -1
        return sum(self.slist[self.k:-self.k]) // (self.m - 2*self.k)
            


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()
