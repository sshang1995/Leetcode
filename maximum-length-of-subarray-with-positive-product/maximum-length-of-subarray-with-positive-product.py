class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        pos, neg = [0] * n, [0] * n
        if nums[0] > 0:
            pos[0] = 1
        elif nums[0] < 0:
            neg[0] = 1
        ans = pos[0]
        for i in range(1,n):
            if nums[i] > 0:
                pos[i] = 1+ pos[i-1]
                if neg[i-1] > 0:
                    neg[i] = 1 + neg[i-1]
                else:
                    neg[i] = 0
            elif nums[i] < 0:
                if neg[i-1] > 0:
                    pos[i] = 1 + neg[i-1]
                else:
                    pos[i] = 0
                neg[i] = 1 + pos[i-1]
            ans = max(ans, pos[i])
            #print(f"pos:{pos}, neg:{neg}")
            
        return ans
           
                
            
        