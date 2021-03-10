class MyCalendarThree:

    def __init__(self):
        self.delta = collections.Counter()

    def book(self, start: int, end: int) -> int:
        self.delta[start]+=1
        self.delta[end]-= 1
        
        active = ans = 0
        for x in sorted(self.delta):
            active += self.delta[x]
            if active > ans: ans = active 
        return ans 
# test case : [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
