class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # Binary search
        # start= max(nums), end = sum(nums), find the mid is maximum subarray
        # maintiin count of subarrays, including all the possible elements in subarray until their sum is less than mild. if count <= K, then mid is good else not.
        def check(mid, nums,m):
            count = 0
            sums = 0
            for i in range(len(nums)):
                sums += nums[i]
                if sums > mid:
                    count += 1
                    sums = nums[i]
            # add last subarray which sums <=mid
            count += 1
            if count <= m:
                return True
            return False
                
        start = max(nums)
        end = sum(nums)
        while start <= end:
            mid = (start + end) //2
            #print(mid)
            if check(mid,nums,m):
                answer = mid
                end = mid -1
            else:
                start = mid +1 
        return answer
    
        
            
                
                
                
                
                
            