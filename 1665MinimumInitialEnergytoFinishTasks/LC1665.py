class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda a: a[1] - a[0])
       
        res = 0 
        # min - actual means how much you save after invest energy, if you start from largest save, you might end up spend too much energy, so start from smallest save and finish tasks
        for a, m in tasks:
            res = max(res + a, m)
        return res
# O(NlogN)
# O(1)


class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda a: a[0] - a[1])
       
        res, curr = 0 , 0
        for a, m in tasks:
            if m > curr:
                res += (m-curr)
                curr = m
            curr -= a
        return res
# O(NlogN)
# O(1)