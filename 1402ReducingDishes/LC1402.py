class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction = sorted(satisfaction)
        res = 0
        total = 0
        for i in range(len(satisfaction)-1, -1, -1):
            if satisfaction[i] + total > 0:
                total += satisfaction[i]
                res += total
        return res
# O(NlogN)
 