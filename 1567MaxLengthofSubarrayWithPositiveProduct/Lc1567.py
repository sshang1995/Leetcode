class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        length = 0
        for i in range(len(nums)):
            product = nums[i]
            maxs = nums[i]
            if maxs > 0 and length == 0:
                length = 1
                
            for j in range(i+1, len(nums)):
                product *= nums[j]
                if product >= maxs and product>0:
                    maxs = product
                    #print(f"maxs:{maxs},lenght:{j,i}")
                    length = max(length,j-i+1)
        return length
                
            
# Time Limited Exceed

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
                pos[i] = pos[i-1] + 1
                if neg[i-1] > 0:# negtive times postive is negetive
                    neg[i] = 1 + neg[i-1]
                else:
                    neg[i] = 0
            elif nums[i] < 0:
                if neg[i-1] > 0:# negative * negetive = postive
                    pos[i] = 1 + neg[i-1]
                else:
                    pos[i] = 0
                neg[i] = 1 + pos[i-1]
            ans = max(ans, pos[i] )
        return ans
        
# TC: O(N)
# SC: O(N)           
                
            
