class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        mins = inf
        evens = []
        # increase odd to their maximum, so we cannot increase minimum, only decrease maximum
        for i in range(len(nums)):
            if  nums[i] % 2 != 0:
                evens.append(-nums[i] * 2)
                mins = min(mins, nums[i] * 2)
            else:
                evens.append(-nums[i])
                mins = min(mins, nums[i])
        #since heapq is min-heap, we use negative of numbers to mimic a max-heap
        heapq.heapify(evens)
        min_diff = inf
        while evens:
            # current max value
            curr = - heapq.heappop(evens) 
            min_diff = min(min_diff, curr - mins)
            if curr % 2 == 0:
                #push negative value to heap
                heapq.heappush(evens, -curr//2)
                mins = min(mins, curr//2)
            else:
                # curr max value is odd, we cannnot decrease.
                break
        return min_diff
            
        
# heap data structure maintain maximum in logarithmic time, return max in constant time
# N is length of nums, M is max value,
# TC: O(Nlog(M)*log(N))
# SC: O(N)

